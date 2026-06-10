#!/usr/bin/env python3
"""Create a project-owned Reddit workflow workspace and profile."""

from argparse import ArgumentParser
import json
from pathlib import Path
import shutil


SCRIPT_DIR = Path(__file__).resolve().parent
PACKAGE_ROOT = SCRIPT_DIR.parent
TEMPLATE_ROOT = PACKAGE_ROOT / "templates" / "project-workspace"


def build_profile(args: ArgumentParser, project_root: Path, workflow_root: Path) -> dict:
    return {
        "schema_version": 1,
        "project": {
            "name": args.name or project_root.name,
            "summary": args.summary,
            "target_users": args.target_user,
            "stage": args.stage,
            "language": args.language,
        },
        "paths": {
            "workflow_root": str(workflow_root.relative_to(project_root)),
            "primary_product_sources": args.primary_source,
            "derived_product_sources": args.derived_source,
        },
        "product": {
            "feature_id_prefix": args.feature_id_prefix,
            "forbidden_claims": args.forbidden_claim,
            "sensitive_topics": args.sensitive_topic,
        },
        "reddit": {
            "priority_subreddits": args.subreddit,
            "browser_access_required": True,
            "public_search_fallback": args.public_search_fallback,
            "allow_product_mention": args.allow_product_mention,
            "allow_links": args.allow_links,
        },
        "approvals": {
            "core_research_updates": "manual",
            "draft_generation": args.draft_generation,
            "posting": "manual",
            "replies": "manual",
        },
    }


def main() -> int:
    parser = ArgumentParser(description=__doc__)
    parser.add_argument("--project-root", required=True)
    parser.add_argument("--workflow-root", default="ops/reddit-workflow")
    parser.add_argument("--name")
    parser.add_argument("--summary", default="")
    parser.add_argument("--target-user", action="append", default=[])
    parser.add_argument("--stage", default="unknown")
    parser.add_argument("--language", default="en")
    parser.add_argument("--primary-source", action="append", default=[])
    parser.add_argument("--derived-source", action="append", default=[])
    parser.add_argument("--feature-id-prefix", default="F")
    parser.add_argument("--forbidden-claim", action="append", default=[])
    parser.add_argument("--sensitive-topic", action="append", default=[])
    parser.add_argument("--subreddit", action="append", default=[])
    parser.add_argument(
        "--public-search-fallback",
        choices=["forbidden", "limited", "allowed"],
        default="forbidden",
    )
    parser.add_argument(
        "--draft-generation",
        choices=["manual", "gated", "automatic"],
        default="gated",
    )
    parser.add_argument("--allow-product-mention", action="store_true")
    parser.add_argument("--allow-links", action="store_true")
    parser.add_argument("--force", action="store_true")
    args = parser.parse_args()

    project_root = Path(args.project_root).resolve()
    if not project_root.is_dir():
        parser.error(f"Project root does not exist: {project_root}")

    workflow_root = (project_root / args.workflow_root).resolve()
    try:
        workflow_root.relative_to(project_root)
    except ValueError:
        parser.error("Workflow root must remain inside the project root.")

    profile_path = workflow_root / "project-profile.json"
    if profile_path.exists() and not args.force:
        parser.error(f"Profile already exists: {profile_path}. Use --force to replace it.")

    workflow_root.mkdir(parents=True, exist_ok=True)
    shutil.copytree(TEMPLATE_ROOT, workflow_root, dirs_exist_ok=True)
    (workflow_root / "runs").mkdir(exist_ok=True)

    profile = build_profile(args, project_root, workflow_root)
    profile_path.write_text(
        json.dumps(profile, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Created Reddit workflow workspace: {workflow_root}")
    print(f"Created project profile: {profile_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
