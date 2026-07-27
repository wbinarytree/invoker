# Item KB quality follow-ups: mechanics packet policy, guard v2, qualifiers, card lore

**Status:** accepted (user sign-off 2026-07-27; codex spend approved, cards-only lore pass now rather than waiting for 7.42)

**Context.** The 7.41d item fleet (batch KB generation spec) produced 291/292
artifacts; the acceptance triage (2026-07-27, this branch) classified every
guard flag and spot-checks surfaced two article-quality findings. Root causes
cluster into four small changes. Findings, with counts from the committed
corpus and the 7.41d snapshot:

1. **Guard flags are mostly the guard fighting the prompt.** Of 240 flags on
   91 items: 93+ demand internal `item_*` identifiers in prose (the prompt
   forbids them), ~11 items' flags demand a table value restated jointly with
   its prose semantics (the prompt forbids restating table values in prose),
   flask's flag is a bare tooltip label ("Use: Salve"), soul_ring's cites an
   unsubstituted `%AbilityHealthCost%` template variable. Only ~10 items carry
   flags for facts genuinely absent (see change C).
2. **`#mechanics` mirrors engine boilerplate.** `AbilityBehavior:
   DOTA_ABILITY_BEHAVIOR_PASSIVE` is stamped on 100 pure-stat records
   (no description token, no ability) — the coverage gate then forces every
   such article to write a vacuous "has Passive behavior" sentence
   (claymore, cloak_of_flames prose; ~24 more as a `| Behavior | Passive |`
   table row). Valve also stores aeon_disk's cooldown twice (`AbilityCooldown`
   + `AbilityValues.cooldown_duration`); the duplicate becomes a `#mechanics`
   line no register-compliant article ever cites → 4/4 deterministic
   coverage rejections, the one parked item.
3. **Raw enums leak into articles.** `_behavior` in `sources/game_files.py`
   maps 9 flags and passes unknowns through raw; 17 distinct unmapped
   `DOTA_ABILITY_BEHAVIOR_*` flags appear in 7.41d KV and reach 44 committed
   articles verbatim (e.g. `DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK`).
4. **Cards have no lore** (by the game-file-grounded generators spec: cards
   are identity + numbers, no flavor). User direction 2026-07-27: the lore
   line belongs in the card too.

## Changes

### A. `#mechanics` packet policy (`gen/items.py`, `sources/game_files.py`)

- **A1 — boilerplate suppression.** Drop the `Behavior` line when behavior is
  exactly `["Passive"]` and the record has no description loc token (no
  ability — the flag is engine boilerplate, not game information). When that
  empties `mechanics_lines`, no `#mechanics` section is emitted (existing
  conditional). Kills the vacuous-Mechanics class (~100 records). For
  ability-bearing items (description present), `Behavior: Passive` stays —
  active/passive is real information there.
- **A2 — duplicate-value dedup.** Drop a `#mechanics` line whose rendered
  value text is identical to an `#attribs` row's rendered value (same
  `_value_text` rendering; string equality). Collapses Valve's own KV
  duplication instead of forcing the article to cite it twice. Unblocks
  aeon_disk.
- **A3 — behavior flag mapping.** Extend `_behavior`'s mapping with the 17
  flags observed in 7.41d (`DONT_RESUME_ATTACK` → "Doesn't Resume Attack",
  `SUPPRESS_ASSOCIATED_CONSUMABLE` → "Suppresses Associated Consumable",
  `IGNORE_CHANNEL` → "Usable While Channelling", `OPTIONAL_UNIT_TARGET`,
  `ROOT_DISABLES`, `DONT_PROC_OTHER_ABILITIES`, `DIRECTIONAL`, `OVERSHOOT`,
  `DONT_CANCEL_MOVEMENT`, `UNSWAPPABLE`, `IGNORE_BACKSWING`, `NOT_LEARNABLE`,
  `DONT_RESUME_MOVEMENT`, `VECTOR_TARGETING`, `IGNORE_INVISIBLE`,
  `IGNORE_PSEUDO_QUEUE`, `DONT_CANCEL_CHANNEL` — final wording at
  implementation, mechanical from the enum name). Fallback for flags unseen
  in this snapshot: strip the `DOTA_ABILITY_BEHAVIOR_` prefix and title-case
  the words — mechanical, faithful, never a raw enum in prose. `_behavior`
  runs at snapshot read time, so no re-export is needed.

### B. Completeness guard prompt v2 (`gen/guard.py`)

Add register rules to `GUARD_SYSTEM` (bump `GUARD_PROMPT_VERSION` to 2):

- A fact counts as carried when its value appears in a table row and its
  meaning appears in prose — the article's register splits them by design;
  joint restatement is never required.
- Internal identifiers (`item_*` names, section keys) are never expected in
  prose; their absence is not a missing fact.
- Bare tooltip labels ("Use: Salve") and unsubstituted `%var%` template
  strings are not load-bearing facts.

The guard stays a pure absence judge — flat report, no ranking, mechanical
downstream handling unchanged.

### C. Item article prompt v7: qualifiers survive (`gen/items.py`)

One added rule: every qualifier the source attaches to a value survives into
the article — cadence ("per second"), damage-type restriction ("magic damage
only"), trigger condition, and each ability's active/passive classification;
when both `#mechanics` and the tooltip state the classification, cite
`#mechanics` (narrowest gamefile source). Motivated by the ~10 true-gap
items: spirit_vessel's article reads "Soul Release deals 25 damage" where the
tooltip states 25 damage *per second* — a materially wrong reading.

### D. Card lore (`gen/items.py` card prompt bump)

User direction 2026-07-27. The card's closing sentence carries the lore as
the source states it, citing the lore `loc:` section — the explicit exception
to the no-flavor rule, because it is quoted record content, not model-authored
flavor. Budget: still ≤ 12 sentences / ~300 tokens. Concepts have no lore
sections; heroes (future) inherit the same rule.

## Execution order and spend

1. Land A + B + C + D with tests (mechanical, no artifacts touched).
2. Re-run the guard only over the 91 flagged items (~1.3M input tokens);
   completeness.json rewritten, bucket report regenerated. Expect the flag
   list to collapse to roughly the true-gap class.
3. Regenerate with the new packet + prompt v7: aeon_disk plus the true-gap
   items (ballista, bfury, bloodstone, boots_of_bearing, crellas_crozier,
   devastator, disperser, glimmer_cape, safety_bubble, spirit_vessel)
   (~0.5M input tokens). Bucket review + acceptance as usual.
4. Cards-only regeneration pass over the remaining committed items so every
   card gains its lore line without regenerating articles: a card-only path
   reusing the stored article via `load_entity_article` (~0.6M input tokens,
   291 small calls). Alternative considered: defer card lore to the 7.42
   full regeneration — rejected only if the user wants lore now; decision at
   sign-off.

The claymore/enum cosmetic classes stay in the committed corpus until the
7.42 snapshot's full regeneration — they are guard-clean and display-only.

## Testing

- A1/A2/A3: unit tests on `build_item_packet` and `_behavior` (suppression
  condition, dedup, mapping + fallback) — pure functions.
- B: no unit tests (LLM prose); the step-2 re-guard run is the check, diffs
  surfaced in the bucket report.
- C/D: existing mark/number checks cover the new sentences; one fixture test
  that the card's last sentence cites the lore section when the packet
  carries one.
