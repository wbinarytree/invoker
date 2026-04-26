# OpenDota Cache

Source of truth for the OpenDota HTTP cache layer: directory layout, hash function, file-to-endpoint mapping, and payload shapes.

Part of the architecture record. See [architecture.md](architecture.md) for system shape.

## Cache directory structure

Raw OpenDota responses are stored under:

```
data/raw/opendota/<patch>/
```

where `<patch>` is whatever string was passed to `CachedClient` — typically
`"7.41b"` for patch-scoped work or `"authoring"` for the prompt pipeline.

Files are named `<16-hex-char>.json`, one response per file.

## Hash function

Filename stems are the first 16 hex characters of the SHA-256 of the
canonicalized request:

```python
blob = json.dumps(
    {"m": method, "u": url, "p": params or {}, "b": body},
    sort_keys=True,
).encode()
filename_stem = hashlib.sha256(blob).hexdigest()[:16]
```

Source: `src/invoker/http/client.py` `_cache_key()`.

To compute the key for any endpoint without fetching:

```python
import hashlib, json

def cache_key(method, url, params=None, body=None):
    blob = json.dumps({"m": method, "u": url, "p": params or {}, "b": body}, sort_keys=True).encode()
    return hashlib.sha256(blob).hexdigest()[:16]
```

## Known file → endpoint mappings

All GET requests with no query params or body.

| Filename (stem)      | Endpoint                         | Shape             | Notes |
|----------------------|----------------------------------|-------------------|-------|
| `154eb197b09ba20f`   | `GET /api/heroes`                | `list[dict]`      | Hero roster. Keys: `id`, `name`, `localized_name`, `primary_attr`, `attack_type`, `roles`. |
| `2d6340a8ec99d459`   | `GET /api/constants/abilities`   | `dict[str, dict]` | All abilities keyed by internal name (`slardar_sprint`, etc.). ~3084 entries. |
| `3924af5614cf8c16`   | `GET /api/constants/hero_abilities` | `dict[str, dict]` | Per-hero ability/talent/facet lists keyed by `npc_dota_hero_*`. |
| `ef778ea33a2bdf3b`   | `GET /api/constants/heroes`      | `dict[str, dict]` | Full hero stat constants keyed by **numeric ID string** (`"28"`, not `"slardar"`). |

Matchup files (keyed by hero ID in the URL path, so each hero has its own hash):

| Filename (stem)      | Endpoint                         | Shape         |
|----------------------|----------------------------------|---------------|
| `d8da40b7276a473e`   | `GET /api/heroes/28/matchups`    | `list[dict]`  |
| `73f917a2a67a4e39`   | `GET /api/heroes/2/matchups`     | `list[dict]`  |
| `1dbec36fd8fbbff1`   | `GET /api/heroes/120/matchups`   | `list[dict]`  |
| `eacc1bcd38115288`   | `GET /api/proMatches`            | `list[dict]`  |

## Key payload shapes

### `/api/heroes` — `154eb197b09ba20f`

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

Used by `OpenDotaFetcher.heroes()`.

### `/api/constants/heroes` — `ef778ea33a2bdf3b`

Dict keyed by **numeric ID string**. Each entry has full stat fields:

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

**Gotcha**: keyed by numeric ID, not internal name. `build_hero_context` remaps:
```python
hero_stats_map = {v["name"]: v for v in raw_stats.values() if "name" in v}
```

Used by `OpenDotaFetcher.hero_stats()`.

### `/api/constants/abilities` — `2d6340a8ec99d459`

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
      {"key": "crush_damage", "header": "DAMAGE:", "value": ["75","150","225","300"]},
      {"key": "stun_duration", "header": "STUN DURATION:", "value": "0.8"},
      {"key": "abilitycastrange", "header": "CAST RANGE:", "value": "0", "generated": true}
    ],
    "mc": "100",
    "cd": "7"
  }
}
```

Field notes:
- `dname` — display name shown in tooltips
- `behavior` — `str` or `list[str]` (e.g. `["No Target", "Instant Cast"]`)
- `dmg_type` — `"Physical"` / `"Magical"` / `"Pure"`, absent for non-damaging abilities
- `bkbpierce` — `"Yes"` / `"No"`, absent if irrelevant
- `dispellable` — `"Yes"` / `"No"` / `"Strong Dispels Only"`, absent if irrelevant
- `is_innate: true` — present only on innate abilities
- `attrib` — list of scaling parameters; entries with `"generated": true` are
  synthetic tooltip fields (cast range, cast time, etc.) not from game data directly
- `mc` — mana cost as string, absent for passives or free abilities
- `cd` — cooldown as string or list of strings per level, absent for passives
- Talent entries have only `dname`, e.g. `{"dname": "+250 Health"}`

Used by `OpenDotaFetcher.abilities()`.

### `/api/constants/hero_abilities` — `3924af5614cf8c16`

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
      {"name": "special_bonus_hp_250",           "level": 2},
      {"name": "special_bonus_unique_slardar_5", "level": 2},
      {"name": "special_bonus_unique_slardar",   "level": 3},
      {"name": "special_bonus_unique_slardar_6", "level": 3},
      {"name": "special_bonus_unique_slardar_4", "level": 4},
      {"name": "special_bonus_unique_slardar_3", "level": 4}
    ],
    "facets": [...]
  }
}
```

Talent `level` is a tier index (1–4), not hero level. Tiers map to hero levels
10 / 15 / 20 / 25 respectively. Two talents per tier.

`generic_hidden` entries in `abilities` are placeholders with no data — skip them.

Talent ability objects in the abilities map typically contain only `dname`.

Used by `OpenDotaFetcher.hero_abilities_map()`.

## Staleness

`/api/constants/*` and `/api/heroes` always return the **current live game
state**. They are sourced from https://github.com/odota/dotaconstants and carry
no patch parameter. The `<patch>` subdirectory is cosmetic — constants fetched
under `authoring/` and `7.41b/` share the same hash and often the same file
(confirmed by duplicate hashes across both directories).

After any patch, cached constants silently drift. See
[`2026-04-26-opendota-constants-not-patch-versioned.md`](2026-04-26-opendota-constants-not-patch-versioned.md).

## How to force a re-fetch

Pass `force=True` to `CachedClient.get()`, or delete the `.json` file manually.
There is currently no CLI command to invalidate the cache.
