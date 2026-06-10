#!/usr/bin/env python3
"""Generate a daily, old-popular, or C5 run file from bundled templates."""

from argparse import ArgumentParser
from datetime import date
import json
from pathlib import Path


PACKAGE_ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_ROOT = PACKAGE_ROOT / "templates"


def main() -> int:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--workflow-root", required=True)
    parser.add_argument("--type", choices=["daily", "old-popular", "c5"], required=True)
    parser.add_argument("--date", default=date.today().isoformat())
    parser.add_argument("--draft-id", default="DRAFT_ID")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    root = Path(args.workflow_root).resolve()
    profile = json.loads((root / "project-profile.json").read_text(encoding="utf-8"))
    project_name = profile["project"]["name"]
    template_name = {
        "daily": "daily-run.md",
        "old-popular": "old-popular-sweep.md",
        "c5": "c5-log.md",
    }[args.type]
    output_name = {
        "daily": f"daily-run-{args.date}.md",
        "old-popular": f"old-popular-sweep-{args.date}.md",
        "c5": f"c5-log-{args.draft_id}.md",
    }[args.type]
    output = root / "runs" / output_name
    output.parent.mkdir(exist_ok=True)
    if output.exists() and not args.force:
        print(f"File already exists: {output}")
        return 1

    text = (TEMPLATE_ROOT / template_name).read_text(encoding="utf-8")
    text = text.replace("{{DATE}}", args.date)
    text = text.replace("{{PROJECT_NAME}}", project_name)
    text = text.replace("{{DRAFT_ID}}", args.draft_id)
    output.write_text(text, encoding="utf-8")
    print(f"Created {output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
