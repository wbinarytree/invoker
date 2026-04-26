# Hero Authoring Context Hardening

Date: 2026-04-26
Status: draft — needs user sign-off before implementation
Stage: Stage 4 quality hardening before broader hero authoring, oracle use, and
Stage 5 rules

## Why

The manual hero authoring prompt is now central to scaling authored facts beyond
the first validation slice. Those authored facts are not only for drafting. They
also feed **Oracle**, the future Dota hero agent that should answer factual hero
questions such as "How is Pangolier recently doing?" without relying on model
memory.

The prompt should therefore collect general, source-grounded hero facts and
draft-relevant mechanics. It should not overfit the authored profile to draft
relations alone.

Recent Stage 4 runs exposed four prompt-context gaps:

- hero stats are absent, and raw values such as `+4 strength per level` need
  repo-computed calibration before the LLM can use them safely;
- innates and talents can materially change a hero's mechanics;
- itemization, especially Scepter, Shard, Blink Dagger, and similar hero-shaping
  purchases, matters long term but needs conditional modeling;
- JSON context blocks in the prompt need clearer boundaries.

## Outcomes

1. Hero authoring prompts include source-grounded stat context with deterministic
   bands or percentiles, not raw numbers alone.
2. Hero stat fetching and normalization is implemented as reusable raw-fact
   context, not owned by the prompt generator.
3. Ability context is normalized into authoring-relevant facts instead of
   passing raw OpenDota JSON through to the LLM.
4. Innates are included as normal ability context.
5. Talents are included as conditional context, but the prompt does not let them
   become baseline capabilities without explicit evidence language.
6. Itemization is explicitly deferred until conditional fact modeling exists.
7. Prompt context JSON is fenced for readability, while the response contract
   remains raw JSON only.

## Non-Goals

- Do not ask the LLM to decide whether a raw stat is high or low from memory.
- Do not add item-, Scepter-, Shard-, or Blink-dependent capabilities to baseline
  authored facts in this change.
- Do not change relation inference rules here. Stage 5 owns rule expansion.
- Do not introduce automated LLM calls; this remains a manual paste workflow.
- Do not reduce authored facts to draft-only utility. The same facts must remain
  useful for hero lookup, explanation, and oracle answers.

## Consumers

The authored hero profile has two equal consumers:

- **Draft/relation engine:** needs normalized mechanics that can drive
  deterministic synergies, counters, targets, liabilities, and requirements.
- **Oracle agent:** needs grounded hero facts, recent-state inputs, and
  readable evidence to answer hero questions without making up Dota knowledge.

This spec only hardens the static hero-context side. "Recently doing" requires
patch- and time-scoped performance evidence that should come from stats and
match data, not the baseline authoring prompt alone.

## Design

### Context Management API

This work should be treated as context management, not prompt-specific glue.
Prompt generation is one consumer of composable context packets; Oracle is
another. The context builder should expose reusable pieces with clear ownership:

```python
@dataclass(frozen=True)
class HeroContextPacket:
    patch: str
    hero: HeroIdentityContext
    stats: HeroStatsContext
    abilities: list[AbilityContext]
    talents: list[TalentContext]
    mechanisms: MechanismPrimerContext
    vocabulary: VocabularyContext
```

The authoring prompt can render the full packet or selected sections:

```python
packet = build_hero_context(data_dir, hero, patch=patch)
prompt = render_draft_prompt(packet)
```

Oracle can reuse the same packet or compose it with recent performance evidence:

```python
packet = build_hero_context(data_dir, "pangolier", patch="7.41b")
answer = oracle.answer(question, context=packet, recent_evidence=evidence)
```

Suggested module ownership:

- `hero_context.py`: composition API and packet model;
- `hero_stats_context.py`: stat bands and percentiles;
- `ability_context.py`: normalized base abilities, innates, and talents;
- `mechanism_primer.py`: global patch-scoped Dota mechanisms;
- `vocabulary_context.py`: live vocabulary metadata for authoring.

The important boundary: prompt generation consumes context; it does not fetch,
calibrate, or normalize raw hero facts itself.

### Stat Context

Hero stat context should be fetched and normalized by reusable source/context
code. The prompt generator should reference that context, not own stat fetching
or calibration. This keeps the same raw fact surface available to Oracle later.

