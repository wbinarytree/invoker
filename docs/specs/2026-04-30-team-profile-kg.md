# Team Profile KG

Date: 2026-04-30
Status: draft for discussion
Scope: team-profile ingestion, derived profile artifacts, and reader API shape

## Purpose

Invoker should add a team-profile layer before expanding hero relationship
extraction. The first useful slice is a hero-pool profile for a given
professional team ID. Later slices can add pick/ban tendencies, pick/ban
associations, lane pairings, and roster-era comparisons.

This work should remain separate from the mechanics-first hero relation layer.
Team profiles are statistical observations about a team or roster era. They may
use the hero KG for names, validation, and future enrichment, but they should
not redefine the core hero relation ontology.

## Goals

- Build a profile for a team selected by ID.
- Fetch enough historical professional match data to produce useful hero-pool
  aggregates.
- Partition profile data by patch when possible.
- Preserve tournament or time-window provenance so consumers know what matches
  produced an answer.
- Expose structured query methods that another agent can call without
  query-time LLM dependence.
- Keep the first slice small enough to review and validate.

## Non-Goals

- No live network fetch from reader/query methods.
- No natural-language query endpoint inside Invoker.
- No GraphRAG as the first API.
- No attempt to make OpenDota or STRATZ roster data authoritative.
- No full lane-pairing model in the first slice.
- No Liquipedia roster ingestion in the first slice.

## Source Boundaries

Game-file snapshots remain the source of truth for hero constants, hero names,
and patch-scoped roster validation.

OpenDota remains a match-data source. For the first team-profile slice it should
provide:

- team match discovery
- per-match draft data when available
- player-slot to hero assignment when available
- pick/ban order when available for later slices
- league or tournament identifiers when available

STRATZ is a candidate later source for more detailed lane and role data. It
should not block the first hero-pool slice because GraphQL schema work and token
availability add more moving parts.

Liquipedia is a candidate later source for roster and tournament metadata. Its
MediaWiki API exists and is publicly documented, but it has stricter access
expectations than the current OpenDota path. Any Liquipedia slice should be
cached, attributed, rate-limited, and scoped narrowly to roster/tournament
metadata instead of reviving broad page scraping.

## First Slice

Add an explicit build command for one team ID.

Proposed CLI:

```text
invoker build-team-profile --team-id <id> --patch <patch> [--limit 50] [--force]
```

The command should:

1. read or write through the shared OpenDota cache
2. fetch or read cached match history for the team
3. fetch or read cached match detail for selected matches
4. group matches by observed patch
5. infer roster snapshots from player account IDs in those matches
6. aggregate hero usage by team, patch, and roster era
7. write derived profile artifacts under `data/derived/<patch>/teams/`

The first implementation should prioritize hero pool:

- heroes picked by the team
- games and wins per hero
- player usage per hero when available
- role or slot hints only when available from the source payload
- source match IDs
- tournament or time-window metadata when discoverable

Pick/ban rates, pick/ban associations, and lane pairings should be
separate follow-up slices.

## Match Window

Professional teams have sparse data, so a strict current-patch-only window will
often be too thin. The default strategy should support a backoff ladder:

1. matches in the requested patch
2. matches from the last three tournaments when tournament grouping is known
3. recent team matches up to the default limit of 50

Derived output should keep these scopes separate instead of collapsing them into
one opaque aggregate. Consumers can then choose strict patch data or broader
recent-form data.

Patch changes during a tournament are uncommon but possible. The profile should
record observed match patch per match and group aggregates by patch rather than
assuming a tournament is patch-homogeneous.

Tournament grouping should start from source league or tournament IDs when the
match payload exposes them. If tournament grouping is unavailable, the command
should record the tournament as `unknown` and fall back to the recent-match
limit.

## Team And Roster Identity

Team identity should start from source team ID because it is stable enough for a
first command.

Invoker should also keep a small local team registry, but only as a resolution
and display aid:

```text
data/authored/teams.yaml
```

Possible shape:

```yaml
schema_version: 1
teams:
  - team_id: 123456
    name: Example Team
    aliases:
      - Example
      - Example Team
```

This registry is not the source of truth for rosters. Roster identity should be
inferred from match payloads.

Roster-era identity should use:

```text
team_id + roster_hash + match_window
```

`roster_hash` should be derived from the sorted stable player account IDs seen
for the team in the relevant matches. This avoids trusting stale OpenDota or
STRATZ roster endpoints.

