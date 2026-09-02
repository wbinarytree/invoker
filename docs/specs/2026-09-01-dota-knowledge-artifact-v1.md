# Dota Knowledge Artifact v1 — Explained Interactions, Vertical Slice

**Date:** 2026-09-01 (proposed from the user interview); revised 2026-09-02
after the first-principles walkthrough recorded in
`docs/notes/2026-09-02-knowledge-artifact-first-principles-review.md`
**Status:** direction accepted in the 2026-09-02 walkthrough (nine decisions,
all accepted; hooks/roles/rules "in principle" pending this contract); this
revised text is up for PR review
**Supersedes:** the product priority and sequencing in
`docs/specs/2026-07-25-grounded-reasoner-rethink.md`; the hero-generator
deferral and the phylactery-side slang ledger in
`docs/specs/2026-07-27-kb-exposure-service-and-bundle.md` (the bundle
contract there stays; this spec bumps its index schema). **Amends** the
"no fuzzy matching" rule for `kb_resolve` in that spec and in
`docs/architecture.md`: the alias layer adds a fuzzy tier that returns
candidates, never a silent choice. Builds on the hero generator design in
`docs/specs/2026-07-26-game-file-grounded-generators.md` ("the accepted
generators spec" below). Implemented behavior in
`docs/architecture.md` remains authoritative until slices land.

## Outcome

A patch-pinned, generated Dota 2 knowledge base that **explains how heroes,
items and mechanics interact**, packaged so any agent can use it, with a
graph as its visible face.

The first milestone is a benchmark-driven vertical slice that proves the
whole loop before any full-roster work:

1. current-patch hero, ability and item substrate for a roster sampled from
   a real professional final;
2. the frozen Mechanics Library, extended with an Interactions block per
   concept (roles and rules);
3. hero and item pages carrying kit facts and **hooks**;
4. pair pages **derived by joining hooks through concept rules**, never
   enumerated;
5. a Markdown vault as the canonical artifact, with derived indexes;
6. the graph as a projection of the vault's typed links; and
7. a paired downstream-agent evaluation with and without retrieved context.

Full-roster generation does not begin until the user accepts the vertical
slice's measured improvement.

### Three inclusion tests

Every candidate piece of content passes all three or stays out:

1. **Patch test.** Can it become wrong without a patch changing? Then it is
   meta, and out.
2. **Grounding test.** Can it be checked against something the KB holds —
   game files, the pinned corpus, or a concept rule? If not, it is a flagged
   escape-hatch observation at most.
3. **Explain or decide.** The KB explains; the consumer decides. Anything
   that decides for the player is out.

## Product boundary

The KB is not an agent, answerer, coach, Liquipedia wrapper, stats service,
graph database, or MCP server. It does the expensive reusable work an agent
builder should not repeat: normalize current-patch entities, synthesize how
they interact, and package that knowledge so an agent can retrieve it in a
bounded way.

A consumer owns its final answer, personality, workflow and product
decisions. Prescriptions — what to build, what to level, where to lane — are
the consumer's to make from live sources; the KB supplies the *why*.

The canonical terms for this spec live in `CONTEXT.md`.

## Agreed decisions

### Scope

- One current patch only. Historical browsing and cross-patch comparison are
  outside v1.
- English knowledge content only. Resolution keys may be any locale (see
  Alias layer).
- The vertical-slice roster is sampled from the TI15 grand final's picks (the
  user's choice: the most contested heroes in the meta). Match ids and
  picks/bans are fetched from OpenDota match details, never typed from
  memory; the roster file records provenance and the match dates are checked
  against `src/invoker/patches.json`. If the final was played on a patch
  other than the KB's, the roster still holds (hero identities are
  patch-stable) and the spec's evaluation report says so.
- Picks only for the slice; bans may extend the roster later. Expect roughly
  25–40 distinct heroes.
- The pair set is every pair that shared a team or faced each other in those
  games (co-occurrence), roughly 150–200 pairs, plus any pair a benchmark case
  names.
- Statistics of any kind are outside v1: not as content, not as build-time
  evidence. Pages carry Valve's stable hero and item ids so consumers can
  join live statistics themselves.
- Draft-state analysis, replay analysis, live-match analysis, team-specific
  coaching, translated content, and full-roster generation are outside the
  vertical slice.

### Sources

