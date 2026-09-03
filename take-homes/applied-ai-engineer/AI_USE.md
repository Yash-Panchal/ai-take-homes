# AI Use Disclosure

## Tool used

I used GitHub Copilot throughout the take-home. I used it for repository
exploration, implementation assistance, and review of local evaluation output.

## What I wrote and designed

I wrote and owned the overall pipeline design and the engineering decisions,
including:

- the deterministic transcript parser and external-speaker trust boundary;
- the LangGraph state flow and the boundary for structured model proposals;
- known-issue matching, new-issue clustering, and candidate identity rules;
- the human approval gate and independent Jira and Slack delivery state;
- idempotency and partial-failure handling;
- evaluation criteria, observability events, and the offline fallback behavior.

I reviewed the final implementation and can explain every submitted line and
the decisions behind it.

## What I delegated to AI assistance

I delegated repository search and navigation, implementation suggestions for
local code paths, and inspection of evaluation output to GitHub Copilot. I
kept suggestions only after checking them against the exercise requirements,
transcript evidence, existing issue data, and executable tests. I did not
delegate product or safety judgment.

## Corrections and overrides

During review, the AI-assisted implementation initially treated a broad
product-term match as sufficient evidence. I corrected that behavior so vague
or internal-only mentions are not promoted to issues, and verified the change
against the labeled cases. I also rejected any interpretation of instructions
inside transcript text as executable commands. Call 005 is an explicit test of
that boundary: transcript content remains data and cannot authorize a sink
call.

The documented offline evaluation passes all 15 labeled cases. The final
implementation keeps transcript parsing, evidence validation, deduplication,
human approval, sink calls, idempotency, and observability deterministic; a
model, when configured, only proposes structured issue intent and first-pass
severity.
