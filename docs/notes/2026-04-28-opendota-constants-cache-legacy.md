# Legacy OpenDota Constants Cache Payloads

Status: superseded by [docs/archive/specs/2026-04-27-game-files-as-primary-constants.md](../archive/specs/2026-04-27-game-files-as-primary-constants.md). Retained as a historical note for reading old cache directories and old PRs. Do not use this note to derive current Invoker behavior.

OpenDota constants were removed from the active cache documentation when
Phase 5b moved hero, ability, talent, item, and hero-stat constants to
`GameFilesSource`. These details are kept here so older cache files remain
interpretable.

## Legacy file to endpoint mappings

All requests were GET requests with no query params or body.

| Filename (stem)      | Endpoint                         | Shape             | Notes |
|----------------------|----------------------------------|-------------------|-------|
| `154eb197b09ba20f`   | `GET /api/heroes`                | `list[dict]`      | Hero roster. Keys: `id`, `name`, `localized_name`, `primary_attr`, `attack_type`, `roles`. |
| `2d6340a8ec99d459`   | `GET /api/constants/abilities`   | `dict[str, dict]` | All abilities keyed by internal name (`slardar_sprint`, etc.). About 3084 entries in the old cache. |
| `3924af5614cf8c16`   | `GET /api/constants/hero_abilities` | `dict[str, dict]` | Per-hero ability, talent, and facet lists keyed by `npc_dota_hero_*`. |
| `ef778ea33a2bdf3b`   | `GET /api/constants/heroes`      | `dict[str, dict]` | Full hero stat constants keyed by numeric ID string (`"28"`, not `"slardar"`). |

## `/api/heroes` - `154eb197b09ba20f`

List of hero objects. Each entry:

```json
{
  "id": 28,
  "name": "npc_dota_hero_slardar",
  "localized_name": "Slardar",
  "primary_attr": "str",
  "attack_type": "Melee",
  "roles": ["Carry", "Durable", "Initiator"]
}
```

Previously used by `OpenDotaFetcher.heroes()`.

## `/api/constants/heroes` - `ef778ea33a2bdf3b`

Dict keyed by numeric ID string. Each entry has full stat fields:

```json
{
  "28": {
    "id": 28,
    "name": "npc_dota_hero_slardar",
    "base_str": 22,
    "base_agi": 16,
    "base_int": 15,
    "str_gain": 3.2,
    "agi_gain": 1.5,
    "int_gain": 1.7,
    "base_armor": 3.0,
    "attack_range": 150,
    "move_speed": 295,
    "primary_attr": "str",
    "attack_type": "Melee"
  }
}
```

Gotcha: this payload was keyed by numeric ID, not internal name. Old context
builder code remapped it before computing stats:

```python
hero_stats_map = {v["name"]: v for v in raw_stats.values() if "name" in v}
```

Previously used by `OpenDotaFetcher.hero_stats()`.

## `/api/constants/abilities` - `2d6340a8ec99d459`

Dict keyed by internal ability name. Sample entry:

```json
{
  "slardar_slithereen_crush": {
    "dname": "Slithereen Crush",
    "behavior": "No Target",
    "dmg_type": "Physical",
    "bkbpierce": "No",
    "dispellable": "Strong Dispels Only",
    "desc": "Slams the ground...",
    "attrib": [
      {"key": "crush_damage", "header": "DAMAGE:", "value": ["75", "150", "225", "300"]},
      {"key": "stun_duration", "header": "STUN DURATION:", "value": "0.8"},
      {"key": "abilitycastrange", "header": "CAST RANGE:", "value": "0", "generated": true}
    ],
    "mc": "100",
    "cd": "7"
  }
}
```

Field notes:

- `dname`: display name shown in tooltips
- `behavior`: `str` or `list[str]`
- `dmg_type`: `"Physical"`, `"Magical"`, or `"Pure"` when present
- `bkbpierce`: `"Yes"` or `"No"` when present
- `dispellable`: `"Yes"`, `"No"`, or `"Strong Dispels Only"` when present
- `is_innate: true`: present only on innate abilities in some old payloads
- `attrib`: list of scaling parameters; entries with `"generated": true` were synthetic tooltip fields
- `mc`: mana cost as string, absent for passives or free abilities
- `cd`: cooldown as string or list of strings per level, absent for passives
- Talent entries often had only `dname`, for example `{"dname": "+250 Health"}`

Previously used by `OpenDotaFetcher.abilities()`.

## `/api/constants/hero_abilities` - `3924af5614cf8c16`

Dict keyed by `npc_dota_hero_*` internal name. Sample entry:

```json
{
  "npc_dota_hero_slardar": {
    "abilities": [
      "slardar_sprint",
      "slardar_slithereen_crush",
      "slardar_bash",
      "slardar_seaborn_sentinel",
      "generic_hidden",
      "slardar_amplify_damage"
    ],
    "talents": [
      {"name": "special_bonus_unique_slardar_7", "level": 1},
      {"name": "special_bonus_unique_slardar_2", "level": 1},
      {"name": "special_bonus_hp_250", "level": 2},
      {"name": "special_bonus_unique_slardar_5", "level": 2},
      {"name": "special_bonus_unique_slardar", "level": 3},
      {"name": "special_bonus_unique_slardar_6", "level": 3},
      {"name": "special_bonus_unique_slardar_4", "level": 4},
      {"name": "special_bonus_unique_slardar_3", "level": 4}
    ],
    "facets": []
  }
}
```

Talent `level` is a tier index from 1 to 4, not hero level. Tiers map to hero
levels 10, 15, 20, and 25. Two talents are present per tier.

`generic_hidden` entries in `abilities` are placeholders with no useful ability
data and were skipped by the context builder.

Previously used by `OpenDotaFetcher.hero_abilities_map()`.

## Why this is historical only

`/api/constants/*` and `/api/heroes` always return the current live game state
and carry no patch parameter. The `<patch>` subdirectory was cosmetic for these
constants; constants fetched under `authoring/` and `7.41b/` shared the same
hash and often the same file.

After any patch, cached constants silently drift. See
[OpenDota constants are not patch-versioned](2026-04-26-opendota-constants-not-patch-versioned.md).