- Freeze the existing 98-page Mechanics Library for the vertical slice. The
  only addition is the Interactions block generated *from* each concept
  article; no revision checks, refetches, or article regeneration.
- Refresh only current-patch game data needed for roster heroes, their
  abilities, and referenced items.
- Hero-specific Liquipedia ingestion is a later evidence source, added only if
  evaluation shows game data plus the Mechanics Library is insufficient.
- Public artifacts preserve the attribution and licensing obligations in
  `data/kb/README.md`; the release carries a `LICENSE` file.

### Generation and review

- Knowledge is generated by a replaceable Generation Provider (the existing
  claude-cli and codex backends qualify). No vendor or model is part of the
  product contract.
- There is no generation on the artifact's query path.
- Human effort maintains benchmark cases and rubrics, reviews the concept
  Interactions blocks once, reviews hook samples, accepts or rejects alias
  proposals, and turns corrections into one edit on one page. Humans do not
  author hero or pair pages.
- An independent Evaluation Provider runs or judges the paired benchmark.
- Provenance (model, prompt version, request hash, packet hash) travels in
  sidecars. Interaction prose carries no inline marks (see Interaction
  Observation).

### Delivery sequence

- The vertical slice ships the vault, its derived indexes, the graph page,
  and the shipped Obsidian configuration.
- A CLI or evaluation harness queries the vault directly in this milestone.
- A real MCP server, hosted endpoint, and other adapters wait until the
  artifact passes evaluation. The existing service ladder keeps working over
  the exported bundle.
- Existing unrelated workflows remain untouched during the vertical slice.
  Cleanup of the authored-KG, relation-engine, and legacy pipeline code is a
  follow-up decision after the new direction proves itself.

## Knowledge model

### Entity layer

Stable current-patch identities for heroes, abilities, items, and the
mechanics of the frozen Mechanics Library. Entity records carry canonical ids,
Valve's numeric ids where the game files ship them, display names, aliases
(see Alias layer), and the source fields dossier generation needs. Abilities
are anchored sections of their hero page, not pages of their own; the catalog
still lists ability ids pointing at those anchors.

### Concept page: Interactions block

Each concept page gains an **Interactions block**, generated once from the
concept's own article and reviewed once by a human:

- **Roles** — named, one-line-defined positions a hero or item can take with
  respect to this mechanic (e.g. for cooldown: a source that grants
  reduction to allies; a sink whose kit is cooldown-bound).
- **Rules** — `role × role → ally synergy | enemy counter`, with direction
  and a one-line mechanism drawn from the article.

The knowledge that decides what an interaction *means* lives here, on the
mechanic, not on heroes. Cross-mechanic cases (the user's example: armor
reduction alongside physical damage) are two roles on one concept page.
Roles are closed per concept and open overall: adding a role edits one
concept page.

### Hero Dossier

One page per roster hero, two layers with different lifetimes:

- **Kit facts** — abilities, per-level values, talents, milestones, and
  Valve's role tags, grounded in `gamefile:` and `loc:` marks per the accepted
  generators spec. Regenerated cheaply per patch.
- **Hooks** — short paragraphs, each stating that this hero takes one role on
  one concept, with reasoning, refs to the source ability, and conditions
  (level, item, phase) inside the text. Roughly 8–20 per hero. Generated
  from kit facts with the full role catalog in the packet; a hook whose
  concept or role does not exist in the catalog fails generation.

Out of the hero page: item builds, starting items, skill order, lane and
position assignment, tier placement. These fail the patch test.

### Item page

The existing item pages gain hooks in the same form as heroes (an item that
grants cooldown reduction is a source on the cooldown concept). "Items that
address this hero's needs" is then the same join as pairs — hero sink against
item source — and is the mechanical basis of a build without being one.

### Pair Dossier

A Pair Dossier is **derived**, never enumerated:

1. The join runs deterministically: same concept, roles match a rule →
   candidate, with the rule's mechanism attached.
2. The pair job receives the candidates, both kit-fact sections, and both
   hook sections; it ranks candidates by mechanical materiality, drops
   immaterial ones, and writes one connecting sentence per kept candidate.
3. No matches, no page. Length follows the game.
4. **Escape hatch:** the pair job may add observations not backed by a
   match, flagged as such. Recurring extras of one kind indicate a missing
   hook or rule; the fix is one edit on one page, and the count is reported.

