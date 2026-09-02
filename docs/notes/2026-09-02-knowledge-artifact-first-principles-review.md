# Knowledge Artifact v1 — first-principles review and decisions

**Date:** 2026-09-02 (review written and walked through with the user the
same day)
**Reviews:** `docs/specs/2026-09-01-dota-knowledge-artifact-v1.md` and `CONTEXT.md`
**Status:** walkthrough complete. The spec text reviewed was the 2026-09-01
proposal; the spec was revised in the same PR, so "the spec says" below
refers to the pre-revision text. The **Decision log** below is the
authoritative record; the **Original review** sections after it are the
starting point and the reasoning, kept as written. The v1 spec was revised
in the same PR as this note.

## Outcome of the walkthrough

**Goal (accepted):** a patch-pinned, generated Dota 2 knowledge base that
explains how heroes, items and mechanics interact, packaged so any agent can
use it, with a graph as its visible face. Three inclusion tests: patch test
(can it be wrong without a patch changing → out), grounding test (checkable
against game files, corpus, or concept rules), explain-or-decide (the KB
explains, the consumer decides).

**Agreed design, in one pass:**

- **Concept pages** (exist) gain an Interactions block: named roles and
  role × role → ally synergy / enemy counter rules, generated once per
  concept from its own article, reviewed once.
- **Hero and item pages** carry kit facts, milestones, Valve role tags, and
  **hooks**: prose statements that pick a concept and a role, with refs to
  the source ability and conditions inside the text.
- **Pairs are derived joins**, never enumerated: same concept, roles match
  a rule → candidate; the pair job ranks, drops, writes one connecting
  sentence; unmatched extras are flagged (escape hatch) and counted.
- **Observation prose is clean**: refs required, quoted numbers checked
  against referenced data, no inline marks, no grade field.
- **Out:** builds, starting items, skill order, lane/position, tier lists,
  win rates, stats of any kind, draft/replay/live/team analysis, an
  answerer.
- **Artifact:** the Markdown vault is canonical (flat layout emitted by the
  compiler, frontmatter with id / kind / patch / aliases / refs); SQLite
  (FTS5, mentions, edges) is a derived, shipped, deletable index; release =
  vault + `index.json` + `graph.json` + `kb.sqlite` + `SKILL.md` +
  `LICENSE`; stable Valve ids in every page so consumers join live stats.
- **Resolution:** an alias layer owned by the KB — Valve-shipped localized
  names and aliases, a curated community ledger (滚滚, 蓝猫 …; generator
  proposals accepted by the user), and a deterministic fuzzy tier. No
  embeddings in v1; vectors are gated on a measured retrieval miss.
- **Benchmark:** sampling frame = TI15 grand-final picks fetched from
  OpenDota match details (roster = picks, pairs = co-occurrence, patch
  checked); 20–30 user-rubric cases by type plus current-patch-delta and
  alias cases; three reported numbers (rubric pass rate, retrieval miss,
  escape-hatch count); judge hygiene; decision rule pre-registered.
- **Graph:** nodes = all pages, typed edges (link / hook / pair); Obsidian
  shipped with `.obsidian` color groups, plus one static force-graph page
  over `graph.json` with a TI15 highlight; backfill linker over existing
  articles with first-occurrence rule and stoplist.

**Sequence (unchanged in spirit):** cases and roster → concept Interactions
blocks → hooks for roster heroes and items → derived pairs for the
co-occurrence set → smoke paired evaluation on the existing answerer rails →
compiler (vault, indexes, graph) → graph page → full evaluation and gate.

**Spec sections to rewrite:** Outcome, Product boundary, Non-goals (entry 4);
Knowledge model — Hero Dossier, Pair Dossier, Interaction Observation
(entries 1–3); Knowledge Artifact contract (entries 5–7); Graph Explorer
(entry 9); Evaluation (entry 8); Implementation slices (all).

## Decision log (walkthrough with the user, 2026-09-02)

One entry per topic as it is settled. Entries record the user's position and
the resulting change to the recommendation above; nothing here amends the v1
spec until the spec itself is revised.

### 1. Grading and citation on Interaction Observations

**User position:** from the agent builder's point of view the payload is the
insight text (their examples: a Pangolier and Keeper of the Light pairing
explained by a cooldown interaction; a Pangolier and Slardar pairing
explained by shared armor reduction and physical damage). The source does not
matter to that consumer. Liquipedia carries no citations either; it is a game
wiki, not a paper, and is trusted anyway.

**Resolution:** recommendation 4 in the verdict is withdrawn as stated. The
consumer-facing decision in the spec stands: observation prose is clean, with
no inline marks. What remains is production-side and already in the spec:

- Refs (hero, ability, item, mechanic IDs) are required on every observation,
  as the spec says. They are the staleness hook (a patch that changes a
  referenced entity flags the observation for re-check) and the graph edges.
  The user's own examples are kit fact plus kit fact plus reasoning, so the
  refs are the source.
