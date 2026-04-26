# PR3 — Normalized Ability/Talent Context

Date: 2026-04-26
Status: accepted

## Goal

Populate `HeroContextPacket.abilities` and `.talents` with typed, source-grounded
context built deterministically from cached OpenDota payloads.

## Decisions from review

- **`generated: true` filter dropped.** The field is arbitrary and unreliable in
  the OpenDota data. Include all attribs as-is.
- **Scepter/Shard ability detection: deferred.** No field in the current ability
  payload distinguishes Scepter/Shard-gated abilities. Accept them as normal
  abilities for now; scope detection in a later stage.
- **Facets: skip entirely.** Removed from recent Dota patches; not present in
  current hero data in any meaningful form.
- **`mechanics` list: omit.** Semantic extraction (mapping attrib keys to
  `{kind, duration, scope}`) requires a hand-maintained table and is not
  deterministic with the current data. `attribs` with `header`/`value` pairs is
  the PR3 representation.
- **`summary` field: omit.** Would require LLM generation (violates deterministic
  constraint) or duplicate `description`.
- **Attrib verbosity: accepted for now.** Some abilities have 10+ attribs. Include
  all of them in PR3. Aggregation or filtering strategy deferred.

## New module: `ability_context.py`

### Output types

```python
@dataclass(frozen=True)
class AttribEntry:
    header: str
    value: str | list[str]

@dataclass(frozen=True)
class AbilityContext:
    internal_name: str
    name: str                             # dname
    source: str                           # "base_ability" | "innate"
    behavior: list[str]                   # normalized from str or list[str]
    damage_type: str | None               # dmg_type field
    pierces_debuff_immunity: bool | None  # bkbpierce "Yes"→True / "No"→False
    dispellable: str | None               # "Yes" / "No" / "Strong Dispels Only"
    description: str | None              # desc field
    attribs: list[AttribEntry]            # all attribs included as-is
    mana_cost: str | None
    cooldown: str | list[str] | None

@dataclass(frozen=True)
class TalentContext:
    internal_name: str
    name: str   # dname joined from abilities map
    level: int  # tier 1–4 (hero levels 10 / 15 / 20 / 25)
```

### Build function

```python
def build_ability_contexts(
    hero_internal_name: str,
    abilities_map: dict[str, Any],       # from OpenDotaFetcher.abilities()
    hero_abilities_map: dict[str, Any],  # from OpenDotaFetcher.hero_abilities_map()
) -> tuple[list[AbilityContext], list[TalentContext]]:
    ...
```

Filtering rules:
- Skip `generic_hidden` entries in the abilities list.
- Skip any ability name absent from `abilities_map` (no data = no context entry).
- `source = "innate"` when `is_innate: true` in the raw ability dict, else `"base_ability"`.

### Updates to `hero_context.py`

`abilities: list[Any]` and `talents: list[Any]` become typed:

```python
abilities: list[AbilityContext] = field(default_factory=list)
talents: list[TalentContext] = field(default_factory=list)
```

`build_hero_context` fetches the two new payloads and populates the packet:

```python
raw_abilities = await fetcher.abilities()
hero_abilities_raw = await fetcher.hero_abilities_map()
abilities, talents = build_ability_contexts(internal_name, raw_abilities, hero_abilities_raw)
return HeroContextPacket(..., abilities=abilities, talents=talents)
```

## Out of scope

- `mechanics` semantic extraction
- `summary` generation
- Facets
- `generated: true` filtering
- Scepter / Shard / item-conditional ability detection
