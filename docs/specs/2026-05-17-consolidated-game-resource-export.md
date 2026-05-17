# Consolidated Game Resource Export

Status: discussion

## Why

The current 7.41c split export is useful as a quick downstream bridge, but it is
not the right long-term resource contract:

- hero identity and item identity are separated, but consumers still need to
  stitch hero stats, abilities, talents, and localization together;
- `ability_localization.json` is too close to raw ability records and does not
  use the successful `GameFilesSource -> HeroContextPacket` normalization path;
- many "missing descriptions" in the current ability export are talent records
  or otherwise conditional records, and talents are important enough to model
  explicitly rather than treat as broken base abilities;
- item records should carry item stats, active/passive item ability metadata,
  aliases, localization, and neutral status together.

The better contract is a compact, patch-scoped game-resource bundle that is
query-friendly for downstream projects such as Phylactery while remaining
source-backed by the Invoker game-file snapshot. The bundle should keep hero
and item resources separate because their query surfaces and update needs are
different.

## Current NPC Snapshot Inputs

`snapshot-game-files` currently creates this patch-scoped source bundle under
`INVOKER_GAME_DATA_DIR/<patch>/`:

- `heroes.json` from `npc/npc_heroes.txt`
- `abilities.json` from `npc/npc_abilities.txt` plus per-hero
  `npc/heroes/npc_dota_hero_*.txt` overlays
- `hero_abilities.json` from hero ability/talent lists
- `items.json` from `npc/items.txt`
- `neutral_items.json` from `npc/neutral_items.txt`
- `localization/<locale>.json` merged from `abilities_<locale>.txt`,
  `items_<locale>.txt`, and `dota_<locale>.txt`
- `snapshot.json` with sanitized source metadata and relative file inventory

This snapshot is intentionally source-like JSON. It should remain the
low-level, patch-specific truth extracted from Valve files, not the downstream
consumer API.

## What Invoker Can Already Derive

From the current snapshot and `GameFilesSource`, Invoker can already derive:

- live hero roster, hero ids, internal names, slugs, localized names, primary
  attribute, attack type, and role tags;
- hero base stats and growth values, plus deterministic percentile/band context
  through `HeroStatsContext`;
- hero ability lists, hidden/filler filtering, innate flags, behavior, damage
  type, debuff-immunity piercing, dispel type, mana cost, cooldown, and
  description through `AbilityContext`;
- talent lists attached to each hero, including level/tier and resolved display
  names; this path already fixed the older `{s:bonus_*}` placeholder problem;
- raw item and neutral item KV, including costs, recipes, neutral active-drop
  flags, purchasability/sellability, `AbilityValues`, and ability behavior;
- official localization for hero names, ability names/descriptions, item
  names/descriptions, search aliases, and hero alias keys where Valve exposes
  them.

Previous notes worth preserving:

- `GameFilesSource` is the source of truth for constants; OpenDota is match data
  only.
- Normalization belongs in the consumer layer (`GameFilesSource`,
  `hero_context.py`, `ability_context.py`), not in the raw snapshot writer.
- The authoring prompt path is the proven quality path: it resolves talent
  templates, filters hidden ability noise, and presents ability/talent context
  attached to one hero.
- Localization lookup rules should stay centralized so string-concat key
  conventions do not leak through the codebase.

## Target Contract

Add a new bundled export command, tentatively:

```bash
uv run invoker export-game-resources \
  --patch 7.41c \
  --locale english \
  --locale schinese \
  --out-dir /tmp/invoker_741c_resources
```

The artifact should be a patch-scoped directory bundle:

```text
/tmp/invoker_741c_resources/
  bundle.json
  heroes.json
  items.json
  index.json
```

`bundle.json` should hold shared metadata:

```json
{
  "schema_version": 1,
  "patch": "7.41c",
  "locales": ["english", "schinese"],
  "generated_from": {},
  "files": {
    "heroes": "heroes.json",
    "items": "items.json",
    "index": "index.json"
  },
  "unknowns": []
}
```

`heroes.json` and `items.json` should each be coherent source-backed artifacts,
not raw snapshot pass-throughs. The bundle is the downstream handoff unit; the
files inside it stay separate. `index.json` should provide lightweight lookup
tables for ids, internal names, slugs, aliases, and display names so downstream
consumers can resolve a query without scanning every full record.

## Hero Records

Hero records should be the primary query surface for hero facts and live in
`heroes.json`:

```json
{
  "hero_id": 73,
  "internal_name": "npc_dota_hero_alchemist",
  "slug": "alchemist",
  "display_names": {"english": "Alchemist", "schinese": "炼金术士"},
  "aliases": {"english": ["alch"], "schinese": []},
  "primary_attr": "str",
  "attack_type": "Melee",
  "roles": ["Carry", "Support"],
  "stats": {
    "base_str": {"value": 23, "percentile": 0.51, "band": "average"}
  },
  "abilities": [],
  "talents": [],
  "sources": ["npc_heroes", "hero_abilities", "abilities", "localization"]
}
```

