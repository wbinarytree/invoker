# Game-File-Grounded Generators (Items + Heroes)

**Date:** 2026-07-26
**Status:** draft — awaiting sign-off
**Direction:** `docs/specs/2026-07-25-grounded-reasoner-rethink.md` (Milestone 1,
generation order `concepts → items → heroes`). One spec, two implementation
slices/PRs: items first (acceptance: `mage-slayer` benchmark case), then
heroes (acceptance: `corrosive-haze`).

## Goal

Extend the S1 generation machinery from corpus-grounded concepts to
**game-file-grounded items and heroes**. The shared design problem — and the
reason this is one spec — is grounding generation in *structured KV data*
instead of corpus prose: a mark grammar for `gamefile:`/`loc:` keys, packet
rendering that makes numbers checkable, resolvers, and vestigial-mechanic
handling. The generation flow itself (packet → article → card → mechanical
faithfulness checks → artifact + sidecar) is reused unchanged from concepts.

## Shared design

### Keyed packet sections

Like `build_packet` for concepts, the item/hero packet renders into
**keyed sections**; the generator may only cite keys present in its packet
(checked mechanically, generation aborts otherwise — unchanged rule).
Numbers in a cited span must appear in that section's rendered text
(`_check_numbers`, reused as-is).

Mark grammar (keys stay short — the agent-exposure model budgets ~15
tokens/key):

- `gamefile:items/<item_internal_name>` (+ optional `#<section>`:
  `cost`, `components`, `attribs`, `mechanics`) — rendered from
  `ItemContext`.
- `gamefile:abilities/<ability_internal_name>` — one section per ability
  or talent record, rendered from `AbilityContext`/`TalentContext`. This
  makes the `corrosive-haze` expected mark (`slardar_amplify_damage`) and
  the talent join (`special_bonus_unique_slardar_3`) natural citations.
- `gamefile:heroes/<hero_internal_name>#stats` — the hero stat rows
  (value + percentile band) from `HeroStatsContext`.
- `loc:<token>` — a localization token whose resolved text appears in the
  packet (descriptions, code-only talent display strings, scepter/shard
  upgrade text). Tooltip-token preference rules from the identity module
  apply (never cosmetic tokens — the `mage-slayer` trap).
- `changelog:<token>` — already defined; available to packets for
  removed-mechanic notes (below).

### Resolvers (benchmark side)

`MarkResolver` gains snapshot-backed resolvers: `gamefile:` keys parse to
class/record(+section) and resolve iff the record exists in the patch
snapshot (sections against a fixed vocabulary); `loc:` keys resolve iff the
token exists in the patch's localization export. Resolution stays
traceability, not truth.

### Vestigial mechanics

7.41d files still carry `Facets` blocks though facets were removed in 7.41
(trial finding 2). Packet builders **drop facet-conditional values** and
hero packets carry a standing removal note cited to
`changelog:DOTA_Patch_7_41_General_Global_Changes`, so generators describe
the mechanic as removed instead of describing vestigial data. The
changelog is the detector; nothing is inferred from file presence.

### Artifacts

Same shapes as concepts: `data/kb/<patch>/items/<slug>/` and
`heroes/<slug>/` with `article.md` + `artifact.json` (kind `item` /
`hero`), card sentences all marked, provenance identical.
`load_kb_entries` gains loaders for both classes (it fails loudly on
unknown classes today by design).

## Slice 1 — Items

- Generator over `ItemContext` (exists; AbilityValues→tooltip joins,
  recipe folding, cosmetic-token-proof resolution).
- Scope: all item records with a localized name and a cost or recipe
  presence (purchasables + neutrals); cosmetic/event records excluded.
- CLI: `invoker generate-item <item> --patch <patch>` (single-entity,
  like `generate-concept`; batch orchestration is shell, not code, until
  volume proves otherwise).
- Prompt: item-article v1 + shared card prompt; inline versioned
  constants (GUIDELINES as amended 2026-07-25).
- Acceptance: `mage-slayer` passes the benchmark; existing three cases
  stay green.

## Slice 2 — Heroes

- Generator over the **kit-wide** `HeroContextPacket`: identity, stat
  rows, every ability (incl. innates, scepter/shard upgrades), every
  talent — including display-string-only talents via the localization
  join. Per-ability generation is explicitly rejected: the code-only
  talent trap is invisible in a single-ability view.
- CLI: `invoker generate-hero <hero> --patch <patch>`.
- Acceptance: `corrosive-haze` passes; battery fully green (M1 gate
  becomes 5/5-answerable).
- Known gap carried, not fixed here: ~30 scepter/shard-granted abilities
  defined only in per-hero KV files are absent from hero ability lists
  (documented in `docs/context-modules.md`); affected hero articles omit
  them until the snapshot builder records defining files (existing
  tracked follow-up).

## Out of scope

- **Stats enrichment on hero pages** (`stats:` marks from OpenDota
  aggregates) — later pass, pending L2 scope (rethink open question 3).
- **Cross-layer citations** (hero articles citing concept articles) — no
  `kb:` mark kind exists yet; M1 item/hero pages cite substrate only.
  Arrives with claim extraction (S4), where layering becomes structural.
- Claims sidecars (S4), pair tier, batch/roster build orchestration and
  its cost ceiling (estimate before scaling — rethink open question 4).

## Decisions needing sign-off

1. **Item scope rule** as above (localized name + cost/recipe presence;
   neutrals in, cosmetics out) — or a curated list first?
2. **Facet handling: drop + cited removal note** (recommended) vs
   annotate-as-vestigial in packets.
3. **Section vocabulary is fixed per class** (recommended: small closed
   set per entity class, extended by code change) vs free-form section
   anchors like corpus headings.
