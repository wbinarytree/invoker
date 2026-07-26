# Game-File-Grounded Generators (Items + Heroes)

**Date:** 2026-07-26
**Status:** accepted (user sign-off 2026-07-26 after two mock-review rounds + Liquipedia cross-reference; recommendations adopted)
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
(trial finding 2). Packet builders **drop facet-conditional values
silently** — the generator never sees them, so articles never mention
facets at all. Removed-mechanic questions resolve at ask time through the
changelog (the `facet-removal` case already passes that way); a
historical concept page can own the mechanic's story later. Decided
against a standing removal note in hero articles (mock review
2026-07-26): a global game fact disclaimed on 126 hero pages is noise —
suppression belongs in the packet, not the output. The changelog is the
detector; nothing is inferred from file presence.

### Article register (mock review 2026-07-26)

Numbers live in **compact stat lines/tables per section** — mechanically
checkable cell-by-cell against the cited source — and prose is reserved
for behavior semantics (interactions, dispellability, immunity piercing,
what the mechanic *does*). Never restate table values in sentences. Stat
context uses the band or the raw value, not both (they double-encode).
Density stays high — over-compression is the named failure mode — but no
value appears twice. **Tables carry every attrib row the packet has,
including scepter/shard bonus columns — the generator never trims
values** (mock review caught silent trimming immediately). Cards
unchanged (~300 tokens, every sentence marked).

### Packet gaps to close (found 2026-07-26, raw-KV + Liquipedia cross-reference)

- **Attrib header macros are not resolved** (item slice): the packet
  renders `BONUS MAGICAL ARMOR: 18` from the KV key, but the tooltip
  token is `'%+$spell_resist'` — in game it reads "+18% Magic
  Resistance". Header derivation must resolve `$variable` label macros
  (and `%` formatting) so articles use the terms players actually see.
  The mage-slayer gold case needed no relaxation — the mock's apparent
  vocabulary gap was this rendering bug.
- **`hero_levelup` modifiers are absent from `AttribEntry`** (hero
  slice): e.g. Seaborn Sentinel `puddle_armor +0.2`/level — innate
  values would read as flat when they scale. Liquipedia lists these;
  KV carries them. `AttribEntry` gains a `levelup_bonus` field.
- **Talent→value joins** (hero slice — promoted from
  recorded-for-S4): KV binds talent modifiers directly to values
  (`river_damage_pct: {special_bonus_unique_slardar_6: "+16"}`,
  `undispellable: {special_bonus_unique_slardar_3: "+1"}`). The latter
  disproves trial finding 3's "no machine-readable effect" claim — the
  undispellable talent IS in AbilityValues, so a `talent_bonus` column
  gives hero articles real `gamefile:` grounding for talent effects
  instead of leaning on display strings alone.

### Cross-reference note (2026-07-26)

Liquipedia's Mage Slayer page still lists 40 DPS; our files and
changelog agree on 35 (`7.41c: "damage per second decreased from 40 to
35"`, 2026-05-06) while the page's own recent-changes section already
documents 7.41d — a live instance of volunteer staleness that
mechanical invalidation is built to beat. When generated, our item
article will disagree with the wiki and carry the changelog mark as the
receipt.

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

## Amendment — slice-1 skim findings (2026-07-26, user decision)

The human skim of the first item artifact drove three changes, folded
into the slice-1 PR:

1. **SKILL.md-style artifact files (schema v3).** Reading the archive,
   the card and the article were indistinguishable (card buried in
   `artifact.json`, article a plain file). `article.md` now carries YAML
   frontmatter — title/kind/patch + the card with per-sentence marks —
   above the article body, like a skill's description-then-content.
   `artifact.json` keeps citations/hashes/provenance and deliberately
   not the card (one home per fact). `article_sha256` binds the whole
   file. Committed v2 artifacts were migrated mechanically (no content
   change, provenance untouched); the loader rejects stale schemas.
2. **Identity-line card register.** The generated card opened with
   flavor prose ("combines magic resistance and regeneration … cripples
   enemy spell output") — unusable as an index summary. Card prompts now
   require sentence 1 to identify the entity concretely with its
   defining numbers (it is the one exception to one-fact-per-sentence
   and carries all contributing marks), ban flavor verbs and "combines
   X with Y" summaries, and forbid attaching a mark to facts its section
   does not state. The item article prompt gets the same concrete-opener
   rule (numberless — its numbers live in the tables).
3. **Percent for label-token-less keys.** `spell_amp_debuff` has no
   tooltip label token, so the packet rendered a unit-less "40". The raw
   description template is the mechanical percent source: `%key%%%`
   renders a literal % after the substituted value. Packets also cite
   the `loc:` token that actually resolved (carried on `ItemContext`)
   instead of synthesizing a casing.

## Decisions needing sign-off

1. **Item scope rule** as above (localized name + cost/recipe presence;
   neutrals in, cosmetics out) — or a curated list first?
2. **Facet handling: drop + cited removal note** (recommended) vs
   annotate-as-vestigial in packets.
3. **Section vocabulary is fixed per class** (recommended: small closed
   set per entity class, extended by code change) vs free-form section
   anchors like corpus headings.
