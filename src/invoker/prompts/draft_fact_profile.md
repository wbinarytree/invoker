<!-- prompt_version: 6 -->
# Draft hero fact profile

You are drafting a Dota 2 hero fact profile for later human review.

Return JSON only. Do not wrap it in prose. Do not use markdown bullets. Do not add markdown fences unless the chat UI forces you.

Use only the live vocabulary terms below. If an important mechanic is supported
by the ability or stat context but no live term fits, omit it from fact buckets
and add it to vocabulary_gaps.

Hero:
- id: {HERO_ID}
- slug: {HERO_SLUG}
- localized_name: {HERO_NAME}
- primary_attr: {PRIMARY_ATTR}
- attack_type: {ATTACK_TYPE}
- roles: {ROLES}
- patch: {PATCH}

Live vocabulary JSON:
```json
{VOCABULARY_CONTEXT_JSON}
```

Bucket definitions:
- capabilities = things this hero actively does well with their own kit
- requirements = things this hero wants from allies or game state to function at full value
- liabilities = ways opponents can mechanically punish or constrain this hero
- targets = enemy profiles this hero naturally preys on or reaches well

Bucket guardrails:
- do not put the same idea in multiple buckets
- do not invent a liability just because it is generally true for many spellcasters
- prefer omission over a weak or speculative entry
- if a concept is real but not expressible with the allowed vocabulary, omit it from fact buckets and add it to vocabulary_gaps

Hero stats JSON (each stat has value, percentile across the roster, and a coarse band):
```json
{STATS_JSON}
```

Stat usage rules:
- cite `band` or `percentile` as evidence, not raw values
- bands below `high` rarely justify a capability claim on their own

Dota mechanism primer JSON for the active patch. Use this to interpret stats; do not infer stat-to-effect formulas from memory:
```json
{MECHANISM_PRIMER_JSON}
```

Ability context JSON (normalized; abilities with `source: "innate"` are part of the baseline kit):
```json
{ABILITIES_JSON}
```

Talent context JSON (level-gated; do NOT promote talents to baseline capabilities):
```json
{TALENTS_JSON}
```

Talent usage rules:
- talents are conditional and level-gated, never baseline capabilities
- if a talent is hero-defining, surface it via vocabulary_gaps with evidence naming the talent and its level

Itemization rules:
- do not include Scepter, Shard, Blink Dagger, or other item-dependent mechanics as baseline capabilities

Output schema:

```json
{
  "hero_id": {HERO_ID},
  "hero_slug": "{HERO_SLUG}",
  "localized_name": "{HERO_NAME}",
  "capabilities": [
    {
      "type": "one_allowed_capability",
      "score": 0.0,
      "evidence": ["short concrete evidence from ability or stat context"]
    }
  ],
  "requirements": [
    {
      "type": "one_allowed_requirement",
      "score": 0.0
    }
  ],
  "liabilities": [
    {
      "type": "one_allowed_liability",
      "score": 0.0,
      "evidence": ["short concrete evidence from ability or stat context"]
    }
  ],
  "targets": [
    {
      "type": "one_allowed_target",
      "score": 0.0,
      "evidence": ["short concrete evidence from ability or stat context"]
    }
  ],
  "vocabulary_gaps": [
    {
      "bucket": "capabilities",
      "concept": "short human-readable missing concept",
      "why_needed": "why the allowed vocabulary cannot express this important mechanic",
      "evidence": "short concrete evidence from ability or stat context",
      "candidate_term": "optional_snake_case_term"
    }
  ],
  "provenance": {
    "authored_by": "human",
    "authored_at": "YYYY-MM-DD",
    "assist_model": "name_of_model_or_null"
  }
}
```

Rules:
- use only live vocabulary terms
- omit entries you cannot justify from the ability, talent, or stat context
- innates count as baseline kit; talents do not
- do not include item-, Scepter-, Shard-, or Blink-dependent capabilities as baseline
- when citing stats, reference `band` or `percentile`, not raw numbers
- keep evidence short and concrete
- paraphrase evidence instead of quoting exact phrases from the source text
- do not include double quote characters inside evidence strings
- requirements may be listed without evidence
- capabilities, liabilities, and targets should include evidence when present
- keep requirements sparse; only include ones that materially change how the hero functions
- only include liabilities that are clearly supported by the current live vocabulary
- use vocabulary_gaps for important mechanics that are supported by the source context but cannot be represented with allowed terms
- keep vocabulary_gaps sparse; do not list vague flavor, item-dependent behavior, or generic Dota properties
- vocabulary_gaps.bucket must be one of capabilities, requirements, liabilities, targets
- every top-level key must stay at the top level of the JSON object
- use JSON arrays with `[]` and objects with `{}`; never use markdown `*` bullets
- set `provenance.authored_by` to `human`