Attach hero abilities and talents directly to hero records. This makes the
common downstream query simple: lookup hero once, get identity, stats, ability
context, talent context, aliases, and localized labels together.

## Ability Records Under Heroes

Use the same normalization path as `HeroContextPacket` instead of exporting raw
ability rows. Ability records under each hero should include:

- `internal_name`
- localized `display_names`
- localized `descriptions`
- `source`: `base_ability`, `innate`, `granted_by_shard`, `scepter_upgrade`, or
  another explicit conditional source when available
- normalized `behavior`
- `damage_type`
- `pierces_debuff_immunity`
- `dispellable`
- `mana_cost`
- `cooldown`
- normalized attribute rows with source keys, machine keys, values, and
  localized headers when present
- raw-source pointers, not raw KV dumps

Do not treat missing base-ability descriptions and missing talent descriptions
as the same problem. Talents should be exported as talents.

## Talent Records Under Heroes

Talent records should be first-class:

```json
{
  "internal_name": "special_bonus_unique_alchemist",
  "level": 1,
  "hero_level": 10,
  "display_names": {"english": "+1 Acid Spray Armor"},
  "value_sources": ["AbilityValues"],
  "sources": ["hero_abilities", "abilities", "localization"]
}
```

Talents need:

- level/tier and hero-level mapping;
- resolved names per locale when possible;
- source-backed value resolution from `AbilityValues`;
- no invented description when Valve only exposes a display template.

This should reduce noisy "missing description" unknowns while preserving real
gaps.

## Item Records

Item records should mirror hero records for item queries and live in
`items.json`:

```json
{
  "internal_name": "item_blink",
  "item_id": 1,
  "display_names": {"english": "Blink Dagger", "schinese": "闪烁匕首"},
  "aliases": {"english": ["blink dagger"], "schinese": ["tiaodao", "跳刀"]},
  "descriptions": {},
  "is_neutral": false,
  "is_recipe": false,
  "cost": 2250,
  "stats": {},
  "ability": {},
  "sources": ["items", "localization"]
}
```

Item records should include:

- purchased vs recipe vs neutral classification;
- cost and stable ids when present;
- recipes as source-backed item records, with `is_recipe: true`, result item,
  and component requirements when available;
- source-backed item stat values from `AbilityValues`;
- active/passive item ability metadata using the same normalized ability shape
  as hero abilities where possible;
- official names, descriptions, and search aliases per locale;
- neutral tier/drop metadata when derivable from `neutral_items.json`.

## Unknowns And Gaps

`unknowns` should distinguish:

- missing hero display names;
- missing item display names;
- missing base ability display names;
- missing item ability display names;
- missing talent display names;
- missing descriptions for entities where descriptions are expected;
- omitted descriptions for talents where Valve only provides a display string;
- alias collisions after normalization.

Null or missing is correct when the snapshot lacks a source-backed value. The
export should never fill plausible names, descriptions, or stats from training
memory.

## Proposed Implementation Slices

- [x] Add this spec and route it from `docs/CURRENT_DIRECTION.md`.
- [x] Add a serializer that builds hero records from `build_hero_context` /
  `build_hero_context_from_source`, not from raw `abilities.json`.
- [x] Extend localization helpers to resolve display names/descriptions/aliases
  across multiple locales from one export pass.
- [x] Promote talent export to a first-class nested hero field.
- [x] Add item normalization from `items.json` and `neutral_items.json`, with
  localized names, descriptions, aliases, costs, stats, recipes, and
  active/passive behavior.
- [x] Add `export-game-resources` CLI that writes a bundle directory with
  `bundle.json`, `heroes.json`, `items.json`, and `index.json`.
- [x] Add lookup indexes for hero and item ids, internal names, slugs/display
  names, and aliases.
- [x] Keep the existing `export-identity-localization` command as a short-term
  compatibility path until Phylactery moves to the consolidated artifact.
- [x] Generate a local 7.41c artifact and compare it against the current split
  files for missing-name and missing-description counts.

## Validation

- `uv run pytest`
- `uv run pyright`
- `uv run ruff check`
- Local smoke against `data/invoker-game-data/7.41c`
- Spot checks:
  - Alchemist hero record includes identity, stats, Acid Spray, and talents.
  - Puck hero record includes Illusory Orb with localized description.
  - Blink Dagger item record includes aliases and active ability text.
  - Occult Bracelet and Fallen Sky recover `:n` display names and descriptions.
  - Talent rows do not inflate missing-description counts as if they were
    ordinary base abilities.

## Decisions

- Include a lightweight lookup index in the bundle. This should not materially
  change the exporter implementation because it can be derived from the final
  hero and item records.
- Include item recipes in the item artifact. Recipes should remain
  source-backed item records, with result/component metadata when available.
- Include localized ability attribute headers when practical in this slice.
  They are official localization labels for `AbilityValues` rows, not ability
  names or descriptions.

## Open Questions

- Should recipes also be nested under their result item for convenience, or is
  the indexed recipe record enough for the first bundle?
