# Invoker — Architecture (Implementation Artifact)

Last updated: 2026-04-28 (Phase 5b — game-file constants consumers)
Current implementation state: Stage 2 is landed, Stage 3 authoring is
implemented, Stage 4 authoring-context hardening is implemented, and Stage 4
vocabulary review reaches a guarded promotion loop (parse → review → promote)
backed by a proposal inbox. Phase 5a/5b game-file constants work is
implemented: hero, ability, talent, and hero-stat constants route through
patch-scoped game-file snapshots instead of OpenDota constants.

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

### Graph cache

`data/cache/graph/<patch>/graph.pkl`

Built from derived hero views plus `relations.json`. Used for graph-oriented local exploration.

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

### OpenDota

Source adapter: [src/invoker/sources/opendota.py](../src/invoker/sources/opendota.py)

Cache layer, endpoint list, hash function, and payload shapes:
[docs/opendota-cache.md](opendota-cache.md)

OpenDota is now used for match data only:

- hero matchups
- pro matches

OpenDota constants are intentionally no longer exposed by `OpenDotaFetcher`.

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
    opendota/<patch>/*.json
    stratz/<patch>/*.json
    manual_prompts/
      draft-facts/<hero_slug>/<hash>.md
    manual_responses/
      draft-facts/<hero_slug>/<hash>.json
  derived/
    <patch>/
      heroes/<hero_id>.json
      relations.json
      summary_<hero_id>.md
      manifest.json
  cache/
    graph/<patch>/graph.pkl
```

External game snapshots are expected outside `data/` and are selected with
`INVOKER_GAME_DATA_DIR`. The current repository does not commit generated
snapshots or raw Valve data.

Notes:

- `data/authored/README.md` is intentionally reviewable
- local authored hero YAML remains local working data in the current flow
- bundle/install/release mechanics are not implemented yet

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
- there is no bundle/install flow for authored data — this is a deliberate roadmap item, planned for after the KG substrate stabilizes; it will be redesigned fresh from the manual-assisted-KG architecture, not from the archived `2026-04-16-bundle-assembly.md` spec
- local authored files are still a workspace convention, not a released data product

These are active roadmap items, not accidental omissions.

---

## Removed Architecture

The following architecture is no longer current and should not be used to reason about the repo:

- hero-centric LLM extract pipeline
- batched LLM reason generation in bootstrap
- `GeminiClient` as production runtime
- `CachingLLMClient` as runtime dependency
- hero files as the primary relation-bearing artifact
