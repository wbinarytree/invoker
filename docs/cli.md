# Invoker — CLI Reference

Part of the architecture record. See [architecture.md](architecture.md) for system shape and artifacts.

Implemented in [src/invoker/cli.py](../src/invoker/cli.py).

---

## Command Index

- `invoker version`
- `invoker draft-facts HERO [HERO ...]`
- `invoker validate-facts HERO [HERO ...]`
- `invoker promote-draft HERO [HERO ...] [--delete-draft]`
- `invoker show-relations HERO`
- `invoker show-hero-context HERO [--patch <patch>]`
- `invoker snapshot-game-files --vpk <path> --out <dir> --patch <patch> [--localization <path>] [--locale <name> ...]`
- `invoker export-identity-localization --patch <patch> --out <path> [--locale <name> ...]`
- `invoker build-team-profile --team-id <id> --patch <patch> [--limit 50] [--force] [--exclude-standins]`
- `invoker serve-knowledge --bundle <path> [--host 127.0.0.1] [--port 8765]`
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
- `invoker publish --patch <patch> [--out <dir>] [--force]`

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

Authoring guidance lives in [data/authored/README.md](../data/authored/README.md).

The manual file-loop helper is [src/invoker/llm/manual.py](../src/invoker/llm/manual.py).
`ManualClient` is a generic file handoff helper, not a production LLM backend.

---

## Commands

### `draft-facts`

Implemented in [src/invoker/kg/authoring.py](../src/invoker/kg/authoring.py).

Behavior:

1. resolves hero metadata and ability text from the game-file snapshot selected
   by `INVOKER_GAME_DATA_DIR` and `--patch`
2. renders `draft_fact_profile.md` with authoring-relevant metadata for every
   accepted vocabulary term and game-file ability context
3. writes a manual prompt file under `data/raw/manual_prompts/draft-facts/<hero_slug>/...`
4. creates the matching empty `.json` response placeholder under
   `data/raw/manual_responses/draft-facts/<hero_slug>/...`
5. on rerun, parses the saved manual response
6. writes normalized YAML to `data/authored/<hero_slug>.yaml` or `<hero_slug>.draft.yaml`
7. records any response-level `vocabulary_gaps` in `data/authored/vocab-gaps.yaml`

Transport format for the LLM response is JSON-only by prompt contract, and
manual response placeholders now use a `.json` suffix.
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

### `show-hero-context`

Assembles and prints the `HeroContextPacket` for one hero as JSON from the
configured game-file snapshot. Useful for inspecting computed stat bands,
percentiles, abilities, and resolved talents before rendering an authoring
prompt.

See [context-modules.md](context-modules.md) for the packet shape.

### `snapshot-game-files`

Bootstrap-only helper for creating a patch-scoped game-file JSON snapshot from
pre-extracted Valve KV files.

Implemented in [src/invoker/snapshot/game_files.py](../src/invoker/snapshot/game_files.py).

Behavior:

1. reads a pre-extracted VPK root or `npc/` directory containing `npc_heroes.txt`
2. parses `npc_heroes.txt`, `npc_abilities.txt`, per-hero ability files under
   `npc/heroes/`, `items.txt`, and `neutral_items.txt`
3. writes `<out>/<patch>/heroes.json`, `abilities.json`,
   `hero_abilities.json`, `items.json`, `neutral_items.json`,
   one `localization/<locale>.json` file for each requested locale, and
   `snapshot.json`

The command does not extract VPKs and is not part of the bootstrap/query hot
path. `--locale` may be passed more than once, for example `--locale english
--locale schinese`. When `--localization` is omitted, the command looks for
`resource/localization/abilities_<locale>.txt`, `items_<locale>.txt`, and
`dota_<locale>.txt` next to the extracted `npc/` directory and merges any files
that exist. If no localization files are present, `localization/<locale>.json`
is written as an empty object and `GameFilesSource` falls back to KV names.
`--localization` can only be used with one locale.

`snapshot.json` records generic source labels and relative source-file
inventory. It does not record local absolute extraction paths.

### `export-identity-localization`

Exports a compact patch-scoped identity/localization JSON artifact from the
configured game-file snapshot root selected by `INVOKER_GAME_DATA_DIR`.

Implemented in [src/invoker/identity.py](../src/invoker/identity.py).

Behavior:

1. reads `INVOKER_GAME_DATA_DIR/<patch>/heroes.json`, `items.json`,
   `neutral_items.json`, `localization/<locale>.json`, and `snapshot.json`
2. emits hero ids, internal names, slugs, locale-scoped display names, and
   locale-scoped aliases from `npc_dota_hero_*__name_alias`
3. emits item and neutral-item internal names, optional ids, display names, and
   aliases where the snapshot exposes source-backed values
4. writes sanitized provenance that identifies the Invoker snapshot and patch
   without local absolute paths
5. fails on duplicate hero ids or duplicate internal hero names, and records
   aliases that normalize to multiple live heroes in `unknowns`

The command is intended for downstream resource packaging. It does not export
hero mechanics or matchup advice.

### `build-team-profile`

Builds a derived team hero-pool profile for one OpenDota team ID.

Implemented in [src/invoker/pipeline/team_profile.py](../src/invoker/pipeline/team_profile.py).

Behavior:

1. reads team match history from OpenDota through the shared cache
2. reads selected match details through the shared cache
3. resolves hero names from `INVOKER_GAME_DATA_DIR/<patch>/`
4. selects a canonical five-player roster and derives `roster_hash` from those
   account IDs
