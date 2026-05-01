# Invoker — Architecture (Implementation Artifact)

Last updated: 2026-05-01 (team profile canonical roster and stand-ins)
Current implementation state: Stage 2 is landed, Stage 3 authoring is
implemented, Stage 4 authoring-context hardening is implemented, and Stage 4
vocabulary review reaches a guarded promotion loop (parse → review → promote)
backed by a proposal inbox. Phase 5a/5b game-file constants work is
implemented: hero, ability, talent, and hero-stat constants route through
patch-scoped game-file snapshots instead of OpenDota constants. Stage 4.5 adds
a local release bundle command for authored KG artifacts and derived patch
outputs. Team-profile work has started with shared OpenDota cache support and
a first hero-pool profile builder.

This document describes the code that actually exists in the repository today. It is not an aspirational design doc. When this document conflicts with an older plan or spec, this document reflects the current implementation.

**Update discipline:** see `GUIDELINES.md` → "Architecture Doc Is Source of Truth". Each PR updates the relevant doc (`cli.md`, `context-modules.md`, or this file) and bumps `Last updated:` here.

Current direction entrypoint: `docs/CURRENT_DIRECTION.md`

Completed design specs for the authoring-context and game-file constants work
now live under `docs/archive/specs/`; use this architecture document and the
module docs below for current behavior.

## Further reading

- [cli.md](cli.md) — CLI command reference and authoring loop
- [context-modules.md](context-modules.md) — static hero context modules (`HeroContextPacket`, stats, mechanism primer)
- [opendota-cache.md](opendota-cache.md) — OpenDota HTTP cache: hash function, file → endpoint map, payload shapes
- [game-files-snapshot.md](game-files-snapshot.md) — local playbook for creating Valve game-file JSON snapshots

---

## System Shape

Invoker is currently a local-file-first, mechanics-first knowledge system.

The implemented flow is:

1. human-authored hero facts live under `data/authored/*.yaml`
2. `bootstrap` loads those files into typed fact profiles
3. deterministic rules infer pairwise relations
4. derived hero views, `relations.json`, summaries, manifest, and graph cache are written per patch
5. `publish` packages validated authored facts, vocabulary, derived artifacts,
   reports, and release metadata into a local tarball

LLMs are no longer part of the bootstrap or query path.

LLMs are used only in the Stage 3 authoring helper flow:

- assemble a `HeroContextPacket` (identity, stats, normalized abilities, talents) plus the patch-scoped mechanism primer
- render that context into `draft_fact_profile.md` (currently prompt version 6) with fenced JSON blocks
- human runs the prompt in an external chat UI
- save the structured response locally
- normalize it into authored YAML

There is no production Gemini client, no cached LLM runtime path, and no extract/reason batch pipeline in the current codebase.

---

## Core Artifacts

### Canonical local source

`data/authored/<hero_slug>.yaml`

This is the working local source for hero facts in the current implementation.

Shape is validated into `HeroFactProfile` from [src/invoker/kg/schemas.py](../src/invoker/kg/schemas.py):

- `hero_id`
- `hero_slug`
- `localized_name`
- `capabilities`
- `requirements`
- `liabilities`
- `targets`
- `role_distribution`
- `provenance`

### Derived hero view

`data/derived/<patch>/heroes/<hero_id>.json`

This is a facts-only view. It does not embed relations.

Stored shape is `HeroDerived` from [src/invoker/schemas/derived.py](../src/invoker/schemas/derived.py).

### Canonical relation artifact

`data/derived/<patch>/relations.json`

This is a flat array of `HeroRelation` records.

Relations are:

- directional
- deterministic
- generated from authored facts, not from pair-stat selection

The in-memory reader is [src/invoker/kg/reader.py](../src/invoker/kg/reader.py).

### Human-readable summary

`data/derived/<patch>/summary_<hero_id>.md`

Summaries are derived from the facts-only hero view plus `relations.json`.

### Patch manifest

`data/derived/<patch>/manifest.json`