Long-term, team and player resolution can move toward:

- local registry for names and aliases
- deterministic exact ID lookup
- normalized alias lookup
- edit-distance suggestions for near misses
- source-specific external IDs
- optional human-reviewed merges when org names or player accounts drift

Do not make fuzzy matching authoritative. It should help users find IDs and
aliases, not silently choose team identity.

## Derived Artifact Sketch

Proposed first artifact:

```text
data/derived/<patch>/teams/index.json
data/derived/<patch>/teams/<team_id>/<roster_hash>/profile.json
```

`profile.json` should stay an aggregate view, not a raw match dump. It is fine
for the first slice because a team profile built from roughly 50 matches is
small, self-contained, and easy for the reader API to load. Queryability should
come from stable reader methods and predictable top-level sections, not from
agents traversing arbitrary nested JSON.

`index.json` should list available profile files by team ID, roster hash, patch,
and window metadata so consumers do not need to scan directories.

Avoid embedding full OpenDota match payloads in `profile.json`. Keep raw match
responses in the shared cache and store only aggregate counts plus evidence
references such as match IDs. If later slices produce large or independent
sections, they can split into sibling files such as `pick_ban.json` or
`lane_pairings.json` without changing the first reader contract.

Sketch:

```json
{
  "schema_version": 1,
  "team": {
    "team_id": 123456,
    "name": "Example Team",
    "aliases": ["Example"]
  },
  "patch": "7.41b",
  "scope": {
    "requested_patch": "7.41b",
    "match_window": "last_three_tournaments_or_recent_limit",
    "match_count": 25
  },
  "roster": {
    "roster_hash": "stable-short-hash",
    "player_account_ids": [1, 2, 3, 4, 5],
    "confidence": "observed_from_matches"
  },
  "hero_pool": [
    {
      "hero_id": 1,
      "localized_name": "Example Hero",
      "games": 4,
      "wins": 3,
      "players": [
        {"account_id": 1, "games": 4}
      ],
      "match_ids": [123]
    }
  ],
  "source": {
    "primary": "opendota",
    "fetched_at": "2026-04-30T00:00:00Z"
  }
}
```

## Reader API

The API should be structured and action-oriented.

First slice:

```python
kb.team_profile(team_id, *, roster_hash=None)
kb.team_hero_pool(team_id, *, roster_hash=None, patch=None)
kb.resolve_team(query)
```

Later slices:

```python
kb.team_pick_ban(team_id, *, phase=None, side=None)
kb.team_pick_ban_associations(team_id, *, mode="ban_to_pick", phase=None)
kb.team_lane_pairings(team_id, *, lane=None)
kb.team_roster_eras(team_id)
```

Reader methods must not fetch network data. Missing profiles should produce a
clear error that tells the operator which build command to run.

## Shared OpenDota Cache

Oracle currently documents a proposed shared OpenDota cache protocol at:

```text
/Users/yaoda/Projects/oracle/docs/CACHE_PROTOCOL.md
```

The useful parts for Invoker are:

- default `CACHE_DIR=~/.cache/dota-agents/`
- source-specific layout under `opendota/`
- JSON envelope with `meta` and raw `data`
- atomic writes via temporary file and rename
- no TTL by default
- derived artifacts remain owned by each project

Invoker currently uses a patch-scoped raw cache under its local `data/raw`
shape. Adopting the shared protocol should happen before the team-profile build
command because the profile workflow depends on multiple match-list and
match-detail requests. Do not preemptively extract a shared package; copying the
protocol shape first is enough if Invoker becomes the second real consumer.

Cache freshness should distinguish immutable historical match details from
rolling list endpoints. Individual match detail responses can be cached
indefinitely. Team match-list responses should support explicit refresh through
`--force` and should carry `fetched_at` metadata so a stale list can be
diagnosed.

The first implementation should adapt or wrap Invoker's `CachedClient` so
OpenDota requests use the shared envelope. A team-profile-specific cache adapter
should be avoided unless the shared envelope proves incompatible.

## Follow-Up Slices

### Pick/Ban Tendencies

Use draft order from match detail payloads where available.

Outputs:

- picked heroes
- banned heroes
- phase buckets when recoverable
- side-specific tendencies
- first-phase comfort picks

### Pick/Ban Associations

The useful question is broader than counter-picking:

