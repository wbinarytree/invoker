# Invoker — Architecture (Implementation Artifact)

Last updated: 2026-04-26
Current implementation state: Stage 2 is landed, Stage 3 authoring is
implemented, and Stage 4 vocabulary review now reaches a guarded promotion
loop (parse → review → promote) backed by a proposal inbox.

This document describes the code that actually exists in the repository today. It is not an aspirational design doc. When this document conflicts with an older plan or spec, this document reflects the current implementation.

**Update discipline:** any PR that adds or modifies a CLI command, schema, validation layer, pipeline step, or module updates this file in the same PR and bumps `Last updated:`. Bug fixes that don't change shape are exempt. See `GUIDELINES.md` → "Architecture Doc Is Source of Truth".

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
- `invoker vocab-audit`
- `invoker review-vocabulary [--bucket <bucket>] [--term <term>]`
- `invoker review-vocab-gaps [--bucket <bucket>] [--candidate-term <term>]`
- `invoker compose-vocabulary-prompt [--bucket <bucket>] [--term <term>] [--reviewed-only]`
- `invoker parse-vocabulary-response RESPONSE_PATH`
- `invoker review-vocabulary-proposals [--bucket <bucket>] [--term <term>] [--proposal-id <id>] [--include-reviewed]`
- `invoker amend-vocabulary-proposal PROPOSAL_ID [--action <action>] [--term <term>] [--review-status <status>] [--human-note <note>]`
- `invoker promote-vocabulary [--bucket <bucket>] [--term <term>] [--proposal-id <id>] [--max-terms <n>] [--dry-run]`
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

### `vocab-audit`

Audits the current live vocabulary, authored hero files, and rule references.

Behavior:

1. loads live terms from `src/invoker/kg/vocabulary.yaml` through
   `src/invoker/kg/vocabulary.py`
2. scans canonical `data/authored/*.yaml` files, excluding drafts and
   `vocab-*.yaml` review inboxes
3. reports blocking errors for authored terms outside live vocabulary and rules
   that reference non-live terms or patterns
4. reports non-blocking warnings for unused live terms, terms without consuming
   rules, relation patterns without rules, and open vocabulary gaps

This is the first Stage 4 guardrail. The vocabulary proposal and promotion
loop now exists (see `parse-vocabulary-response`, `review-vocabulary-proposals`,
`amend-vocabulary-proposal`, and `promote-vocabulary` below).

### `review-vocabulary`

Interactive human vocabulary review.

Behavior:

1. walks current terms from `src/invoker/kg/vocabulary.yaml`
2. prints each term's status, definition, authored-hero usage, and consuming
   rules
3. prompts for a desired action (`keep`, `revise`, `rename`, `merge`, `split`,
   `remove`, `defer`, or `skip`)
4. records the human natural-language note in `data/authored/vocab-review.yaml`
5. appends the same review event to `data/authored/vocab-review-log.jsonl`

The command supports `--bucket` and `--term` filters so review can happen in
small sessions. Review notes are intentionally kept out of the canonical
vocabulary file until a later promotion step applies accepted changes.

### `review-vocab-gaps`

Interactive human review for missing concepts captured during hero authoring.

Behavior:

1. walks unresolved entries from `data/authored/vocab-gaps.yaml`
2. prints each gap's hero, bucket, concept, candidate term, reason, and evidence
3. prompts for a desired action (`promote`, `merge`, `rename`, `reject`,
   `defer`, or `skip`)
4. records the human natural-language note in
   `data/authored/vocab-gap-review.yaml`
5. appends the same review event to `data/authored/vocab-gap-review-log.jsonl`

Gap review is intentionally separate from live vocabulary review: a gap is a
proposal queue item, not an accepted term.

### `parse-vocabulary-response`

Parses a manual LLM response file produced by `compose-vocabulary-prompt`
into the proposal inbox at `data/authored/vocab-proposals.yaml`.

Implemented in [src/invoker/kg/vocabulary_proposals.py](/Users/yaoda/Projects/invoker/src/invoker/kg/vocabulary_proposals.py).

Behavior:

1. reads the JSON-only response file emitted by the manual workflow
2. validates each proposal's shape and bucket/action
3. appends or updates entries in `data/authored/vocab-proposals.yaml`,
   keyed by deterministic `proposal_id`
4. reports counts of parsed, added, and updated proposals

Bad LLM output surfaces as a non-zero exit; nothing is silently dropped.

### `review-vocabulary-proposals`

Interactive human review for parsed vocabulary proposals.

Behavior:

1. iterates pending proposals from `data/authored/vocab-proposals.yaml`
2. prints each proposal's id, bucket, term, action, definition, rationale
3. prompts for a decision (review status from `REVIEW_STATUSES`) plus a
   human note
4. records the decision back onto the proposal in place

`--include-reviewed`, `--bucket`, `--term`, `--proposal-id` filter the
queue for small focused sessions.

### `amend-vocabulary-proposal`

Edits a single proposal in place. Used when the LLM-suggested action,
term name, review status, or human note needs correction without
discarding the proposal.

### `promote-vocabulary`

Promotes accepted proposals from the inbox into the live vocabulary
file `src/invoker/kg/vocabulary.yaml`.

Behavior:

1. selects accepted proposals matching `--bucket`, `--term`, or
   `--proposal-id` filters
2. validates that promotions form a coherent set (no conflicting
   add/rename/remove on the same term)
3. warns if a single round adds or renames more than `--max-terms`
   (default 10) terms
4. writes the new vocabulary file, appends decision notes to
   `docs/specs/kg-vocabulary-notes.md`, and clears promoted entries
   from the inbox
5. `--dry-run` prints the planned change set without writing

This is the only command that mutates `src/invoker/kg/vocabulary.yaml`.
Hand-edits to that file are discouraged because they bypass the
proposal trace.

### `compose-vocabulary-prompt`

Writes a manual LLM handoff prompt for vocabulary revision.

Inputs:

- selected current terms from `src/invoker/kg/vocabulary.yaml`
- compact `invoker vocab-audit` summary
- reviewed and unreviewed entries from `data/authored/vocab-gaps.yaml`
- relevant entries from `data/authored/vocab-gap-review.yaml`
- relevant entries from `data/authored/vocab-review.yaml`
- authored term usage and current rule consumption for selected terms

Output:

- prompt under `data/raw/manual_prompts/revise-vocabulary/...`
- matching response placeholder under
  `data/raw/manual_responses/revise-vocabulary/...`

The prompt asks for JSON output, matching the existing manual hero authoring
loop. The command does not apply LLM output. It only prepares a grounded prompt
for an external chat UI.

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
