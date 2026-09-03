## What I built

This `_AI` copy adds a constrained LangGraph orchestration layer in
`solution/agent.py`. Its nodes parse a call, send only filtered
external evidence to a structured LLM classifier, validate the proposal, and
construct the existing review-queue candidate format. `OPENAI_API_KEY` enables
the model path; otherwise the copied deterministic classifier is used as an
offline fallback.

`solution/main.py` is a small standard-library pipeline with three explicit
operations:

- `discover` parses the 140 transcripts, considers only external turns as
	customer evidence, matches corroborations against `existing_issues.json`,
	clusters repeated new symptoms, and writes `solution/state/review_queue.json`.
- `approve` delivers only an explicitly selected review queue through the local
	Jira and Slack stubs.
- `eval` scores the labeled calls 001-015 and writes an auditable case report.

The queue is the human gate. It includes the proposed Jira fields, severity and
priority, call owner, account, candidate signature, confidence, and exact
external-speaker transcript turns. Discovery never calls a sink. Embedded text
such as the fake wire-transfer instruction in call 005 is data, never a command.

## Design decisions

The offline exercise uses deterministic extraction rather than inventing a
model dependency or requiring credentials. Regexes identify concrete product
areas, while explicit negative evidence rejects internal-only calls, hearsay,
vague complaints, resolved customer-side errors, shipped requests, cosmetic
remarks, and explicit retractions. Known issue matching is field-aware enough
to distinguish the Azure AD post-password-change redirect loop from the Okta
session-expiry issue. New reports use a stable issue signature, so the search
staleness reports become one candidate with multiple sources.

In a production version I would put a structured model call after the parser
for the judgment-heavy extraction and severity proposal. The executable report
records this boundary under `ai_placement`: the current run is
`deterministic-offline`, while the model's role is only to propose structured
candidates and first-pass severity. Its JSON would be schema-validated against
the raw transcript and quarantined on failure or unsupported evidence. The
transcript parser, external/internal trust boundary, dedupe rules, review gate,
state machine, and sink adapters would remain deterministic. The raw
transcript remains the source of truth and is retained in every candidate's
evidence. `approve` persists independent `jira_status` and
`slack_status` records before future retries. A Jira success therefore is not
repeated if Slack fails, and a rerun skips both already-sent operations. The
stubs are intentionally naive, so this local delivery state is the idempotency
authority. Transcript read/parse failures are caught per file, reported in the
run report, counted in metrics, and recorded in JSONL while the remaining
transcripts continue through discovery.

## Evaluation and observability

The dev eval defines a pass at the issue-count/type level, exact known-issue
target level, correct separation of multiple issues in a call, and no output
for calls labeled with no issue. It reports 15 case results rather than only a
single aggregate, and the executable result records the pass definition and
reliability protocol. The current deterministic run passes all 15 cases. A
model-backed version would run every case N times with the same labels and
report per-case stability as `passing runs / total runs`; any case below 100%
stability would be sent to `needs-review`, even if its aggregate accuracy were
high. Aggregate accuracy would be reported alongside, never instead of, this
per-case stability.

The run report includes transcript counts, parsed and failed transcript counts,
external-call counts, new candidates, corroborations, AI mode, and an `ok` or
`degraded` status. `events.jsonl` records structured
`discovery_completed`/`approval_completed` lifecycle events, candidate IDs,
actions, run IDs, source calls, transcript failures, sink attempts, sink
successes, sink failures, and idempotent rerun skips. This makes an unattended
run distinguish a silent stop from a healthy zero-candidate run, and a genuine
miss can be compared with the per-case eval report rather than inferred from
the aggregate filing count. Production alerting should page on missing
completion events, parse/model-validation failures, unexpected zero throughput,
or a sudden increase in filing rate.

## Validation and tradeoffs

I ran the eval against all 15 labeled calls and a full discovery pass over all
140 transcripts. The full pass produced 23 clustered review candidates: 9 new
issues and 14 corroborations. The remaining limitation is intentionally small
scope: this is an offline deterministic fallback plus a LangGraph model path,
not a hosted model deployment or review UI. The model path was not exercised
here because no API key is configured; the structured-output and evidence-line
validation boundary is implemented. Another day would go toward a richer
field-aware similarity layer, an interactive approve/edit screen,
property-based parser tests, and repeated model-run calibration on the holdout
set.

## AI-tool disclosure

I used GitHub Copilot for repository exploration, implementation, and review of
the local eval output. I wrote the pipeline structure, LangGraph state flow,
and safety boundaries, then used targeted inspection of the labeled failures to
correct regex scope, known-issue suppression, and clustered-eval accounting.
During review, the AI-assisted implementation initially treated a broader
product-term match as sufficient evidence and needed correction so vague or
internal-only mentions were not promoted to issues. I also overrode any
interpretation of transcript instructions as executable; call 005 is an
explicit test of that boundary. I reviewed and can explain each submitted
line, including the delegated suggestions I kept.
