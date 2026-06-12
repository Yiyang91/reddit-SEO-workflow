#!/usr/bin/env python3
"""Print recurrence and confidence fields from project research files."""

from argparse import ArgumentParser
from pathlib import Path


FILES = (
    "research/pain-point-database.md",
    "research/pain-point-clusters.md",
)
KEYWORDS = (
    "cumulative recurrence",
    "cumulative_threads_count",
    "cumulative_comment_units_count",
    "cumulative_similar_user_count_observed",
    "confidence change",
    "confidence_change",
    "recurrence",
)


def main() -> int:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--workflow-root", required=True)
    args = parser.parse_args()
    root = Path(args.workflow_root).resolve()
    missing = [item for item in FILES if not (root / item).is_file()]
    if missing:
        for item in missing:
            print(f"Missing file: {item}")
        return 1

    found = False
    for relative in FILES:
        print(f"\n## {relative}")
        local_found = False
        for number, line in enumerate(
            (root / relative).read_text(encoding="utf-8").splitlines(), 1
        ):
            lowered = line.lower()
            if any(keyword in lowered for keyword in KEYWORDS):
                print(f"{number}: {line}")
                found = True
                local_found = True
        if not local_found:
            print("(No recurrence fields found.)")
    return 0 if found else 1


if __name__ == "__main__":
    raise SystemExit(main())