The first implementation can still use the OpenDota roster payload, but the API
shape should not be prompt-specific. The context is useful both for drafting
mechanics and for general hero explanation. For each relevant stat, expose:

```json
{
  "value": 4.0,
  "percentile": 0.93,
  "band": "very_high"
}
```

Initial stat set:

- base strength, agility, intelligence;
- strength/agility/intelligence gain;
- base armor or armor proxy if available in OpenDota roster payload;
- attack range and attack type if available;
- movement speed if available.

Band names should be deterministic and coarse, for example:

- `very_low`
- `low`
- `average`
- `high`
- `very_high`

The prompt should instruct the LLM to cite `band` or `percentile` if it uses
stats as evidence. Raw values alone are not evidence.

These stats are static hero facts, not recent performance facts. They should not
be used to answer "recently doing" questions without patch-scoped performance
evidence.

### Dota Mechanism Primer

The prompt should not assume the LLM correctly remembers Dota stat formulas. If
stat-derived interpretation matters, include a small source-grounded mechanism
primer next to the stat context.

Examples of mechanism facts that may be needed:

- strength contributes maximum health and health regeneration;
- agility contributes armor and attack speed;
- intelligence contributes mana, mana regeneration, and magic resistance if the
  current Dota patch rules say so;
- primary attribute contributes attack damage.

This primer must be sourced from repo data or an explicitly maintained mechanism
reference. It is reviewed per patch because core stat mechanics can change. Do
not ask the LLM to infer these conversions from training memory.

### Ability Context

The prompt should not pass raw OpenDota ability JSON directly to the LLM. Raw
fields are too noisy and source-shaped; they include implementation names,
generated tooltip values, and uneven metadata.

Instead, add a normalized ability-context layer that turns source payloads into
authoring-relevant facts, for example:

```json
{
  "name": "Slithereen Crush",
  "source": "base_ability",
  "damage_type": "Physical",
  "pierces_debuff_immunity": false,
  "dispellable": "Strong Dispels Only",
  "mechanics": [
    {"kind": "stun", "duration": 0.8, "scope": "area"},
    {"kind": "damage", "values": [75, 150, 225, 300]},
    {"kind": "movement_slow", "values": ["-20%", "-25%", "-30%", "-35%"]}
  ],
  "summary": "Area physical damage, short stun, then movement and attack slow."
}
```

The normalized layer can still preserve source-backed raw labels where useful,
but the prompt should prefer this compact shape over an unfiltered raw JSON dump.

Normalization should be deterministic and built on the fly from source payloads.
Do not add an LLM pre-pass that "normalizes" a hero before the authoring prompt.
That would create a second fallible LLM artifact before validation and would
make failures harder to inspect. The intended flow is:

1. fetch/cache raw OpenDota source payloads;
2. transform them with code into normalized ability context;
3. include that normalized context in the manual authoring prompt;
4. validate the LLM-authored facts after response parsing.

If source fields are ambiguous, preserve a conservative raw label or omit the
derived mechanic and let the authoring LLM surface a `vocabulary_gaps` entry.

### Innates

Innates are part of current Dota hero identity and should be included in ability
context. If OpenDota exposes `is_innate`, translate it into a normalized source
field such as `source: "innate"` rather than making every ability carry a raw
`is_innate` boolean.

The LLM may use innate evidence for baseline facts because every hero has an
innate and the mechanic is part of the hero kit.

### Talents

Talents should be included in prompt context because some are game-changing, but
they are level-gated and conditional.

Prompt rules:

- talents are not baseline capabilities by default;
- talent evidence must explicitly mention the level and talent source;
- if the current authored schema cannot express the condition cleanly, capture
  the mechanic in `vocabulary_gaps` or defer it rather than silently promoting it
  to baseline facts.

Implementation should preserve talent metadata from
`/api/constants/hero_abilities`, including level and referenced talent name, and
join it to ability text from `/api/constants/abilities` when available.

### Itemization

Itemization should be deferred from the current baseline authoring prompt.
Scepter, Shard, Blink Dagger, and other hero-shaping items are real KG inputs,
but mixing them into baseline facts would make relation inference overfire.

Future direction should add conditional facts, for example:

```yaml
conditional_capabilities:
  - type: vision_reveal
    source: shard
    timing: mid_game
    evidence:
      - Shard grants an early vision mechanic.
```

Until that exists, the prompt should not ask the LLM to include item-dependent
mechanics as normal capabilities.

### JSON Fences

Prompt context JSON should be wrapped in fenced `json` blocks:

````md
Live vocabulary JSON:
```json
{VOCABULARY_CONTEXT_JSON}
```

Ability context JSON:
```json
{ABILITIES_JSON}
```
````

The response contract remains:

- return raw JSON only;
- do not wrap the response in markdown fences;
- do not add prose.

## Implementation Plan

This should land as small PRs rather than one large prompt rewrite.

### PR 1 — Spec and Low-Risk Prompt Contract Cleanup

- Add this spec and index it in `docs/CURRENT_DIRECTION.md`.
- Keep `.json` manual response placeholders and the raw-JSON response contract.
- Remove `role_distribution` from the LLM-facing response schema.
- Strip operational vocabulary metadata such as `status` and `introduced_in`
  from prompt context.
- Add the collaboration rule in `AGENTS.md` that design/vision/plan alignment
  triggers discussion mode before implementation.

### PR 2 — Reusable Static Hero Context Skeleton

- Add the composable context packet model and module boundaries.
- Add reusable stat-context computation with deterministic bands/percentiles.
- Add a per-patch mechanism primer source/reference.
- Do not change the authored fact schema yet.

### PR 3 — Normalized Ability/Talent Context

- Add deterministic ability-context normalization from cached OpenDota payloads.
- Represent innates as normalized source context.
- Add talent context as conditional evidence.
- Avoid itemization and Scepter/Shard/Blink handling in this PR.

### PR 4 — Prompt Integration and Trial Heroes

- Render the composable context packet into `draft_fact_profile.md`.
- Wrap context JSON in fenced `json` blocks.
- Regenerate a small hero slice and review quality before Stage 5 rules depend
  on the new facts.

## Detailed First Implementation Steps

1. Add a reusable hero stat context module/API that computes deterministic stat
   bands and percentiles.
2. Add normalized ability-context rendering shared by prompt generation and
   future Oracle use.
3. Represent innates as one normalized ability source type within that ability
   context.
4. Add talent context to the prompt as conditional evidence.
5. Wrap prompt context JSON in fenced blocks.
6. Add or reference a small Dota mechanism primer if stats are included.
7. Update `draft_fact_profile.md` rules to distinguish baseline kit, innates,
   talents, and deferred itemization.
8. Add tests for:
   - stat band computation;
   - prompt includes stat context;
   - prompt includes normalized ability context instead of raw source-shaped JSON;
   - prompt includes innate source context when present;
   - prompt includes talent context without `role_distribution`;
   - response placeholder remains `.json`.
9. Update `docs/architecture.md` if the prompt contract changes.

## Future Oracle Context

This prompt hardening should leave room for a later query/oracle layer that can
combine:

- static authored hero facts;
- reusable raw hero facts such as normalized stats and ability context;
- patch-scoped derived relations;
- recent performance evidence such as pick rate, win rate, lane outcomes, item
  timing, or pro/pub cohort stats;
- explicit source timestamps and patch identifiers.

The baseline hero profile should not pretend to know recent form. It should give
the oracle a clean static fact layer that can be joined with fresh evidence.

## Verification

- `uv run pytest`
- `uv run pyright`
- `uv run ruff check`
- `uv run invoker vocab-audit`
- Generate one prompt for Slardar or Pangolier and inspect that:
  - stats include `value`, `percentile`, and `band`;
  - innate and talent context are present where source data provides them;
  - Scepter/Shard/item-dependent mechanics are not requested as baseline facts;
  - context JSON is fenced, but the response instructions still demand raw JSON.

## Open Questions

- Should vocabulary examples stay in the prompt, or should they be stripped once
  the prompt includes stats/talents and grows further?
- Which exact percentile cutoffs should define `low`, `average`, `high`, and
  `very_high`?
- Should talent-derived mechanics always become `vocabulary_gaps` until a
  conditional schema exists, or can very hero-defining talents be allowed as
  baseline notes with explicit evidence?
- What source should own the Dota mechanism primer for stat conversions? Review
  cadence is per patch.
