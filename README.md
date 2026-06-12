# Reddit Research and Content Workflow

A complete, evidence-first, project-configurable workflow for Reddit research,
product matching, Reddit-native content preparation, posting checks, and
post-publication learning.

## Repository Status

This is a private, proprietary repository. No open-source license is granted.
See [`NOTICE`](NOTICE). All rights reserved.

The repository is platform-aware but platform-independent at its core:

- `core/` contains schemas, research rules, templates, and deterministic scripts.
- `adapters/codex/` contains the Codex Skill.
- `plugins/reddit-workflow/` is the generated Codex Plugin distributed through the repository marketplace.
- Project research data stays in each target project and is never stored in this mother repository.

## Current Scope

The first implementation supports Codex only. The core avoids Codex-specific browser and permission instructions so future adapters can be added for Claude Code, Cursor, or generic agents without duplicating the research methodology.

## Install In Codex

Add this repository as a plugin marketplace:

```bash
codex plugin marketplace add Yiyang91/reddit-SEO-workflow
```

Then install the `reddit-workflow` plugin and start a new Codex thread.

Upgrade later with:

```bash
codex plugin marketplace upgrade
```

## First Use In A Project

Invoke the skill explicitly:

```text
Use $reddit-workflow to initialize this project.
```

The initializer creates a project-owned workspace, normally:

```text
ops/reddit-workflow/
├── project-profile.json
├── research/
├── strategy/
├── content/
└── runs/
```

The Skill scans the project first, then asks only for material information that cannot be inferred safely.

## Full Workflow Coverage

The plugin preserves the complete operating model:

- neutral fresh-post and old-popular research tracks
- authenticated comment-thread evidence and A3 sampling rules
- duplicate and revisit gates
- pain-point and cumulative recurrence maintenance
- primary-versus-derived product source hierarchy
- Product-Match Gate
- C0-C5 Reddit content and monitoring stages
- Light and Full review rules
- explicit human approval boundaries
- complete command contracts, file responsibilities, and run templates

Detailed methodology lives under `core/references/` and is copied into the
installed Skill. Project data remains in each project's
`ops/reddit-workflow/`.

## Project Upgrades

Plugin upgrades replace the installed workflow code, not project-owned research
data. After upgrading the Plugin, preview any project schema migration:

```text
Use $reddit-workflow to upgrade this Reddit workflow project.
```

The Skill runs migrations in preview mode first and applies them only after
approval. Existing evidence, pain points, drafts, and run records are not
overwritten by upgrades.

## Development

Build the committed Codex Plugin from `core/` and `adapters/codex/`:

```bash
python3 build/build_codex_plugin.py
```

Validate source and generated artifacts:

```bash
python3 tests/validate_repository.py
```

Do not edit `plugins/reddit-workflow/` manually. Change `core/` or `adapters/codex/`, then rebuild.
