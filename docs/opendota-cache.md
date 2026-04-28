# OpenDota Cache

Source of truth for the OpenDota HTTP cache layer: directory layout, hash function, file-to-endpoint mapping, and payload shapes.

Part of the architecture record. See [architecture.md](architecture.md) for system shape.

## Cache directory structure

Raw OpenDota responses are stored under:

```
data/raw/opendota/<patch>/
```

where `<patch>` is whatever string was passed to `CachedClient` — typically
`"7.41b"` for patch-scoped match-data work.

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

## Active file → endpoint mappings

All GET requests with no query params or body.

Matchup files (keyed by hero ID in the URL path, so each hero has its own hash):

| Filename (stem)      | Endpoint                         | Shape         |
|----------------------|----------------------------------|---------------|
| `d8da40b7276a473e`   | `GET /api/heroes/28/matchups`    | `list[dict]`  |
| `73f917a2a67a4e39`   | `GET /api/heroes/2/matchups`     | `list[dict]`  |
| `1dbec36fd8fbbff1`   | `GET /api/heroes/120/matchups`   | `list[dict]`  |
| `eacc1bcd38115288`   | `GET /api/proMatches`            | `list[dict]`  |

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

## How to force a re-fetch

Pass `force=True` to `CachedClient.get()`, or delete the `.json` file manually.
There is currently no CLI command to invalidate the cache.