5. aggregates team hero games, wins, per-hero manual position counts, player
   usage, match IDs, patch windows from `src/invoker/patches.json`,
   tournament metadata, and stand-in evidence
6. writes `data/derived/<patch>/teams/<team_id>/<roster_hash>/profile.json`
7. updates `data/derived/<patch>/teams/index.json`

The first slice uses a recent-match window with a default limit of 50. Missing
match-detail payloads are recorded in the profile source metadata instead of
failing the whole build.

Observed match patch names are resolved from each match `start_time` using the
tracked `src/invoker/patches.json` UTC date windows. OpenDota numeric patch IDs
are retained as raw evidence when present, but they are not the source of truth
for patch names.

By default, stand-in matches contribute to team-level hero-pool counts, but
per-player aggregates include only the canonical roster. Use
`--exclude-standins` to skip stand-in matches from hero and player aggregates
while still recording the excluded stand-ins under `roster.stand_ins`.

The command runs as a two-step flow when `data/authored/teams.yaml` has no
entry for `--team-id`:

1. **First call** discovers every observed team-side account ID/personaname and
   the most-frequent observed team name from match payloads, appends a stub
   entry to `data/authored/teams.yaml` with `position: null` for each player,
   and exits without writing `profile.json`.
2. The user removes stand-ins and leaves exactly five original roster players,
   assigning positions (1-5) by editing the registry file.
3. **Second call** sees the existing entry, leaves the registry untouched,
   and proceeds to generate `profile.json` using authored positions.

Existing registry entries are never overwritten. Entries with anything other
than exactly five players, or without one valid manual position for each slot
1-5, stop before profile generation and ask the user to curate the registry.

### `serve-knowledge`

Runs the local read-only knowledge service over HTTP.

Implemented by [src/invoker/service/core.py](../src/invoker/service/core.py)
and [src/invoker/service/http.py](../src/invoker/service/http.py).

Required resource bundle layout:

- `bundle.json`
- `authored/teams.yaml`
- `game_constants/<patch>/...` with the same JSON files produced by
  `snapshot-game-files`
- `derived/<patch>/teams/index.json`
- `derived/<patch>/teams/<team_id>/<roster_hash>/profile.json`

The command does not fetch network data. It serves the bundle as-is and exposes
routes matching the service method names:

- `/list_bundle_patches`
- `/lookup_hero`
- `/get_hero_constants`
- `/resolve_team`
- `/resolve_player`
- `/get_team_profile`
- `/get_team_roster`
- `/get_team_hero_pool`
- `/get_team_player_hero_pool`

Routes accept `GET` query parameters or a `POST` JSON object. Public responses
use the service envelope with `service_schema_version`, `patch`, `kind`, `data`,
and `source`. `roster_hash` is not exposed in service payloads.
When `authored/teams.yaml` is present, team aliases and curated player names
from the registry are available for exact resolution and roster responses.
`lookup_hero` searches hero id, internal name, slug, localized display names,
and source aliases across all locales present in the bundled game-file snapshot.
Each candidate includes matched field evidence so consumers can audit why the
query resolved.

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

Implemented in [src/invoker/kg/vocabulary_proposals.py](../src/invoker/kg/vocabulary_proposals.py).

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
  `data/raw/manual_responses/revise-vocabulary/.../*.json`

The prompt asks for JSON output, matching the existing manual hero authoring
loop. The command does not apply LLM output. It only prepares a grounded prompt
for an external chat UI.

### `bootstrap`

Builds patch-scoped derived artifacts from local authored files.

Implemented in [src/invoker/pipeline/orchestrator.py](../src/invoker/pipeline/orchestrator.py).

Behavior:

1. discover canonical authored YAML files, excluding drafts and vocabulary
   review inboxes
2. validate and load them into `HeroFactProfile`
3. write facts-only `HeroDerived` views
4. infer relations with `infer_relations`
5. write `relations.json`
6. write summaries
7. write manifest
8. build graph cache

This command contains no LLM calls.

### `status`

Prints the current patch state: authored hero count, derived artifact presence,
and manifest summary.

### `validate`

Runs derived-artifact validation for the given patch. See Validation Layers in
[architecture.md](architecture.md).

### `publish`

Creates a local full release bundle for authored and derived KG artifacts.

Implemented in [src/invoker/pipeline/release.py](../src/invoker/pipeline/release.py).

Behavior:

1. validates canonical `data/authored/*.yaml`, excluding drafts and vocabulary
   review inboxes
2. requires patch-scoped derived artifacts under `data/derived/<patch>/`
3. requires the derived manifest to be `complete` and to match the authored
   hero IDs
4. validates derived hero views, manifest hero content hashes, and
   `relations.json` endpoints
5. requires per-hero summaries to exist
6. requires `INVOKER_GAME_DATA_DIR/<patch>/snapshot.json` so release metadata
   records the source game-file snapshot
7. runs `vocab-audit`; blocking errors stop the release, warnings are captured
   as non-blocking report metadata
8. stages vocabulary, authored YAML, derived artifacts, and reports under
   `<out>/invoker-kg-<patch>-<timestamp>/`
9. writes `release.json`
10. writes `<out>/invoker-kg-<patch>-<timestamp>.tar.gz`

Default output root is `dist/`. Existing release paths are not overwritten
unless `--force` is passed.
