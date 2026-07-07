# The June Tapes — Senior Applied AI Engineer Take-Home

*A month of customer calls. Do something useful with them.*

Welcome, and thanks for the time. This is a small but real slice of the actual job. Spend **2–3 hours** — please don't gold-plate. A tight, well-engineered small build beats a sprawling half-finished one; if you run out of time, stub the lowest-value piece and say so in your write-up.

It is the spine of the loop: submit it **at least 24 hours before your technical deep-dive**, which is a working session on your solution — how you approached the problem, and how you know it works. Build something you can stand behind.

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
- **An eval.** A small eval over the provided transcripts with a pass/fail definition a second engineer would independently agree with. The model is non-deterministic, so say how you'd measure reliability across repeated runs (does a case that passes once pass every time?), not just a single green run.
- **Observability.** Structured logs or a trace such that, if this ran unattended and silently started mis-filing (or silently stopped), someone could tell from the output — and could tell a genuine miss from the grader being wrong.

## What's provided (in this folder)

- `transcripts/` — **140 mock call transcripts** (`call-001` … `call-140`), each marking `[EXTERNAL]` vs `[INTERNAL]` speakers: long, meandering, realistic calls between customers and the team, in all their variety.
- `data/existing_issues.json` — the currently tracked (and recently shipped) issues, for de-duplication.
- `data/dev_labels.json` — **a labeled dev set: expected outcomes for calls 001–015.** Build and tune your eval against these. The other 125 calls are the holdout we grade.
- `stubs/` — local Jira and Slack sinks (`jira_stub.py`, `slack_stub.py`). They validate and **record the payload they would send** to `stubs/outbox/` — no network, no credentials. They're intentionally naive: they do **not** de-duplicate. Idempotency is your job.

**On the dev set:** build and tune your eval against the labeled calls; report your numbers on them and what you expect on the rest.


Python 3.11+; the stubs use only the standard library. Run a stub directly (`python -m stubs.jira_stub`) to see the recorded-payload shape.

## Stack

Use what you'd actually reach for — your language, your orchestration approach (custom, an agent framework, an n8n/Zapier-style tool, or a mix), your eval and observability approach. We score *how you build*, not stack conformance. If you'd use a different tool for the production version than for this prototype, call that out.

## AI-tool use (allowed, expected, and disclosed)

Use AI tools — Claude, Claude Code, Copilot, Cursor, agents, whatever you build with normally. We do, every day. **The one rule: disclose it.** In your write-up, tell us which tools you used and for what — and specifically **where you wrote/designed versus delegated, where the AI got it wrong, and a concrete case where you rejected its output and why.** In the deep-dive, expect to speak to any part of your solution and the decisions behind it — including what you delegated and how you verified it.

## Write-up (1–2 pages, `WRITEUP.md` in your solution)

- What you built and the key design decisions.
- Where AI is and is not in the pipeline, and why.
- The hardest **engineering** problem (not the hardest prompt) and how you handled it.
- How you kept it idempotent / safe to re-run, and how you handled partial failure.
- What your eval catches and what would slip through; how you'd measure reliability across repeated runs.
- How you validated it actually works.
- Your AI-tool disclosure (the seams: wrote vs. delegated, where you overrode it).
- What you'd do with another day, and what you deliberately left out.

## What we're evaluating

Mapped to the role's signals: **software-engineering depth** (weighted highest), **cross-system integration + reliability**, **AI judgment** (where the model belongs and where it doesn't), and **translator / stakeholder fit** (is the human-review output something a person could actually act on). "Great" is a clean, defensible, idempotent build with a real eval; "excellent" reads like someone who has shipped systems that survive real traffic. We'd rather see one piece done with production instincts than four pieces half-built.

## What happens next

You submit; we read your repo; the deep-dive is a ~60-minute working session on your solution: the problem, your approach, your results, and the choices you made along the way. Come ready to show it running. Build something you're proud to stand behind.
