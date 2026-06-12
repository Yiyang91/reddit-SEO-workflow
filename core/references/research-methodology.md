# Reddit Research Methodology

## Contents

1. Stage A boundary
2. Research planning
3. Daily scan workload
4. Old-popular backlog selection
5. Duplicate and revisit rules
6. Comment-thread collection
7. Sampling
8. Keep, skip, and expand rubric
9. Evidence records
10. Pain-point extraction
11. Bias control

## Stage A Boundary

Stage A collects and classifies Reddit evidence. It does not perform product
matching, generate marketing copy, post, reply, or make treatment, diagnostic,
or clinical claims.

Record a tension before considering whether the product can address it. Keep
real non-matches and out-of-scope evidence because they protect positioning.

Evidence levels:

- Post-level evidence establishes the thread's stated tension.
- Comment-level evidence validates, expands, challenges, or reframes it.
- Reply-level evidence reveals recurrence, disagreement, causes, context,
  consequences, and workarounds.

## Research Planning

The project-owned research plan must define:

- research goal and assumptions to test
- verified product facts that may shape inclusion boundaries
- priority and secondary subreddits
- search and browsing vocabulary
- time range
- sampling limits
- sensitive and excluded contexts
- pilot size and success criteria

Do not mass scrape Reddit. Prefer recent evidence, but include older threads
when language is unusually clear, discussion is substantial, or the tension
appears stable. Record post date and capture date separately.

## Daily Scan Workload

For a normal fresh-post scan:

- scan 3-5 priority subreddits
- inspect recent, new, or rising posts
- stop after 5 useful signals, 30 reviewed posts, or 45-60 minutes

A useful signal contains at least one of:

- a concrete user pain or tension
- a meaningfully new weak candidate
- useful user language
- a safe reply opportunity
- a possible content opportunity supported by evidence
- a new nuance under an existing pain point

Scan neutrally. Do not search with the goal of confirming existing pain
points. Classify only after recording what appeared.

## Old-Popular Backlog Selection

Use old-popular sweeps to test stable demand and discussion depth. Complete
the main backlog in 1-3 sessions; afterward use it weekly or as needed.

Before selecting threads:

1. Build or consult a candidate list.
2. Rank by visible heat: comment count, score when visible, reply density,
   age, and discussion quality.
3. Select 2-4 of the highest-ranked readable, in-scope threads.
4. Record the selection basis.
5. If a hotter candidate is skipped, record whether it was already swept,
   unreadable, off-scope, or unsafe.

Do not prioritize a lower-heat thread merely because it fills an evidence
gap. Under-evidenced clusters are only a tie-breaker among similarly strong
candidates, or a later research pass after the hottest backlog is complete.

## Duplicate And Revisit Rules

Compare every thread URL against `research/reddit-research-log.md` before
processing it.

Fresh-post revisit is allowed only when:

- the visible comment count roughly doubled
- at least 20 new comments appeared
- the post is under 72 hours old and still developing
- new top comments directly affect a relevant tension

Record:

- `seen_before`
- `previous_capture_date`
- `previous_comment_count`
- `current_comment_count`
- `revisit_decision`
- `revisit_reason`

Append a revisit under the existing RRL ID. Do not create a second captured
entry for the same thread.

For an old-popular thread, apply the 48-hour gate only after determining prior
sweep status:

1. Never deep-read: perform a first sweep regardless of latest reply time.
2. Prior access limitation, insufficient sampling, or unclear sampling
   record: repair the old sampling first.
3. Valid completed sweep: apply the 48-hour gate.
4. No visible activity in the last 48 hours: skip.
5. New activity in the last 48 hours: inspect only new comments and replies.

A valid completed sweep requires browser-opened comment reading, a recorded
sampling scope that satisfies the rules below, and saved CTUs when useful
evidence existed. A title-level record, RRL entry, unreadable page, or partial
read is not a completed sweep.

