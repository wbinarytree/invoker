# Concept Interactions Blocks — Roles and Rules (Knowledge Artifact v1, slice 2)

**Date:** 2026-09-07
**Status:** proposed; up for discussion before implementation
**Direction:** `docs/specs/2026-09-01-dota-knowledge-artifact-v1.md` ("the v1
spec" below), implementation slice 2. Resolves the first half of the v1
spec's open question 1: the roles-and-rules sidecar schema. The hook sidecar
schema is slice 4's and is not decided here.
**Builds on:** the concept generator and mechanical checks in
`docs/architecture.md` (`gen/concepts.py`, `gen/checks.py`,
`gen/artifacts.py`); the batch and report scripts from
`docs/specs/2026-07-26-batch-kb-generation.md`.

## Goal

Every concept page in the 7.41d Mechanics Library gains an **Interactions
block**: the closed set of **roles** a hero or item can take with respect to
that mechanic, and the **rules** that say what happens when two roles meet.
The block is generated once per concept from the concept's own accepted
article, checked mechanically against that article, reviewed once by the
user, and stored as a structured sidecar next to the article. Nothing
downstream (hooks in slice 4, the join in slice 5) can name a role that is not
declared here.

Three properties the v1 spec fixes and this slice must deliver:

- **The meaning of an interaction lives on the mechanic.** A rule's mechanism
  is a sentence drawn from the concept article, cited to the article's own
  marks. Heroes and items never explain why two roles interact; they only
  claim a role (slice 4).
- **Closed per concept, open overall.** Role ids are unique within a concept
  and addressed globally as `<concept>/<role>`. Adding or removing a role is
  one edit on one concept's sidecar.
- **Reviewed once, by accept or reject.** The user does not author roles or
  rules from memory. Every item, generated or human-added, must pass the same
  mechanical checks against the article; the human's contribution is the
  accept/reject mark and the note behind it.

## Decisions

### 1. The block is a sibling sidecar, not an article edit

`data/kb/<patch>/concepts/<slug>/interactions.json` sits next to
`article.md`, `artifact.json`, and `completeness.json`. The accepted article is
not touched: it stays sha-bound to its artifact, keeps its completeness
report, and needs no re-guard. The vault compiler (slice 7) renders the block
into the concept page on export; a deterministic renderer in this slice
produces that markdown so the review view and the compiler share one
function. The JSON file is the one home of every role and rule.

### 2. The packet is the article, not the corpus

Generation input is the concept's article body (the text `article_sha256`
binds), including its `[corpus:…]` marks. The article is the accepted,
guarded, lossless compression of the corpus sections, so a role or rule
grounded in the article is grounded in the corpus transitively, and its marks
are the article's marks. The packet hash recorded on the sidecar is the sha256
of the article body sent.

The alternative, regenerating from corpus sections, would let the block cite
facts the article dropped or the guard flagged. The article is the surface the
user has already accepted; the block must not outrun it.

### 3. Schema

`interactions.json`, schema version 1:

```json
{
  "schema_version": 1,
  "kind": "concept",
  "slug": "cooldown",
  "patch": "7.41d",
  "article_sha256": "<sha of article.md, copied from artifact.json>",
  "packet_sha256": "<sha of the article body sent>",
  "roles": [
    {
      "id": "reduction_source",
      "name": "Reduction source",
      "definition": "Grants flat, percentage-based, or current cooldown reduction to allies.",
      "marks": ["corpus:liquipedia_dota2/cooldown@2391634#Sources_of_Reduction"],
      "origin": "generated",
      "status": "proposed",
      "note": null
    }
  ],
  "rules": [
    {
      "id": "source_feeds_bound_kit",
      "subject": "reduction_source",
      "object": "cooldown_bound_kit",
      "effect": "ally_synergy",
      "mechanism": "Flat reductions apply before percentage-based ones and stack additively, so a kit limited by its cooldowns casts more often with a source nearby.",
      "marks": ["corpus:liquipedia_dota2/cooldown@2391634#Flat_Reduction"],
      "origin": "generated",
      "status": "proposed",
      "note": null
    }
  ],
  "provenance": { "...": "GenerationProvenance of the proposal call" }
}
```

Field rules:

- `id` matches `[a-z][a-z0-9_]*`, unique within its list. The global role
  key is `<slug>/<role id>`; hooks (slice 4) reference roles by that key.
- `name` is a short noun phrase; `definition` and `mechanism` are one
  sentence each. Neither names a specific hero or item: roles are positions,
  and the entities that take them are declared on entity pages.
- `marks` is a non-empty list of `corpus:KEY` strings copied from the
  article. This is the same shape as a card sentence's marks.
- `subject` and `object` are role ids on this same block. `subject == object`
  is allowed (two entities in the same role, e.g. stacking sources) and the
  join treats it as an unordered match.
