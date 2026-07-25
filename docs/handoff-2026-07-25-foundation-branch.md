# Handoff: grounded-encyclopedia-foundation branch

**Date:** 2026-07-25
**Branch:** `grounded-encyclopedia-foundation` (all work; local `main` equals
`origin/main`, nothing pushed)
**Direction:** `docs/specs/2026-07-25-grounded-reasoner-rethink.md` — read it
first; it carries every decision made during the rethink.

## What this branch contains (Milestone 0, complete)

- Product rethink spec: generated grounded encyclopedia ("AI Liquipedia"),
  marks-not-verdicts, decision framework, artifact shapes, agent exposure
  model, complex-question composition, feasibility bounds.
- 7.41d game-file snapshot (128 heroes / 1953 abilities / 544 items,
  english + schinese) + end-to-end extraction playbook
  (`docs/game-files-snapshot.md`) and `.claude/skills/new-patch-snapshot`.
- Mechanics corpus: 98 revision-pinned Liquipedia pages, coverage audit
  (`corpus-coverage`: 463-page universe fully accounted, 0 unreviewed).
- In-game changelog ingestion: 123 patches / 23,481 notes in
  `changelog.json`, searchable via `invoker changelog`.
- Basic-QA benchmark: schema + loader + 5 gold cases in
  `benchmarks/basic-qa/` encoding the first trial and both human-caught
  traps (vestigial facets, code-only talent).
- Expanded-text pass: `invoker expand-corpus` (template-expanded HTML per
  pinned revision; incremental; aborts on HTTP 429 or 5 consecutive
  failures).

## Expanded-text backfill: complete (2026-07-25 17:39)

**98 of 98 pages expanded, 0 failures** (log:
`data/logs/expand-corpus-20260725.log`). The closing verification
passed: the uphill-miss 25% figure is present in the *stored* expanded
corpus for `evasion` (raw wikitext only had the
`{{G|uphill miss chance}}` template — benchmark case `uphill-miss`,
trial finding 1 in the spec).

Rate-limit history, for future refreshes: the first pass got HTTP 429
~30 parse calls in at 2/min despite the documented 1-per-30s limit
(live enforcement appears to have an hourly-budget component); the
registry now encodes 1 parse/min, a browser CAPTCHA self-unblock lifted
the temp IP ban, the User-Agent carries a contact email per Liquipedia's
API terms, and the repo is public so the User-Agent URL resolves. At
that pace a full 98-page expand is ~100 minutes; `expand-corpus` is
incremental (already-expanded revisions skip) and aborts politely on
429 — just re-run later.

## Next steps (in order)

1. **Ship this branch** (task #3): on the user's "ready to ship" signal —
   sub-agent review per `docs/specs/2026-04-26-collaboration-harness.md`,
   surface findings, paste review summary into the PR body, PR to `main`.
   Nothing gates the PR (backfill complete; `data/` is local/gitignored).
2. **Milestone 1** (task #4, fresh branch): deterministic context assembler
   (kit-wide hero packets via the existing `HeroContextPacket` path — the
   code-only-talent trap is why; item packets with AbilityValues→tooltip
   joins; corpus section slicing), production LLM client (model pinned in
   provenance), first generators, benchmark runner. Priorities sharpened in
   discussion: **concept articles before pair depth** (they're the
   composition substrate), **cards (~300 tokens, marks on every sentence)
   and claims are the real deliverables** (articles are the evidence trail),
   and the claim schema needs `synthesis:` as a mark kind from day one.
   Output shape: `data/kb/<patch>/` per the spec's artifact-shapes section.

## Gotchas discovered this session (don't relearn these)

- Game files assert removed mechanics: all 127 heroes still carry `Facets`
  blocks in 7.41d though facets were removed in 7.41 (changelog:
  `DOTA_Patch_7_41_General_Global_Changes`). Presence-in-files ≠
  presence-in-game; the changelog is the detector.
- Some talent effects are display-string + engine-code only (e.g.
  `special_bonus_unique_slardar_3` "Corrosive Haze Undispellable") —
  invisible unless the hero's talent list is joined with localization.
- Liquipedia: requires gzip Accept-Encoding (406 otherwise), identifying
  User-Agent; parse endpoint enforcement is stricter than documented.
- The patch-notes manifest repeats KV keys; parse it with
  `parse_kv1_file(..., collect_duplicates=True)` only.
- Localization token search must prefer `DOTA_Tooltip_ability_*` prefixes —
  naive substring search surfaces cosmetics first.
