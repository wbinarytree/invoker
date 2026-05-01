# OpenDota Cache

Source of truth for the OpenDota HTTP cache layer: directory layout, hash
function, envelope shape, and payload boundaries.

Part of the architecture record. See [architecture.md](architecture.md) for system shape.

## Cache directory structure

Invoker uses the shared Dota agents cache for OpenDota responses:

```
$CACHE_DIR/opendota/responses/
```

`CACHE_DIR` defaults to `~/.cache/dota-agents/`. If provided through the
environment, it must be an absolute path.

Files are named from the endpoint plus sorted params, matching Oracle's current
shared-cache helper:

```text
proMatches.json
proMatches__less_than_match_id=8792587799.json
heroes_28_matchups.json
```

## Hash Function

The legacy local `CachedClient` still uses a 16-character SHA-256 suffix for
non-shared source caches. The shared OpenDota response cache uses endpoint and
params only so sibling Dota projects can reuse the same files.

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

## File Envelope

Each shared cache file is a JSON envelope:

```json
{
  "meta": {
    "endpoint": "/proMatches",
    "params": {},
    "fetched_at": "2026-04-30T00:00:00Z",
    "schema_version": 1,
    "fetched_by": "invoker@0.1.0"
  },
  "data": []
}
```

`data` is the raw OpenDota API response. Normalization stays inside Invoker
consumers. `source_patch` is optional and should only be written when the source
payload is genuinely patch-scoped. Current OpenDota match-data endpoints do not
write it.

Writes are atomic: the client writes a temporary file and then replaces the
target path.

## Active Endpoint Mappings

All current OpenDota requests are GET requests with no request body. Matchup
requests have no params; `proMatches` may include `less_than_match_id` when
paginating.

Matchup files (keyed by hero ID in the URL path, so each hero has its own hash):

| Filename pattern                         | Endpoint                         | Shape         |
|------------------------------------------|----------------------------------|---------------|
| `heroes_28_matchups.json`                | `GET /api/heroes/28/matchups`    | `list[dict]`  |
| `heroes_2_matchups.json`                 | `GET /api/heroes/2/matchups`     | `list[dict]`  |
| `heroes_120_matchups.json`               | `GET /api/heroes/120/matchups`   | `list[dict]`  |
| `proMatches.json`                        | `GET /api/proMatches`            | `list[dict]`  |
| `proMatches__less_than_match_id=<id>.json` | `GET /api/proMatches?less_than_match_id=<id>` | `list[dict]` |
| `teams_<team_id>_matches.json`           | `GET /api/teams/<team_id>/matches` | `list[dict]` |
| `matches_<match_id>.json`                | `GET /api/matches/<match_id>`    | `dict`        |

## Key payload shapes

OpenDota is now used only for match data. Hero, ability, talent, item, and hero
stat constants come from `GameFilesSource` and the game-file snapshot described
in [game-files-snapshot.md](game-files-snapshot.md). Historical OpenDota
constants cache mappings and payload examples are retained in
[2026-04-28-opendota-constants-cache-legacy.md](notes/2026-04-28-opendota-constants-cache-legacy.md).

## Staleness

`/api/constants/*` and `/api/heroes` always return the current live game state
and carry no patch parameter. Invoker no longer consumes those OpenDota
constants because cached constants silently drift after patches. See
[`2026-04-26-opendota-constants-not-patch-versioned.md`](notes/2026-04-26-opendota-constants-not-patch-versioned.md).

Historical match detail responses can be cached indefinitely. Rolling list
endpoints such as team match history should be refreshed explicitly when stale
data matters; the envelope's `fetched_at` field exists to diagnose that.
Patch-name assignment for team profiles does not call OpenDota constants. It
uses the tracked `src/invoker/patches.json` date windows and match `start_time`.

## How to force a re-fetch

Pass `force=True` to `SharedOpenDotaCachedClient.get()`, or delete the `.json`
file manually.
There is currently no CLI command to invalidate the cache.
