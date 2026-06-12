# Product-Match Gate

No product-mentioned Reddit draft may be generated directly from a user pain
point.

## Source Hierarchy

1. Primary product sources listed in `project-profile.json`
2. Derived product summaries listed in the profile
3. Workflow outputs such as feature matrices and drafts

Primary sources decide current product facts. Derived summaries provide
orientation only. Workflow outputs do not prove that a feature exists.

When sources conflict:

- record the conflict
- do not silently choose a side
- omit the disputed claim or use only wording supported by a primary source
- block final public output when the disputed claim is necessary

## Required Gate Record

For every candidate record:

- Pain Point or Cluster ID
- evidence IDs or CTUs
- matched feature IDs
- supported product selling point
- source status
- primary source support: yes, no, or partial
- derived-only status
- unresolved conflict
- match strength: strong, medium, weak, no match, or sensitive
- allowed public wording
- forbidden wording
- gate decision: pass, revise, or reject

## Decision Rules

Reject product mention when:

- match is weak, no match, forced, or sensitive
- the context is crisis, clinical, treatment-seeking, or otherwise unsafe
- subreddit context prohibits or strongly disfavors self-promotion
- useful value cannot be provided without the product
- the wording depends on an unresolved or derived-only claim

`medium` or `strong` match does not automatically authorize a mention. The
subreddit, account context, disclosure, link policy, and C2/C4 review must also
permit it.

## Claim Discipline

- Preserve the user's original tension before interpreting product relevance.
- Describe only verified present capabilities.
- Do not turn roadmap, experiment, or derived wording into a current feature.
- Use conservative qualifiers when availability is conditional.
- Do not promise outcomes unsupported by product and external evidence.
- Keep a clear `what not to claim` field in the feature-match record.
