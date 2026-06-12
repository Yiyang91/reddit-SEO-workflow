#!/usr/bin/env python3
"""Regression checks for initialization, validation, run versioning, and migration."""

import json
from pathlib import Path
import subprocess
import sys
import tempfile


ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "core" / "scripts"


def run(*args: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [sys.executable, *args],
        check=False,
        capture_output=True,
        text=True,
    )


def main() -> int:
    with tempfile.TemporaryDirectory() as directory:
        project = Path(directory) / "sample-project"
        project.mkdir()
        (project / "README.md").write_text("# Sample\n", encoding="utf-8")

        initialized = run(
            str(SCRIPTS / "initialize_project.py"),
            "--project-root",
            str(project),
            "--summary",
            "A sample product",
            "--target-user",
            "sample users",
            "--subreddit",
            "r/example",
        )
        if initialized.returncode:
            print(initialized.stdout, initialized.stderr)
            return 1

        workflow = project / "ops" / "reddit-workflow"
        required = [
            "project-profile.json",
            "research/reddit-research-plan.md",
            "research/reddit-research-log.md",
            "strategy/product-feature-source-map.md",
            "content/draft-library.md",
        ]
        if any(not (workflow / item).is_file() for item in required):
            print("ERROR: initialization omitted required full-workflow files.")
            return 1

        profile = json.loads(
            (workflow / "project-profile.json").read_text(encoding="utf-8")
        )
        if profile["project"]["summary"] != "A sample product":
            print("ERROR: initialization profile mismatch.")
            return 1

        validated = run(
            str(SCRIPTS / "validate_project.py"),
            "--workflow-root",
            str(workflow),
        )
        if validated.returncode:
            print(validated.stdout, validated.stderr)
            return 1

        for _ in range(2):
            generated = run(
                str(SCRIPTS / "generate_run.py"),
                "--workflow-root",
                str(workflow),
                "--type",
                "old-popular",
                "--date",
                "2026-06-12",
            )
            if generated.returncode:
                print(generated.stdout, generated.stderr)
                return 1
        if not (workflow / "runs" / "old-popular-sweep-2026-06-12-v2.md").is_file():
            print("ERROR: same-day run versioning failed.")
            return 1

        plan = workflow / "research" / "reddit-research-plan.md"
        plan.unlink()
        preview = run(
            str(SCRIPTS / "migrate_project.py"),
            "--workflow-root",
            str(workflow),
        )
        if preview.returncode or plan.exists() or "add missing file" not in preview.stdout:
            print("ERROR: migration preview was not non-destructive.")
            return 1
        applied = run(
            str(SCRIPTS / "migrate_project.py"),
            "--workflow-root",
            str(workflow),
            "--apply",
        )
        if applied.returncode or not plan.is_file():
            print("ERROR: migration did not restore missing structure.")
            return 1

        legacy_project = Path(directory) / "legacy-project"
        legacy_workflow = legacy_project / "ops" / "reddit-workflow"
        legacy_workflow.mkdir(parents=True)
        legacy_log = legacy_workflow / "research" / "reddit-research-log.md"
        legacy_log.parent.mkdir()
        original_evidence = "# Existing Evidence\n\nDo not overwrite.\n"
        legacy_log.write_text(original_evidence, encoding="utf-8")

        refused = run(
            str(SCRIPTS / "initialize_project.py"),
            "--project-root",
            str(legacy_project),
            "--summary",
            "Legacy product",
        )
        if refused.returncode == 0:
            print("ERROR: existing workflow was initialized without adoption approval.")
            return 1

        adopted = run(
            str(SCRIPTS / "initialize_project.py"),
            "--project-root",
            str(legacy_project),
            "--summary",
            "Legacy product",
            "--adopt-existing",
        )
        if adopted.returncode:
            print(adopted.stdout, adopted.stderr)
            return 1
        if legacy_log.read_text(encoding="utf-8") != original_evidence:
            print("ERROR: adoption overwrote existing evidence.")
            return 1
        if not (legacy_workflow / "project-profile.json").is_file():
            print("ERROR: adoption did not create a project profile.")
            return 1

    print("Project workflow regression checks passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
