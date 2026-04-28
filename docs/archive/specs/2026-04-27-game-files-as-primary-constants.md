# Game Files as Primary Source for Hero / Ability / Item Constants

Status: superseded by [docs/architecture.md](../../architecture.md),
[docs/context-modules.md](../../context-modules.md), and
[docs/game-files-snapshot.md](../../game-files-snapshot.md). Phase 5a/5b are
implemented; Phase 5c item/neutral-item consumers and Phase 6 release bundles
remain deferred future work. Archived on 2026-04-28.

Date: 2026-04-27
Original status: draft (discussion)
Stage: post-PR4 quality / source hardening, before Stage 5 rule expansion

## Why

Both community APIs we currently rely on are stale and lossy against the live
patch (7.41b as of this date):

- OpenDota `/api/constants/*` returns 7.41 data and is not patch-versioned —
  the URL is the cache key and the upstream silently drifts.
- Stratz returns 7.40b, one minor patch further behind.

The lossiness on talents (`{s:bonus_*}` placeholders, missing
`LinkedSpecialBonus` resolution map), innates (heuristic boolean instead of
canonical KV flag), and Scepter / Shard upgrades pushed PR 4 to ship
workarounds (`?` placeholder, hand-curated mechanism primer). Those are
acceptable as one-time cushions but violate the project rule that Dota facts
must come from a citable, current source.

Valve's own KV files are the canonical source. A snapshot of `pak01_dir.vpk`
gives us:

- accurate, patch-tagged numbers for every base ability, innate, and talent;
- inline talent value resolution (no `LinkedSpecialBonus` chase — values sit
  next to `AbilityValues` keyed by `special_bonus_unique_*`);
- explicit `Innate`, `HasShardUpgrade`, `HasScepterUpgrade`, `IsGrantedByShard`
  flags;
- full item and neutral-item KV (net new).

This spec replaces the deferred "overlay" approach captured in
`docs/notes/2026-04-27-game-file-overlay.md`. That note proposed game KV as a
gap-filler layered after OpenDota; here we make game KV the primary source for
constants and demote OpenDota to match-data only.

## Scope

In:

- Hero metadata, base stats, attribute gain, attack range, role tags
- Base abilities, innates, talents, Scepter / Shard variants
- Items and neutral items (KV exposure; consumption deferred to Stage 5
  conditional facts)
- Localized display strings (ability/item names, tooltip prose)

Out:

- Match data: matchups, pro matches, win/pick rates, lane outcomes — these
  stay on OpenDota / STRATZ. Game files do not have aggregated player data.
- Stage 5 rule changes.
- Bundle/install flow for authored data.

## Non-Goals

- No live VPK extraction at runtime. The snapshot is built externally and
  injected into the builder.
- No raw game data committed to this repo. `data/` stays gitignored; this
  project is a KG builder, not a game-data archive.
- No silent fallback to OpenDota when the snapshot is missing a field — surface
  the gap explicitly so the cause is debuggable.
- No workarounds when the canonical source is available. The talent `?`
  placeholder and the per-patch `mechanism_primer_*.yaml` retire in Phase 5b.

## Data Injection Model

The snapshot lives **outside** the repo and **the core flow consumes JSON,
never raw KV**. Two cleanly separated concerns, both inside invoker:

- **Bootstrap snapshot tool** (one-off per patch, not on any hot path):
  KV → JSON translation. Lives in invoker so we don't pay cross-repo cost
  when the parser needs a fix; explicitly *not* imported by the core flow.
- **Core flow:** reads the JSON snapshot via an injected path through
  `GameFilesSource`. Never touches raw KV, never imports the parser.

The split is enforced by module boundary, not by repo boundary: the parser
lives under `src/invoker/snapshot/` and the consumer under
`src/invoker/sources/game_files.py`. `sources/game_files.py` must not import
from `snapshot/`. If we ever decide to move the snapshot tool out, the move
is mechanical because the boundary already exists.

Builder contract:

- New config field: `INVOKER_GAME_DATA_DIR` (path to a snapshot root).
- Layout invoker expects under that root:
  ```
  <root>/<patch>/
    heroes.json              # all heroes, keyed by internal name
    abilities.json           # all abilities, keyed by internal name
    hero_abilities.json      # hero internal name → ability list
    items.json               # all items
    neutral_items.json
    localization/
      english.json           # display strings; future: chinese.json, etc.
    snapshot.json            # metadata: patch, source revision, timestamp
  ```
