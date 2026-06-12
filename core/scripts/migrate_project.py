#!/usr/bin/env python3
"""Preview or apply supported Reddit workflow project schema migrations.

Migrations may update workflow metadata and add missing template files, but
must never rewrite accumulated research evidence, pain points, or drafts.
"""

from argparse import ArgumentParser
import json
from pathlib import Path
import shutil


CURRENT_SCHEMA_VERSION = 1
PACKAGE_ROOT = Path(__file__).resolve().parent.parent
TEMPLATE_ROOT = PACKAGE_ROOT / "templates" / "project-workspace"


def template_files() -> dict[str, Path]:
    return {
        str(path.relative_to(TEMPLATE_ROOT)): path
        for path in TEMPLATE_ROOT.rglob("*")
        if path.is_file()
    }


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
        missing = {
            relative: source
            for relative, source in template_files().items()
            if not (root / relative).exists()
        }
        if not missing:
            print(f"No migration required. schema_version={CURRENT_SCHEMA_VERSION}")
            print("No files changed.")
            return 0
        print("Non-destructive structure additions available:")
        for relative in sorted(missing):
            print(f"- add missing file: {relative}")
        if not args.apply:
            print("Preview only. Re-run with --apply after approval.")
            return 0
        for relative, source in missing.items():
            destination = root / relative
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
        print(f"Added {len(missing)} missing file(s).")
        print("Existing project files were not overwritten.")
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