- Numbers quoted in an observation must appear in the referenced entity's
  data. Same mechanical rule the generators use today; invisible to consumers.
- The `grade` enum (mechanical / tendency / synthesis) is dropped as a field.
  If a trust signal is ever needed it can be derived from refs later.
- Per-sentence marks on concept and item pages are unchanged; that display
  decision was made with phylactery for the mini-wiki.

**Deferred to its own entry:** stats in the pair packet and the disagreement
check. Scope note for then: the cached OpenDota data is hero-versus-hero;
same-team synergy stats would need the STRATZ path or are unavailable.

### 2. Density: pairs cannot be enumerated one article at a time

**User position:** Dota is complex; a hero connected to another hero has
"tons of interactions". One generated article per pair is unlikely to
enumerate them.

**Status:** accepted in principle (user, 2026-09-02). The user noted this was
invoker's original design, done clunkily; the difference now is that all
concepts exist as generated pages and the claude-cli / codex backends
automate generation. **Not a reuse exercise (user):** the old fact schema,
vocabulary and rule engine are reference material at most; the model below
is derived from what the join needs, not from the old code.

**Analysis:** the unit is wrong, not the density. Both of the user's examples
(entry 1) have the same shape: a property of hero A, a property of hero B, and
a mechanic connecting them. That is hero-side knowledge joined through a
mechanic, not knowledge about the pair. Open-ended pair generation asks the
model to think of everything about two heroes at once, at O(n²) jobs and
O(n²) review.

**Design:**

- **Concept pages declare roles and rules.** Each concept page gains an
  "Interactions" block: named roles with a one-line definition (e.g. for
  cooldown: a source that grants reduction to allies; a sink whose kit is
  cooldown-bound) and rules of the form role × role → ally synergy or enemy
  counter, with direction and a one-line mechanism. Generated once per
  concept from its own article (~100 jobs), reviewed once. The mechanic
  knowledge that decides what an interaction means lives here, not on
  heroes. Cross-concept cases (armor reduction with physical damage) are two
  roles on one concept page.
- **Hero hooks** pick a concept and a role: prose with reasoning, refs to the
  source ability, conditions (level, item, phase) inside the text. Roughly
  8–20 per hero, generated per hero from kit facts with the role catalog in
  the packet. Vocabulary is closed per concept, open overall, and every role
  is defined next to its mechanism on a readable page.
- **Join** is deterministic: same concept, roles match a rule, candidate
  emitted with the rule's mechanism attached.
- **Pair page** is derived: ranked candidates, immaterial ones dropped, one
  connecting sentence each. No matches, no page. Length follows the game.
- **Escape hatch:** the pair job may add observations not backed by a match,
  flagged. Recurring extras of one kind mean a missing hook or a missing
  concept rule; the fix is one edit on one page.

**Why:** coverage at O(n²) with review at O(n) (heroes) plus O(concepts);
cost bounded by matches, not pairs, and tierable; the graph gets
hero → concept → hero structure for free, which is both the Obsidian look and
the actual explanation; the ceiling is honest — what does not reduce to a
role match is a stat tendency or tacit knowledge with no source.

**Checking it:** the user's own examples and rubric are the gold for hook
generation, not prior authored data. Escape-hatch counts in the smoke
evaluation measure hook and rule completeness.

**Spec impact:** concept pages gain an Interactions block (roles, rules) with
a structured sidecar; hero page gains a hooks section and sidecar; pair job
becomes rank-and-write over a candidate list; Interaction Observation is
redefined as a matched hook pair plus connecting text, with escape-hatch
observations flagged.

### 3. Hero page boundary: what a hero page holds

**User position:** users of a hero page want starting items, lane position,
ability leveling, item build. Unclear whether that belongs in the KB; a
boundary is needed.

**Status:** accepted via entry 4 (the boundary rule and the in/out list were
folded into the accepted goal statement).

**Boundary rule:** *can it become wrong without a patch changing?*
If yes, it is meta and stays out of a patch-pinned KB. If it can only change
when the game changes, it is in.

**Applied:**

- **In: kit facts and milestones.** Abilities, per-level values, talents, what
  changes at level thresholds. Mechanically checked against game files (the
  accepted generators spec).
- **In: Valve role tags.** Hero records in the game files carry a `Role`
  field, already parsed by the snapshot reader (`roles`). Patch-stable and
  citable; enough for "what kind of hero" without inventing a position.
- **In: mechanical needs and adaptations, via hooks (entry 2).** "Kit is
  cooldown-bound", "deals mostly physical damage", "exposed to silence".
  Items get hooks too: an item granting cooldown reduction is a source on the
  cooldown concept exactly like a hero. "Items that address this hero's
  needs" is the same join as pairs (hero sink × item source), grounded, and
  is the mechanical basis of a build without being one.
