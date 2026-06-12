# Project File Contracts

## Workflow Root

The default workflow root is `ops/reddit-workflow/`. The profile may configure
another path, but it must remain inside the project.

## Control Files

- `project-profile.json`: project identity, source paths, product boundaries,
  Reddit policy, and approvals
- `README.md`: project workspace orientation
- `research/reddit-research-plan.md`: project-specific research goal,
  subreddits, vocabulary, workload, exclusions, and pilot criteria

## Research Files

### `research/reddit-research-log.md`

Owns raw thread evidence, access limitations, duplicate/revisit history, and
comment-thread units. It does not prove product relevance.

### `research/pain-point-database.md`

Owns Pain Point IDs, neutral tensions, linked evidence, intensity, evidence
strength, recurrence, confidence changes, sub-signals, and status.

### `research/pain-point-clusters.md`

Owns higher-level groupings without turning clusters into campaign ideas.

## Strategy Files

### `strategy/product-feature-source-map.md`

Owns feature IDs, primary evidence, derived references, conflicts, allowed
public wording, forbidden wording, and source status.

### `strategy/feature-match-matrix.md`

Owns pain-point/cluster to feature matching, match strength, valid scope,
limits, sensitivity, and what not to claim.

## Content Files

### `content/content-angle-bank.md`

Owns C0 Reddit angles with A/B traceability. It does not own full drafts.

### `content/draft-library.md`

Owns durable C1 candidates, Product-Match Gate results, C2 review, C3/C4
decisions, and published-output references. Working drafts may remain in run
files until approved for promotion into the library.

## Run Files

`runs/` owns working evidence and decisions for a bounded execution. Run files
are append-only/versioned working records and are not automatically
authoritative core research.

- `daily-run-YYYY-MM-DD.md`
- `old-popular-sweep-YYYY-MM-DD[-vN].md`
- `c5-log-DRAFT_ID.md`

## Authority Rules

- Primary product sources prove current product facts.
- Derived product summaries orient but do not independently authorize claims.
- Research files prove only what their cited Reddit evidence supports.
- Strategy files record decisions; they do not create product truth.
- Content and run files do not prove either prevalence or product capability.

## Write Ownership

- Daily and old-popular commands write run files first.
- Core research files change only through an approved update.
- Product source map changes only after primary source review.
- Feature match matrix changes only after Stage A classification.
- Draft library changes only after the relevant gates and configured approval.
- Existing files are not overwritten without explicit approval.
