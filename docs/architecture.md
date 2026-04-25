# Invoker — Architecture (Implementation Artifact)

Last updated: 2026-04-22
Current implementation state: Stage 2 is landed and the first Stage 3 authoring loop is implemented.

This document describes the code that actually exists in the repository today. It is not an aspirational design doc. When this document conflicts with an older plan or spec, this document reflects the current implementation.

Current direction entrypoint: `docs/CURRENT_DIRECTION.md`

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

- generate a prompt for one hero
- human runs that prompt in an external chat UI
- save the structured response locally
- normalize it into authored YAML

There is no production Gemini client, no cached LLM runtime path, and no extract/reason batch pipeline in the current codebase.

---

## Core Artifacts

### Canonical local source

`data/authored/<hero_slug>.yaml`

This is the working local source for hero facts in the current implementation.

Shape is validated into `HeroFactProfile` from [src/invoker/kg/schemas.py](/Users/yaoda/Projects/invoker/src/invoker/kg/schemas.py):

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

Stored shape is `HeroDerived` from [src/invoker/schemas/derived.py](/Users/yaoda/Projects/invoker/src/invoker/schemas/derived.py).

### Canonical relation artifact

`data/derived/<patch>/relations.json`

This is a flat array of `HeroRelation` records.

Relations are:

- directional
- deterministic
- generated from authored facts, not from pair-stat selection

The in-memory reader is [src/invoker/kg/reader.py](/Users/yaoda/Projects/invoker/src/invoker/kg/reader.py).

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

## Runtime Commands

Implemented CLI commands in [src/invoker/cli.py](/Users/yaoda/Projects/invoker/src/invoker/cli.py):

- `invoker version`
- `invoker draft-facts HERO [HERO ...]`
- `invoker validate-facts HERO [HERO ...]`
- `invoker promote-draft HERO [HERO ...] [--delete-draft]`
- `invoker show-relations HERO`
- `invoker bootstrap --patch <patch> [--heroes ...]`
- `invoker status --patch <patch>`
- `invoker validate --patch <patch>`
- `invoker publish --patch <patch>`

### `draft-facts`

Implemented in [src/invoker/kg/authoring.py](/Users/yaoda/Projects/invoker/src/invoker/kg/authoring.py).

Behavior:

1. resolves hero metadata and ability text from OpenDota
2. renders `draft_fact_profile.md`
3. writes a manual prompt file under `data/raw/manual_prompts/draft-facts/<hero_slug>/...`
4. creates the matching empty response placeholder under `data/raw/manual_responses/draft-facts/<hero_slug>/...`
5. on rerun, parses the saved manual response
6. writes normalized YAML to `data/authored/<hero_slug>.yaml` or `<hero_slug>.draft.yaml`
7. records any response-level `vocabulary_gaps` in `data/authored/vocab-gaps.yaml`

Transport format for the LLM response is JSON-only by prompt contract.
Stored local format remains YAML. Canonical authored files stay strict;
vocabulary gaps are review inbox items and do not directly affect relation
inference.

### `validate-facts`

Validates one or more authored YAML files against the current local vocabulary
and authoring rules.

This is separate from derived-artifact validation.

Checks include:

- required top-level keys
- vocabulary membership
- duplicate features
- score bounds
- evidence presence rules
- role distribution bounds
- provenance presence

### `promote-draft`

Promotes reviewed regenerated drafts into canonical authored facts.

Behavior:

1. resolves each requested hero to `data/authored/<hero_slug>.yaml`
2. validates `data/authored/<hero_slug>.draft.yaml`
3. backs up the current canonical YAML under `data/authored/.backups/`
4. copies the draft into the canonical YAML path
5. optionally deletes the draft when `--delete-draft` is passed

The draft naming is intentionally `<hero_slug>.draft.yaml` so editors keep YAML
syntax highlighting.

### `show-relations`

Loads the selected authored hero plus the currently valid authored corpus and
prints inferred outbound and inbound relations for review. Human output labels
related heroes as `Localized Name (id)` so relation review does not require
manually mapping numeric IDs.

This command is meant for authoring-time sanity checking, not for final patch build output.

### `bootstrap`

Builds patch-scoped derived artifacts from local authored files.

Implemented in [src/invoker/pipeline/orchestrator.py](/Users/yaoda/Projects/invoker/src/invoker/pipeline/orchestrator.py).

Behavior:

1. discover authored YAML files
2. validate and load them into `HeroFactProfile`
3. write facts-only `HeroDerived` views
4. infer relations with `infer_relations`
5. write `relations.json`
6. write summaries
7. write manifest
8. build graph cache

