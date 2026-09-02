"""LangGraph entry point for the BetterBark issue-triage pipeline."""

from __future__ import annotations

import argparse

from langgraph_agent import approve, discover, evaluate


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("discover", help="run LangGraph discovery and build the review queue")
    sub.add_parser("eval", help="run the labeled evaluation")
    approve_parser = sub.add_parser("approve", help="deliver approved candidates idempotently")
    approve_parser.add_argument("candidate_ids", nargs="*", help="candidate IDs; omit to approve all")
    args = parser.parse_args()
    if args.command == "discover":
        report = discover()
        print(report["metrics"])
        return 0
    if args.command == "eval":
        return evaluate()
    return approve(args.candidate_ids)


if __name__ == "__main__":
    raise SystemExit(main())