The manifest lists present heroes and content hashes for the derived hero files.

### Team profile view

`data/derived/<patch>/teams/<team_id>/<roster_hash>/profile.json`

This is an aggregate team view built from OpenDota match history and match
details. The first implemented profile slice contains a team-wide hero pool
(with per-hero player breakdown), a per-player hero pool, the canonical roster
(account IDs with personanames and game counts), stand-in evidence, patch
buckets mapped to OpenDota patch names where available, tournament metadata,
and match ID evidence. It does not embed raw match payloads.

`roster_hash` is derived from the canonical five-player roster, not from every
account observed across the match window. The canonical roster comes from
`data/authored/teams.yaml` when it contains exactly five unique accounts. If no
registry entry exists, the first build scaffolds every observed team-side
account into `teams.yaml` and stops; the user removes stand-ins until only the
original roster remains. If an existing registry entry contains anything other
than exactly five players, the build stops and asks for curation instead of
guessing.
Observed accounts outside the curated five are written to `roster.stand_ins`
and per-match classifications under `source.match_roster_classifications`.
By default, stand-in matches still contribute to team-level hero-pool counts
while per-player aggregates only include canonical players. Operators can pass
`--exclude-standins` to skip stand-in matches from hero and player aggregates
while still recording which stand-ins were excluded.

`build-team-profile` uses a two-step flow when `data/authored/teams.yaml` has
no entry for the requested `team_id`. The first call discovers every observed
team-side account and team name from match payloads, appends a stub entry with
`position: null` per player, and exits before writing `profile.json`. The user
removes stand-ins and leaves exactly five original roster players with
positions (1-5), then a second call uses the curated entry to generate the
profile. Existing registry entries are never overwritten; entries with more
than five players stop for manual curation before building.

Position (1-5) per player is sourced in this order:

1. **Authored override** in `data/authored/teams.yaml` under the team's
   `players: [{account_id, position}]` list. Wins over STRATZ when both
   disagree. Use this for known-wrong STRATZ classifications.
2. **STRATZ** `player.proSteamAccount.position` when `STRATZ_API_TOKEN` is
   configured. One GraphQL call per roster account, cached indefinitely.
   Skipped per-account when the registry already has an authored position.
3. **null** otherwise.

Each player carries `primary_position` and `position_source` ("authored",
"stratz", or `null`). Top-level `source.position_sources` is the sorted
list of distinct sources actually used in the profile, or `null` if none.

Earlier OpenDota-only heuristics (raw `lane_role`; GPM-rank with
`lane_role` core-disambiguator) are documented in the team-profile spec
under "Position Inference (Failed Attempts)" and are intentionally not
used — both produced wrong-by-default classifications on roaming supports.

`team.name` is taken from `data/authored/teams.yaml` when an entry exists
(`name_source: "registry"`); otherwise it is auto-filled from the most-frequent
team name observed in the match payloads
(`name_source: "opendota_match_payload"`). Authored entries always win over
observed names. `team.observed_names` records every variant seen so consumers
can audit drift.

`data/derived/<patch>/teams/index.json` lists available team profile files so
consumers do not need to scan directories.

`KnowledgeBase` exposes `team_profile()`, `team_hero_pool()`, and
`resolve_team()` for offline consumers. The reader does not fetch network data;
missing profiles raise `TeamProfileNotFoundError` with the build command to
run.

### Graph cache

`data/cache/graph/<patch>/graph.pkl`

Built from derived hero views plus `relations.json`. Used for graph-oriented local exploration.

### Local release bundle

`dist/invoker-kg-<patch>-<timestamp>.tar.gz`

Created by [src/invoker/pipeline/release.py](../src/invoker/pipeline/release.py)
through `invoker publish --patch <patch> --out dist/`.

The staging directory inside `dist/` contains:

- `release.json`
- `vocabulary/vocabulary.yaml`
- `vocabulary/kg-vocabulary-notes.md`
- `authored/*.yaml`
- `derived/heroes/<hero_id>.json`
- `derived/relations.json`
- `derived/summary_<hero_id>.md`
- `derived/manifest.json`
- `reports/validation.txt`
- `reports/vocab-audit.txt`

Publishing validates canonical authored YAML, requires a complete derived
manifest matching the authored hero IDs, checks manifest hero content hashes,
validates derived hero views and relation endpoints, requires per-hero summaries
to exist, requires `INVOKER_GAME_DATA_DIR/<patch>/snapshot.json`, runs
`vocab-audit`, records git hash and dirty state, and writes a full `.tar.gz`
bundle. Local publishing does not require a clean worktree; `git_dirty` is
recorded in `release.json`.

---

## Data Sources

### Game-file snapshots

Bootstrap parser and snapshot writer:
[src/invoker/snapshot/](../src/invoker/snapshot)

JSON-only source adapter:
[src/invoker/sources/game_files.py](../src/invoker/sources/game_files.py)

The implemented Phase 5a contract writes patch-scoped JSON snapshots under an
operator-provided root:

```text
<root>/<patch>/
  heroes.json
  abilities.json
  hero_abilities.json
  items.json
  neutral_items.json
  localization/english.json
  snapshot.json
```

`GameFilesSource` reads these JSON files and exposes the constants surface used
by authoring and fetch code: heroes, abilities, hero ability lists, hero stats,
items, and neutral items. It must not import from `invoker.snapshot`.

The snapshot command consumes pre-extracted KV files only. It does not extract
VPKs itself and is not part of bootstrap or query hot paths. When present, it
auto-discovers Valve localization KV files under `resource/localization/`
(`abilities_<locale>.txt`, `items_<locale>.txt`, and `dota_<locale>.txt`) so
ability names/descriptions and talent display templates are available to the
authoring context.

Current consumers:

- `hero_context.py` assembles `HeroContextPacket` from `GameFilesSource`
  through a narrow constants-source protocol used by the packet assembly helper
- `pipeline/fetch.py` reads roster, ability, and hero ability constants from
  `GameFilesSource`, while keeping OpenDota for matchups and pro matches
- `ability_context.py` consumes already-resolved talent names; it no longer
  substitutes unresolved talent template values with `?`
- `pipeline/team_profile.py` reads team match history and match details from
  OpenDota while resolving hero names from the game-file snapshot

### OpenDota

Source adapter: [src/invoker/sources/opendota.py](../src/invoker/sources/opendota.py)

Cache layer, endpoint list, hash function, and payload shapes:
[docs/opendota-cache.md](opendota-cache.md)

OpenDota is now used for match data only:

- hero matchups
- pro matches
- team match history
- match details

OpenDota constants are intentionally no longer exposed by `OpenDotaFetcher`.
OpenDota responses are cached in the shared Dota agents cache under
`$CACHE_DIR/opendota/responses/` using a JSON envelope; callers receive the
raw API payload from the envelope's `data` field.

### STRATZ

Still available as a source adapter and still used for fetching matchup evidence inputs, but no longer drives the primary relation ontology.

Source adapter: [src/invoker/sources/stratz.py](../src/invoker/sources/stratz.py)

### What is no longer used

- no Liquipedia scraping
- no Gemini production path
- no LLM extraction or reason generation in bootstrap

---

## Implemented Models

### Fact schema

[src/invoker/kg/schemas.py](../src/invoker/kg/schemas.py)

Important models:

- `HeroFactFeature`
- `FactProvenance`
- `HeroFactProfile`
- `RelationEvidenceStatistical`
- `HeroRelation`

### Derived schema

[src/invoker/schemas/derived.py](../src/invoker/schemas/derived.py)

Current `HeroDerived` is intentionally slim:

- schema metadata
- hero identity
- fact buckets
- role distribution
- provenance

It no longer stores `functional_tags`, embedded synergy/counter lists, or reason prose.

### Reader/query surface

[src/invoker/kg/reader.py](../src/invoker/kg/reader.py)

Implemented relation queries:

