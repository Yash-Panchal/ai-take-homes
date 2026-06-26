"""Local Jira sink for the take-home.

Stands in for the Jira API. Validates a minimal payload shape and appends it to
stubs/outbox/jira.jsonl instead of calling any API. No network, no credentials.

Intentionally naive: it does NOT de-duplicate. If you call it twice with the
same issue, you get two records. Idempotency is your job.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone

_OUTBOX = os.path.join(os.path.dirname(__file__), "outbox")
_JIRA_LOG = os.path.join(_OUTBOX, "jira.jsonl")

_REQUIRED = ("project", "type", "summary", "description")
_ALLOWED_TYPES = {"Bug", "Feature"}


def create_issue(payload: dict) -> dict:
    """Record a Jira issue the system WOULD create. Returns the stored record."""
    missing = [k for k in _REQUIRED if not payload.get(k)]
    if missing:
        raise ValueError(f"jira_stub: payload missing required fields: {missing}")
    if payload["type"] not in _ALLOWED_TYPES:
        raise ValueError(f"jira_stub: type must be one of {_ALLOWED_TYPES}")

    os.makedirs(_OUTBOX, exist_ok=True)
    existing = sum(1 for _ in open(_JIRA_LOG)) if os.path.exists(_JIRA_LOG) else 0
    record = {
        "key": f"PROJ-{1000 + existing + 1}",
        "recorded_at": datetime.now(timezone.utc).isoformat(),
        **payload,
    }
    with open(_JIRA_LOG, "a") as f:
        f.write(json.dumps(record) + "\n")
    return record


if __name__ == "__main__":
    demo = create_issue(
        {
            "project": "PROJ",
            "type": "Bug",
            "summary": "Demo issue",
            "description": "This is a demo of the Jira stub.",
            "priority": "P3",
            "source": {"call_id": "demo", "snippet": "…"},
        }
    )
    print("recorded:", demo)