- `effect` is `ally_synergy` (subject's role benefits object's role on the
  same team) or `enemy_counter` (subject's role counters object's role on
  the opposing team). Direction is subject → object in both cases; a
  counter that runs both ways is two rules.
- Rules are same-concept only. The v1 spec's cross-mechanic case (armor
  reduction alongside physical damage) is two roles on one concept page, so
  a rule never references another concept.
- `origin` is `generated` or `human`. `status` is `proposed`, `accepted`, or
  `rejected`. Generated items start `proposed`; human-added items are
  `accepted` by construction. `note` is free text, required when `status`
  is `rejected`.
- An empty `roles` list (and therefore empty `rules`) is a legitimate output:
  some mechanics have no hero-or-item position (the v1 spec's stoplist
  examples: map, trees). The report lists empty blocks so the reviewer
  confirms rather than assumes.

The generation provider returns only the proposal shape (`roles` and `rules`
without `origin`, `status`, `note`); the generator wraps it into the block.
Provenance is the proposal call's `GenerationProvenance`, so model, prompt
version, request hash, and tokens are recorded per block as for articles.

### 4. Mechanical checks, on generation and on every load

All of these fail loudly with the offenders listed; none repairs or retries
(hard line). A failed generation persists the proposal and error under
`data/logs/rejected/<patch>/interactions/<slug>/<ts>/`, as articles do.

1. **Schema.** Strict validation, extra fields forbidden.
2. **Closure.** Every rule's `subject` and `object` is a role id on this
   block. Role and rule ids are unique; no two rules share
   `(subject, object, effect)`.
3. **Marks resolve.** Every mark on every role and rule is one of the
   article's distinct marks (`artifact.json` → `citations`). Never checked
   against live sources or the corpus store.
4. **Numbers.** Every number in a definition or mechanism appears literally in
   the article text attributed to that item's marks. The article is split
   at its marks (the existing `article_segments`) so each mark owns the text
   preceding it; the check is the existing `check_numbers` over that text.
5. **Binding.** `article_sha256` equals the current artifact's; a regenerated
   article invalidates its block. `schema_version` matches. `kind`, `slug`,
   `patch` match the artifact.
6. **Review integrity.** `rejected` items carry a note; `human` items are
   `accepted`; a rule whose subject or object is a `rejected` role is itself
   invalid unless rejected.

Checks 2–6 run in the loader as well as the generator, so a hand-edited
sidecar (an accepted human-added rule, a status change) is re-validated every
time it is read. That is what makes human additions legal without opening a
second, unchecked authoring path: a human may add a role or rule only when the
article supports it and the checks agree.

### 5. Prompt

One structured call, prompt `concept-interactions` v1, on the existing
`GenerationBackend` protocol (codex for the fleet, as the concept and item
fleets ran). The system prompt states, in the register of the article
prompts:

- Roles are named positions a hero or item can take with respect to this
  mechanic: a party that grants, applies, removes, depends on, or is exposed
  to it. Define each in one sentence using only the article. Never name a
  hero or item; never state the patch.
- Rules only where the article states the mechanism. Subject acts on
  object; `ally_synergy` for same team, `enemy_counter` for opposing team.
  One sentence, from the article, with the marks of the text it draws on.
- Marks are copied exactly from the article; numbers only when literally in
  the cited text; ranges never expanded, values never derived.
- If the article supports no position, return empty lists. Never invent a
  role to have one.

Prompt text is a versioned inline constant next to the code that parses its
output (GUIDELINES amendment 2026-07-25). Behavior-changing edits bump the
version; the request hash catches unbumped drift.

### 6. Review flow

The user reviews once. The realistic shape of that review is "most blocks
fine, some items wrong, a few missing", so the tooling optimizes for that:

- `invoker review-interactions <slug> --patch <patch> --accept-all` moves
  every `proposed` item on the block to `accepted`.
- `invoker review-interactions <slug> --patch <patch> --reject <id> --note
  "<why>"` marks one role or rule rejected (repeatable). Rejecting a role
  requires every rule that references it to be rejected in the same command
  or already; the command refuses otherwise (check 6).
- Missing roles or rules the article supports are added by hand in the JSON
  with `origin: human`, `status: accepted`, and the article marks that
  support them; the loader's checks gate the edit. A missing role the article
  does not support is a corpus gap, not a KB edit, and is noted for the
  concept's next regeneration.
- Rejected items stay in the file with their note. The join (slice 5) uses
  `accepted` items only; a block with any `proposed` item is unreviewed and
  the join refuses to run over it. Hooks (slice 4) are generated against the
  accepted role catalog only.
- Regeneration (`generate-interactions --force`) discards the block,
  including its review marks. The command refuses to overwrite a block that
  has any non-`proposed` item unless `--force` is passed, and prints how many
  reviewed items it is discarding.

Commit is the acceptance act, as for articles: the reviewed sidecars are
committed under `data/kb/`.

### 7. Rendering and the role catalog

