# Invoker — Static Hero Context Modules

Part of the architecture record. See [architecture.md](architecture.md) for system shape and artifacts.

These modules produce reusable, source-grounded context packets for hero authoring.
They are not prompt-specific; prompt generation is one consumer.

Current packet shape:

```python
@dataclass(frozen=True)
class HeroContextPacket:
    patch: str
    hero: HeroIdentityContext
    stats: HeroStatsContext
    abilities: list[AbilityContext]
    talents: list[TalentContext]
```

`MechanismPrimerContext` is patch-scoped, not hero-scoped. Load it separately
via `load_mechanism_primer(packet.patch)` when needed alongside a packet.

---

## `hero_context.py`

[src/invoker/kg/hero_context.py](/Users/yaoda/Projects/invoker/src/invoker/kg/hero_context.py)

Composition API. `build_hero_context(game_data_dir, hero, patch=patch)` assembles a
`HeroContextPacket` from a game-file JSON snapshot. `game_data_dir` is the
`INVOKER_GAME_DATA_DIR` root, and `patch` selects `<game_data_dir>/<patch>/`.

The default entrypoint intentionally constructs `GameFilesSource` because game
snapshots are the primary constants source. Packet assembly itself is split into
`build_hero_context_from_source(source, hero, patch=patch)`, where `source`
implements the narrow constants surface (`heroes`, `hero_stats`, `abilities`,
`hero_abilities_map`). That keeps future source swaps mechanical without adding
a runtime source-selection layer today.

## `hero_stats_context.py`

[src/invoker/kg/hero_stats_context.py](/Users/yaoda/Projects/invoker/src/invoker/kg/hero_stats_context.py)

Computes a `HeroStatsContext` for one hero relative to the full roster. Each tracked
stat (`base_str`, `base_agi`, `base_int`, `str_gain`, `agi_gain`, `int_gain`,
`base_armor`, `attack_range`, `move_speed`) is reported with:

```json
{ "value": 4.0, "percentile": 0.93, "band": "very_high" }
```

Bands are deterministic quintiles: `very_low` / `low` / `average` / `high` / `very_high`.

Source data comes from `GameFilesSource.hero_stats()`, backed by the
patch-scoped `heroes.json` snapshot.

## `ability_context.py`

[src/invoker/kg/ability_context.py](/Users/yaoda/Projects/invoker/src/invoker/kg/ability_context.py)

Builds `AbilityContext` and `TalentContext` lists from game-file snapshot
payloads (`GameFilesSource.abilities()` and `hero_abilities_map()`).

```python
def build_ability_contexts(
    hero_internal_name: str,
    abilities_map: dict[str, Any],
    hero_abilities_map: dict[str, Any],
) -> tuple[list[AbilityContext], list[TalentContext]]: ...
```

**`AbilityContext`** — one per base ability or innate:

- `source`: `"base_ability"` or `"innate"` (from `is_innate: true` in raw data)
- `behavior`: always `list[str]` (normalized from string or list)
- `pierces_debuff_immunity`: `bool | None` (from `bkbpierce` "Yes"/"No")
- `attribs`: `AttribEntry` rows from the raw `attrib` array, with Scepter/Shard/tooltip-noisy headers dropped
- `mana_cost` / `cooldown`: absent on passives

**`TalentContext`** — one per talent entry from `hero_abilities_map`:

- `level`: tier 1–4 (maps to hero levels 10 / 15 / 20 / 25)
- `name`: display name joined from the abilities map. Talent `{s:bonus_*}`
  templates are resolved upstream in `GameFilesSource` from KV `AbilityValues`;
  unresolved placeholder substitution with `?` has been retired.

Filtering: `generic_hidden` entries and abilities absent from the abilities map
are skipped. Non-innate abilities whose behavior contains `Hidden` are also
dropped. Scepter/Shard flags are exposed by `GameFilesSource` in the raw ability
records for downstream conditional-fact work.

## `mechanism_primer.py`

[src/invoker/kg/mechanism_primer.py](/Users/yaoda/Projects/invoker/src/invoker/kg/mechanism_primer.py)

Loads a per-patch YAML file (`mechanism_primer_{patch}.yaml`, co-located in the
`src/invoker/kg/` package) into a `MechanismPrimerContext`. Returns empty mechanics
for unknown patches.

The YAML is human-maintained and reviewed per patch. `reviewed_by` and `reviewed_at`
must be set after each verification pass against official Dota documentation.
Current file: `mechanism_primer_7.41b.yaml`.

This primer remains active after Phase 5b because the current game-file snapshot
does not expose an equivalent source for global stat-conversion constants
(HP per Strength, armor per Agility, and related mechanics).

---

## Inspection

```
invoker show-hero-context HERO [--patch <patch>]
```

Dumps the assembled packet as JSON. See [`cli.md`](cli.md) → `show-hero-context`.