Coverage scales with pairs; review scales with heroes and concepts.

### Interaction Observation

The smallest independently retrievable unit of pair knowledge: a matched hook
pair plus its connecting text (or a flagged escape-hatch observation). It
contains:

- the pair and perspective (ally synergy, A into B, B into A);
- the concept and rule it came from, or the escape-hatch flag;
- the connecting text, self-contained, in domain language;
- referenced hero, ability, item, and mechanic ids (refs).

Refs are required: they are the staleness hook (a patch that changes a
referenced entity flags the observation for re-check) and the graph edge.
Any number quoted in the text must appear in the referenced entity's data
(the existing mechanical rule). There are **no inline marks, no grade, no
confidence label, no universal score** on observations. Marks on concept and
item pages are unchanged.

The user's seed hypotheses, to be established from the slice's sources and
the benchmark rubric rather than asserted here: a Keeper of the Light and
Pangolier pairing explained through a cooldown interaction; a Slardar and
Pangolier pairing explained through shared armor reduction and physical
damage; Storm Spirit into Queen of Pain across laning, level six, and later
item adaptation.

## Build flow

```text
current-patch game data        frozen Mechanics Library
        |                                |
        |                    Interactions block per concept
        |                        (roles + rules; reviewed once)
        +---------------+----------------+
                        |
             hero + item pages (kit facts, hooks)
                        |
               deterministic join over rules
                        |
              pair job: rank, drop, write, flag
                        |
               lint + compile (vault, indexes)
                 /                    \
      evaluation harness           graph page / Obsidian
```

## Knowledge Artifact contract

The artifact is a **Markdown vault**, one release per patch, plus derived
indexes. The vault is canonical; every index is rebuildable from it by one
command and can be deleted.

```text
dota-kb-<patch>/
  index.md            entry for humans and agents: categorized TOC, one line per page
  index.json          the existing bundle index (schema bump: aliases, Valve ids, new kinds)
  sources.json        corpus host base URLs + licenses (existing; renders corpus marks as links)
  graph.json          nodes (pages) + typed edges (link | hook | pair)
  kb.sqlite           derived: FTS5 over pages and observations, mentions, edges
  SKILL.md            how an agent navigates: index → page → observation
  LICENSE             CC-BY-SA for corpus-derived pages; attribution list
  aliases.yaml        community alias ledger (source-tagged)
  .obsidian/          graph color groups by folder; nothing else
  concepts/<slug>.md  items/<slug>.md  heroes/<slug>.md  pairs/<a>--<b>.md
  _meta/<kind>/<slug>.json   sidecars: provenance, hooks, observations, refs
```

- **Flat layout, emitted by the compiler.** Obsidian resolves links by file
  name; the repo's `data/kb/<patch>/<kind>/<slug>/article.md` layout stays
  as the committed build source and the compiler renames on export.
  Repository-native outputs remain diffable Markdown and JSON.
- **Output path.** The compiler writes `dist/dota-kb-<patch>/` (untracked,
  like the existing bundle export) and the release is that folder zipped.
  Whether the compiled vault also gets its own public git tree (a mirror
  repository) is a distribution decision after the slice passes; this repo's
  `data/kb/` stays the browsable source in the meantime.
- **Bundle continuity.** `index.json` and `sources.json` are the files the
  2026-07-27 consumer bundle already ships; this spec bumps the index schema
  rather than adding a second catalog. A schema bump is a re-vendor event for
  phylactery, as the bundle 1→2 bump was; consumers may refuse a mismatched
  `schema_version` (GUIDELINES), so nothing claims the old vendored copy keeps
  working.
- **Links.** Every entity mention links on first occurrence
  (`[[heroes/storm_spirit|Storm Spirit]]`); a link that does not resolve in
  the catalog fails generation, exactly like an unresolvable mark. Marks
  (`[gamefile:…]`) and wikilinks (`[[…]]`) do not collide.
- **Frontmatter** carries `id`, `kind`, `patch`, `aliases`, `refs`, and
  Valve ids. Obsidian reads `aliases` natively.
- **Lint** reports orphans, dangling links, and missing cross-references.
- **Backfill linker.** A deterministic pass inserts links into the existing
  concept and item articles for exact titles and aliases, first occurrence
  only, with a stoplist for concept titles that are ordinary words (gold,
  map, trees, health). No LLM; reversible.
