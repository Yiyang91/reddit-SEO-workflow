# Command Contracts

Read the relevant contract before executing a short workflow command. A short
trigger delegates the documented procedure; it does not authorize extra work.

## Global Contract

- Work only inside the target project's configured Reddit workflow root.
- Keep output Reddit-only.
- Do not post, reply, commit, push, deploy, or publish automatically.
- Do not force product fit or create treatment/diagnostic claims.
- Write working findings to `runs/` before proposing core research updates.
- Preserve existing files and version run filenames rather than overwriting.

## Prepare Reddit Workflow Task

Do:

- resolve project and workflow roots
- inspect Git status without modifying it
- run project validation
- run duplicate URL review
- summarize recurrence
- report blockers and the next safe command

Do not:

- browse Reddit
- edit files
- create drafts
- update research data

Expected output:

- roots and profile summary
- status and structure result
- duplicate URL result
- recurrence summary
- safe next action

## Run Daily Reddit Workflow

Do:

1. Use or create `runs/daily-run-YYYY-MM-DD.md`.
2. Read the profile and existing research/strategy records.
3. Scan fresh posts neutrally in 3-5 priority subreddits.
4. Stop after 5 useful signals, 30 posts, or 45-60 minutes.
5. Check every URL before processing.
6. Record visible tensions before classification.
7. Classify useful signals as existing support, sub-signal, new weak
   candidate, out-of-scope, or exclude.
8. Decide whether evidence justifies A -> B -> C0 -> C1 -> C2 -> C3.
9. If justified, preserve the complete evidence/product/content/review chain.
10. End with the Daily Cumulative Recurrence Brief and recommended action.

Do not:

- automatically update core research files
- generate a product-mentioned draft before the Product-Match Gate
- search specifically to confirm an existing pain point
- generate non-Reddit content

May modify only the current daily run file unless the user separately approves
core updates.

## Run Old Popular Backlog Sweep

Do:

1. Build or read a candidate list.
2. Rank by visible heat and discussion quality.
3. Select 2-4 highest-ranked readable, in-scope threads.
4. Apply prior-sweep and 48-hour revisit rules.
5. Read comments in the authenticated browser under A3 sampling rules.
6. Save 5-10 strongest CTUs per thread.
7. Record skipped hotter candidates and access limitations.
8. Write a new versioned old-popular run file.
9. Optionally run a narrow B/C test only when evidence justifies it.

Do not:

- choose lower-heat posts primarily to fill a desired cluster
- treat title-level evidence as a completed sweep
- re-count old evidence during a valid revisit
- update core records or draft library automatically

## Review Run For Core Updates

Read the specified run and propose:

- RRL/CTU additions or revisit appendices
- existing Pain Point and Cluster updates
- sub-signals and new weak candidates
- cumulative recurrence and confidence changes
- out-of-scope/excluded evidence

Do not edit core files. Return an exact proposed edit list for approval.

## Apply Approved Core Updates

Apply only the approved items to:

- `research/reddit-research-log.md`
- `research/pain-point-database.md`
- `research/pain-point-clusters.md`

Then run project validation, duplicate URL review, and recurrence summary.
Do not add unapproved evidence or generate content.

## Run C4 Final Posting Check

Use an existing C3 candidate. Read current browser-visible subreddit context.
Use Light C4 unless Full C4 triggers apply.

Return:

- review depth and reason
- rule/pinned/flair/AutoModerator findings when Full C4 is required
- safest/growth/postpone/do-not-post decision
- final title/body only if safe
- target subreddit, required flair, posting order, and risk notes

Do not post, reply, add a new claim, add a new link, or invent a new angle.

## Run C5 Monitoring

Use or create `runs/c5-log-DRAFT_ID.md`. Check the appropriate monitoring
window, record quantitative and qualitative signals, classify reply
opportunities, and propose research updates.

Return `Scale`, `Iterate`, `Reply-only`, `Research-only`, or `Retire`.

Do not reply automatically, update core research automatically, create a new
draft automatically, or treat upvotes alone as validation.

## Upgrade Reddit Workflow Project

Run migration preview first. Show every proposed addition or metadata change.
Apply only after approval. Never overwrite accumulated evidence, pain points,
angles, drafts, or run records.