- **Out: prescriptions.** Starting items, skill order, item build, lane
  assignment. Meta tendencies that drift within a patch, not derivable from
  anything the KB holds, and already published live by stats APIs (every
  existing Dota agent tool is a stats wrapper). Duplicating them makes the KB
  wrong fast and weakens the patch-pinned promise.

**Principle:** the KB explains, stats prescribe. A consumer pulls the current
build from OpenDota/STRATZ and the "why" from the KB. If stats enter the KB
(own entry), they enter as dated tendencies with sample sizes, never as
recommendations. Consistent with the spec's product boundary (consumer owns
the final answer) and with "opinionated" meaning positions on interactions
(checkable), not on purchases (not).

**Spec impact:** Hero Dossier contents narrowed to kit facts, milestones, role
tags, hooks; item pages gain hooks; "relevant item adaptations" in the spec
becomes the hero-sink × item-source join; build/lane/skill-order content is
an explicit non-goal.

### 4. Goal and non-goals (scope statement)

**User ask:** establish a clear goal and non-goals to narrow scope, given
entries 1–3.

**Status:** accepted (user, 2026-09-02: "this is good").

**Goal:** a patch-pinned, generated Dota 2 knowledge base that
explains how heroes, items and mechanics interact, packaged so any agent can
use it, with a graph as its visible face.

**Promises:**

- Mechanics explained: one page per concept, from the corpus (exists).
- Entities explained: one page per hero and item — kit facts, per-level
  milestones, role tags — checked against game files.
- Interactions explained: concept pages declare roles and rules; heroes and
  items carry hooks; pair pages and item adaptations are derived joins, never
  enumerated.
- True for one patch: content can only become wrong when the game changes;
  refs say what to re-check when it does.
- Pluggable: a Markdown vault with index and dense links plus derived
  indexes; file-tool agents, tool-calling agents and programs consume one
  build.
- Visible: the graph is a projection of links; a hero → concept → hero path
  is the synergy, drawn.

**Inclusion tests:**

1. Patch test — can it become wrong without a patch changing? Out.
2. Grounding test — checkable against game files, corpus, or concept rules?
   If not, escape-hatch observation at most, flagged.
3. Explain or decide — the KB explains, the consumer decides; anything that
   decides for the player is out.

**Non-goals:**

- Prescriptions: item builds, starting items, skill order, lane/position
  assignment (entry 3).
- Meta-variable content: tier lists, win rates as advice, "current meta"
  narratives.
- An answerer, coach or agent; the consumer owns the final answer.
- Draft, replay, live-match, or team-specific analysis.
- Exhaustive pair enumeration; pairs come from hooks (entry 2).
- Citations in interaction prose; provenance is production-side (entry 1).
- Multi-patch history, translated content, a simulator, a universal score, a
  graph database, query-time generation, a Liquipedia mirror (from the spec).
- Graph polish beyond the projection: no editing, collaboration, or second
  product.

**Success:** a paired evaluation shows a downstream agent answers interaction
questions better with the KB than without, and the graph renders from links
alone.

**Open, each its own entry:** stats as dated tendencies; vault vs SQLite as
canonical artifact; embeddings; benchmark size; graph rendering.

**Spec impact:** replaces the Outcome, Product boundary and Non-goals
sections of the v1 spec.

### 5. Stats as dated tendencies

**Question:** do aggregate match statistics (OpenDota, STRATZ) enter the KB,
and in what form? Context: the rethink wanted stats as evidence and a
disagreement detector; the v1 spec made them optional; entry 3 said "dated
tendencies with sample sizes" if at all. OpenDota hero-vs-hero matchups are
cached in the repo; a STRATZ adapter exists.

**Tests (entry 4):** fails the patch test (a win rate changes without a
patch); passes grounding; a raw number does not explain. Two of three say no.

**Status:** accepted, strict form (user, 2026-09-02: "exclude stats"). Stats
are out of v1 entirely: not content, and not build-time evidence either. The
pair job ranks on mechanical materiality alone. Stable external ids stay so
consumers can join live stats themselves. The build-time uses below are
recorded as the weaker option that was *not* taken, for the record.

**Recommendation as originally proposed:** stats are never KB content.
Build-time evidence only, recorded in the pair sidecar:

- **Ranking prior** for the pair job's materiality decision and for tiering
  at full roster: pick frequency and matchup deltas shape which matched
  hooks get prose, never what the prose says.
- **Review flag** when a derived pair page's direction strongly disagrees
  with the observed matchup delta. A signal for a human look, not a verdict
  (two heroes can interact well and both be weak this month).
- **Provenance only:** stats snapshot id, date, sample sizes in the sidecar
  next to model and prompt version. The consumer surface never carries a
  number that can go stale without a patch.

**Consumer story:** the vault carries stable ids — Valve's hero id from the
game files is the id OpenDota and STRATZ key on; item ids likewise — so an
agent builder joins KB explanations to live stats in one line.