- **SQLite** is the query index only. **No embeddings in v1**; vectors are an
  optional derived table added when the evaluation's retrieval-miss report
  shows lexical misses, with the model pinned in metadata.
- **No statistics** anywhere in the release.

### Alias layer

Owned by the KB; index data, not content, so the patch test does not apply.

- **Valve-shipped tier:** localized display names in every bundled locale
  plus Valve's alias keys from the localization files (the service resolves
  these today).
- **Community ledger:** names not present in Valve's shipped aliases. Whether
  a given name is shipped is checked against the localization snapshot at
  compile time, never assumed; the user's examples (滚滚 for Pangolier, 蓝猫
  for Storm Spirit, short forms like "qop") are ledger candidates until that
  check runs. One line per alias with a source tag. Bootstrapped by
  generator proposals marked unverified; the user's acceptance is the source
  mark, so nothing enters from model memory as fact. This replaces the
  phylactery-side slang ledger.
- **Fuzzy tier:** edit-distance or trigram matching over the whole alias
  table, candidates on ambiguity as `kb_resolve` does today. No model.

## Graph

The graph is a projection of the vault's typed links, not a second product
or a graph database.

- **Nodes** are all pages. **Edges** are typed: `link` from prose wikilinks,
  `hook` from a hero or item to a concept (carrying the role), `pair` from
  derived pair pages (carrying the observations as payload). A synergy is a
  visible hero → concept → hero path.
- **Obsidian, shipped configured.** The vault opens in Obsidian with the
  graph for free; the shipped `.obsidian` folder colors heroes, items,
  concepts and pairs by folder. Obsidian is free for personal and
  commercial use (checked 2026-09-02); the vault is a plain folder, so
  other tools read the same files.
- **One static page over `graph.json`.** A canvas force graph from a
  permissively licensed CDN library, emitted by the existing site renderer.
  Nodes sized by degree and colored by kind; click a node to open its page;
  click a pair edge to read its observations; filter by edge type; a TI15
  mode that highlights the finalists' heroes and the paths between them.
- Not now: Quartz (a full public wiki; second toolchain), Cosmograph
  (non-commercial license), editing, collaboration, or polish beyond the
  above.

## Evaluation

### Sampling frame

The TI15 grand final's picks (Scope) give the roster; co-occurrence gives the
pair set. The draft is a sampling frame, not a question: draft analysis
stays a non-goal.

### Cases

20–30 cases, each with a user-authored rubric. The existing `QACase` schema
(`src/invoker/benchmark/schemas.py`) needs a bump for this: new categories
(`pair`, `matchup`, `item-adaptation`, `alias`), `expected_marks` made
optional (observations carry no marks), and two new fields —
`expected_entities` (ids the answer must resolve) and `expected_sources`
(page or observation ids the rubric relies on, which the retrieval-miss
number reads). Existing fields (expected facts, forbidden assertions, word
cap) stay:

