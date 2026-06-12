# Recurrence And Classification Rules

## Thread-Level Recurrence

Thread-level recurrence estimates only the number of visible users in one
thread expressing a substantially similar tension.

| Level | Definition |
| --- | --- |
| `isolated` | one visible user |
| `repeated` | two to three visible users |
| `recurring` | four to seven visible users |
| `strong` | eight or more visible users, or multiple substantive reply chains |

Count only visible comments or replies that express the tension. Do not count
upvotes, vague agreement, or the same user twice. Preserve whether the whole
thread or a sampled slice was reviewed.

## Cumulative Recurrence

| Level | Definition |
| --- | --- |
| `weak` | one thread or mostly isolated evidence |
| `emerging` | two to three threads or five to ten CTUs |
| `validated` | at least three threads and ten CTUs across two subreddits or repeated batches |
| `strong` | consistent language across multiple threads, batches, and subreddits |

Thresholds guide classification; they do not override contradictory evidence
or poor sampling.

Maintain:

- `cumulative_threads_count`
- `cumulative_comment_units_count`
- `cumulative_similar_user_count_observed`
- `latest_evidence_added`
- `confidence_change`: upgraded, unchanged, or downgraded
- `evidence_scope_note`

Cumulative observed users are traceable evidence counts, not estimates of
Reddit prevalence.

## Classification Order

For every saved CTU:

1. Preserve its neutral tension.
2. Compare it with existing Pain Point IDs and Cluster IDs.
3. Append as existing support when the underlying tension is the same.
4. Add a sub-signal when it is a narrower variant.
5. Create a new weak candidate only when meaningfully different.
6. Keep out-of-scope and excluded evidence visible with a reason.

Do not create duplicate pain points to make recurrence appear stronger.

## Daily Brief

End each daily run with:

- pain points matched or updated
- new CTUs and threads
- cumulative recurrence changes
- confidence changes
- new weak candidates
- B/C strategy implications
- recommended action: post, reply, observe only, postpone, or do not post

Do not apply the brief to core research files until the configured approval
gate passes.