- The active patch is selected by the existing `--patch` flag / config; the
  core flow asserts the directory exists and fails loudly otherwise. No
  silent fallback to OpenDota constants.

The JSON shape preserves KV nesting (e.g., `AbilityValues` blocks stay as
nested objects); the translation is a thin pass, not a normalization.
Normalization stays in `ability_context.py` as it does today.

Snapshot refresh is infrequent (only when Valve ships a patch) and is a
one-off operator action: re-extract with Source2Viewer-CLI, run
`uv run invoker snapshot-game-files --vpk … --out …`, point
`INVOKER_GAME_DATA_DIR` at the new patch directory. A short playbook lives
under `docs/`.

## Module Shape

A new source adapter mirrors the constants surface that `OpenDotaFetcher`
exposes, so consumer modules swap implementations rather than rewriting:

```python
class GameFilesSource:
    def __init__(self, root: Path, patch: str, locale: str = "english") -> None: ...
    def heroes(self) -> list[dict[str, Any]]: ...
    def abilities(self) -> dict[str, Any]: ...
    def hero_abilities_map(self) -> dict[str, Any]: ...
    def hero_stats(self) -> dict[str, Any]: ...
```

Return shapes match the OpenDota return shapes that current consumers
(`hero_context.py`, `hero_stats_context.py`, `ability_context.py`,
`pipeline/fetch.py`, `pipeline/derive.py`) already parse — Phase 5a is a pure
backend swap behind those signatures. Net new fields (canonical `Innate`,
Scepter/Shard flags, fully resolved talent values) are additive.

`OpenDotaFetcher` keeps `matchups()` and `pro_matches()` only.

`hero_context.py` uses `GameFilesSource` as the default source because game
snapshots are the primary constants source. The packet assembly function still
accepts a narrow constants-source protocol (`heroes`, `hero_stats`,
`abilities`, `hero_abilities_map`) so a future source swap would be localized
to adapter construction rather than prompt rendering, stats computation, or
ability normalization. There is no runtime source selector in Phase 5b because
the project has no current need for an alternate constants source.

### Localization

`locale` is a dimension on the adapter from day one (defaults to English) so
adding Chinese or other languages later is a content drop, not a code change.
Only English content lands in 5a — invoker-internal consumers (authored YAML,
LLM authoring prompt) are English-only. Multi-locale is provisioned for the
narrow future case of showing Valve's official localized tooltip verbatim;
Oracle answers in non-English are handled at the answering-model layer, not by
quoting localized KV.

## KV Parser (bootstrap-only, isolated from the core flow)

The parser is a one-off bootstrap concern, not on any hot path. It lives in
invoker (under `src/invoker/snapshot/`) so format surprises don't require a
cross-repo round-trip. The core flow (`src/invoker/sources/game_files.py`
and everything downstream) reads JSON only and must not import from
`snapshot/` — this isolation is what protects the "scale to all 128 heroes +
tags + relations" work in 5b/5c when the parser needs a fix.

**Decision: write our own, narrow KV1 parser.** Vendoring is rejected for
now — the PyPI vdf packages handle `#base` includes inconsistently and lose
duplicate-key semantics, both of which we'd want to control. KV1 (text) is
stable and well-documented; the fields we need are scalar strings inside
nested blocks with no exotic features in scope.

Constraints:

- Only the fields the JSON contract emits; ignore everything else.
- Fail loud on syntax not recognized (`[$WIN32]` conditional gates,
  `#include`, KV3 markers) — no silent pass-through.
- No `#base` resolution unless a needed file requires it. If a file carries
  a `#base` directive that hides data, promote a small include resolver
  — no general macro expansion.
- Pure parser; no source-shape transforms. Normalization stays in
  `ability_context.py`.

If the parser spike against `npc_dota_hero_alchemist.txt` turns up real-world
syntax that pushes scope materially, fall back to vendoring at that point.
The JSON output contract is unchanged either way.

If the snapshot tool ever needs to move out of invoker, the move is
mechanical because the module boundary already exists.

## Phasing

Both the snapshot tool and the consumer live in invoker, separated by module
boundary. Phase 5a delivers both.

### Phase 5a — Snapshot Tool + JSON Contract + Consumer

Snapshot tool (`src/invoker/snapshot/`, bootstrap-only):

