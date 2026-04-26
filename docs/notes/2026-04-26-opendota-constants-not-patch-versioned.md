# OpenDota Constants Are Not Patch-Versioned

Date: 2026-04-26

## Context

During PR2 implementation of hero stat context, we verified the accuracy of
cached OpenDota data against known 7.41b patch notes.

## Learning

`/api/constants/heroes` and `/api/constants/abilities` always return the
**current live game state**. They have no patch parameter. The underlying data
comes from the community-maintained repo:
https://github.com/odota/dotaconstants

Our `CachedClient` caches by URL only, so the patch namespace in
`data/raw/opendota/<patch>/` is cosmetic — it does not version the constants
data.

Verified against 7.41b patch notes:

- **Hero stats stale**: Alchemist `base_agi` cached as 22; 7.41b reduced it
  to 19. Cache hash `ef778ea33a2bdf3b.json` under `authoring/` predates the
  patch.
- **Ability values stale**: Anti-Mage Mana Break `mana_per_hit_pct` cached as
  `[1.6, 2.4, 3.2, 4]`; 7.41b increased it to `[1.8, 2.7, 3.6, 4.5]`. Both
  the `authoring/` and `7.41b/` caches share the same file hash
  (`2d6340a8ec99d459.json`), confirming they are the same fetch.

## Implications

- Stat bands and ability descriptions in hero context are only accurate as of
  the last time the constants were fetched. After any patch they silently
  drift.
- The current data is acceptable for development and initial hero authoring,
  but authored facts citing specific stat values or ability numbers must be
  treated as approximate until the cache is refreshed.
- A production-grade context pipeline needs a **patch-aware, versioned data
  source** for both hero stats and ability values. OpenDota constants alone
  are not sufficient.
- When a new patch lands, constants caches should be manually invalidated and
  re-fetched. There is currently no tooling for this — it is a known gap.

## Future direction

- The dotaconstants repo is git-tagged — it may be possible to pin a specific
  commit corresponding to a patch and fetch from that revision rather than
  the live API.
- Consider maintaining a lightweight hand-curated patch-delta file (similar
  to `mechanism_primer_7.41b.yaml`) that overrides stale constant values
  until a versioned source exists.
- Any data source chosen for Oracle must carry an explicit patch identifier
  and timestamp alongside each fact.
