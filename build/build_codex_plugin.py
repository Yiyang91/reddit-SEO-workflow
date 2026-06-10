#!/usr/bin/env python3
"""Build the committed Codex plugin from platform-neutral core and adapter source."""

import json
from pathlib import Path
import shutil


REPO_ROOT = Path(__file__).resolve().parents[1]
CORE = REPO_ROOT / "core"
ADAPTER = REPO_ROOT / "adapters" / "codex" / "reddit-workflow"
PLUGIN = REPO_ROOT / "plugins" / "reddit-workflow"
SKILL = PLUGIN / "skills" / "reddit-workflow"


def copy_tree(source: Path, destination: Path) -> None:
    shutil.copytree(source, destination, dirs_exist_ok=True)


def main() -> int:
    if PLUGIN.exists():
        shutil.rmtree(PLUGIN)

    (PLUGIN / ".codex-plugin").mkdir(parents=True)
    SKILL.mkdir(parents=True)

    shutil.copy2(ADAPTER / "SKILL.md", SKILL / "SKILL.md")
    copy_tree(ADAPTER / "agents", SKILL / "agents")
    copy_tree(CORE / "references", SKILL / "references")
    copy_tree(CORE / "scripts", SKILL / "scripts")
    copy_tree(CORE / "schemas", SKILL / "schemas")
    copy_tree(CORE / "templates", SKILL / "templates")

    manifest = {
        "name": "reddit-workflow",
        "version": "0.1.0",
        "description": "Evidence-first Reddit research and Reddit-only content workflow",
        "author": {"name": "Yiyang91"},
        "skills": "./skills/",
        "interface": {
            "displayName": "Reddit Research Workflow",
            "shortDescription": "Reusable Reddit research and content workflow",
            "longDescription": (
                "Initialize and operate project-owned Reddit research, "
                "product-match, content-preparation, and monitoring workflows."
            ),
            "developerName": "Yiyang91",
            "category": "Productivity",
            "capabilities": [],
            "defaultPrompt": "Use $reddit-workflow to initialize this project."
        }
    }
    manifest_path = PLUGIN / ".codex-plugin" / "plugin.json"
    manifest_path.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"Built Codex plugin: {PLUGIN}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
