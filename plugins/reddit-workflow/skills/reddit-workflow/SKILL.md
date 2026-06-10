---
name: reddit-workflow
description: Initialize and operate an evidence-first Reddit research and Reddit-only content workflow for any product project. Use when the user asks to initialize a Reddit workflow, scan fresh Reddit posts, deep-read old popular threads, classify pain points, update cumulative recurrence, run a Product-Match Gate, prepare Reddit posts or replies, perform final subreddit checks, or monitor published Reddit output.
---

# Reddit Workflow

## Start With Project Context

Locate the repository root. Look for `ops/reddit-workflow/project-profile.json`.

If it is missing:

1. Run `scripts/scan_project.py --project-root <repo-root>`.
2. Read `references/project-initialization.md`.
3. Read likely primary product sources discovered by the scan.
4. Ask only for material fields that cannot be inferred safely:
   - product summary and target users
   - product stage and language
   - forbidden claims and sensitive topics
   - priority subreddits
   - product mention and link policy
   - draft-generation approval mode
5. Show the proposed profile and workspace path.
6. Initialize only after the user approves the proposed configuration.
7. Run `scripts/validate_project.py`.

Never copy evidence, pain points, drafts, or product facts from another project.

## Route The Command

- `Prepare Reddit workflow task`: validate structure, profile, duplicate URLs, and current recurrence without modifying project data.
- `Run Daily Reddit Workflow`: scan fresh posts neutrally, write the run file, and enter A -> B -> C0 -> C1 -> C2 -> C3 only when evidence and gates justify it.
- `Run Old Popular Backlog Sweep`: deep-read old high-discussion threads using browser-opened comments and the sampling rules.
- `Review run for core updates`: propose research database updates without applying them.
- `Apply approved core updates`: apply only approved evidence changes, then validate.
- `Run C4 Final Posting Check`: check live subreddit rules and prepare a posting decision without posting.
- `Run C5 Monitoring`: monitor published output without replying automatically.
- `Upgrade Reddit Workflow Project`: run `scripts/migrate_project.py` in preview mode first and apply only after approval.

## Load References As Needed

- Read `references/research-methodology.md` and `references/recurrence-rules.md` for Stage A work.
- Read `references/product-match-gate.md` before Stage B or any product-mentioned output.
- Read `references/content-pipeline.md` for C0-C5.
- Read `references/reddit-safety.md` before public-facing decisions.

## Browser Evidence

Use authenticated browser control when the project profile requires it. Read visible Reddit pages and comments directly. Do not substitute public JSON, search snippets, or indexed excerpts when the profile forbids fallback.

If authenticated browser access or comments are unavailable, stop the evidence pass and record the limitation. Never invent comments.

## Project Data Boundaries

- Write accumulated evidence only inside the target project's workflow workspace.
- Do not modify the installed Skill or Plugin during a project run.
- Do not update core research files unless the configured approval rule and user approval allow it.
- Do not post or reply automatically.
- Do not commit or push unless explicitly requested.

## Product Claims

Read primary product sources listed in `project-profile.json` before relying on derived summaries. Run the Product-Match Gate before any product-mentioned draft. Mark unresolved conflicts and omit disputed claims.

## Output Discipline

Keep Stage A neutral. Preserve traceability from evidence through product matching to content. Prefer observe-only, reply-only, postpone, or do-not-post when evidence or safety gates fail.
