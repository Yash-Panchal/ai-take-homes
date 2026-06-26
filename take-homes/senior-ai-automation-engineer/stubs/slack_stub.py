"""Local Slack sink for the take-home.

Stands in for the Slack API. Validates a minimal payload shape and appends it to
stubs/outbox/slack.jsonl instead of calling any API. No network, no credentials.

Intentionally naive: it does NOT de-duplicate.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone

_OUTBOX = os.path.join(os.path.dirname(__file__), "outbox")
_SLACK_LOG = os.path.join(_OUTBOX, "slack.jsonl")

_REQUIRED = ("channel", "text")


def post_message(payload: dict) -> dict:
    """Record a Slack message the system WOULD post. Returns the stored record."""
    missing = [k for k in _REQUIRED if not payload.get(k)]
    if missing:
        raise ValueError(f"slack_stub: payload missing required fields: {missing}")

    os.makedirs(_OUTBOX, exist_ok=True)
    record = {
        "ts": datetime.now(timezone.utc).isoformat(),
        **payload,
    }
    with open(_SLACK_LOG, "a") as f:
        f.write(json.dumps(record) + "\n")
    return record


if __name__ == "__main__":
    demo = post_message({"channel": "#cs-owner", "text": "Demo notification."})
    print("recorded:", demo)
