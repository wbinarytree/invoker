# PR3 — Normalized Ability/Talent Context

Date: 2026-04-26
Status: draft — pending sign-off

## Goal

Populate `HeroContextPacket.abilities` and `.talents` with typed, source-grounded
context built deterministically from cached OpenDota payloads.

## New module: `ability_context.py`

### Output types

```python
@dataclass(frozen=True)
class AttribEntry:
    header: str
    value: str | list[str]   # scaling values, one entry or per-level list

@dataclass(frozen=True)
class AbilityContext:
    internal_name: str
    name: str                        # dname
    source: str                      # "base_ability" | "innate"
    behavior: list[str]              # normalized from str or list[str]
    damage_type: str | None          # dmg_type field
    pierces_debuff_immunity: bool | None   # bkbpierce "Yes"→True / "No"→False
    dispellable: str | None          # "Yes" / "No" / "Strong Dispels Only"
    description: str | None          # desc field
    attribs: list[AttribEntry]       # scaling data; generated=true entries dropped
    mana_cost: str | None
    cooldown: str | list[str] | None

@dataclass(frozen=True)
class TalentContext:
    internal_name: str
    name: str    # dname joined from abilities map
    level: int   # tier 1–4 (hero levels 10 / 15 / 20 / 25)
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
- Drop `attrib` entries where `generated: true` (synthetic tooltip fields).
- `source = "innate"` when `is_innate: true` in the raw ability dict, else `"base_ability"`.

### Update to `HeroContextPacket`

`abilities: list[Any]` and `talents: list[Any]` become typed:

```python
abilities: list[AbilityContext] = field(default_factory=list)
talents: list[TalentContext] = field(default_factory=list)
```

### Update to `build_hero_context`

Fetch both new payloads and populate the packet:

```python
raw_abilities = await fetcher.abilities()
hero_abilities_raw = await fetcher.hero_abilities_map()
abilities, talents = build_ability_contexts(internal_name, raw_abilities, hero_abilities_raw)
return HeroContextPacket(..., abilities=abilities, talents=talents)
```

## Open questions — sign-off required

### Q1 — No `mechanics` list in PR3

The parent spec example shows a `mechanics: [{kind, duration, scope}]` list.
Deriving it deterministically requires mapping internal attrib keys
(`crush_damage`, `stun_duration`) to semantic kinds — that needs a
hand-maintained key→kind table and is not trivially deterministic.

**Proposal:** omit `mechanics` in PR3. The `attribs` list with structured
`header`/`value` pairs is already readable and source-grounded. Defer semantic
mechanic extraction to a later PR.

### Q2 — No `summary` field in PR3

`summary` either requires an LLM pass (violates deterministic constraint) or
duplicates `description`. Proposal: omit.

### Q3 — Scepter/Shard attribs on innate abilities

`slardar_seaborn_sentinel` has `scepter_*` and `shard_*` keyed attribs. In the
current data they are all marked `generated: true`, so the existing filter drops
them. The parent spec says to avoid Scepter/Shard handling in this PR.

**Proposal:** rely on the `generated: true` filter only — no explicit key-prefix
block. If a future data update exposes non-generated Scepter attribs they would
appear, which is acceptable to revisit then.

### Q4 — Facets

`hero_abilities_map` includes a `facets` array per hero (Slardar has 2, both
currently `deprecated: "true"`). Facets are not mentioned in the parent spec for
this PR.

**Proposal:** ignore facets in PR3. No field on `HeroContextPacket`.

## Out of scope

- `mechanics` semantic extraction
- `summary` generation
- Facets
- Scepter / Shard / item-conditional abilities
