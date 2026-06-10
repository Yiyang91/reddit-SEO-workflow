#!/usr/bin/env python3
"""Inspect a project and suggest inputs for Reddit workflow initialization."""

from argparse import ArgumentParser
import json
from pathlib import Path


PRIMARY_CANDIDATES = [
    "README.md",
    "README.zh.md",
    "docs",
    "app",
    "web",
    "marketing",
    "supabase",
]


def scan(project_root: Path) -> dict:
    project_root = project_root.resolve()
    primary_sources = [
        item for item in PRIMARY_CANDIDATES if (project_root / item).exists()
    ]
    existing_workflow = project_root / "ops" / "reddit-workflow"
    return {
        "project_root": str(project_root),
        "inferred_project_name": project_root.name,
        "primary_product_sources_found": primary_sources,
        "existing_workflow": str(existing_workflow) if existing_workflow.exists() else None,
        "git_repository": (project_root / ".git").exists(),
        "questions_remaining": [
            "What is the one-sentence product summary?",
            "Who are the target users?",
            "What product stage is this?",
            "Which product claims or topics are forbidden or sensitive?",
            "Which subreddits should be prioritized?",
            "May the workflow generate gated drafts?",
            "May public Reddit output mention the product or include links?"
        ],
    }


def main() -> int:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", required=True)
    args = parser.parse_args()
    print(json.dumps(scan(Path(args.project_root)), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
