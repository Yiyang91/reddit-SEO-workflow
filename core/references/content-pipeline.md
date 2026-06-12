# Reddit Content Pipeline

## Contents

1. Pipeline entry
2. C0 angles
3. C1 output types
4. Product mention and link policy
5. C2 review depth
6. C3 and C4
7. C5 monitoring
8. Traceability

## Pipeline Entry

Enter A -> B -> C0 -> C1 -> C2 -> C3 only when evidence is concrete,
non-duplicative, relevant, and safe enough for a Reddit-native discussion or
reply. Otherwise choose observe only, reply-only, postpone, or do not post.

The pipeline remains Reddit-only.

## C0: Content Angles

C0 creates angle candidates, not full drafts. Each angle must include:

- A-stage basis: cluster, pain point, evidence IDs, strength, conclusion
- B-stage basis: features, match strength, limits, and prohibited claims
- Reddit reader tension
- core angle
- intended output type
- product mention level
- evidence-alignment and safety notes

## C1: Output Types

### Standalone Reddit Post

Modes:

1. `no-product discussion`
   - high self-promotion risk
   - low account credibility
   - testing pain-point or subreddit fit
   - product mention would feel forced
2. `solution-sharing + soft product mention`
   - medium or strong validated match
   - Product-Match Gate passes
   - useful non-product methods come first
   - product is one optional method, normally without a link
3. `founder-disclosure / product-soft`
   - subreddit allows project sharing, tools, or beta discussion
   - transparent disclosure
   - feedback/discussion CTA, not conversion

Standalone formats may be discussion, method-sharing, product-soft, or
research-question posts.

### Reply Comment

Types:

1. `empathy-only`: sensitive or unsafe product context
2. `method-sharing`: useful help without product mention
3. `method + soft product`: value first, natural optional fit, medium/strong
   match, gate passed
4. `product disclosure + link`: only when tools/apps/links were requested and
   subreddit rules permit it

Do not draft a response when the user needs crisis/clinical support, product
fit is forced, rules prohibit the necessary disclosure, or the response has
no value without the product.

## Product Mention And Link Policy

Product mention options:

- none
- soft
- explicit with transparent disclosure

Link options:

- no link
- mention only, no link
- link only if asked
- link allowed in first reply

Default to `mention only, no link` after all other gates pass. A link requires
explicit contextual justification and subreddit permission.

No-product is the safest test, but not a permanent default. A natural product
mention may be tested when the evidence, Product-Match Gate, subreddit
context, and disclosure all support it.

## C2: Editorial And Risk Review

Use Light C Review when the subreddit and mention policy were reviewed within
30 days and no meaningful condition changed.

Light review checks:

- evidence alignment
- Reddit-native tone
- self-promotion smell
- new product claims
- obvious new subreddit risk
- whether mention should stay, soften, move later, or be removed

Use Full C Review when:

- subreddit is new
- draft introduces a product mention or link
- rules, pinned context, flair, or AutoModerator guidance changed
- topic is sensitive
- claim boundary is unclear
- last full subreddit review is older than 30 days

Full review checks evidence, product match, claims, current rules, pinned
posts, flair, AutoModerator notices, posting norms, self-promotion policy,
link policy, and safest versus growth version.

C2 is a risk gate, not merely prose polishing.

## C3: Posting Preparation

Prepare both versions when useful:

- Safest: no product, no link, discussion or method-sharing
- Growth: soft product mention, normally no link, transparent disclosure

Choose:

- use safest version
- use growth version
- postpone
- do not post

Record target subreddit, required C4 checks, known flair, account credibility,
product-match strength, and risk notes.

## C4: Final Browser Check

C4 uses an existing C3 candidate. It does not create a new angle or add a new
claim, mention, or link.

Light C4:

- reuse a recent full review
- confirm no obvious new rule risk
- confirm draft has no new claim or link
- confirm tone remains native

Full C4 uses the authenticated browser to inspect current:

- rules
- pinned posts
- flair requirements
- AutoModerator notices
- posting format and norms
- self-promotion, app mention, and link posture

Return the decision, final title/body if safe, target subreddit, required
flair, posting order, and risk notes. Do not post automatically.

## C5: Post-Publication Monitoring

Monitoring windows:

- T+24h main check
- T+72h final check
- optional T+7d when discussion continues
- ad hoc early record for removal, moderator warning, or unusually fast
  discussion

Record metadata, score, comments, ratio when visible, removal/lock/moderation
signals, useful user language, repeated or new pain points, promotional
reactions, subreddit fit, and reply opportunities.

For each promising comment classify:

- reply appropriate: yes, no, or maybe
- reply type
- product mention allowed
- link policy
- risk
- recommended action

Propose, but do not automatically apply, research updates.

C5 outcomes:

- `Scale`
- `Iterate`
- `Reply-only`
- `Research-only`
- `Retire`

Upvotes alone do not validate a post. High-quality discussion may matter more
than score.

## Traceability

Every C0/C1 item must preserve:

1. A-stage basis
2. B-stage basis and Product-Match Gate
3. output type, reader tension, angle, mention level, link policy, and draft
4. evidence-alignment note
5. C2 decision
6. C3/C4 decision when applicable
7. C5 learning when published
