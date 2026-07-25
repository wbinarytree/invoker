# Product Rethink v2: The Generated, Grounded Encyclopedia

**Date:** 2026-07-25 (revised same day after discussion)
**Status:** draft — direction discussion with user; v1 (question-driven reasoner)
revised after user set the goal: comprehensive patch-scoped understanding,
"Liquipedia but better," synergy understanding with reasonable quality.
**Constraint reset (user decision):** all prior hard lines are dropped except
code hygiene. LLM use anywhere in the pipeline is allowed. Rethink from scratch.

---

## The goal (user's words, paraphrased)

A knowledge base that **understands Dota — everything, for a given patch**.
Liquipedia but better. It should understand hero synergies with reasonable
quality. A named failure cause of the old system: **forcing knowledge to be
too concise** (terse typed tags as the only truth destroyed the richness that
made knowledge usable).

**Ambition calibration (user, 2026-07-25):** stop chasing an "AlphaGo moment"
for Dota drafting — that is not reachable with current LLMs and chasing it
distorted the design. The target is the **"AI Liquipedia moment"**: a
generated encyclopedia that gets every common concept *right*. Draft
reasoning is an optional later layer, not the goal the architecture serves.

**Quality bar for the base tier (user):** the KB must answer basic questions
correctly and concisely — "what is Mage Slayer", "what is uphill miss",
"what does this item do" — including game bugs and special-case behaviors
that are only observable in game, not present in game files. Synergy work
does not start until this bar is met.

## Diagnosis carried over from v1 (still true)

1. Human authoring throughput is fatal: 11/126 heroes in ~3 months.
2. A closed typed vocabulary throttles everything behind human promotion.
3. Ungrounded bulk LLM generation failed because wrong output looks identical
   to right output — review cost ate the savings.
4. The substrate quietly succeeded: patch-scoped game-file snapshots, OpenDota
   cache, team profiles, service adapters. Deterministic and provenance-first.

**New failure cause (user):** over-compression. Knowledge was stored as
minimal tags; the reasoning that justified a tag was discarded, so the KB
could never explain anything and every consumer had to re-derive context.

## Core stance changes from the old system

1. **Rich first, structure second.** The canonical artifact is a full written
   analysis (an article). Structured claims are *extracted from* articles as
   an index — never the only truth. This directly fixes over-compression.
2. **Generated, not authored.** Humans review samples and adjudicate flags;
   they do not write hero knowledge. The pipeline must be able to rebuild the
   entire encyclopedia from sources without human authoring in the loop.
3. **Grounded, not remembered.** Every article is generated from an assembled
   context packet (game-file facts + stats + lower-layer articles) and must
   cite substrate keys. Citation resolution is mechanically checked. This is
   what makes bulk generation reviewable — the thing the old agentic attempt
   lacked.
4. **Layered understanding, not all-at-once.** The old agentic build asked the
   model to understand all of Dota simultaneously. Instead, generate in
   dependency order, each layer grounded in the previous:
   `concepts → heroes → pairs → meta/teams`.
5. **Coverage through tiering, not uniform depth.** Everything is covered;
   not everything gets the same depth. Depth follows evidence and demand.
6. **Marks, not verdicts (user decision 2026-07-25).** The KB is not a
   knowledge authority and does not rank sources by trustworthiness. Every
   claim carries *source marks* (game file key, wiki doc@revision, stats
   aggregate, in-game test note) and nothing more. Even game files can be
   wrong — ability data and tooltips often misdescribe actual behavior — so
   no source class is privileged as ground truth. When sources disagree, the
   disagreement is recorded and surfaced, not adjudicated. If the community
   is wrong, we're wrong together, visibly.

## Substrate: a third source class is required

Game files cannot capture the user's base-tier bar. "Uphill miss" is
hardcoded behavior; item quirks, bugs, and special-case treatments are only
observable in game. So the substrate gains an observational corpus:

- **L1a — game-file snapshot** (exists): heroes, abilities, items, neutral
  items, localization. 7.41d extracted from the local Dota 2 client via
  Source 2 Viewer, ingested with the existing `snapshot-game-files` playbook.
- **L1b — mechanics corpus (new):** curated observational documents covering
  behavior not in game files: Valve patch notes, community wiki mechanics
  pages, and manual in-game test notes (demo-mode verification). Every corpus
  document carries source URL/label, retrieval date, and patch applicability,
  and is citable by ID exactly like a game-file key. Licensing note: wiki
  content is CC-BY-SA — fine as cited evidence for locally generated
  articles, needs attribution review before any public redistribution.

  **Ingestion (user decision 2026-07-25): use the MediaWiki API rather than
  authoring from scratch.** A generic MediaWiki adapter (works for any
  MediaWiki host — Liquipedia, the dota2 fandom wiki) fetches wikitext for a
  curated per-host page list. Corpus provenance pins the **wiki revision ID**,
  not just a retrieval date, so corpus staleness is detectable by comparing
  revision IDs — the same mechanical-invalidation idea as game-file keys.
  Raw responses cached under the shared cache dir following the existing
  OpenDota cache pattern; respect per-host rate limits and send an
  identifying User-Agent. Wiki text is *cited evidence*, never copied as
  output: generated articles remain original prose citing corpus doc IDs.
- **L2 — stats evidence** (exists/extend): OpenDota aggregates.

