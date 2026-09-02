# BetterBark issue triage

Run from `take-homes/applied-ai-engineer_AI` with Python 3.11+:

```text
pip install -r requirements.txt
set OPENAI_API_KEY=your-key
python solution/main.py discover
python solution/main.py eval
python solution/main.py approve <candidate-id> ...
```

This copy uses `solution/langgraph_agent.py`. The graph runs parse, model
extraction, structured validation, and candidate construction nodes. The LLM
is used only to propose issue intent and first-pass severity. External-speaker
filtering, evidence-line validation, existing-issue deduplication, human
approval, sink calls, idempotency, and observability remain deterministic.

Without `OPENAI_API_KEY` or the optional dependencies, discovery uses the
copied deterministic classifier so the exercise remains runnable offline.
Transcript content is always data: it cannot override the system prompt or
authorize a sink call.

`discover` parses transcripts, considers only external turns for issue evidence,
matches known issues, clusters new issues, and writes `solution/state/review_queue.json`.
It never calls either sink. Review the queue and approve explicitly. Delivery
state is stored per candidate and per sink, so a rerun does not repeat a Jira or
Slack write and a partial sink failure can be retried independently. Transcript
read/parse failures are isolated per file, reported under `errors`, counted in
`metrics.failed_transcripts`, and appended to `events.jsonl`; healthy calls
still produce a queue.

The classifier is deterministic in this offline exercise. Each discovery
report records this explicitly under `ai_placement`. In production, a
structured model extraction step could propose candidates and first-pass
severity after parsing, because issue intent and severity are the judgment-heavy
parts. The parser, untrusted-transcript boundary, schema validation,
deduplication, review gate, state transitions, and sink adapters remain
deterministic. The raw transcript is the source of truth and is retained in
every candidate's evidence; invalid or unsupported model output is quarantined
instead of being delivered.

Discovery reports use `run_status` (`ok` or `degraded`) and include parsed and
failed transcript counts. `events.jsonl` provides structured lifecycle events,
candidate creation events, transcript failures, sink attempts/outcomes, and
idempotent skips. A scheduler can alert when a completion event is missing,
the run is degraded, throughput is unexpectedly zero, or filing volume changes
sharply.