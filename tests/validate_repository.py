#!/usr/bin/env python3
"""Validate source layout, JSON files, and generated Codex plugin output."""

import json
from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]

REQUIRED = [
    "README.md",
    "core/schemas/project-profile.schema.json",
    "core/references/research-methodology.md",
    "core/references/project-initialization.md",
    "core/references/command-contracts.md",
    "core/references/file-contracts.md",
    "core/references/operations-manual.md",
    "core/references/review-approval.md",
    "core/references/content-pipeline.md",
    "core/references/product-match-gate.md",
    "core/references/recurrence-rules.md",
    "core/references/reddit-safety.md",
    "core/templates/project-workspace/research/reddit-research-plan.md",
    "core/templates/project-workspace/research/reddit-research-log.md",
    "core/scripts/initialize_project.py",
    "core/scripts/migrate_project.py",
    "core/scripts/check_duplicate_urls.py",
    "core/scripts/check_structure.py",
    "core/scripts/summarize_recurrence.py",
    "adapters/codex/reddit-workflow/SKILL.md",
    "adapters/codex/reddit-workflow/agents/openai.yaml",
    "build/build_codex_plugin.py",
    ".agents/plugins/marketplace.json",
]


def fail(message: str) -> int:
    print(f"ERROR: {message}")
    return 1


def main() -> int:
    missing = [item for item in REQUIRED if not (ROOT / item).is_file()]
    if missing:
        return fail("Missing required files: " + ", ".join(missing))

    for relative in [
        "core/schemas/project-profile.schema.json",
        "core/schemas/comment-thread-unit.schema.json",
        "core/schemas/run-record.schema.json",
        "examples/minimal-project-profile.json",
        "examples/feelune-profile.example.json",
        ".agents/plugins/marketplace.json",
    ]:
        try:
            json.loads((ROOT / relative).read_text(encoding="utf-8"))
        except json.JSONDecodeError as exc:
            return fail(f"Invalid JSON in {relative}: {exc}")

    result = subprocess.run(
        [sys.executable, str(ROOT / "build" / "build_codex_plugin.py")],
        cwd=ROOT,
        check=False,
    )
    if result.returncode:
        return fail("Codex plugin build failed.")

    generated = [
        "plugins/reddit-workflow/.codex-plugin/plugin.json",
        "plugins/reddit-workflow/skills/reddit-workflow/SKILL.md",
        "plugins/reddit-workflow/skills/reddit-workflow/scripts/initialize_project.py",
        "plugins/reddit-workflow/skills/reddit-workflow/scripts/migrate_project.py",
        "plugins/reddit-workflow/skills/reddit-workflow/references/project-initialization.md",
        "plugins/reddit-workflow/skills/reddit-workflow/references/command-contracts.md",
        "plugins/reddit-workflow/skills/reddit-workflow/references/operations-manual.md",
        "plugins/reddit-workflow/skills/reddit-workflow/scripts/check_structure.py",
        "plugins/reddit-workflow/skills/reddit-workflow/scripts/summarize_recurrence.py",
        "plugins/reddit-workflow/skills/reddit-workflow/templates/daily-run.md",
        "plugins/reddit-workflow/skills/reddit-workflow/templates/project-workspace/research/reddit-research-plan.md",
    ]
    missing_generated = [item for item in generated if not (ROOT / item).is_file()]
    if missing_generated:
        return fail("Missing generated files: " + ", ".join(missing_generated))

    duplicate_test = subprocess.run(
        [sys.executable, str(ROOT / "tests" / "test_duplicate_urls.py")],
        cwd=ROOT,
        check=False,
    )
    if duplicate_test.returncode:
        return fail("Duplicate URL regression checks failed.")

    workflow_test = subprocess.run(
        [sys.executable, str(ROOT / "tests" / "test_project_workflow.py")],
        cwd=ROOT,
        check=False,
    )
    if workflow_test.returncode:
        return fail("Project workflow regression checks failed.")

    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
