# Project Initialization And Migration

## Scan First

Infer:

- repository root and Git availability
- project name
- likely primary product sources
- likely derived summaries
- existing workflow location
- current workflow files that may predate the plugin

Ask only for material unknowns:

- one-sentence product summary
- target users
- product stage and language
- forbidden claims and sensitive topics
- priority subreddits and research vocabulary
- product mention and link policy
- draft-generation and core-update approval modes

Show the proposed `project-profile.json` and target paths before creating or
changing files.

## Initialize

Create:

- profile
- project research plan
- research, strategy, content, and runs directories
- structured core file templates

Then validate the workspace. Never import evidence or conclusions from another
project.

## Existing Project Adoption

When `ops/reddit-workflow/` already contains a pre-plugin workflow:

1. Inventory every file.
2. Treat existing evidence, pain points, strategy, drafts, and runs as
   project-owned data.
3. Create a proposed profile from existing product and workflow documents.
4. Compare current structure with the plugin's required file contracts.
5. Add missing metadata or templates without replacing populated files.
6. Preserve original filenames through a documented mapping when renaming is
   unnecessary.
7. Validate before normal operation.

Do not reduce a mature project to empty templates.

## Data Separation

The installed Skill owns:

- methodology
- command and file contracts
- schemas
- blank templates
- deterministic helper scripts

The project owns:

- product facts and source paths
- Reddit evidence and CTUs
- pain points and recurrence
- feature matches
- content angles and drafts
- run records and publication learning

## Migration

Use `schema_version`. Always preview migrations.

A migration may:

- add missing blank files
- add profile fields with explicit defaults
- add non-destructive headings or metadata
- update validation requirements

A migration must not overwrite or silently rewrite accumulated evidence,
pain points, clusters, source maps, angles, drafts, or run records.