- `render_interactions_block(block, *, include_unreviewed=False)` returns the
  markdown block: an `## Interactions` heading, a `### Roles` list (`**Name**`
  (`id`) — definition, then its marks) and a `### Rules` list (subject →
  object: effect — mechanism, then its marks). Accepted items only by
  default; the review view passes `include_unreviewed=True` and tags
  proposed and rejected items. The compiler (slice 7) calls the default
  form when it emits the concept page.
- `role_catalog(kb_dir)` loads every block under `concepts/` and returns the
  accepted roles keyed `<slug>/<role id>` with name and definition. It is the
  packet for slice 4's hook generation and the closed vocabulary for slice 5's
  join, and it fails on a block that does not load.

### 8. CLI and scripts

- `invoker generate-interactions SLUG --patch <patch> [--backend <name>]
  [--model <id>] [--effort <level>] [--kb-dir <dir>] [--force]` — one block.
  Requires the concept's `artifact.json`; loads the article through
  `load_entity_article` so a drifted article fails before any paid call.
- `invoker review-interactions SLUG --patch <patch> (--accept-all |
  --reject <id> --note <text>) [--kb-dir <dir>]` — as in decision 6.
- `invoker render-interactions SLUG --patch <patch> [--include-unreviewed]`
  — prints the markdown block; the review surface for one concept.
- `scripts/concept_batch.py --kind interactions` — discovers concepts with an
  artifact and no block, runs one `generate-interactions --backend codex`
  subprocess per concept through the existing worker pool, manifest, and
  circuit breaker. No guard step: the block has no compression contract, and
  the checks are mechanical.
- `scripts/concept_report.py --kind interactions` — buckets from disk
  state: missing, proposed (unreviewed), partially reviewed, reviewed,
  empty, failed; prints per-block role and rule counts, and writes one
  markdown document of every block (review view) under `data/logs/batch/`
  so the user can read the fleet top to bottom.

### 9. What this slice does not do

- No hooks, no join, no pair pages (slices 4 and 5).
- No cross-concept rules and no rule weights or scores; materiality is the
  pair job's (slice 5, open question 2 of the v1 spec).
- No statistics anywhere.
- No carry-forward of review marks across article regenerations. When 7.42
  articles are generated, blocks regenerate and the review runs again; the
  cost is bounded by the concept count. Matching accepted items across
  regenerations by id is a follow-up if that cost turns out to matter.
- No hint or steering text into the prompt from the reviewer. Recurring
  rejections of one kind bump the prompt version and regenerate; the
  rejection notes are the evidence for the bump.

## Implementation

- `src/invoker/gen/interactions.py`: proposal and block models, the prompt
  constant and version, `generate_interactions`, `load_interactions`,
  `check_interactions` (checks 2–6, shared by generator and loader),
  `render_interactions_block`, `role_catalog`, review transitions.
- `src/invoker/cli.py`: the three commands, wired like `generate-concept`
  (backend factory, rejected dir, exit 1 on `GenerationError`).
- `scripts/concept_batch.py`, `scripts/concept_report.py`: the
  `interactions` kind.
- Tests (`tests/invoker/`): schema and each check with a small fixture
  article; loader refuses drift and stale schema; review transitions and the
  rejected-role rule; `--force` protection; renderer output for accepted
  and review views; catalog key uniqueness; generation end to end with the
  existing fake backend returning a proposal. No test asserts on prose.
- Docs in the same PR: `docs/architecture.md` (new module, sidecar, CLI,
  date bumped), `docs/cli.md` (three commands), `docs/CURRENT_DIRECTION.md`
  (this spec under the v1 spec entry).

## Acceptance criteria

1. `interactions.json` exists for all 98 concepts under `data/kb/7.41d/`,
   every block loads, and every check passes on load.
2. The fleet report lists the empty blocks and the user has confirmed each
   one; no block has a `proposed` item at merge time.
3. The role catalog builds with globally unique keys.
4. `uv run pytest`, `uv run pyright`, `uv run ruff check` pass; docs updated
   as listed; fresh-context review at the ship signal per the harness spec.

Reported with the PR, not as gates: roles and rules per concept
(distribution), rejected items with their notes grouped by kind, and the
count of human-added items.

## Open points for discussion

1. **Effect vocabulary.** Two values, per the v1 spec. A "neutral" or
   "conditional" effect was considered and dropped: conditions belong in the
   mechanism sentence and in hooks, and a third value would leak into the
   join as a score.
2. **Entity names in definitions.** Forbidden by the prompt, not checked
   mechanically. A check against the game-file hero and item names is cheap
   and could be added if the fleet shows the prompt rule is not enough.
3. **Batch surface.** Extending the two existing scripts keeps the fleet
   discipline in one place. If `--kind interactions` bends them too far, a
   separate `scripts/interactions_batch.py` is acceptable; the spec cares
   about the manifest, circuit breaker, and report, not the file.
