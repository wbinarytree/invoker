# Batch KB Generation — All Concepts + Items Overnight on Codex

**Date:** 2026-07-26
**Status:** draft — needs sign-off
**Direction:** `docs/specs/2026-07-25-grounded-reasoner-rethink.md`;
completes the coverage of `docs/specs/2026-07-26-game-file-grounded-generators.md`
(slice 1 at full scope) and the concept generator's corpus scope.
User direction 2026-07-26: **concepts first — tonight**; items deferred
to a follow-on run (the item scope/enumerator below stays as recorded
design). Codex backend, sharded; allowlist extended from the dry sweep;
nothing auto-commits — bucket review, user is the acceptance authority.

## Goal

Tonight: generate article + card + guard report for every remaining
in-scope 7.41d **concept** — **96** (98 corpus pages minus the 2
canonical) — in one sharded batch on `--backend codex`, leaving
artifacts, completeness reports, and a run manifest on disk for a
bucket-review acceptance pass. The **290 items** (291 in scope minus
canonical `mage_slayer`) run later with the same machinery once their
codex-v5 pilot passes.

## Dry-sweep evidence (2026-07-26, no LLM)

Every packet for the full scope builds cleanly today: 98/98 concept
packets (0 errors), 291/291 item packets (0 errors). Concept packets
total ~362k est. tokens (largest: `map`, `buildings`, `vision` at ~10k
each); item packets are small (~70k est. tokens total).

## Item scope enumerator

The generators spec's scope rule ("localized name and a cost or recipe
presence (purchasables + neutrals); cosmetic/event records excluded")
realized mechanically from file-native flags — no training-memory
judgment anywhere:

In scope = non-recipe record, and:

1. has a localized name token (`DOTA_Tooltip_ability_<name>`,
   case-insensitive) — excludes 74 (cosmetic/unnamed records);