- `relations_for`
- `relations_from`
- `relations_to`
- `relations_between`
- `synergies_with`
- `counters_of`
- `countered_by`
- `relations_by_pattern`

---

## Relation Inference

Inference lives in [src/invoker/kg/infer.py](../src/invoker/kg/infer.py).

This is a deterministic rule engine over the current small vocabulary.

Current implemented relation families are still intentionally narrow, for example:

- `mana_burn -> mana_dependence`
- `vision_reveal -> weak_to_reveal`
- `armor_reduction -> magic_burst`
- `save -> needs_save`
- `reliable_stun -> mobility`

The engine is useful now, but still coarse. Stage 5 is where rule coverage and semantics are expected to improve materially.

---

## Validation Layers

### Authored-facts validation

[src/invoker/kg/authoring.py](../src/invoker/kg/authoring.py)

Used by `validate-facts`, `show-relations`, and the `draft-facts` write path.

Keeps local authored YAML inside the current vocabulary and shape constraints.

### Derived-artifact validation

[src/invoker/pipeline/validators.py](../src/invoker/pipeline/validators.py)

Used by `validate --patch` and bootstrap during patch build.

Validates facts-only derived hero views, not the old hero-centric relation artifact.

---

## Config and Environment

Current config model: [src/invoker/config.py](../src/invoker/config.py)

Implemented config fields:

- `STRATZ_API_TOKEN`
- `INVOKER_DATA_DIR`
- `CACHE_DIR`
- `INVOKER_GAME_DATA_DIR`
- `INVOKER_LOG_LEVEL`
- `INVOKER_DEV_HEROES`

There is no active config for Google API key, Gemini model selection, or LLM RPM/RPD
controls — those belonged to the removed production LLM path.

---

## Files and Cache Layout

```text
data/
  authored/
    *.yaml
    README.md
  raw/
    stratz/<patch>/*.json
    manual_prompts/
      draft-facts/<hero_slug>/<hash>.md
    manual_responses/
      draft-facts/<hero_slug>/<hash>.json
  derived/
    <patch>/
      heroes/<hero_id>.json
      teams/
        index.json
        <team_id>/<roster_hash>/profile.json
      relations.json
      summary_<hero_id>.md
      manifest.json
  cache/
    graph/<patch>/graph.pkl
dist/
  invoker-kg-<patch>-<timestamp>/
  invoker-kg-<patch>-<timestamp>.tar.gz

$CACHE_DIR/
  opendota/
    responses/*.json
```

External game snapshots are expected outside `data/` and are selected with
`INVOKER_GAME_DATA_DIR`. The current repository does not commit generated
snapshots or raw Valve data.

Notes:

- `data/authored/README.md` is intentionally reviewable
- local authored hero YAML remains local working data in the current flow
- local release bundle output under `dist/` is intentionally untracked
- `CACHE_DIR` defaults to `~/.cache/dota-agents/` and must be absolute when
  provided through the environment

---

## KnowledgeBase Surface

[src/invoker/kb.py](../src/invoker/kb.py)

The local KB now reads:

- manifest
- facts-only hero views
- `relations.json`
- summary markdown
- graph cache

The KB is no longer reading embedded per-hero synergy/counter lists because those no longer exist in the derived hero files.

---

## Known Gaps

The current implementation is intentionally incomplete in these ways:

- vocabulary is still small and fixed in code
- many reasonable hero facts are not yet expressible without Stage 4 vocabulary expansion
- relation rules are still broad and sometimes overfire
- there is no evidence attachment pass yet
- release publishing is local-only; public hosting, release inspection, and
  consumer handoff policy are still future work

These are active roadmap items, not accidental omissions.

---

## Removed Architecture

The following architecture is no longer current and should not be used to reason about the repo:

- hero-centric LLM extract pipeline
- batched LLM reason generation in bootstrap
- `GeminiClient` as production runtime
- `CachingLLMClient` as runtime dependency
- hero files as the primary relation-bearing artifact
