#!/usr/bin/env python3
"""Validate a project-owned Reddit workflow structure."""

from argparse import ArgumentParser
from pathlib import Path


REQUIRED_FILES = (
    "project-profile.json",
    "README.md",
    "research/reddit-research-plan.md",
    "research/reddit-research-log.md",
    "research/pain-point-database.md",
    "research/pain-point-clusters.md",
    "strategy/product-feature-source-map.md",
    "strategy/feature-match-matrix.md",
    "content/content-angle-bank.md",
    "content/draft-library.md",
)
REQUIRED_DIRS = ("research", "strategy", "content", "runs")


def main() -> int:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--workflow-root", required=True)
    args = parser.parse_args()
    root = Path(args.workflow_root).resolve()

    missing_dirs = [item for item in REQUIRED_DIRS if not (root / item).is_dir()]
    missing_files = [item for item in REQUIRED_FILES if not (root / item).is_file()]

    print(f"Checking Reddit workflow structure: {root}")
    if not missing_dirs and not missing_files:
        print("Structure check passed.")
        return 0
    for item in missing_dirs:
        print(f"Missing directory: {item}")
    for item in missing_files:
        print(f"Missing file: {item}")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
