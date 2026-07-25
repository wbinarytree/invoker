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

## In flight: expanded-text backfill (the only pending item)

State when this doc was written: **30 of 98 pages expanded**
(`find data/corpus -name "*.expanded.html" | wc -l`). Liquipedia
rate-limited the first pass (HTTP 429 ~30 parse calls in at 2/min); the
registry now encodes 1/min. A detached (`nohup`) process waits out the
cooldown until ~16:05 on 2026-07-25, then resumes the backfill,
logging to `data/logs/expand-corpus-20260725.log`. It survives session
close and notifies no one. To check on it:

```bash
tail data/logs/expand-corpus-20260725.log
find data/corpus -name "*.expanded.html" | wc -l   # target: 98
```

If it died or got rate-limited again, just re-run (incremental, polite):

```bash
uv run invoker expand-corpus
```

It resumes where it stopped (already-expanded revisions are skipped) and
aborts politely if the server is still rate-limiting — wait longer and
re-run. ~68 pages at 1/min ≈ ~70 minutes.

**Verification that closes this item** (task #1 in the session task list):
after the backfill, confirm the uphill-miss value is answerable from
*stored* corpus (not live calls):

```bash
python3 -c "
import pathlib, re
p = list(pathlib.Path('data/corpus/liquipedia_dota2/evasion').glob('*.expanded.html'))[0]
text = re.sub(r'<[^>]+>', ' ', p.read_text())
i = text.find('Uphill Miss Chance', 2000)
print(re.sub(r'\s+', ' ', text[i:i+400]))
"
```

Expect the 25% figure in the section text (raw wikitext only has the
`{{G|uphill miss chance}}` template — that gap is benchmark case
`uphill-miss` and trial finding 1 in the spec).

## Next steps (in order)

1. **Ship this branch** (task #3): on the user's "ready to ship" signal —
   sub-agent review per `docs/specs/2026-04-26-collaboration-harness.md`,
   surface findings, paste review summary into the PR body, PR to `main`.
   The pending backfill does NOT gate the PR (`data/` is local/gitignored).
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
