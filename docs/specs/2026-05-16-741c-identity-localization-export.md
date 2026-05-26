# 7.41c Identity Localization Export

Status: in progress

## Outcome

Invoker should produce compact patch-scoped identity/localization artifacts for
downstream consumers such as Phylactery. The first artifact covered
source-backed hero and item identity only:

- hero ids, internal NPC names, slugs, display names, and aliases;
- item and neutral item internal names, optional ids, display names, and aliases
  where the game-file snapshot exposes them;
- locale-scoped data for at least `english` and `schinese`;
- sanitized provenance that identifies the Invoker snapshot and patch without
  embedding local absolute paths.

This is not a hero mechanics, matchup, or coaching-advice feature.

The current export path preserves that combined artifact for existing
consumers, and also supports split resource artifacts:

- `hero_identity_localization.json`
- `item_identity_localization.json`
- `ability_localization.json`

The split item artifact carries source-backed item names, descriptions, search
aliases, ids, and neutral flags. The split ability artifact carries hero-linked
ability and talent names, descriptions, search aliases, and owner heroes.

## Source Boundary

Invoker owns the local game-file snapshot and compact export boundary.
Downstream consumers should not parse raw extracted Valve KV files at runtime.

Expected local flow:

1. Extract Valve files into a local untracked directory.
2. Run `invoker snapshot-game-files --patch 7.41c` against that extraction.
3. Export a compact identity/localization JSON artifact from the snapshot.
4. Commit only the compact downstream artifact if the consumer repo decides it
   is small and stable enough to ship.

Generated snapshots and raw Valve files remain untracked. Export metadata must
use generic labels such as `dota2npc extraction`, `invoker game-file snapshot`,
and `patch 7.41c`; it must not contain personal usernames or local absolute
paths.

## Artifact Contract

Invoker exports JSON shaped like:

```json
{
  "schema_version": 1,
  "patch": "7.41c",
  "generated_from": {
    "source": "invoker game-file snapshot",
    "source_patch": "7.41c",
    "source_snapshot": {
      "kind": "invoker_snapshot",
      "metadata": {}
    }
  },
  "locales": ["english", "schinese"],
  "heroes": [
    {
      "hero_id": 120,
      "internal_name": "npc_dota_hero_pangolier",
      "slug": "pangolier",
      "display_names": {
        "english": "Pangolier"
      },
      "aliases": {
        "english": ["pangolier"],
        "schinese": ["shilinjianshi", "gungun", "tangte"]
      },
      "sources": ["npc_heroes", "localization"]
    }
  ],
  "items": [],
  "unknowns": []
}
```

Alias values stay distinct from official display names. Lookup code may
normalize case and separators, but the artifact preserves source tokens.

## Implementation Slices

- [x] Add this Invoker-side spec and route it from current-direction docs.
- [x] Extend snapshot generation to preserve multiple locale JSON files in one
  patch snapshot.
- [x] Sanitize snapshot/export provenance so downstream metadata does not expose
  local paths.
- [x] Add a compact identity/localization export command.
- [x] Extract hero aliases from localization keys ending in `__name_alias`.
- [x] Include item and neutral item identity when the snapshot exposes stable
  internal names and display names.
- [x] Extend hero lookup to include source aliases and return matched fields.
- [x] Add validation for duplicate hero ids and duplicate internal names, and
  record alias collisions that normalize to multiple heroes.
- [x] Add split hero, item, and ability localized resource export files.
- [x] Recover item display names from `DOTA_Tooltip_Ability_<item>:n` keys.
- [x] Include source-backed item and ability descriptions where localization
  exposes them.

## Validation

- `uv run pytest`
- `uv run pyright`
- `uv run ruff check`
- Local smoke with the current extracted 7.41c files:

```bash
uv run invoker snapshot-game-files \
  --vpk /path/to/extracted-dota-files \
  --out data/invoker-game-data \
  --patch 7.41c \
  --locale english \
  --locale schinese

uv run invoker export-identity-localization \
  --patch 7.41c \
  --locale english \
  --locale schinese \
  --out /tmp/identity_localization_7.41c.json

uv run invoker export-localized-resources \
  --patch 7.41c \
  --locale english \
  --locale schinese \
  --out-dir /tmp/invoker_741c_resources
```

Acceptance checks:

- Pangolier resolves by id, internal name, slug, English display name, and the
  source-backed `schinese` alias token `gungun` when present in the source.
- Ambiguous aliases are surfaced explicitly in `unknowns` and through lookup
  candidate lists.
- Export metadata has no local absolute paths or personal usernames.
- The artifact can be consumed without importing Invoker Python modules.
