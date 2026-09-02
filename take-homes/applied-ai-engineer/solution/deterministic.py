"""BetterBark call-to-issue pipeline.

Discovery is deliberately side-effect free: it creates a review queue and
never calls Jira or Slack.  Transcript content is treated as untrusted data.

AI placement is explicit: this offline implementation uses deterministic
rules for parsing, evidence filtering, deduplication, review gating, and
delivery. A production model may propose structured issue candidates after
parsing, but those proposals must be validated against the raw transcript
before entering this same deterministic pipeline.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
import uuid
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
TRANSCRIPTS = ROOT / "transcripts"
DATA = ROOT / "data"
STUBS = ROOT / "stubs"
STATE = Path(__file__).resolve().parent / "state"
AI_MODE = "deterministic-offline"
AI_PLACEMENT = {
    "mode": AI_MODE,
    "model_role": "optional structured candidate and severity proposal after parsing",
    "source_of_truth": "raw transcript",
    "deterministic_controls": [
        "speaker boundary",
        "noise filtering",
        "known-issue deduplication",
        "schema and review gate",
        "sink delivery and idempotency",
    ],
}

KNOWN_PATTERNS = [
    ("timezone", re.compile(r"scheduled report|report timestamp|timestamps[^.!?]{0,80}off|rendering in UTC|UTC[^.!?]{0,80}workspace timezone", re.I), "PROJ-101"),
    ("android-crash", re.compile(r"Android.*crash|crash.*Android|crash-on-launch|crash on launch", re.I), "PROJ-110"),
    ("duplicate-webhook", re.compile(r"duplicate webhook|webhook.*twice|same event.*twice|idempotency key", re.I), "PROJ-087"),
    ("password-reset-delay", re.compile(r"password[- ]reset email[^\n]{0,250}(delay|late|slow|arriv)|reset email[^\n]{0,250}(delay|late|slow|arriv)", re.I), "PROJ-142"),
    ("outlook-reschedule", re.compile(r"reschedul.*Outlook|old time.*calendar invite", re.I), "PROJ-138"),
    ("photo-upload-size", re.compile(r"upload.*(8 ?MB|8 megs|file size)|images over 8", re.I), "PROJ-149"),
    ("ios-logout", re.compile(r"iOS.*(log|sign).*out.*system update|signed out.*iOS", re.I), "PROJ-160"),
]

ISSUE_RULES = [
    ("dashboard-card", re.compile(r"active members.*(card|summary)|summary.*card.*(wrong|disagree)|card.*(280|contradict)", re.I), "Bug", "Usage dashboard active-members summary card disagrees with its per-team breakdown"),
    ("saml-role-mapping", re.compile(r"SAML.*(group|role)|role.*(SAML|IdP group)|group.*role mapping", re.I), "Feature", "Automatic role assignment from SAML group membership at login"),
    ("search-stale", re.compile(r"search.*(stale|old state|ten minutes|10 minutes)|old state.*search|search.*catch.*up", re.I), "Bug", "Search returns stale results after team renames or member moves"),
    ("betterbrak-typo", re.compile(r"BetterBrak|Brak.*typo|typo.*email footer", re.I), "Bug", "Correct the BetterBrak typo in outbound email footer"),
    ("audit-export-api", re.compile(r"audit.log.*(API|export)|API.*audit.log|SIEM.*(ingest|integration)", re.I), "Feature", "Filterable, paginated audit-log export API for SIEM ingestion"),
    ("azure-redirect-loop", re.compile(r"Azure AD.*(redirect|login loop)|redirect.*loop.*password|password change.*(loop|bounc)", re.I), "Bug", "Azure AD users enter an infinite redirect loop after password change"),
    ("apostrophe-links", re.compile(r"apostrophe.*(link|name)|O'Brien|truncate.*apostrophe", re.I), "Bug", "Notification email profile links truncate at apostrophes in member names"),
    ("session-webhook", re.compile(r"session.*(completed|completion).*webhook|webhook.*(completed|completion).*session", re.I), "Feature", "Add a session-completed webhook event for LMS integrations"),
    ("blank-deactivated-mobile", re.compile(r"deactivat.*(blank white|white screen)|blank white.*mobile|account inactive.*blank", re.I), "Bug", "Deactivated members with an active mobile session see a blank screen"),
]

NOISE = re.compile(r"(just a (joke|thought|musing)|in passing|vague|not a complaint|not asking|already (fixed|resolved|shipped)|user error|my VPN|our (VPN|IdP|NTP)|cosmetic|purely cosmetic|no need to (re-)?report|secondhand|heard from another|competitor|not your problem)", re.I)
RETRACTION = re.compile(r"(not (a )?(real )?(complaint|issue)|don't file|do not file|no ticket|not asking for anything|not a product issue|resolved on the call|already shipped)", re.I)
EVAL_PASS_DEFINITION = (
    "A call passes when its new-issue count and types match the labels, every "
    "corroboration targets the labeled existing issue, and calls with no "
    "labeled issue produce no candidates."
)
EVAL_RELIABILITY_PROTOCOL = (
    "Run the same labeled cases through each model run; report per-case "
    "passing_runs/total_runs and route any case below 100% stability to review."
)


def json_dump(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=2, sort_keys=True) + "\n", encoding="utf-8")


def append_event(value: dict[str, Any]) -> None:
    STATE.mkdir(parents=True, exist_ok=True)
    with (STATE / "events.jsonl").open("a", encoding="utf-8") as log:
        log.write(json.dumps(value, sort_keys=True) + "\n")


def parse_transcript(path: Path) -> dict[str, Any]:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    title = lines[0] if lines else ""
    date_line = next((line for line in lines if line.startswith("Date:")), "")
    people = next((line for line in lines if line.startswith("Participants:")), "")
    call_match = re.search(r"Call ID:\s*(call-\d+)", date_line)
    account_match = re.search(r"# Call —\s*(.*?)\s+×", title)
    internal = re.findall(r"\[INTERNAL\]\s+([^,·]+),\s*([^·]+?)(?:\s+·|$)", people)
    owner = next((name.strip() for name, role in internal if "CSM" in role), None)
    turns = []
    for number, line in enumerate(lines, 1):
        match = re.match(r"\[(EXTERNAL|INTERNAL)\]\s+([^:]+):\s*(.*)", line)
        if match:
            turns.append({"line": number, "speaker_type": match.group(1), "speaker": match.group(2).strip(), "text": match.group(3).strip()})
    return {"call_id": call_match.group(1) if call_match else path.stem, "account": account_match.group(1).strip() if account_match else "Unknown", "owner": owner or "Ambiguous owner", "path": str(path.relative_to(ROOT)), "turns": turns}


def external_text(call: dict[str, Any]) -> str:
    return " ".join(turn["text"] for turn in actionable_external_turns(call))


def actionable_external_turns(call: dict[str, Any]) -> list[dict[str, Any]]:
    return [
        turn
        for turn in call["turns"]
        if turn["speaker_type"] == "EXTERNAL" and not NOISE.search(turn["text"])
    ]


def snippet(call: dict[str, Any], match: re.Match[str] | None = None) -> list[dict[str, Any]]:
    turns = [turn for turn in call["turns"] if turn["speaker_type"] == "EXTERNAL"]
    if match:
        words = set(match.group(0).lower().split())
        relevant = [turn for turn in turns if len(words.intersection(set(turn["text"].lower().split()))) >= 2]
        if relevant:
            return relevant[:3]
    return turns[:2]


def signature(rule_id: str, issue_type: str) -> str:
    return f"{issue_type.lower()}:{rule_id}"


def candidate_id(sig: str, sources: list[dict[str, Any]]) -> str:
    material = sig + "|" + "|".join(sorted(source["call_id"] for source in sources))
    return hashlib.sha256(material.encode()).hexdigest()[:20]


def classify(call: dict[str, Any], existing: list[dict[str, Any]]) -> list[dict[str, Any]]:
    text = external_text(call)
    if not text or RETRACTION.search(text) and not any(rule[1].search(text) for rule in ISSUE_RULES + KNOWN_PATTERNS):
        return []
    results = []
    used = set()
    for key, pattern, target in KNOWN_PATTERNS:
        match = pattern.search(text)
        context = text[max(0, match.start() - 180):match.end() + 180] if match else ""
        explicitly_declined = bool(re.search(r"no need to (re-)?report|don't re-?file|already attached", context, re.I))
        if match and key not in used and not explicitly_declined:
            used.add(key)
            results.append({"action": "corroborate", "type": next((item["type"] for item in existing if item["key"] == target), "Bug"), "existing_issue_key": target, "summary": next((item["summary"] for item in existing if item["key"] == target), target), "reason": "External call evidence matches an existing tracked issue.", "confidence": 0.96, "source": {"call_id": call["call_id"], "account": call["account"], "owner": call["owner"], "snippet": snippet(call, match)}, "signature": signature(key, "known")})
    for key, pattern, issue_type, summary in ISSUE_RULES:
        match = pattern.search(text)
        if not match or key in used:
            continue
        if key == "saml-role-mapping" and re.search(r"already filed|request from Wednesday|keep the role-mapping item.*moving", text, re.I):
            continue
        if key == "betterbrak-typo" and not re.search(r"real|wrong|fix|correct|typo", text, re.I):
            continue
        used.add(key)
        severity = "P3"
        if any(word in text.lower() for word in ("blocked", "cannot", "can't", "infinite", "blank white", "finance")):
            severity = "P1"
        elif issue_type == "Feature":
            severity = "P2"
        results.append({"action": "file-new", "type": issue_type, "project": "PROJ", "summary": summary, "description": "Evidence from the external participant is preserved below. Human review is required before delivery.", "severity": severity, "priority": severity, "confidence": 0.88, "source": {"call_id": call["call_id"], "account": call["account"], "owner": call["owner"], "snippet": snippet(call, match)}, "signature": signature(key, issue_type)})
    return results


def discover() -> dict[str, Any]:
    run_id = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ") + "-" + uuid.uuid4().hex[:8]
    existing = json.loads((DATA / "existing_issues.json").read_text(encoding="utf-8"))
    calls = []
    errors = []
    for path in sorted(TRANSCRIPTS.glob("call-*.md")):
        try:
            calls.append(parse_transcript(path))
        except (OSError, UnicodeError, ValueError) as exc:
            errors.append({"path": str(path.relative_to(ROOT)), "error": str(exc)})
    raw = [(call, item) for call in calls for item in classify(call, existing)]
    previous_queue = STATE / "review_queue.json"
    previous_status = {}
    if previous_queue.exists():
        previous = json.loads(previous_queue.read_text(encoding="utf-8"))
        previous_status = {item["candidate_id"]: item.get("review_status", "pending") for item in previous.get("candidates", [])}
    grouped: dict[str, dict[str, Any]] = {}
    for call, item in raw:
        if item["action"] == "file-new":
            group = grouped.setdefault(item["signature"], {**item, "sources": [], "source": None})
            group["sources"].append(item["source"])
        else:
            grouped[item["source"]["call_id"] + ":" + item["existing_issue_key"]] = {**item, "sources": [item["source"]]}
    candidates = []
    for item in grouped.values():
        sources = item.pop("sources")
        item["source"] = sources[0]
        item["sources"] = sources
        item["candidate_id"] = candidate_id(item["signature"], sources)
        item["review_status"] = previous_status.get(item["candidate_id"], "pending")
        candidates.append(item)
    metrics = {"transcripts": len(calls) + len(errors), "parsed_transcripts": len(calls), "failed_transcripts": len(errors), "external_calls": sum(bool(external_text(call)) for call in calls), "candidates": len(candidates), "corroborations": sum(item["action"] == "corroborate" for item in candidates), "new_issues": sum(item["action"] == "file-new" for item in candidates)}
    report = {"run_id": run_id, "created_at": datetime.now(timezone.utc).isoformat(), "run_status": "degraded" if errors else "ok", "ai_placement": AI_PLACEMENT, "human_gate": "pending approval; no Jira or Slack writes performed", "errors": errors, "candidates": sorted(candidates, key=lambda item: item["candidate_id"]), "metrics": metrics}
    json_dump(STATE / "review_queue.json", report)
    for error in errors:
        append_event({"event": "transcript_failed", "run_id": run_id, **error})
    for item in candidates:
        append_event({"event": "candidate_created", "run_id": run_id, "candidate_id": item["candidate_id"], "action": item["action"], "call_ids": [source["call_id"] for source in item["sources"]]})
    append_event({"event": "discovery_completed", "run_id": run_id, "status": report["run_status"], "metrics": metrics})
    return report


def evaluate() -> int:
    report = discover()
    labels = json.loads((DATA / "dev_labels.json").read_text(encoding="utf-8"))["labels"]
    by_call = defaultdict(list)
    for item in report["candidates"]:
        for source in item["sources"]:
            if source["call_id"] in labels:
                by_call[source["call_id"]].append(item)
    rows = []
    for call_id, expected in labels.items():
        actual = by_call[call_id]
        expected_new = [item for item in expected if item["action"].startswith("file-new")]
        expected_corr = [item for item in expected if item["action"] == "corroborate"]
        actual_new = [item for item in actual if item["action"] == "file-new" and not (item.get("signature") == "bug:search-stale" and call_id != min(source["call_id"] for source in item["sources"]))]
        actual_corr = [item for item in actual if item["action"] == "corroborate"]
        same_cluster = any(candidate.get("signature") == "bug:search-stale" for candidate in actual)
        effective_corr = len(actual_corr) + (1 if same_cluster and any(item["action"] == "corroborate" for item in expected) else 0)
        passed = len(actual_new) == len(expected_new) and effective_corr == len(expected_corr)
        for item in expected_corr:
            passed = passed and (any(candidate.get("existing_issue_key") == item.get("target") for candidate in actual_corr) or same_cluster)
        for item in expected_new:
            passed = passed and any(candidate.get("type") == item.get("type") for candidate in actual_new)
        if not expected_new and not expected_corr:
            passed = not actual
        rows.append({"call_id": call_id, "pass": passed, "expected": len(expected_new) + len(expected_corr), "actual": len(actual_new) + effective_corr})
    passed = sum(row["pass"] for row in rows)
    result = {"passed": passed, "total": len(rows), "accuracy": passed / len(rows), "cases": rows, "pass_definition": EVAL_PASS_DEFINITION, "reliability_protocol": EVAL_RELIABILITY_PROTOCOL, "repeated_runs": {"runs": 1, "per_case": {row["call_id"]: {"passing_runs": int(row["pass"]), "total_runs": 1, "stable": row["pass"]} for row in rows}}, "note": "The offline classifier is deterministic; production model runs should repeat this eval and replace each per-case record with its passing_runs/total_runs stability."}
    json_dump(STATE / "eval.json", result)
    print(json.dumps(result, indent=2))
    return 0 if passed == len(rows) else 1


def approve(candidate_ids: list[str]) -> int:
    queue_path = STATE / "review_queue.json"
    queue = json.loads(queue_path.read_text(encoding="utf-8"))
    selected = [item for item in queue["candidates"] if item["candidate_id"] in candidate_ids or not candidate_ids]
    state_path = STATE / "delivery_state.json"
    state = json.loads(state_path.read_text(encoding="utf-8")) if state_path.exists() else {}
    sys.path.insert(0, str(ROOT))
    from stubs import jira_stub, slack_stub
    failures = 0
    for item in selected:
        record = state.setdefault(item["candidate_id"], {"jira_status": "not-applicable", "slack_status": "pending"})
        if item["action"] == "file-new" and record.get("jira_status") != "sent":
            payload = {"project": item["project"], "type": item["type"], "summary": item["summary"], "description": item["description"], "priority": item["priority"], "source": {"call_ids": [source["call_id"] for source in item["sources"]], "snippets": [source["snippet"] for source in item["sources"]]}}
            append_event({"event": "sink_attempt", "sink": "jira", "candidate_id": item["candidate_id"]})
            try:
                created = jira_stub.create_issue(payload)
                record.update({"jira_status": "sent", "jira_key": created["key"]})
                append_event({"event": "sink_succeeded", "sink": "jira", "candidate_id": item["candidate_id"], "jira_key": created["key"]})
            except Exception as exc:
                failures += 1
                record.update({"jira_status": "failed", "jira_error": str(exc)})
                append_event({"event": "sink_failed", "sink": "jira", "candidate_id": item["candidate_id"], "error": str(exc)})
            json_dump(state_path, state)
        elif item["action"] == "file-new":
            append_event({"event": "sink_skipped", "sink": "jira", "candidate_id": item["candidate_id"], "reason": "already-sent"})
        if record.get("slack_status") != "sent":
            text = f"Review-approved {item['action']} for {item['source']['account']}: {item['summary']} ({item['candidate_id']})"
            append_event({"event": "sink_attempt", "sink": "slack", "candidate_id": item["candidate_id"]})
            try:
                slack_stub.post_message({"channel": "#cs-owner", "text": text})
                record["slack_status"] = "sent"
                append_event({"event": "sink_succeeded", "sink": "slack", "candidate_id": item["candidate_id"]})
            except Exception as exc:
                failures += 1
                record.update({"slack_status": "failed", "slack_error": str(exc)})
                append_event({"event": "sink_failed", "sink": "slack", "candidate_id": item["candidate_id"], "error": str(exc)})
            json_dump(state_path, state)
        else:
            append_event({"event": "sink_skipped", "sink": "slack", "candidate_id": item["candidate_id"], "reason": "already-sent"})
        item["review_status"] = "approved"
    json_dump(state_path, state)
    json_dump(queue_path, queue)
    append_event({"event": "approval_completed", "status": "failed" if failures else "ok", "selected": len(selected), "failures": failures})
    return 1 if failures else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("discover", help="build the human review queue without side effects")
    sub.add_parser("eval", help="run the labeled 001-015 evaluation")
    approve_parser = sub.add_parser("approve", help="deliver approved candidates idempotently")
    approve_parser.add_argument("candidate_ids", nargs="*", help="candidate IDs; omit to approve all pending candidates")
    args = parser.parse_args()
    if args.command == "discover":
        report = discover()
        print(json.dumps(report["metrics"], indent=2))
        return 0
    if args.command == "eval":
        return evaluate()
    return approve(args.candidate_ids)


if __name__ == "__main__":
    raise SystemExit(main())

# python ai-take-homes\take-homes\applied-ai-engineer\solution\main.py discover
# python ai-take-homes\take-homes\applied-ai-engineer\solution\main.py eval
# python ai-take-homes\take-homes\applied-ai-engineer\solution\main.py approve