2. not `IsObsolete` — excludes 19 vestigials (the in-files-not-in-game
   gotcha, detected by the game's own flag);
3. neutral drops (`ItemIsNeutralActiveDrop`/`ItemIsNeutralPassiveDrop`)
   are in unconditionally (spec: neutrals in);
4. otherwise `ItemPurchasable` must not be `0` — excludes 30
   (Roshan/event drops: aegis, cheese, couriers, ofrenda, …);
5. and the record must have nonzero `ItemCost`, or a recipe that builds
   it, or shop stock (`ItemStockMax`) — the stock clause admits
   `item_ward_observer` (cost 0 but shop-stocked); nothing else hinges
   on it.

Result: **291 items**. Recipe records (129) are excluded as records but
their content already renders into each result item's `#components`
section.

## Coverage allowlist extension

Boilerplate anchors observed across all 98 concept packets, added to
`COVERAGE_ALLOWLIST` (exact-match, both case variants where observed):

- `References` (already exempt; 2 pages)
- `Gallery` (10 pages) — image captions whose charts never survive
  corpus extraction; the one surviving canonical evasion flag is
  exactly this class
- `See_Also` (4 pages) / `See_also` (2 pages) — navigation links

`Trivia` (8 pages) stays **content** — same ruling as item lore: the
fun is part of the encyclopedia, never allowlisted.
`Recent_Changes` / `Version_History` / `Patch_History` are content
(canonical precedent: evasion and random_distribution cite them).

Known interaction, accepted for tonight: allowlisted sections stay in
the packet, so the compression guard may still flag them as uncovered.
The morning report auto-annotates any guard flag whose cited section
anchor is allowlisted ("known boilerplate") so the flagged bucket stays
readable. The packet-strip redesign (drop boilerplate at packet build,
pure set-equality coverage, `packet_sha256` drift) stays deferred to
its own decision.

## Rejected-article persistence

A mechanical check failure (marks, coverage, numbers) currently
discards the paid article text — and so does any later failure in the
same entity (card call dies, daemon crashes): the article lives only in
memory until the final artifact write. Before the batch: in
`generate_concept` and `generate_item`, **any** failure after the
article call persists what was paid for before the error propagates —
`data/logs/rejected/<patch>/<kind>/<slug>/<UTC timestamp>/` holding
`article.md` (and `card.json` when the card existed) plus `error.txt`
with the error text. Nothing under `data/logs/` is committed. The
abort behavior itself is unchanged: same error, same exit code, no
artifact written.

## Pilot gate (before any fleet spend)

The codex-unproven paths get a small pilot before any fleet launches; a
systematic failure discovered at fleet scale would burn millions.

Tonight (concepts — ~3 entities, ~150k input tokens): codex v5 is
proven only mid-size, so the pilot covers the extremes — `map` or
`vision` (~10k-token packet, output-truncation risk), `turn_rate`
(pathological anchor names), plus one ordinary mid-size page as
control.

Deferred with the item run: **items on codex under prompt v5 have
never run** (the codex `mage_slayer` variant was v4) — one full-kit
item (cost + components + attribs + mechanics + lore), one neutral
enhancement (no cost, no components, no lore — a packet shape never
generated anywhere), one no-lore purchasable (e.g. `aeon_disk`).

Gate: all pilot entities land clean or explainably-flagged and one
article spot-reads sane. A systematic failure stops the run and gets
fixed first; the fleet only launches on a passed pilot.

## Batch driver

Shell-level orchestration per the generators spec ("batch orchestration
is shell, not code, until volume proves otherwise"): a script under
`scripts/` that

- reads an entity list (kind + slug), skips entities whose
  `artifact.json` already exists;
- invokes `uv run invoker generate-concept|generate-item <slug>
  --patch 7.41d --backend codex` one process per entity — a fresh codex
  daemon per entity (3 calls each), so no long-lived daemon risk and
  natural resume;
- appends one JSONL line per entity to a run manifest
  (`data/logs/batch/<UTC stamp>-<shard>.jsonl`): slug, kind, exit code,
  duration, disk-state bucket;
- **circuit-breaks**: 3 consecutive failures, or >30% failure rate
  after 10 entities, halts the shard — an unattended systematic
  breakage (backend outage, prompt regression) must stop spending, not
  run to the end of the list;
- distinguishes failure classes: a **transport-level** error (rate
  limit, daemon death — no output produced) re-queues the entity once
  at the end of the shard, recorded in the manifest; **bad output**
  (mark/coverage/number failure, guard refusal) is never retried, per
  the hard line — regeneration is a morning decision;
- shards by list-slice: N independent script invocations over disjoint
  slices (each entity is fully independent; concurrency is bounded only
  by the Codex plan's rate limits, which the circuit breaker detects).

Bucketing is disk-state, not exit-code parsing:

- **clean** — `artifact.json` present, `completeness.json` `missing`
  empty;
- **flagged** — `artifact.json` present, guard flags recorded (exit 1
  by design, artifact stays for review);
- **failed** — no artifact; the rejected dir and manifest carry what
  happened.

## Cost and wall-clock (estimates, calibrated on canonical provenance)

Per entity: 3 codex calls (article, card, guard), each with the
~13-14k input-token codex harness floor. Calibrated on the codex v5
variant runs (concept article ≈ 19-20k in / 7-10k out; card ≈ 19k in /
2-4k out; guard ≈ 14-25k in / 1-3k out): tonight's concept run is
**~6M input / ~1.2M output tokens** on the Codex/ChatGPT budget. The
deferred item run adds ~12.5M / ~1.2M; the floor dominates item calls
(content ~1k vs floor ~13.5k per guard call), so batching small guards
is a noted optimization to weigh before that run.

Wall-clock at observed 15-65s/call, one entity ≈ 2-4 min. Shard count
is a driver parameter (user direction: codex parallelism is not the
bottleneck): plan **8 shards** for the concept fleet (~30-60 min),
launched after the pilot gate; sustained rate-limit errors trip the
circuit breaker rather than being pre-hedged. Estimates are estimates
— the manifest records real durations, provenance records real token
counts.

## Amendment 1 (2026-07-26, during the concept fleet)

Three fleet rounds surfaced systematic failure patterns; each fix is
recorded, none silently retried (v5/v6 rejects stay in
`data/logs/rejected/`, every attempt in the manifests):

- **Concept prompt v6:** the model sometimes titled articles
  "X (7.41d)" — the patch string from the request line is not vouchable
  by any packet section. Rule added: the patch is context, never stated
  in the article. Also: never derive, sum, convert, count, or round
  numbers.
- **Concept prompt v7:** card sentences counted table rows (the
  never-derive rule was article-only — now in the card prompt), and
  articles expanded "3 to 9"-style ranges into integer lists (ranges
  stay ranges).
- **Structural digits are not claims (check refinement):**
  `check_numbers` now strips markdown heading lines and ordered-list
  markers before extracting numbers. Headings mirror source section
  *titles* ("Example 3: …"), which are not part of any section's
  checkable text, and list numbering is the model's own — both were
  false-positive aborts (5 of 9 failures in round 3). List/table
  *content* stays fully checked; prompt-mandated topic mirroring and
  the strict number check are no longer in conflict.
- Driver `--limit N` for chunked launches: the session harness kills
  long background runs, so the fleet runs as bounded chunks; resume
  is the existing skip-existing behavior.

## Acceptance (user decision 2026-07-26)

Nothing auto-commits. Morning report groups entities into the three
buckets; guard flags citing allowlisted anchors are annotated as known
boilerplate. The user skims clean in bulk, reviews flagged
per-artifact, queues failed for regeneration. Committing remains the
acceptance act.

## Task breakdown

Tonight (concepts):

1. Coverage allowlist extension (+ test) — `Gallery`, `See_Also`,
   `See_also`.
2. Rejected-output persistence on any post-article failure in
   `generate_concept` (+ tests); `generate_item` gets the same
   treatment when the item run rides.
3. Test pin: coverage is article-only (card citing a subset passes) —
   PR #49 follow-up rides along.
4. Concept-list emitter + batch driver script (circuit breaker,
   transport re-queue, manifest) + bucket-report script.
5. Pilot gate: 3 concepts per the pilot section; fleet only on pass.
6. Run the fleet: remaining ~93 concepts, 8 shards.
7. Bucket report, user acceptance, commit accepted artifacts, retro
   note in `docs/notes/`.

Deferred (items, same machinery): item pilot (3 entities), item fleet
(12 shards), item-side rejected persistence.

## Out of scope

- Heroes (no generator — slice 2).
- Packet-strip allowlist redesign (own decision, deferred).
- claude-cli follow-ups from PR #49 (token comparability, key-rename
  smoke) — claude transport off the critical path per user direction.
- Auto-retry or auto-accept of any kind.

## Verification

- `uv run pytest`, `uv run pyright`, `uv run ruff check` green on the
  code changes before the batch starts.
- Dry sweep numbers reproduced by the entity-list emitter (96 concepts
  tonight; 290 items when that run rides).
- Batch end state: every in-scope concept is exactly one of
  clean/flagged/failed in the bucket report; manifest line count
  matches entity count.