> Given a team's observed draft history, which bans tend to appear before its
> picks, and which picks tend to follow those bans?

This should be stored as observed draft association evidence, not proof of
strategic intent.

The first practical slice should implement a simple `ban_to_pick` counter:
whenever hero X was banned before the team's pick, count which heroes the team
later picked in that draft. This is enough to answer useful profile questions
without modeling full draft state.

Recommended output fields:

- anchor ban hero
- following picked hero
- count
- conditional rate within the observed anchor-ban sample, if easy to compute
- match IDs as evidence

Side-specific breakdowns, phase buckets, own-ban versus opponent-ban splits, and
full `state_to_next_action` modeling should be deferred until the simple counter
has proven useful.

### Position Inference (Implemented: STRATZ + authored override)

Position is sourced in priority order:

1. Authored override in `data/authored/teams.yaml` under
   `teams[].players[]` (`account_id`, `position`). Wins over STRATZ.
2. STRATZ `player.proSteamAccount.position`, one GraphQL call per roster
   account (5 per pro profile), cached indefinitely.
3. `null` when neither source has a value.

Each player record carries `primary_position` and `position_source`
("authored", "stratz", or `null`). Top-level `source.position_sources` is
the sorted list of distinct sources actually used.

STRATZ's curated position is reasonably reliable for established pro
players but has been observed to misclassify (e.g. tagging a known pos5
support as pos4). The authored override is the escape hatch for those
cases — preferable to silently shipping a wrong value or to inventing a
new heuristic.

The OpenDota-only heuristics below are kept here as a record of what was
tried and why it failed — do not reintroduce them.

### Position Inference (Failed Attempts)

Per-player position (pos 1-5) is essential for hero-pool questions like "is
this hero a flex pick or a dedicated mid?" and "what is MieRo's hero pool as
pos3?". The first implementation tried two heuristics from OpenDota match
detail data:

1. **`lane_role` directly** (1=safe → pos1, 2=mid → pos2, 3=off → pos3,
   4=jungle → pos4, with intra-role GPM rank splitting safe and off into
   pos1/5 and pos3/4). OpenDota's parser tags roaming pos5 supports with
   `lane_role=2` (mid) when they spend laning phase rotating through mid, so
   genuine pos5 players surfaced as "primary_position: 2".
2. **GPM rank with `lane_role` as core-disambiguator** (top 3 GPM = cores
   1/2/3 by `lane_role`, bottom 2 = supports pos4/pos5 by GPM). Better, but
   still depends on `lane_role` to distinguish pos1 vs pos2 vs pos3 among
   cores. When `lane_role` itself is wrong (which it is, often), the
   classification is still wrong.

Both failed loudly on real BetBoom data. Rather than ship a misleading-by-
default signal, position fields were removed entirely.

Open questions for the STRATZ-backed implementation:

- Does STRATZ's `proSteamAccount.position` field stay accurate when a player
  switches teams or roles mid-patch? If not, we may need a "position observed
  at fetched_at" timestamp rather than a single field.
- Should the registry (`data/authored/teams.yaml`) be allowed to override
  STRATZ when a stand-in or recent-role-change makes the curated value stale?
- Stand-ins on a roster (one match) currently get the same STRATZ lookup as
  permanent members. Worth distinguishing later.
- Is per-(player, hero) position useful for flex-pick questions, or does
  primary-position-per-player + hero distribution suffice?

### Lane Pairings

OpenDota may be enough for player-to-hero assignment and rough role inference.
STRATZ is a stronger candidate for detailed laning data and should be evaluated
when this slice starts.

First lane-pairing output should carry confidence and source:

- exact lane data from STRATZ when available
- inferred role/slot data from OpenDota when not
- unknown when neither source is reliable

## Open Questions

- Should `data/authored/teams.yaml` be required before building a team profile,
  or should `--team-id` work without any registry entry?
  **Resolved:** the build command now runs in two steps. A first call with no
  registry entry scaffolds one (roster + observed name, `position: null`) and
  exits; the user fills positions; a second call writes `profile.json`.
  Existing entries are never overwritten.
- Should the first profile build require match details for every selected match,
  or tolerate partial match-detail coverage with explicit missing-data counts?
- Where should tournament metadata come from if OpenDota match payloads do not
  expose enough tournament grouping?
- What exact Liquipedia API surface is suitable for roster metadata, and does
  it require a separate user-agent/contact policy in Invoker config?
