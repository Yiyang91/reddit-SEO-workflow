# Recurrence Rules

## Thread-Level Recurrence

- `isolated`: one visible user in one thread
- `repeated`: two to three visible users
- `recurring`: four to seven visible users
- `strong`: eight or more visible users, or multiple reply chains expressing substantially similar tension

## Cumulative Recurrence

- `weak`: one thread or mostly isolated evidence
- `emerging`: two to three threads or five to ten CTUs
- `validated`: at least three threads and ten CTUs across at least two subreddits or repeated batches
- `strong`: consistent language across multiple threads, batches, and subreddits

Maintain:

- `cumulative_threads_count`
- `cumulative_comment_units_count`
- `cumulative_similar_user_count_observed`
- `latest_evidence_added`
- `confidence_change`
- `evidence_scope_note`

Cumulative observed users are an evidence count, not an estimate of Reddit prevalence.
