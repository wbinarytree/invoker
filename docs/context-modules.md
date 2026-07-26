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

[src/invoker/kg/hero_context.py](../src/invoker/kg/hero_context.py)

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

[src/invoker/kg/hero_stats_context.py](../src/invoker/kg/hero_stats_context.py)

Computes a `HeroStatsContext` for one hero relative to the full roster. Each tracked
stat (`base_str`, `base_agi`, `base_int`, `str_gain`, `agi_gain`, `int_gain`,
`base_armor`, `base_attack_min`, `base_attack_max`, `base_attack_speed`,
`base_attack_time`, `attack_animation_point`, `attack_acquisition_range`,
`attack_range`, `move_speed`) is reported with:

```json
{ "value": 4.0, "percentile": 0.93, "band": "very_high" }
```

Bands are deterministic quintiles: `very_low` / `low` / `average` / `high` / `very_high`.

Source data comes from `GameFilesSource.hero_stats()`, backed by the
patch-scoped `heroes.json` snapshot. `base_attack_time` maps Valve's
`AttackRate` key. `base_attack_speed` maps `BaseAttackSpeed`; when a hero row
omits it, the adapter uses the inherited `npc_dota_hero_base` default of `100`
from the extracted npc files.

## `ability_context.py`

[src/invoker/kg/ability_context.py](../src/invoker/kg/ability_context.py)

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
- `attribs`: `AttribEntry` rows from the raw `attrib` array (tooltip-noisy
  headers dropped). Rows carry `scepter_bonus` / `shard_bonus` when the KV
  value has `special_bonus_scepter` / `special_bonus_shard` modifiers;
  upgrade-only rows (no base value in KV) have `value: None`
- `cast_range`: source-backed `AbilityCastRange`, absent when not present in the snapshot
- `timing`: source-backed low-level timing fields from the snapshot, currently
  `cast_point`, `channel_time`, `cast_animation`, `cast_gesture_slot`, and
  `animation_playback_rate` when present
- `mana_cost` / `cooldown`: absent on passives
- `scepter_upgrade` / `shard_upgrade`: localized upgrade description
  (`..._scepter_description` / `..._shard_description` tokens,
  `%field%`-resolved), absent when the snapshot carries none
- `granted_by`: `"scepter"` / `"shard"` for abilities granted by the upgrade
  item; these are kept even when behavior contains `Hidden`

Known gap: a granted ability appears in the packet only when it is listed in
the hero's ability slots. ~30 scepter/shard-granted abilities (e.g.
`slardar_scepter`) are defined only in per-hero KV files and are in no
hero's list; joining them needs the snapshot builder to record each
ability's defining file (tracked follow-up).

**`TalentContext`** — one per talent entry from `hero_abilities_map`:

- `level`: tier 1–4 (maps to hero levels 10 / 15 / 20 / 25)
- `name`: display name joined from the abilities map. Talent `{s:bonus_*}`
  templates are resolved upstream in `GameFilesSource` from KV `AbilityValues`;
  unresolved placeholder substitution with `?` has been retired.

Filtering: `generic_hidden` entries and abilities absent from the abilities map
are skipped. Non-innate abilities whose behavior contains `Hidden` are also
dropped. Scepter/Shard flags are exposed by `GameFilesSource` in the raw ability
records for downstream conditional-fact work.

Ability descriptions resolve source-backed `%field%` localization templates from
KV `AbilityValues`; unresolved placeholders remain visible rather than being
filled from memory.

## `item_context.py`

[src/invoker/kg/item_context.py](../src/invoker/kg/item_context.py)

`build_item_context(game_data_dir, item, patch=patch)` assembles an
`ItemContext` from the snapshot's `items.json` + localization
(`GameFilesSource.item_records()`). `item` resolves by internal name (with or
without the `item_` prefix) or localized name — resolution keys off the item
record, so cosmetic localization tokens (e.g. "Glaive of the Mage Slayer")
can't pollute the join.

- `name` / `description` / `lore`: localized; descriptions resolve `%field%`
  templates from `AbilityValues` and strip tooltip HTML (`<h1>`, `<br>`
  become line breaks); `description_token` / `lore_token` record which
  localization token actually resolved (packets cite them, never a
  synthesized casing)
- `cost` / `recipe_cost`: `ItemCost` as int; `recipe_cost` present only when
  the recipe itself costs gold
- `components`: `ItemRef` rows (internal name, localized name, gold cost)
  from the recipe's `ItemRequirements` (first variant, optional-`*` markers
  stripped); costs looked up from the same item records — `None` when a
  component record is missing, never an invented price
- `builds_into`: `ItemRef` rows for every item whose recipe requires this
  one (deterministic order); empty for items nothing builds from
- `attribs`: `AttribEntry` rows from `AbilityValues` (same shape as ability
  packets, including scepter/shard bonuses)
- `behavior` / `damage_type` / `dispellable` / `cast_range` / `mana_cost` /
  `cooldown`: as in ability contexts; recipes are folded into their result
  item and never appear as records

Inspection: `invoker show-item-context ITEM [--patch <patch>]`.

## `mechanism_primer.py`

[src/invoker/kg/mechanism_primer.py](../src/invoker/kg/mechanism_primer.py)

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
