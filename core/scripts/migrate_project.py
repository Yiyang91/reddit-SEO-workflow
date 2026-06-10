#!/usr/bin/env python3
"""Preview or apply supported Reddit workflow project schema migrations.

Migrations may update workflow metadata and add missing template files, but
must never rewrite accumulated research evidence, pain points, or drafts.
"""

from argparse import ArgumentParser
import json
from pathlib import Path


CURRENT_SCHEMA_VERSION = 1


def main() -> int:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--workflow-root", required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()

    root = Path(args.workflow_root).resolve()
    profile_path = root / "project-profile.json"
    if not profile_path.is_file():
        print(f"Missing profile: {profile_path}")
        return 1
    profile = json.loads(profile_path.read_text(encoding="utf-8"))
    version = profile.get("schema_version")
    mode = "apply" if args.apply else "preview"
    print(f"Migration mode: {mode}")
    print(f"Workflow root: {root}")

    if version == CURRENT_SCHEMA_VERSION:
        print(f"No migration required. schema_version={CURRENT_SCHEMA_VERSION}")
        print("No files changed.")
        return 0
    if not isinstance(version, int):
        print(f"Unsupported schema_version: {version}")
        print("No files changed.")
        return 1
    if version > CURRENT_SCHEMA_VERSION:
        print(
            f"Project schema_version={version} is newer than this "
            f"tool supports ({CURRENT_SCHEMA_VERSION})."
        )
        print("Upgrade the installed workflow before touching project files.")
        print("No files changed.")
        return 1

    print(f"Migration required: {version} -> {CURRENT_SCHEMA_VERSION}")
    print("No legacy migrations are registered in this initial release.")
    print("No files changed.")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