**Scope notes:** cached OpenDota data is opponent-only; same-team synergy
pairs use pick frequency as the prior unless the STRATZ path is cheap; do not
block on it. The smoke evaluation does not need stats.

**Spec impact:** "optional statistics" is removed from the Pair Dossier
section; stats join the non-goals for v1; the Knowledge Artifact contract
lists stable external ids (Valve hero id, item ids) as a required field.

### 6. Canonical artifact: vault vs SQLite

**Question:** the spec names one versioned SQLite file as the consumer
release (entities, dossiers, observations, mentions, FTS, embeddings), with
repo Markdown/JSON as build outputs. The review said the opposite.

**Status:** accepted (user, 2026-09-02: "md vault is better, plays well
with LLMs").

**Decision:** the Markdown vault is canonical; SQLite is a derived index
shipped alongside it.

- It is the consumer contract already accepted with phylactery
  (2026-07-27, "the boundary is the bundle"): a folder tree of Markdown plus
  JSON. SQLite as the release would reverse that decision.
- It serves all three consumption modes (file-tool agents and Obsidian read
  the folder; programs read the derived SQLite; tool-calling agents use the
  service ladder over either). SQLite-only serves one.
- Generated prose is reviewed in pull requests; Markdown diffs, SQLite does
  not. The repo already commits the KB for this reason.
- Obsidian and Quartz build the graph from wikilinks in a folder; nothing
  builds it from a database.
- Field convergence: Basic Memory, kbx, qmd, Karpathy's wiki treat Markdown
  as source and the database as disposable; Agent Skills are folders.
- Cost: the vault exists; SQLite as derived index is one compile command;
  SQLite as canonical means migrating everything and keeping two
  representations honest.

**SQLite's role:** the query index — FTS5 over pages and observations, a
mentions table for filtering, an edges table that also feeds `graph.json`.
Shipped in the release; rebuildable by one command; deletable.

**Layout implication (compile-time, not repo):** Obsidian resolves links by
file name and every repo article is `article.md` inside a slug directory, so
`[[heroes/storm_spirit]]` would not resolve there. The compiler emits the
vault flat — one file per entity, sidecar beside it or under a metadata
directory. The repo layout stays; export already copies and can rename.

**Release unit:** one folder per patch — vault, `index.json`, `graph.json`,
`kb.sqlite`, `SKILL.md`, `LICENSE` — as a zip and as the git tree.

**Spec impact:** Knowledge Artifact contract rewritten around the vault;
SQLite demoted to derived index; layout rule added to the compiler slice.

### 7. Embeddings

**Question:** the spec requires an embedding layer in the release (model,
vector extension, chunking, reranking deferred). Intended uses: selecting
mechanics for generation packets; retrieving pages/observations from
natural-language queries.

**Status:** accepted (user, 2026-09-02) including the alias layer below.

**Decision:** not in the v1 release; gate on a measured retrieval miss.

- Shipping vectors pins every consumer to one embedding model. Agent
  builders have their own stacks and can embed the vault themselves;
  observations are already the chunks. Vectors in the release are a
  liability for "everyone can plug in".
- Slice scale (~400 pages, ~100 pair pages, ~1000 observations) is where
  index-then-read works (Karpathy's wiki: no embeddings at hundreds of
  pages). The answerer already selects over the catalog; SQLite FTS5
  (stdlib) adds lexical search with aliases; LLM agents reformulate queries.
- Hooks (entry 2) give retrieval structure: entity resolution then a walk
  (hero → hooks → joins → pair pages) beats similarity search for
  entity-centric questions, which is nearly all of them. Vague mechanic
  questions land on concept pages via identity lines plus FTS.
- The generation-packet use is gone: with entry 2 the packet is the bounded
  role catalog, no selection problem.
- The gate is cheap: a `retrieval-miss` outcome in the evaluation (rubric
  names required pages/observations; report says whether retrieval surfaced
  them). On misses, add vectors as an optional derived table with a small
  local open model pinned in metadata.

**User concern (2026-09-02):** embeddings were meant for aliases with typos
and community slang — Pangolier is 滚滚, Storm Spirit is 蓝猫 — and it is
unclear who should own that, given how many concepts Dota has.

**Analysis:** two different problems. A nickname (滚滚 → Pangolier) is a fact
only a list can hold; no embedding recovers it. A typo is a string-distance
problem; embedding models are unreliable on short misspelled strings. Neither
wants vectors. Both want an alias table plus deterministic fuzzy matching.

**Alias layer (proposed, v1 requirement; owned by the KB):** index data, not
content, so the patch test does not apply (the exposure spec already made
resolution any-locale while content stays English).

- **Valve-shipped tier:** localized display names in every bundled locale
  plus Valve's alias keys in the localization files; the service resolves
  these today. Whether 蓝猫 is shipped is checkable from the snapshot, not
  assumed.
- **Community ledger:** nicknames Valve does not ship (滚滚; 蓝猫 if not
  shipped; "qop", "storm"; CN/RU/SEA community names). A curated file in the
  vault, one line per alias with a source tag. Bootstrapped by generator
  proposals marked unverified; the user's acceptance is the source mark, so
  nothing enters from model memory as fact. Phylactery's planned slang
  ledger moves here, shared by all consumers.
- **Fuzzy tier:** edit distance / trigram similarity over the whole alias
  table, candidates on ambiguity as `kb_resolve` does today. No model.

**Where aliases live:** each page's frontmatter `aliases` list, merged at
compile time from localization files and the ledger. Obsidian reads that
field natively (`[[滚滚]]` resolves in the vault); catalog and SQLite carry
the same list.

**Consumer LLM handles phrasing:** it usually maps slang to the canonical
name itself; when not, description search over identity lines via FTS ("the
hero that rolls") covers it. That is the only place vectors would add
anything, and with an LLM in the loop the gain is small. Position on
embeddings unchanged: not in v1, gated on retrieval miss.

**When they return:** at full roster the catalog stops fitting in context and
hybrid (lexical + vector, fused) becomes the norm (kbx, qmd). Scale decision
after the gate.

**Spec impact:** "the release must include an embedding layer" → "the release
includes FTS5, the catalog, and the alias layer (Valve-shipped + community
ledger + fuzzy tier); vectors are an optional derived table added on
evidence"; `retrieval-miss` joins the evaluation section; the alias ledger
and its proposal/acceptance flow become an implementation slice.

### 8. Benchmark size and composition

**Question:** the spec says ~10 real questions, roster derived from them,
paired baseline/treatment with a judge, threshold chosen after the first
baseline run. Seed: Storm Spirit vs Queen of Pain.

**Status:** accepted (user, 2026-09-02) with the sampling frame below.

**Sampling frame (user):** the TI15 grand final's ban/pick across its games
(the user cited five) — the most contested heroes in the meta.

- **Source from data, not memory:** match ids via the OpenDota pro-match
  listing the repo already fetches; picks/bans as hero ids from the match
  detail payloads; a small script writes a roster file with provenance and
  checks match dates against `src/invoker/patches.json`. The KB is pinned to
  7.41d; if the final was on another patch, the roster still holds (hero
  identities are patch-stable) and the note must say so.
- **Picks give the roster, co-occurrence gives the pairs:** picks only for
  the slice (bans can extend the roster later); ~25–40 distinct heroes after
  overlaps, affordable because hook cost is per hero. Pair set = every pair
  that shared a team or faced each other in those games (~45 per game before
  overlaps, ~150–200 pair pages), each corresponding to a real TI-final
  choice.
- **The draft is a sampling frame, not a question:** draft analysis stays a
  non-goal. Cases remain "how do X and Y interact" / "how does X play into
  Y", chosen by the user from co-occurring pairs with a rubric each. The
  ~4 current-patch-delta and ~3 alias cases are kept separately.
- Graph demo for free: light up the finalists' heroes and the paths between
  them; same projection.

**Recommendation as accepted:** 20–30 cases composed to measure the three
things the design now depends on; decision rule fixed before the treatment
run.

- **Why not ten:** published LLM-judge agreement with humans is roughly half
  to three-quarters on three-level verdicts; with ten cases one or two judge
  wobbles flip the verdict. 20–30 cases × 3 repeats is distinguishable from
  noise and cheap (~180 answer calls, ~90 judge calls on codex).
- **Composition:** pair synergy ~8 (the user's KotL and Slardar examples are
  the first two; checks hooks and joins); matchup ~8 (Storm vs QoP first;
  checks enemy-counter rules); item adaptation ~4 ("what addresses this
  hero's needs", not a build; checks hero-sink × item-source and the entry 3
  boundary); current-patch delta ~4 (where frontier memory is stale, e.g.
  the existing facet-removal case; where the KB wins on checkable facts);
  alias/multilingual ~3 ("我玩滚滚" must resolve to Pangolier; checks entry 7).
- **Rubric per case, user-authored:** must mention, must not claim, expected
  entities. The existing case schema (expected_facts, forbidden_assertions,
  word cap) already fits. The judge checks the rubric only.
- **Three numbers per run:** rubric pass rate baseline vs treatment (the
  gate); retrieval miss (rubric-named pages/observations surfaced or not;
  separates retrieval failure from knowledge failure); escape-hatch count
  from the build (hook and rule completeness).
- **Judge hygiene:** same judge both arms, randomized answer order, explicit
  "Unknown" verdict, temperature zero. Decision rule pre-registered before
  the treatment run (serving-format spec discipline), e.g. "treatment wins a
  majority of cases with no fact regressions" — not chosen after seeing
  numbers.
- **Roster:** superseded by the TI15 sampling frame above (picks from the
  grand final; pairs by co-occurrence).

**Spec impact:** Evaluation section rewritten: TI15 grand-final sampling
frame with data provenance and patch check, case count, composition by type,
rubric fields, the three reported numbers, pre-registered rule. Implementation
slice 1 gains the roster-from-matches script.

### 9. Graph rendering

**Question:** the spec wants a minimal explorer (heroes as nodes, pair
dossiers as connections, click-through to dossier and observations, no
layout quality or polish). The review said nodes should be all pages and
edges typed.

**What the graph is after entries 2 and 7:** hooks give hero→concept and
item→concept edges with a role; joins give hero–hero and hero–item pair
edges with observations as payload; wikilinks in prose give the rest. A
synergy is a visible path; a hero's cluster is the mechanics it lives on.

**Status:** accepted (user, 2026-09-02). Obsidian licensing checked on
obsidian.md/pricing the same day: the app is free for personal and
commercial use (a $50/user/year commercial license exists but is optional);
Sync and Publish are paid add-ons, not needed here; graph view is a core
feature. The vault is a plain folder, so Logseq, Foam, or grep read the same
files; no lock-in.

**Decision:** two cheap renderers in the slice; density work matters more
than either.

- **Obsidian, shipped configured:** the vault opens in Obsidian with the
  graph for free; ship the `.obsidian` folder with graph color groups by
  folder (heroes / items / concepts / pairs) so it is colored on first open.
  Zero code; the shareable screenshot.
- **One static page over `graph.json`:** canvas force graph from a
  permissively licensed CDN library, emitted by the existing site renderer.
  Nodes sized by degree, colored by kind; click node → page; click pair edge
  → observations; filter by edge type; a TI15 mode lighting up the
  finalists' heroes and paths. ~200 lines; deploys as static files.
- **Not now:** Quartz (full public wiki with search/backlinks; second
  toolchain) later if wanted; Cosmograph excluded (CC BY-NC).

**Density is the real work:** link discipline in generation for new pages;
hooks and joins for structural edges; a deterministic backfill linker over
the 390 existing articles using exact titles plus the alias layer. Linker
caution: concept titles like gold, map, trees, health are ordinary words —
first occurrence only plus a stoplist, or the graph becomes a hairball
again.

**Spec impact:** Graph Explorer section rewritten — nodes = all pages, typed
edges (link / hook / pair), the two renderers, TI15 highlight, backfill
linker as an implementation slice; existing non-goals (no editing,
collaboration, second product) kept.

## Original review (as written before the walkthrough)

### What "plug into their agent" means now

Three consumption modes exist in the wild, and the design should serve all
three from one build.

| Mode | Who | What they do | What they need |
|---|---|---|---|
| File tools | Claude Code, Codex, Cursor, Obsidian CLI + skills | `ls`, `grep`, read pages, follow links | Markdown folder, index page, aliases, dense wikilinks |
| Tool calls | MCP-using agents | resolve → search → read snippet | stable ids, version pin, snippet-level results |
| Programs | apps such as phylactery | vendor a bundle, query offline | one folder or one file, JSON index, SQLite optional |

The spec designs for the third mode, defers the second, and does not mention
the first. The first is where "everyone" and "Obsidian graph" live, and it is
almost free: the repo already commits `data/kb/<patch>/` as Markdown.

Evidence from the research pass (see Sources): Basic Memory, qmd and kbx all
treat Markdown as canonical and the search database as disposable ("delete and
re-index"); Obsidian shipped an official CLI and agent skills in early 2026;
Karpathy's LLM-wiki pattern uses an index page and explicitly no embeddings at
hundreds of pages; Context7 wins by being version-pinned and returning
snippets rather than pages; Anthropic's Agent Skills format is now used to
package domain knowledge for agents. Every existing Dota or LoL MCP server is
a stats wrapper. Nobody ships versioned, cited "how X plays into Y" pages.
That niche is empty, which is the opportunity and also the credibility bar.

### The design from scratch

#### 1. Canonical artifact: a patch-pinned vault

```text
dota-kb-7.41d/
  index.md            human and agent entry: categorized TOC, one line per page
  index.json          catalog: id, kind, slug, title, aliases, identity line
  graph.json          nodes (pages) + typed edges (link | pair | cites)
  SKILL.md            how an agent navigates: index → page → observation
  LICENSE             CC-BY-SA for corpus-derived pages, attribution list
  concepts/<slug>/article.md   (exists)
  items/<slug>/article.md      (exists)
  heroes/<slug>/article.md
  pairs/<a>--<b>/article.md
  kb.sqlite           derived: FTS5, mentions, edges, optional vectors
```

Rules that make it a vault and not a dump:

- Every entity mention links on first occurrence: `[[heroes/storm_spirit|Storm
  Spirit]]`. A link that does not resolve in the catalog fails generation,
  exactly like an unresolvable mark today. Marks (`[gamefile:…]`) and links
  (`[[…]]`) do not collide.
- Frontmatter carries `id`, `kind`, `patch`, `aliases`, `refs`, and for
  observations `grade`. Obsidian reads it; grep reads it; the compiler reads it.
- A lint pass reports orphans, missing cross-references, and dangling links
  (Karpathy's wiki lint). Orphans are a generation bug, not a display detail.
- Backfill: a deterministic linker inserts links into the 390 existing
  articles for exact title and alias matches. No LLM, reversible, gives the
  graph thousands of edges on day one.

Everything else is derived from the vault by one command and can be deleted.

#### 2. Knowledge units

- **Entity pages** (hero, item, concept). A hero page has two layers with
  different lifetimes: the kit fact section, grounded in `gamefile:` and
  `loc:` marks per the accepted generators spec, and the analysis section
  (needs, threats, phase patterns, adaptations), which is synthesis. Facts
  regenerate per patch cheaply; analysis regenerates only when a cited key
  changed. Abilities are anchored sections, not pages, so node count stays
  equal to page count; the catalog still lists `ability/<internal_name>` ids
  pointing at anchors.
- **Pair pages** are containers of Interaction Observations, as the spec says.
- **Interaction Observation**: id, perspective (synergy, A into B, B into A),
  scope, condition in domain language, text, links, marks, and one `grade`:
  `mechanical` (derivable from cited kit values), `tendency` (cited stats
  aggregate with sample size), `synthesis` (reasoning that cites the
  mechanical and tendency inputs it rests on). One enum. This is not a closed
  ontology and it is not a confidence score.
- **Stats are always in the pair packet** (OpenDota matchups are already
  cached in this repo) and always run as a consistency check: an observation
  whose direction contradicts the matchup delta gets a `disagreement` mark,
  recorded and shown, never adjudicated. Same rule the rethink already set.

#### 3. Retrieval: index first, vectors on evidence

At slice scale the corpus is roughly 400 pages, a hundred pair pages and
perhaps a thousand observations. The catalog is a few thousand tokens. The
current answerer's select-then-compose over the catalog is the same shape as
Karpathy's index-then-read and Context7's resolve-then-query.

- Ship `index.json` and SQLite FTS5 over pages and observations, with an
  entity-mention table for filtering. FTS5 is in the standard library; no
  dependency.
- Add a `retrieval-miss` outcome to the evaluation: the rubric names the
  pages or observations a good answer needs, and the report says whether
  retrieval surfaced them. This isolates retrieval failure from generation
  failure, which the current failure taxonomy cannot do.
- Add vectors only when that report shows lexical misses. If shipped, they are
  an optional table with the model pinned in metadata, never on the gate.

#### 4. Graph: a projection of links, rendered cheaply

- Nodes are pages. Edges are typed: `link` from wikilinks, `pair` from pair
  pages carrying their observations as payload, `cites` optional. With hero,
  item and concept nodes the graph is sparse, clustered and hub-shaped, which
  is what reads as "Obsidian".
- Local: the vault opens in Obsidian and the graph is free.
- Public: one static page over `graph.json` using a canvas force graph via
  CDN, emitted by the existing site renderer. Quartz is the alternative if a
  full public site with search is wanted later. Cosmograph is CC BY-NC, so
  avoid it for anything commercial.
- No graph database, no graph reasoning. The research consensus is that graph
  structure pays for multi-hop and global questions, not lookups; this KB's
  questions are lookups over pre-synthesized pages.

#### 5. Serving and distribution

- The existing service ladder and MCP-style adapter read the vault plus
  `kb.sqlite`. A real stdio MCP server is a thin wrapper later, as the spec
  says.
- Distribution channels, all from the same build: the git repo (browsable,
  forkable), a release zip, and the `SKILL.md` so Claude Code and Codex users
  install it as a skill with no code. A Hugging Face dataset mirror is optional.

#### 6. Evaluation

- Size: 20 to 30 cases rather than 10, drawn from real failures where
  possible. Ten cases with an LLM judge cannot separate signal from judge
  noise.
- Composition: the baseline is a frontier model that already knows a lot of
  Dota. The KB's edge is current-patch correctness, pair synthesis, and
  traceability. Include cases that hinge on 7.4x changes so the treatment can
  win on checkable facts, and score mark coverage as a second axis.
- Judge hygiene: fixed decision rule before the run (the serving-format spec
  already set this discipline), randomized A/B order, an explicit "Unknown"
  verdict, three or more repeats per case. A published GraphRAG win rate fell
  from 67% to 39% after correcting judge position and length bias.
- Rubrics are user-authored per case: must mention, must not claim. The user
  is the domain expert; the judge only checks the rubric.

#### 7. Sequence

1. Benchmark cases and rubrics (20 to 30); derive roster.
2. Substrate for the roster; link-discipline prompts; alias-based backfill
   linker over existing articles.
3. Hero pages for three roster heroes, inspected.
4. Pair pilot: the seed pair plus two extreme pairs, with stats and grades.
5. **Smoke paired evaluation on the existing answerer rails.** No compiler,
   no graph. This answers the only risky question: is generated pair
   knowledge good enough to move a downstream agent?
6. Compiler: vault layout, `index.json`, `graph.json`, `kb.sqlite`, lint.
7. Graph page over `graph.json`.
8. Remaining pairs, full paired evaluation, gate.

Steps 6 and 7 are plumbing; step 5 is the bet. Order them accordingly.

### Where this differs from the spec

| Spec says | Recommend | Why |
|---|---|---|
| SQLite is the consumer release | Vault is canonical; SQLite derived | Matches every adopted pattern; serves file-tool agents; graph for free |
| Graph: heroes as nodes, pairs as edges | All pages as nodes, typed edges | K15 is a hairball; Obsidian look needs sparse heterogeneous links |
| Embedding layer required in release | FTS5 + index now; vectors on measured miss | Compatibility burden; no evidence; index-then-read is the norm at this scale |
| Stats optional; no confidence label; provenance maintainer-facing | Stats always in packet; one grade enum; marks stay in the product | Grade plus citation is the credibility bar for synthesized synergy knowledge |
| Eval after compiler and graph | Smoke eval after pair pilot | Validate the bet before the plumbing |
| About ten cases | 20 to 30, with current-patch-delta cases | Judge noise; measure the KB's actual edge over weights |
| Articles as they are | Link discipline + backfill linker + lint | Zero cross-links today; the graph has no edges |

Unchanged and endorsed: product boundary, generated-not-authored, frozen
mechanics library, one patch, English only, observation as unit, conditions in
domain language, no universal score, no query-time generation, no graph
database, eval gate before full roster.

### Decisions for the user

1. Vault canonical, SQLite derived. Yes or keep SQLite as the release?
2. Grades and stats mandatory on observations, or optional as specced?
3. Vectors gated on evidence, or shipped in v1 regardless?
4. Entity-wide graph with link discipline and backfill, or hero-only?
5. Benchmark size and whether to add current-patch-delta cases.
6. Abilities as anchored sections rather than pages.

If accepted, the v1 spec needs a revision pass on the Knowledge Artifact
contract, the Graph Explorer, the Interaction Observation, and the
implementation slices. `CONTEXT.md` needs no new terms; "Knowledge Artifact"
becomes the vault plus its derived indexes.

## Sources (research pass, 2026-09-02)

- Basic Memory, Markdown-per-entity with wikilink graph and FTS default:
  https://github.com/basicmachines-co/basic-memory
- kbx, "the DB is a derived index, delete and re-index":
  https://github.com/tenfourty/kbx
- qmd, local hybrid search over Markdown: https://github.com/tobi/qmd
- Karpathy LLM wiki (index page, lint, no embeddings at this scale):
  https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f
- Obsidian CLI and agent skills (Feb 2026):
  https://zenn.dev/shimo4228/articles/obsidian-cli-claude-code-vault-management?locale=en
- Agent Skills as a knowledge packaging format:
  https://arxiv.org/html/2602.12430v3
- Context7 design (version-pinned, snippet-level):
  https://upstash.com/blog/context7-llmtxt-cursor
- Mintlify llms.txt benchmark, "a navigation map matters more than format":
  https://www.mintlify.com/blog/llms-txt-agent-benchmark
- Quartz graph view over wikilinks: https://quartz.jzhao.xyz/features/graph-view
- sigma.js: https://github.com/jacomyal/sigma.js/ ; Cosmograph licensing:
  https://cosmograph.app/library/compare/
- GraphRAG vs RAG systematic evaluation: https://arxiv.org/abs/2502.11371 ;
  GraphRAG-Bench: https://github.com/GraphRAG-Bench/GraphRAG-Benchmark
- Judge bias collapsing a GraphRAG win rate:
  https://venturebeat.com/orchestration/stop-graphing-everything-when-graphrag-actually-beats-vector-rag
- OpenDota MCP (stats wrapper): https://github.com/hkaanengin/opendota-mcp-server
- DotaCoach skill (prompt-side synthesis, no knowledge pages):
  https://gist.github.com/insulineru/0aee1fc00d44c9df4631507ce7ed2570
- Liquipedia API terms (CC-BY-SA, rate limits, no AI clause):
  https://liquipedia.net/api-terms-of-use
- Anthropic on agent evals (20 to 50 tasks, Unknown verdict):
  https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents
- TREC 2024 RAG judge agreement: https://arxiv.org/abs/2504.15205

Unverified in the research pass: Obsidian core's graph renderer internals,
whether `dota-brain` is still public, and LightRAG and PageIndex numbers,
which are self-reported.
