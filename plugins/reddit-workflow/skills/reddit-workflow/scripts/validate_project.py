#!/usr/bin/env python3
"""Validate a project-owned Reddit workflow workspace without external packages."""

from argparse import ArgumentParser
import json
from pathlib import Path


REQUIRED_PATHS = [
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
    "runs",
]


def main() -> int:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--workflow-root", required=True)
    args = parser.parse_args()
    root = Path(args.workflow_root).resolve()

    missing = [item for item in REQUIRED_PATHS if not (root / item).exists()]
    if missing:
        print("Missing workflow items:")
        for item in missing:
            print(f"- {item}")
        return 1

    try:
        profile = json.loads((root / "project-profile.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Invalid project-profile.json: {exc}")
        return 1

    required_top = {"schema_version", "project", "paths", "product", "reddit", "approvals"}
    missing_keys = sorted(required_top - profile.keys())
    if missing_keys:
        print("Missing profile keys: " + ", ".join(missing_keys))
        return 1
    if profile["schema_version"] != 1:
        print(f"Unsupported schema_version: {profile['schema_version']}")
        return 1

    configured_root = profile.get("paths", {}).get("workflow_root")
    if not isinstance(configured_root, str) or not configured_root:
        print("Invalid paths.workflow_root.")
        return 1

    for key in ("primary_product_sources", "derived_product_sources"):
        value = profile.get("paths", {}).get(key)
        if not isinstance(value, list):
            print(f"Invalid paths.{key}; expected a list.")
            return 1

    print(f"Workflow validation passed: {root}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
