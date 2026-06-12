# Reddit Workflow Documentation

This page is the human-readable map of the complete workflow. The short
commands in `README.md` are entry points only; they delegate to the rules
listed here.

## Where The Complete Rules Live

The authoritative source is `core/references/`. The built Codex Plugin contains
the same files under
`plugins/reddit-workflow/skills/reddit-workflow/references/`.

Read these files in this order for a complete understanding:

1. [`operations-manual.md`](core/references/operations-manual.md) explains why
   the workflow separates evidence, product matching, content, approval, and
   monitoring.
2. [`command-contracts.md`](core/references/command-contracts.md) defines
   exactly what every short command may do, may modify, and must return.
3. [`research-methodology.md`](core/references/research-methodology.md) defines
   Stage A: planning, fresh scans, old-popular sweeps, comment-thread units,
   sampling, evidence records, pain-point extraction, and bias control.
4. [`recurrence-rules.md`](core/references/recurrence-rules.md) defines
   thread-level and cumulative recurrence, classification order, and daily
   briefs.
5. [`product-match-gate.md`](core/references/product-match-gate.md) defines
   Stage B: source hierarchy, fit decisions, allowed claims, and the required
   gate record.
6. [`content-pipeline.md`](core/references/content-pipeline.md) defines C0-C5:
   angles, Reddit posts or replies, editorial review, posting preparation,
   final live checks, and post-publication learning.
7. [`review-approval.md`](core/references/review-approval.md) defines Light and
   Full review, human approval boundaries, and team review questions.
8. [`file-contracts.md`](core/references/file-contracts.md) defines every
   project-owned file, authority order, run records, and write ownership.
9. [`project-initialization.md`](core/references/project-initialization.md)
   defines scanning, initialization, adoption of existing workflows, data
   separation, and migrations.
10. [`reddit-safety.md`](core/references/reddit-safety.md) defines platform and
    automation boundaries.

The Skill entry point is
[`SKILL.md`](plugins/reddit-workflow/skills/reddit-workflow/SKILL.md). It tells
Codex which governing references must be loaded for each command.

## Complete Stage Order

### Project Setup

The workflow scans the target project, establishes primary and derived product
sources, creates `ops/reddit-workflow/project-profile.json`, and validates the
project-owned workspace. Existing populated workspaces are adopted rather than
overwritten.

### Stage A: Neutral Reddit Evidence

Fresh-post scans and old-popular sweeps remain separate. The workflow checks
duplicate and revisit rules, reads visible Reddit pages and comments through
the required browser, records comment-thread units, classifies evidence
without product influence, and writes bounded findings to versioned run files.

### Recurrence And Core Research

Run findings propose updates to research logs, pain-point records, and
clusters. Durable core files change only after review and explicit approval.
Recurrence is cumulative evidence accounting, not a claim of market
prevalence.

### Stage B: Product-Match Gate

Only after neutral classification may the workflow compare a pain point with
verified product capabilities. It records source quality, match strength,
allowed claims, caveats, unresolved claims, and whether the safest outcome is
no product mention, a soft mention, reply-only, or postponement.

### C0-C3: Reddit Content Preparation

C0 creates Reddit-native angles. C1 creates either a standalone post or reply
candidate. C2 runs Light or Full editorial and risk review. C3 returns the
safest, growth, postpone, or do-not-post decision with traceability back to
evidence and verified product sources.

### C4: Final Live Check

The workflow reopens the current subreddit context, checks relevant rules,
pinned posts, flair, AutoModerator signals, link and disclosure risks, and
returns final posting guidance. It never posts automatically.

### C5: Monitoring And Learning

Published output is monitored in a C5 run record. Quantitative and qualitative
signals may propose research updates, reply opportunities, iteration, scaling,
or retirement. Engagement alone is never treated as proof.

## Files Created In A Project

The project workspace normally lives at `ops/reddit-workflow/`:

```text
project-profile.json
research/
  reddit-research-plan.md
  reddit-research-log.md
  pain-point-database.md
  pain-point-clusters.md
strategy/
  product-feature-source-map.md
  feature-match-matrix.md
content/
  content-angle-bank.md
  draft-library.md
runs/
```

The exact responsibilities and authority order are defined in
[`file-contracts.md`](core/references/file-contracts.md). Run structures live
under [`core/templates/`](core/templates/).

## Short Commands

The full contracts for these commands are in
[`command-contracts.md`](core/references/command-contracts.md):

- `Prepare Reddit workflow task`
- `Run Daily Reddit Workflow`
- `Run Old Popular Backlog Sweep`
- `Review run for core updates`
- `Apply approved core updates`
- `Run C4 Final Posting Check`
- `Run C5 Monitoring`
- `Upgrade Reddit Workflow Project`

Short commands never replace the detailed rules and never authorize posting,
replying, core-data changes, commits, pushes, or publishing beyond their
documented boundary.
