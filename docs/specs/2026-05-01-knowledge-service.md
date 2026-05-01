# Knowledge Service

Date: 2026-05-01
Status: approved
Scope: read-only local knowledge service, resource bundle shape, HTTP/MCP API shape, and first consumer queries

## Purpose

Invoker currently produces useful team-profile artifacts and game-file-backed
hero constants, but other agents have to either import Invoker Python code or
understand local file layouts. The next step is a stable read surface: a local
knowledge service that loads a resource bundle and answers structured agent
queries.

The first implementation should be small. It should expose basic hero facts and
team aggregate facts that already exist or are directly backed by existing
snapshots. It should not redesign KG generation, team-profile generation,
artifact storage, or relation inference.

## Goals

- Let other agents consume Invoker knowledge without importing internal modules
  or traversing arbitrary JSON files.
- Provide a shared service core with thin HTTP and MCP-style adapters.
- Make each service instance rely on one explicit resource bundle.
- Keep local JSON artifacts inside that resource bundle as the canonical
  knowledge source for the service instance.
- Expose game-file-backed hero constants only in the first hero slice.
- Expose team aggregate views such as roster, stand-ins, played heroes, and
  per-player hero pools from existing team-profile artifacts.
- Resolve common team names and player names so callers do not need to know
  OpenDota team IDs or account IDs upfront.
- Keep the first API domain-oriented, not graph- or file-layout-oriented.
- Keep the service shape compatible with later hosted deployment.

## Non-Goals

- No DB-canonical migration in the first slice.
- No Neo4j, hosted graph database, or external service dependency.
- No query-time network fetches.
- No natural-language query endpoint.
- No LLM in the read path.
- No raw OpenDota payload exposure through the service.
- No arbitrary file-browser or JSONPath API.
- No public hosting implementation in the first slice.
- No KG facts, authored fact buckets, inferred relations, summaries, graph
  queries, or NetworkX-backed APIs in the first slice.
- No public `roster_hash` parameter in the service API.

## Resource Bundle And Storage

Each service instance should start from a resource bundle. The bundle is the
complete read source for that running service instance; the service should not
reach back into arbitrary working-tree paths during normal reads.

The first resource bundle should include:

- game-file-backed hero constants for the bundled patch or patch set;
- `data/derived/<patch>/teams/index.json`
- `data/derived/<patch>/teams/<team_id>/<roster_hash>/profile.json`
- bundle metadata that identifies available patches and generated-at/source
  metadata.

For team facts, `profile.json` is the reliable source in the current redesigned
project state. `roster_hash` remains an internal storage detail used to locate a
profile file. Consumers should not pass it or see it as a required identifier.

For hero facts, the first service slice should read game-file-backed constants
from the bundled equivalent of `INVOKER_GAME_DATA_DIR`. Authored/derived KG hero
facts are out of scope until the KG cleanup is done.

No graph index is required for this first service. NetworkX is not part of the
service contract.

Later resource bundles may add generated indexes. Those indexes should remain
rebuildable implementation details and must not change the public service API.

## Service Shape

The first implementation should introduce a shared service core, for example
`KnowledgeService`, that owns bundle loading, validation, resolution, and query
methods. HTTP and MCP adapters should call the same service methods and return
equivalent payloads.

Reader methods must be local and read-only. Missing artifacts should produce
actionable errors:

- missing team index artifacts should report that the resource bundle does not
  contain team profiles for the requested patch or bundle default;
- missing team profiles should tell the operator to run
  `build-team-profile --team-id <id> --patch <patch>`;
- missing hero constants should report that the resource bundle does not contain
  game constants for the requested hero or patch.

The service should be bundle-explicit, not necessarily patch-required. Many
upstream data sources and consumer questions do not naturally start from a patch
filter. If the loaded resource bundle contains one patch, callers should not
have to pass `patch`. If it contains multiple patches, the service may use the
bundle default or return a clear ambiguity error that lists available patches.

## Response Boundaries

Responses should keep source-backed sections explicit.

### Hero constants

`hero_constants` is backed by bundled game-file snapshots. It is the right place
for hero attributes, abilities, talents, localized names, and similar game
constants. Missing snapshot data should remain missing; the service must not
fill values from model memory or approximate public knowledge.

### Team profile facts

`team_profile` is backed by generated team-profile artifacts. It is the right
place for roster, stand-ins, team hero pool, per-player hero pool, observed
patch windows, tournaments, and match-ID evidence.

Each response should include enough metadata for consumers to understand source
and freshness: patch, schema version, source artifact type, and provenance or
evidence fields where available.

## First API Surface