Record `prior_sweep_status`, `prior_sampling_scope`, `sampling_complete`,
`revisit_status`, `latest_reply_time`, `new_reply_window`, and whether new
material adds evidence, nuance, challenge, or no useful signal.

## Comment-Thread Collection

Use `browser_opened_reddit_page` for formal evidence unless the profile
explicitly permits a labeled fallback pass.

For each thread:

1. Open the visible thread and comments in an authenticated browser.
2. Prefer Best or Top sorting unless the research question needs another
   visible sort.
3. Apply the sampling rule.
4. Inspect replies for each promising top-level comment.
5. Preserve replies that support, expand, challenge, or reframe the tension.
6. Save comment-thread units, not disconnected quotations.

## Sampling

| Visible total comments | Required review |
| --- | --- |
| `<= 50` | All visible top-level comments; replies for every promising comment |
| `51-100` | Top 30 top-level comments, or all when feasible |
| `101-300` | Top 20% of visible top-level comments, capped at 50 |
| `> 300` | Top 50-60 top-level comments; optional visible in-thread keyword scan |

Inspect up to five relevant replies per promising top-level comment. Save 5-10
strongest CTUs per thread. Save more only for an unusually high-signal thread
and record `high_signal_thread = yes`.

When the page exposes only a partial set, record the limitation and do not
claim full-thread prevalence.

## Keep, Skip, And Expand Rubric

Keep evidence that reveals:

- concrete frustration, hesitation, unmet need, or emotional reaction
- behavior, cause, context, trigger, consequence, or workaround
- specific user language
- resonance, useful agreement, disagreement, or reframing
- why a current tool, practice, or workaround succeeds or fails

Expand replies when they form a real discussion or add specificity to the
top-level tension.

Skip:

- jokes, memes, one-word reactions, or generic praise
- bare recommendations with no tension or explanation
- duplicate statements with no new nuance
- content without enough context to interpret safely
- crisis, treatment-seeking, or otherwise unsafe material for product/content
  use
- domain discussion that does not express a user problem

## Evidence Records

Each thread-level record should include:

- RRL ID, capture date, URL, subreddit, title, post date
- visible engagement signal and sampling scope
- plain-language user tension
- short quote or careful paraphrase with context
- comment patterns and current workaround
- mentioned tools or practices
- sensitive-context flag
- initial classification notes
- access method and limitations
- duplicate/revisit fields

Each CTU should include:

- `comment_unit_id`, `thread_id`, subreddit, URL, and permalink when visible
- top-level quote or short snippet
- relevant reply snippets
- reply function: supports, expands, challenges, or reframes
- revealed tension and possible pain-point candidate
- confidence
- `similar_user_count_observed`
- thread-level `recurrence_level`
- `reply_discussion_present` and `reply_discussion_value`
- `keep_reason`, `high_signal_thread`, access method, and limitations

Keep quotations short and traceable. Do not infer beyond visible text.

## Pain-Point Extraction

Keep these labels distinct:

- real pain point
- casual complaint
- product opportunity
- content angle

During Stage A, only the first two and neutral candidate notes are decided.
Product opportunity belongs to Stage B; content angle belongs to C0.

Useful scoring fields:

- `intensity`: 1 mild preference through 5 high distress/sensitivity
- `evidence_strength`: Single, Thread, Recurring, Cross-subreddit
- classification: existing support, sub-signal, new weak candidate,
  out-of-scope, exclude

High distress increases sensitivity; it does not increase growth value.

## Bias Control

- Start from user language, not product features.
- Do not treat topic keywords alone as product relevance.
- Do not count upvotes as users.
- Do not claim Reddit-wide prevalence.
- Do not discard a real tension because the product is irrelevant.
- Append to an existing pain point when the underlying tension is the same.
- Add a sub-signal when evidence is a more specific variant.
- Create a new weak candidate only when the underlying tension is meaningfully
  different.
- Preserve negative and contradictory evidence.