No source class is authoritative (stance #6). Game-file values misdescribe
actual behavior often enough that L1a is a source mark like any other, not
ground truth. Citations exist for two mechanical purposes only: **traceability**
(where did this come from) and **drift detection** (the cited key/revision
changed → the claim is flagged stale). They are not truth verdicts. When two
cited sources conflict, the claim records both marks and a `disagreement`
flag; readers and downstream consumers see the conflict instead of a silent
winner.

## Content model (per patch)

| Layer | Artifact | Count (approx) | Depth |
|---|---|---|---|
| C — Concepts/Mechanisms | mechanic/role/strategy pages: armor & resistances, spell immunity, illusions, disable taxonomy, vision/smoke/uphill miss, tempo & timings, farm priority, lane roles, archetypes, **plus quirk/bug pages grounded in L1b** | 50–100 | rich article; the shared language everything else links to |
| I — Items | per-item page (including neutrals): what it does with source values, mechanics interactions (grounded in C pages + L1b), common carriers from stats | ~200 | rich article + structured facets |
| H — Heroes | per-hero page: kit breakdown with source values, power curve, what the hero *provides / needs / fears*, role data from stats | 126 | rich article + structured facets |
| P — Pairs | synergy (same team) and matchup (opponents) analyses, both directions | ~7.9k unordered pairs × 2 kinds | tiered (below) |
| M — Meta | patch overview, archetype viability, role tier notes | ~10 | article |
| T — Teams | existing team profiles, later enriched with reasoned tendencies | as needed | keep current shape |

Generation dependency order becomes: `concepts → items → heroes → pairs → meta`
(items before heroes so hero pages can cite item-interaction facts).

**Pair tiering:**
- **Tier A** (~1–2k pairs selected by stat signal + mechanical triggers +
  pick frequency): full analysis article.
- **Tier B**: structured claim record with a short rationale paragraph.
- **Tier C** (long tail): stats-only auto-record; promoted to B/A on demand
  (a query or a stat anomaly triggers deepening).

Every artifact carries: patch, generator model + prompt version, context
packet hash, citations into the substrate, and extracted structured claims.

## Pipeline (batch, rebuildable)

```
S0  substrate refresh          game-file snapshot + stats aggregates   (exists)
S1  concept pages              LLM over game-file facts; human skim (only ~100 docs)
S2  hero pages                 context = full kit values + stats + concept index
S3  pair records               context = both hero pages + pair/matchup stats + shared concepts
S4  claim extraction           structured claims (subject, predicate, objects,
                               citations, scope) pulled from every article into an index
S5  site + service publish     browsable per-patch site; claims/articles served via
                               existing KnowledgeService (HTTP + MCP)
```

Checks at every stage — all are *faithfulness and bookkeeping* checks, not
truth verdicts (stance #6):
- **Mechanical:** citations resolve to real substrate keys/doc revisions;
  quoted numbers match what the cited source actually says; schema checks.
  This checks that generation was faithful to its sources, nothing more.
- **Disagreement surfacing:** source-vs-source conflicts (game file vs wiki,
  claim vs stats — e.g. a "strong synergy" claim on a pair with strongly
  negative winrate delta) get a `disagreement` mark carried on the claim.
  Recorded and shown, never silently resolved.
- **Cross-model / self-consistency spot checks** on flagged or sampled items.
- **Human look** only where a disagreement mark makes it worth a manual
  in-game test; the test result becomes one more source mark, not a final
  ruling.

## Patch update story (the "better than Liquipedia" ops win)

New patch → snapshot diff → every article/claim citing a changed key is
mechanically flagged stale → regenerate only flagged + new content.
Regeneration cost is proportional to patch size, not to the encyclopedia.
Liquipedia lags because volunteers must notice staleness; here staleness is
computed.

## Why "better than Liquipedia" is credible

1. **Patch-versioned truth** with mechanical staleness detection; browse any
   patch's state of knowledge.
2. **Relational understanding**: synergy/matchup pages with reasoning +
   evidence — Liquipedia barely covers this at all.
3. **Machine-consumable**: every claim structured and cited → agents/MCP can
   use it without a scraping-and-hoping step.
4. **Guaranteed coverage** by pipeline, not volunteer attention.

## What we keep / drop (unchanged from v1 except reframing)

Keep: snapshot pipeline, `GameFilesSource`, OpenDota cache, team profiles,
`KnowledgeService` + HTTP/MCP adapters, export bundles, benchmark idea.
Drop/archive: authored YAML loop, vocabulary promotion machinery, deterministic
relation engine, `relations.json`, graph cache, Stage 4/5 roadmap.
The 11 authored heroes become the **evaluation baseline** (below).

## Roadmap (reordered per discussion: foundation before synergy)

**Milestone 0 — 7.41d substrate.** Extract game files from the local client
with Source 2 Viewer; run `snapshot-game-files --patch 7.41d`. Define the
L1b corpus document format and seed it (patch notes + the mechanics topics
the base tier needs: uphill miss, disjointing, status resistance, etc.).

**Milestone 1 — Foundation tier (the "AI Liquipedia moment").**
Concept/mechanism pages, item pages, hero pages for 7.41d, with claim
extraction and mechanical/stat validation wired.
**Gate: a basic-QA benchmark** — a battery of questions like "what is Mage
Slayer", "what is uphill miss", "what does hero X's ability Y do" scored for
correctness *and concision* against the KB. Includes deliberately
quirk-flavored questions that can only be answered from L1b. Synergy work
does not start until this gate passes.

**Milestone 2 — Synergy tier.** Pair analyses (synergy + matchup, both
directions) built on top of foundation pages, tiered A/B/C. Evaluation
includes comparison against the 11 hand-authored 7.41b hero YAMLs (the old
system's output becomes gold data for the new one) plus stat-consistency
checks.

**Milestone 3 (optional, later) — draft reasoning.** Only if foundation +
synergy prove quality. Explicitly not the goal the architecture serves.

## Open questions

1. Delivery surface priority: browsable site vs service/MCP first? (Milestone
   1 can defer both — markdown output is enough to evaluate.)
2. Model policy: pin one generator model per patch build; record in
   provenance. Which model, and do we gate upgrades on the QA benchmark?
3. Stat aggregates needed for pair grounding (pair winrate deltas, lane
   outcomes) — OpenDota-derivable; confirm scope of L2 extension.
4. Cost ceiling for a full-roster build (tiering keeps this bounded;
   estimate before scaling).
5. L1b sourcing discipline: which wiki/mechanics sources are trusted enough
   to cite, and what triggers a manual in-game verification pass?