The first API should be intentionally small and action-oriented.

Hero methods:

```text
list_bundle_patches() -> patches
lookup_hero(query, patch?) -> hero identity candidates
get_hero_constants(hero, patch?) -> hero_constants
```

Team methods:

```text
resolve_team(query, patch?) -> team candidates
resolve_player(query, team?, patch?) -> player candidates
get_team_profile(team, patch?) -> full aggregate profile
get_team_roster(team, patch?) -> roster and stand-ins
get_team_hero_pool(team, patch?) -> team played heroes
get_team_player_hero_pool(team, player, patch?) -> player played heroes
```

HTTP route names and MCP tool names should mirror the service method names as
closely as practical. The adapters should not introduce separate business logic.

`team` may be a team ID, exact team name, alias, or observed team name. `player`
may be an account ID or exact player/persona name. Name resolution should be
deterministic and conservative:

- exact numeric IDs resolve directly;
- exact normalized names and aliases resolve when unambiguous;
- ambiguous names return candidates instead of choosing silently;
- fuzzy matching may be added later as suggestions, not as authoritative
  automatic resolution.

## HTTP And MCP Roles

HTTP and MCP are different transports over the same service core.

HTTP is the better public and hosted-service shape. It gives normal routes,
status codes, auth/rate-limit options, browser/debug tooling, and an obvious
path to deploy behind a server.

MCP is the better direct agent-tool shape. It lets agent runtimes discover tools
and call structured methods without hand-writing HTTP clients. MCP is not the
canonical business logic layer; it should be a thin adapter around the same
service methods used by HTTP.

The first implementation should keep both thin. The public contract is the
method schema and response envelope, not transport-specific code.

## First Slice Data

Hero constants should start with fields already available through bundled game
file snapshots and `GameFilesSource`. The target use case is basic factual
questions such as "what are this hero's attributes?" or "what abilities does
this hero have?".

Team facts should start with the current profile artifact:

- team identity and observed names;
- canonical roster and manual positions;
- stand-ins and stand-in match IDs;
- team hero pool with games, wins, positions, players, and match evidence;
- per-player hero pool;
- observed patch windows and tournaments;
- missing match detail counts.

The service should not expose raw OpenDota match payloads or `roster_hash`.
Match IDs are enough as evidence references in this slice.

## API Stability

The service contract should be versioned independently from internal artifact
schema versions. A first response envelope can be simple:

```json
{
  "service_schema_version": 1,
  "patch": "7.41b",
  "kind": "hero_constants",
  "data": {},
  "source": {
    "artifact": "game_constants",
    "schema_version": 1
  }
}
```

Adapters may add transport-specific framing, but the `data` object and source
metadata should remain equivalent between HTTP and MCP.

## Implementation Slices

1. Create the design spec and route it through `docs/CURRENT_DIRECTION.md`.
2. Add the shared service core over a resource bundle, game-file-backed hero
   constants, team profile index, and team profile loader.
3. Add a minimal local HTTP server command that exposes the first API surface.
4. Add an MCP-style adapter that exposes the same methods as tools.
5. Add tests for service methods, missing-artifact errors, and HTTP/MCP payload
   equivalence.

## Verification

The implementation PR should include tests for:

- hero constants coming from bundled game-file-backed data;
- team roster and hero-pool queries matching `profile.json`;
- team and player name resolution returning candidates instead of guessing when
  ambiguous;
- missing team profile errors including the build command;
- no network fetches from service read methods;
- no public API field or required parameter for `roster_hash`;
- HTTP and MCP adapters calling the same service core;
- schema-version metadata on public responses.

Expected validation commands:

```bash
uv run pytest
uv run pyright
uv run ruff check
```

## Implementation Defaults

The remaining choices can be closed during implementation with these defaults:

- Keep the HTTP server dependency minimal and local-first. If the chosen HTTP
  framework adds meaningful runtime weight, gate it behind the service command
  rather than forcing unrelated authoring flows to use it.
- Keep MCP as a thin adapter over the service core. Use a dedicated SDK only if
  it reduces adapter code without changing the service method contract.
- Define the resource bundle layout in the first implementation PR. It must
  contain game-file-backed hero constants, team profile index/files, and bundle
  metadata, and it must be the only normal read source for a service instance.
- For multi-patch bundles, allow an explicit bundle default patch. If no default
  exists and a call is patch-ambiguous, return an ambiguity error listing
  available patches.
- Keep fuzzy team/player matching out of authoritative resolution. If added in
  the first implementation, expose it only as non-authoritative candidates from
  `resolve_team` and `resolve_player`.