- KV1 parser sufficient for the fields the JSON contract emits.
- New CLI subcommand `invoker snapshot-game-files --vpk <path> --out <dir>`
  that runs the KV → JSON translation. Operator pre-extracts the VPK
  with Source2Viewer-CLI; this command does not call the extractor itself.
- First snapshot for the active patch (7.41b at spec date), spot-checked
  against alchemist (talent value resolution, innate flag, Scepter/Shard
  flags, ability KV).
- Short refresh playbook under `docs/`.

Consumer (`src/invoker/sources/game_files.py`):

- `GameFilesSource` reads JSON only. Must not import from `snapshot/`.
- Add `INVOKER_GAME_DATA_DIR` to `config.py`.
- Tests against an alchemist JSON fixture committed under
  `tests/fixtures/game_snapshot/`: hero stats, ability list, talent values,
  innate flag, Scepter/Shard flags.
- No call-site changes yet. OpenDota constants still drive the build.

### Phase 5b — Swap Constants Behind Existing Consumers

- Flip `hero_context.py`, `hero_stats_context.py`, `ability_context.py`,
  `pipeline/fetch.py`, `pipeline/derive.py` to read constants from
  `GameFilesSource` instead of `OpenDotaFetcher`.
- Retire the talent `?` placeholder.
- Retire `mechanism_primer_*.yaml` if all stat-conversion facts it carries
  are derivable from KV (verify per-key before deletion; archive otherwise).
- Regenerate trial-slice authoring prompts (Slardar, Pangolier, Alchemist)
  and diff against current outputs to confirm fidelity is *better*, not
  worse.
- Scale fact authoring across remaining heroes — confidently, because the
  parser is decoupled from invoker.
- Update `docs/architecture.md` and `docs/context-modules.md`.
- `OpenDotaFetcher.heroes() / abilities() / hero_abilities_map() /
  hero_stats()` removed. `matchups()` and `pro_matches()` stay.

### Phase 5c — Items and Neutral Items (deferred)

- Snapshot tool already emits `items.json` and `neutral_items.json` from 5a,
  so this is consumer-side only.
- Expose via `GameFilesSource.items()` / `neutral_items()`.
- Wire into the conditional-fact pipeline when Stage 5 needs Scepter / Shard
  / Blink-dependent capabilities. Not in the initial swap.

### Phase 6 — Release Bundle (separate spec)

5a produces snapshots locally. Phase 6 turns them into a release bundle —
patch tag + invoker version + timestamp correlated together — and decides
the publication mechanism. Does **not** revisit the parser, the JSON
contract, or the module boundary:

- Versioned bundle (patch + invoker + timestamp) and publication target
  (GitHub releases, object store, TBD)
- Schema versioning and migration policy when the JSON contract evolves
- Optional: invoker auto-fetch of a bundle for a given patch
- Different concern (distribution / ops). Does not block 5a.

## Risks

- **KV edge cases.** If `#base` includes turn out to be load-bearing for the
  fields we read, parser scope expands. Phase 5a spike confirms before
  committing.
- **Field-name drift across patches.** Valve renames KV keys occasionally.
  The narrow consumer surface means drift is loud (KeyError) rather than
  silent. Acceptable.
- **Snapshot freshness.** Patches are infrequent; refresh is a one-off
  operator action whenever Valve ships. No automation needed in 5a.
- **Display-string availability.** `dota_english.txt` covers ability and item
  names plus tooltip prose. Confirm in Phase 5a that the keys we render
  (ability `dname`, item `dname`, talent display strings) are all present.
- **Module boundary erosion.** `sources/game_files.py` importing from
  `snapshot/` would re-couple the core flow to the parser and undo the main
  reason for keeping the parser in-repo. Enforce by code review; consider a
  pyright/ruff rule if it slips.

## Verification

- `uv run pytest`, `uv run pyright`, `uv run ruff check`
- `uv run invoker vocab-audit`
- Trial-slice authoring prompt regen + diff (Slardar, Pangolier, Alchemist):
  - talent values are resolved numbers, not `?`
  - innate source flag matches KV
  - hero stats match the live patch
  - ability lists, mana costs, cooldowns match the live patch

## Open Questions

- JSON contract shape: thin pass that preserves KV nesting verbatim (current
  proposal), or modest normalization at translation time (e.g. coerce
  `"1.5 2.0 2.5 3.0"` to `[1.5, 2.0, 2.5, 3.0]`)? Thin-pass is simpler and
  pushes interpretation into the consumer where the existing normalization
  already lives.
