<!-- prompt_version: 2 -->
# Revise Invoker vocabulary

You are helping revise a mechanics-first Dota 2 hero vocabulary.

Return JSON only. Do not wrap it in prose. Do not add markdown fences unless the
chat UI forces you.

The human review notes are the highest-priority input. Preserve them unless they
directly contradict authored usage evidence or the vocabulary design goal.

Goal:
- improve the vocabulary contract used by human authors, validators, and deterministic rules
- avoid terms that are too hero-specific, flavor-based, or item-dependent
- prefer clearer definitions over adding near-duplicate terms
- preserve existing accepted terms when they are still useful
- propose additions, revisions, merges, splits, removals, or deferrals

Input context is compact JSON:
- `scope` describes which bucket or term was requested
- `audit_summary` contains blocking issues and non-blocking warnings
- `terms` contains current term definitions plus usage and rule consumption
- `human_reviews` contains the user's natural-language suggestions
- `reviewed_vocabulary_gaps` contains user's decisions on missing concepts from authored heroes
- `unreviewed_vocabulary_gaps` contains lower-priority background gaps that have not been reviewed yet

Output schema:

```json
{
  "schema_version": 1,
  "proposals": [
    {
      "bucket": "capabilities",
      "term": "attack_speed_reduction",
      "action": "add",
      "definition": "Reduces enemy attack rate through a hero-owned mechanic.",
      "include_when": [
        "The hero directly applies attack speed slow or reduction."
      ],
      "exclude_when": [
        "The hero only slows movement.",
        "The effect depends primarily on purchased items."
      ],
      "examples": [
        {
          "hero_slug": "pangolier",
          "evidence": "Lucky Shot can drastically slow enemy attack speed."
        }
      ],
      "enabled_rules": [
        {
          "source_feature": "attack_speed_reduction",
          "target_bucket": "liabilities",
          "target_feature": "weak_to_attack_focus",
          "pattern": "resource_punish",
          "relation_kind": "counter"
        }
      ],
      "rationale": "Human review and authored gaps show this mechanic appears across multiple heroes.",
      "status": "proposed"
    }
  ]
}
```

Allowed proposal actions:
- add
- revise
- rename
- merge
- split
- remove
- defer

Vocabulary context:

```json
{VOCABULARY_CONTEXT_JSON}
```

Rules:
- Return JSON only.
- Keep proposals grounded in current authored heroes, vocabulary gaps, or human notes.
- Prefer reviewed vocabulary gaps over unreviewed vocabulary gaps.
- For add, revise, rename, merge, and split proposals, include `definition`, `include_when`, `exclude_when`, and `examples` when available.
- For remove proposals, explain which authored facts or rules must change first.
- For defer proposals, explain what additional evidence would make the decision better.
- Do not silently delete existing accepted terms.
- Do not propose a new term if an existing term can be clarified instead.
- Keep `enabled_rules` as proposals only; do not invent precise confidence values.
- Use arrays for `include_when`, `exclude_when`, `examples`, and `enabled_rules`; use empty arrays when none apply.