- pair synergy, ~8 (the user's Keeper of the Light and Slardar seeds first);
- matchup, ~8 (Storm Spirit into Queen of Pain first);
- item adaptation, ~4 ("what addresses this hero's needs", never a build);
- current-patch delta, ~4 (where a frontier model's memory is stale, e.g. the
  existing facet-removal case);
- alias and multilingual, ~3 ("我玩滚滚" must resolve to Pangolier).

### Paired run

For every case, the same consumer configuration runs twice: baseline with no
KB context, treatment with context retrieved from the vault. Three repeats
per case. Capture question, resolved entities, retrieved context, answer,
judge result, provider configuration, and artifact fingerprint.

Three numbers per run:

1. **Rubric pass rate**, baseline vs treatment — the gate.
2. **Retrieval miss** — whether the pages and observations the rubric names
   were surfaced; separates retrieval failure from knowledge failure.
3. **Escape-hatch count** from the build — hook and rule completeness.

Judge hygiene: same judge for both arms, randomized answer order, an explicit
"Unknown" verdict, temperature zero.

### Gate

The decision rule is **pre-registered before the treatment run** (the
serving-format spec's discipline), e.g. "treatment wins a majority of cases
with no fact regressions". The vertical slice passes only when the paired
report meets that rule and the user accepts it. Full-roster work is blocked
until then.

## Non-goals

- Prescriptions: item builds, starting items, skill order, lane or position
  assignment.
- Meta-variable content: tier lists, win rates as advice, "current meta"
  narratives.
- Statistics of any kind, as content or as build-time evidence.
- An answerer, coach, or agent; the consumer owns the final answer.
- Draft, replay, live-match, or team-specific analysis.
- Exhaustive pair enumeration; pairs come from hooks.
- Citations, grades, or confidence labels in interaction prose.
- Embeddings in the v1 release.
- MCP, HTTP, or hosted-service implementation beyond the existing ladder.
- Historical or multi-patch knowledge; translated content.
- A Dota simulator, a universal synergy/counter score, a closed ontology, a
  graph database or graph-reasoning engine, query-time generation, a full
  Liquipedia hero corpus, or graph polish beyond the projection.
- Removing existing authored-KG, team-profile, service, or legacy pipeline
  code before the vertical slice proves the replacement direction.

## Implementation slices

Implementation begins after this revised spec is accepted in PR review.

1. **Roster and cases** — fetch the TI15 grand-final match details from
   OpenDota; write the roster and co-occurrence pair set with provenance and
   the patch check; the user writes the rubric cases.
2. **Concept Interactions blocks** — generate roles and rules for the 98
   concepts from their own articles, with a structured sidecar; the user
   reviews once.
3. **Current-patch substrate** — selected hero/ability/item game data; stable
   entity resolution including Valve ids.
4. **Hero and item hooks** — extend the hero generator (accepted generators
   spec) with the hooks section; add hooks to roster-referenced items;
   inspect samples.
5. **Join and pair job** — deterministic join over concept rules; pair job
   with rank/drop/write and the escape hatch; run the co-occurrence set;
   report the escape-hatch count.
6. **Smoke paired evaluation** — on the existing answerer rails, no compiler,
   no graph. Decides whether derived pair knowledge moves a downstream agent
   before any plumbing is built.
7. **Compiler** — flat vault, frontmatter, links, alias layer (three tiers,
   proposal/acceptance flow), `index.md`, `index.json`, `graph.json`,
   `kb.sqlite`, `SKILL.md`, `LICENSE`, lint, backfill linker.
8. **Graph** — `.obsidian` configuration; static force-graph page with the
   TI15 highlight.
9. **Full paired evaluation** — against the pre-registered rule; present the
   report for the scale/no-scale decision.

Every behavior-changing slice carries proportionate tests and must pass
`uv run pytest`, `uv run pyright`, and `uv run ruff check`. Shape changes
update `docs/architecture.md` and companion docs in the same PR, with the
architecture date bumped. `CONTEXT.md` terms are updated with this spec.

## Acceptance criteria

- The user accepts this revised spec in PR review and the rubric cases before
  code.
- Every concept page carries a reviewed Interactions block; every role a
  hook uses exists in the catalog.
- A fresh build generates kit facts and hooks for every roster hero and
  referenced item, and derives every co-occurrence pair, without manual
  per-entity authoring.
- Every generated link and ref resolves in the substrate or Mechanics
  Library; every quoted number appears in its referenced data.
- The compiled vault opens in Obsidian with the shipped color groups;
  `graph.json` and `index.json` rebuild from the vault byte-stably, and
  `kb.sqlite` rebuilds to the same logical content hash (SQLite files are
  not byte-stable across rebuilds).
- The alias layer resolves Valve-shipped names in every bundled locale, the
  accepted community ledger, and near-miss typos, returning candidates on
  ambiguity.
- The paired evaluation report records reproducible baseline and treatment
  runs, the three numbers, and the pre-registered rule, and demonstrates
  user-accepted downstream-agent improvement.
- No statistics, embeddings, builds, translations, historical patches,
  replay, full-roster, or legacy-cleanup work enters the vertical slice.

## Open questions for sign-off

These are resolved before their implementation slice and do not change the
direction:

1. The exact roles-and-rules sidecar schema and the hook sidecar schema
   (slice 2 and 4), and the `QACase` schema bump (slice 1).
2. The rank/drop materiality rule for the pair job without statistics: what
   makes a matched candidate "immaterial" (slice 5).
3. The backfill linker's stoplist and the first-occurrence rule's scope
   (per section or per page) (slice 7).
4. Which force-graph library, pinned version, and how the TI15 highlight is
   encoded in `graph.json` (slice 8).
5. The pre-registered decision rule's exact wording (slice 9, fixed before
   the treatment run).
