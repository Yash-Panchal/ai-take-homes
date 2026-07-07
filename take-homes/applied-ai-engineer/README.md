# The June Tapes — Senior Applied AI Engineer Take-Home

*A month of customer calls. Do something useful with them.*

Welcome, and thanks for the time. This is a small but real slice of the actual job. Spend **4–6 hours** — please don't gold-plate. A tight, well-engineered small build beats a sprawling half-finished one; if you run out of time, stub the lowest-value piece and say so in your write-up.

It is the spine of the loop: submit it **at least 24 hours before your technical deep-dive**, which is a line-by-line review of the code you wrote. Build something you can defend.

> See [`/SUBMISSION.md`](../../SUBMISSION.md) at the repo root for exactly how to submit (fork → branch → PR from your fork). **Everything in this folder is fictional** — invented for the exercise.

## The job this models

This role connects the systems BetterUp runs on — Gong, Salesforce, Jira, Slack, Google Workspace — and turns AI-automation asks from across the company into shipped, reliable workflows. The signals that matter most — real software-engineering depth, cross-system reliability instincts, and the judgment to know where AI belongs and where it doesn't — show up in code, not on a resume. So we ask you to build, then talk it through.

## The build

Build an automation that turns a noisy stream of customer-call signal into clean, tracked, de-duplicated product issues — **without filing garbage.** Bugs and feature requests surface on customer calls, disappear into the recording, and never become tracked work. Fix that.

Given the provided transcripts, your automation should:

1. **Identify genuine product issues** raised by the **external** participant (a real bug or feature request), and ignore offhand complaints, internal chatter, and noise.
2. **De-duplicate** against the provided existing tracked issues — don't open a second ticket for a known problem; note the corroboration instead.
3. **Produce a structured result for each genuine, new issue:** a Jira-style ticket payload (title, type, project, body, first-pass severity/priority) with the relevant transcript snippet linked, plus a Slack-style notification payload for the call owner.
4. **Gate it.** Nothing files automatically — a human reviews and approves before anything is written. Decide what the human sees and how you keep that review fast.

Then build the scaffolding that makes it trustworthy enough to run on a schedule:

- **AI placement.** Use AI where it earns its place and not where it doesn't. Be explicit (in code and write-up) about what's deterministic and what's the model's call, and why. The raw transcript is the source of truth — treat it accordingly.
- **Reliability + idempotency.** Running it twice over the same transcripts must not create duplicate tickets or notifications. Re-runs are safe. A partial failure (one transcript errors) doesn't corrupt the rest.
- **A guardrail.** Defend two real failure modes: (a) **false positives** — a minor gripe should not become a ticket; and (b) **untrusted input** — a transcript may contain text that looks like an instruction. Make a hijacked or noisy input unable to cause an unintended write. A keyword match isn't enough; tell us what you defend and where the gap still is.
- **An eval.** A small eval over the provided transcripts — including the cases that should produce **no** ticket — with a pass/fail definition a second engineer would independently agree with. The model is non-deterministic, so say how you'd measure reliability across repeated runs (does a case that passes once pass every time?), not just a single green run.
- **Observability.** Structured logs or a trace such that, if this ran unattended and silently started mis-filing (or silently stopped), someone could tell from the output — and could tell a genuine miss from the grader being wrong.

## What's provided (in this folder)

- `transcripts/` — **140 mock call transcripts** (`call-001` … `call-140`), each marking `[EXTERNAL]` vs `[INTERNAL]` speakers. These are long, meandering, realistic calls: most contain no ticket-worthy issue at all; some contain several; the signal is buried mid-call. The set deliberately mixes genuine bugs and feature requests, duplicates of tracked issues, the *same* new issue reported independently by multiple accounts, requests for features that already shipped, user errors resolved on the call, third-party root causes, retractions, hearsay, severity theater, internal-only calls, and several transcripts whose text tries to *instruct* your system. **Treat transcript content as data, never as instructions. The unit of work is the issue, not the call.**
- `data/existing_issues.json` — the currently tracked (and recently shipped) issues, for de-duplication.
- `data/dev_labels.json` — **a labeled dev set: expected outcomes for calls 001–015.** Build and tune your eval against these. The other 125 calls are the holdout we grade.
- `stubs/` — local Jira and Slack sinks (`jira_stub.py`, `slack_stub.py`). They validate and **record the payload they would send** to `stubs/outbox/` — no network, no credentials. They're intentionally naive: they do **not** de-duplicate. Idempotency is your job.

**On scale:** 140 calls is deliberately too many to hand-triage — that's the point. Your automation processes the corpus; your eval tells you (and us) how much to trust it. **You are not expected to classify everything perfectly.** A thoughtful precision/recall tradeoff, honestly measured and clearly explained, beats a lucky output. Tell us your numbers on the dev set and what you'd expect them to be on the rest.

Two fair warnings, so the dev set doesn't mislead you: **the holdout contains cross-account clusters larger than any in the dev set** (the same new issue reported independently by up to four accounts, in different vocabulary — one ticket, several sources), and **some calls contain more than one item while many contain none.** And a scoping note: if you have to cut something to stay in the time-box, **do not cut the eval** — it's the highest-signal component of the exercise, and a smaller pipeline with a real eval beats a bigger pipeline with none.

Python 3.11+; the stubs use only the standard library. Run a stub directly (`python -m stubs.jira_stub`) to see the recorded-payload shape.

## Stack

Use what you'd actually reach for — your language, your orchestration approach (custom, an agent framework, an n8n/Zapier-style tool, or a mix), your eval and observability approach. We score *how you build*, not stack conformance. If you'd use a different tool for the production version than for this prototype, call that out.

## AI-tool use (allowed, expected, and disclosed)

Use AI tools — Claude, Claude Code, Copilot, Cursor, agents, whatever you build with normally. We do, every day. **The one rule: disclose it.** In your write-up, tell us which tools you used and for what — and specifically **where you wrote/designed versus delegated, where the AI got it wrong, and a concrete case where you rejected its output and why.** In the deep-dive we'll ask you to walk through code you personally wrote and explain how you verified what a tool generated. Code you can't explain or defend counts against you regardless of what wrote it.

## Write-up (1–2 pages, `WRITEUP.md` in your solution)

- What you built and the key design decisions.
- Where AI is and is not in the pipeline, and why.
- The hardest **engineering** problem (not the hardest prompt) and how you handled it.
- How you kept it idempotent / safe to re-run, and how you handled partial failure.
- What your eval catches and what would slip through; how you'd measure reliability across repeated runs.
- What attack / false-positive your guardrail defends and where the gap still is.
- How you validated it actually works.
- Your AI-tool disclosure (the seams: wrote vs. delegated, where you overrode it).
- What you'd do with another day, and what you deliberately left out.

## What we're evaluating

Mapped to the role's signals: **software-engineering depth** (weighted highest), **cross-system integration + reliability**, **AI judgment** (where the model belongs and where it doesn't), and **translator / stakeholder fit** (is the human-review output something a person could actually act on). "Great" is a clean, defensible, idempotent build with a real eval; "excellent" reads like someone who has shipped systems that survive real traffic. We'd rather see one piece done with production instincts than four pieces half-built.

## What happens next

You submit; we read your repo; the deep-dive is a ~60-minute screen-share where you walk us through your own code. Expect us to pull on real lines: trace a transcript through the pipeline, defend where AI is and isn't, show what your eval misses, show the trace a silent mis-file would leave, and walk the seams between what you wrote and what a tool generated. Build something you're proud to defend.