This command contains no LLM calls.

---

## Authoring Loop

The current Stage 3 authoring loop is:

1. run `invoker draft-facts HERO [HERO ...]`
2. copy the generated prompt into an external LLM
3. save the LLM's JSON reply into the created response file
4. rerun `invoker draft-facts HERO [HERO ...]`
5. review any generated `<hero>.draft.yaml` and `vocab-gaps.yaml`
6. optionally run `invoker promote-draft HERO [HERO ...]`
7. run `invoker validate-facts HERO [HERO ...]`
8. run `invoker show-relations HERO`

Authoring guidance lives in:

- [data/authored/README.md](/Users/yaoda/Projects/invoker/data/authored/README.md)

The manual file-loop helper is:

- [src/invoker/llm/manual.py](/Users/yaoda/Projects/invoker/src/invoker/llm/manual.py)

`ManualClient` is now a generic file handoff helper, not a production LLM backend.

---

## Data Sources

### OpenDota

Used directly by the implemented code for:

- hero roster and roles: `/api/heroes`
- ability descriptions: `/api/constants/abilities`
- hero -> ability mapping: `/api/constants/hero_abilities`
- matchups: `/api/heroes/{id}/matchups`
- pro matches: `/api/proMatches`

Source adapter:

- [src/invoker/sources/opendota.py](/Users/yaoda/Projects/invoker/src/invoker/sources/opendota.py)

### STRATZ

Still available as a source adapter and still used for fetching matchup evidence inputs, but no longer drives the primary relation ontology.

Source adapter:

- [src/invoker/sources/stratz.py](/Users/yaoda/Projects/invoker/src/invoker/sources/stratz.py)

### What is no longer used

- no Liquipedia scraping
- no Gemini production path
- no LLM extraction or reason generation in bootstrap

---

## Implemented Models

### Fact schema

[src/invoker/kg/schemas.py](/Users/yaoda/Projects/invoker/src/invoker/kg/schemas.py)

Important models:

- `HeroFactFeature`
- `FactProvenance`
- `HeroFactProfile`
- `RelationEvidenceStatistical`
- `HeroRelation`

### Derived schema

[src/invoker/schemas/derived.py](/Users/yaoda/Projects/invoker/src/invoker/schemas/derived.py)

Current `HeroDerived` is intentionally slim:

- schema metadata
- hero identity
- fact buckets
- role distribution
- provenance

It no longer stores `functional_tags`, embedded synergy/counter lists, or reason prose.

### Reader/query surface

[src/invoker/kg/reader.py](/Users/yaoda/Projects/invoker/src/invoker/kg/reader.py)

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

Inference lives in:

- [src/invoker/kg/infer.py](/Users/yaoda/Projects/invoker/src/invoker/kg/infer.py)

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

[src/invoker/kg/authoring.py](/Users/yaoda/Projects/invoker/src/invoker/kg/authoring.py)

Used by:

- `validate-facts`
- `show-relations`
- `draft-facts` write path

This keeps local authored YAML inside the current vocabulary and shape constraints.

### Derived-artifact validation

[src/invoker/pipeline/validators.py](/Users/yaoda/Projects/invoker/src/invoker/pipeline/validators.py)

Used by:

- `validate --patch`
- bootstrap during patch build

This validates facts-only derived hero views, not the old hero-centric relation artifact.

---

## Config and Environment

Current config model is in:

- [src/invoker/config.py](/Users/yaoda/Projects/invoker/src/invoker/config.py)

Implemented config fields:

- `STRATZ_API_TOKEN`
- `INVOKER_DATA_DIR`
- `INVOKER_LOG_LEVEL`
- `INVOKER_DEV_HEROES`

There is no active config for:

- Google API key
- Gemini model selection
- LLM RPM/RPD controls

Those belonged to the removed production LLM path.

---

## Files and Cache Layout

Implemented local layout:

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
      draft-facts/<hero_slug>/<hash>.txt
  derived/
    <patch>/
      heroes/<hero_id>.json
      relations.json
      summary_<hero_id>.md
      manifest.json
  cache/
    graph/<patch>/graph.pkl
```

Notes:

- `data/authored/README.md` is intentionally reviewable
- local authored hero YAML remains local working data in the current flow
- bundle/install/release mechanics are not implemented yet

---

## KnowledgeBase Surface

[src/invoker/kb.py](/Users/yaoda/Projects/invoker/src/invoker/kb.py)

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
- there is no bundle/install flow for authored data
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

If older plans or docs still mention those as current implementation, they are stale.
