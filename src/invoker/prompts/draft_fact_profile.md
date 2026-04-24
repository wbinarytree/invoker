<!-- prompt_version: 3 -->
# Draft hero fact profile

You are drafting a Dota 2 hero fact profile for later human review.

Return JSON only. Do not wrap it in prose. Do not use markdown bullets. Do not add markdown fences unless the chat UI forces you.

Use only the allowed vocabulary terms below.

Hero:
- id: {HERO_ID}
- slug: {HERO_SLUG}
- localized_name: {HERO_NAME}
- roles: {ROLES}

Allowed vocabulary:
- capabilities: {CAPABILITIES}
- requirements: {REQUIREMENTS}
- liabilities: {LIABILITIES}
- targets: {TARGETS}

Bucket definitions:
- capabilities = things this hero actively does well with their own kit
- requirements = things this hero wants from allies or game state to function at full value
- liabilities = ways opponents can mechanically punish or constrain this hero
- targets = enemy profiles this hero naturally preys on or reaches well

Bucket guardrails:
- do not put the same idea in multiple buckets
- do not invent a liability just because it is generally true for many spellcasters
- prefer omission over a weak or speculative entry
- if a concept is real but not expressible with the allowed vocabulary, omit it for now

Ability text:
{ABILITIES}

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
      "evidence": ["short concrete evidence from ability text"]
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
      "evidence": ["short concrete evidence from ability text"]
    }
  ],
  "targets": [
    {
      "type": "one_allowed_target",
      "score": 0.0,
      "evidence": ["short concrete evidence from ability text"]
    }
  ],
  "role_distribution": {},
  "provenance": {
    "authored_by": "human",
    "authored_at": "YYYY-MM-DD",
    "assist_model": "name_of_model_or_null"
  }
}
```

Rules:
- use only allowed vocabulary terms
- omit entries you cannot justify from the ability text
- keep evidence short and concrete
- paraphrase evidence instead of quoting exact phrases from the source text
- do not include double quote characters inside evidence strings
- requirements may be listed without evidence
- capabilities, liabilities, and targets should include evidence when present
- keep requirements sparse; only include ones that materially change how the hero functions
- only include liabilities that are clearly supported by the current live vocabulary
- every top-level key must stay at the top level of the JSON object
- use JSON arrays with `[]` and objects with `{}`; never use markdown `*` bullets
- set `provenance.authored_by` to `human`
