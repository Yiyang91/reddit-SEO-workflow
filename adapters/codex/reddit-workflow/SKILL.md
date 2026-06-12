---
name: reddit-workflow
description: Initialize and operate a project-owned, evidence-first Reddit research and Reddit-only content workflow. Use for project onboarding, workflow preparation, fresh-post scans, old-popular backlog sweeps, comment-thread evidence collection, pain-point classification, recurrence updates, Product-Match Gates, Reddit angle or draft preparation, C2/C3 review, C4 final posting checks, C5 monitoring, approved research updates, or workflow migrations.
---

# Reddit Workflow

Treat the installed Skill as methodology and tooling. Treat
`ops/reddit-workflow/` inside the target project as the only home for project
facts, evidence, strategy, drafts, and run records.

## Resolve Context

1. Locate the project root.
2. Look for `ops/reddit-workflow/project-profile.json`.
3. If it is missing, read `references/project-initialization.md`, run
   `scripts/scan_project.py`, inspect primary project sources, propose a
   profile, and initialize only after approval.
4. If it exists, read it before opening Reddit, classifying evidence, matching
   product features, or generating content.
5. Run `scripts/validate_project.py` before substantive work.

Never copy evidence, pain points, product facts, drafts, or recurrence values
between projects.

## Load The Governing Contract

Always read `references/command-contracts.md` and the command-specific
references below before executing a workflow command.

| Command or task | Required references |
| --- | --- |
| Prepare Reddit workflow task | `file-contracts.md`, `review-approval.md` |
| Run Daily Reddit Workflow | `research-methodology.md`, `recurrence-rules.md`, `content-pipeline.md`, `product-match-gate.md`, `reddit-safety.md` |
| Run Old Popular Backlog Sweep | `research-methodology.md`, `recurrence-rules.md`, `reddit-safety.md`, then B/C references only if a test pipeline is justified |
| Review run for core updates | `research-methodology.md`, `recurrence-rules.md`, `review-approval.md` |
| Apply approved core updates | `file-contracts.md`, `recurrence-rules.md`, `review-approval.md` |
| Run C4 Final Posting Check | `content-pipeline.md`, `product-match-gate.md`, `reddit-safety.md` |
| Run C5 Monitoring | `content-pipeline.md`, `recurrence-rules.md`, `review-approval.md` |
| Upgrade Reddit Workflow Project | `project-initialization.md`, `file-contracts.md` |

When detailed rationale, examples, file ownership, or team review criteria are
needed, also read `references/operations-manual.md`.

## Execute In Stage Order

- Stage A: collect visible Reddit evidence neutrally.
- Stage B: match classified pain points to verified product features.
- C0: create Reddit-native angle candidates.
- C1: create a Standalone Reddit Post or Reply Comment candidate.
- C2: run Light or Full editorial and risk review.
- C3: prepare safest/growth/postpone/do-not-post decisions.
- C4: check live subreddit context before posting; never post automatically.
- C5: monitor published output and propose learning updates; never reply
  automatically.

Do not skip directly from a user pain point to product content. Preserve the
traceability chain from visible evidence through classification, recurrence,
product match, content decision, and review.

## Browser Evidence

Use authenticated browser control when required by the profile. Formal
comment-thread evidence must come from visible Reddit pages and comments.
Never substitute search snippets, public JSON, or indexed excerpts when the
profile forbids fallback. If comments are inaccessible, record the limitation
and stop or replace the candidate. Never invent comments.

## Data And Approval Boundaries

- Write working findings to a run file first.
- Do not update core research files without the configured approval and the
  user's explicit approval.
- Do not overwrite existing run files; create a versioned filename.
- Do not use unresolved or derived-only product claims in public content.
- Do not post, reply, commit, push, deploy, or publish unless explicitly
  requested and separately authorized.
- Keep all output Reddit-only.

## Deterministic Tools

Use bundled scripts for scanning, initialization, validation, duplicate URL
checks, recurrence summaries, run-file generation, and migrations. Scripts do
not replace browser reading or human/model judgment.
