# Game-File Overlay for Hero Constants

Date: 2026-04-27
Status: deferred follow-up. Not blocking PR 4.

## Why

The two community APIs we currently rely on are stale and lossy. As of this
spec date:

- OpenDota `/api/constants` returns 7.41 data while the live patch is **7.41b**.
- Stratz returns **7.40b**, one full minor patch behind that.

Staleness is the primary problem. Lossiness is the second:

- Talent `dname` strings carry unresolved `{s:bonus_*}` template tokens because
  OpenDota does not ship the `LinkedSpecialBonus` resolution map. Our PR 4
  workaround substitutes `?` for the value (`+?s Slithereen Crush Cooldown`).
- `AbilityValues` for higher-level scaling and conditional fields are
  partially stripped.
- Innate detection in OpenDota is a heuristic on a `is_innate` boolean; the KV
  source has the canonical flag plus innate-specific fields.
- Scepter / Shard upgrade descriptions are not normalized; they live in the
  ability KV and are only sometimes mirrored into OpenDota's text.

Both staleness and lossiness violate the project rule that Dota facts must
come from a citable source — if the source itself is a patch behind, the cited
fact is wrong even when correctly attributed.

## What This Is Not

- Not a replacement for OpenDota. OpenDota stays the spine for hero list,
  match data, and the bulk of ability text.
- Not a live extractor. The overlay is a per-patch snapshot committed to the
  repo; it does not read the user's Dota install at runtime.
- Not a rule-engine change. Stage 5 relation rules are independent.

## What the Overlay Fills

Scoped, gap-driven. Only fields that OpenDota is demonstrably wrong or
missing on:

1. Talent value resolution. Every `{s:bonus_*}` token becomes a real number
   or list of numbers via the talent's `LinkedSpecialBonus` → ability
   `AbilityValues` chain.
2. Patch identifier. The snapshot's directory name is the authoritative
   patch tag; we stop trusting OpenDota's patch metadata.
3. Innate flag and innate-specific fields, taken from the KV directly.
4. Future: Scepter / Shard descriptions and conditional-fact inputs, when
   Stage 5 needs them. Not part of the first overlay version.

## Approach

Per-patch snapshot, layered after OpenDota.

1. **Extract.** Use `Source2Viewer-CLI` (or equivalent) to decompile
   `pak01_dir.vpk`. Pull only:
   - `scripts/npc/npc_abilities.txt`
   - `resource/localization/dota_english.txt`
2. **Snapshot.** Commit under `data/raw/game/<patch>/` (e.g.
   `data/raw/game/7.41b/`). The directory name is the patch tag.
3. **Parse.** Add `src/invoker/sources/game_kv.py` with a small KeyValues
   parser. KV format is stable and well-documented; ~200 lines.
4. **Overlay.** In `ability_context.py`, after the OpenDota build, apply the
   overlay to fill the targeted gaps. Overlay misses (talent has no
   resolvable `LinkedSpecialBonus`) keep the OpenDota fallback or the `?`
   placeholder — never silently fabricate.
5. **Refresh playbook.** Document the per-patch refresh under `docs/`:
   when Valve ships a patch, re-run the extractor, drop the new snapshot
   under a new directory, bump the active-patch constant. No code change in
   the common case.

## Costs and Risks

- One-off tooling: VPK extraction is local, not a stable API. We own the
  extractor invocation but not its source.
- Patch-day work: someone has to refresh the snapshot. Cadence is roughly
  every 4-6 weeks at current Valve velocity.
- KV parser bugs become our bugs. Mitigated by keeping the parser narrow
  (only the fields the overlay reads).
- License: Valve's content is redistributable for community tooling per
  precedent (OpenDota, Dotabuff, Stratz all do this), but the snapshot is
  derived data — keep it under `data/raw/` with a NOTE on provenance.

## When To Build It

After PR 4 ships, generate authored facts for a slice of heroes with the
current OpenDota-only context. If:

- talent gaps materially break authored fact quality, or
- a hero has a confirmed mechanic that OpenDota's stale 7.41 data does not
  reflect and that affects authored buckets,

then escalate this spec to accepted and build the overlay. Otherwise the
`?` placeholder + stale-but-close OpenDota data is acceptable for the
authoring workflow.

## Open Questions

- Snapshot scope: just `npc_abilities.txt` + `dota_english.txt`, or also
  `npc_heroes.txt` (would let us drop the `hero_stats` OpenDota call too)?
- How do we surface the patch mismatch when OpenDota disagrees with the
  snapshot? Explicit warning at build time, or silently prefer the snapshot?
- Should the overlay snapshot be committed to the repo, or pulled from a
  separate releases bucket so the repo does not bloat over patches?
- Do we keep historical snapshots, or only the active patch?
