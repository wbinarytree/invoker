# Game-File Snapshot Playbook

Use this when Valve ships a patch. Covers the full flow: extracting KV files
from the local Dota 2 client with Source2Viewer-CLI, then building the
patch-scoped JSON snapshot. First run for a new patch: 2026-07-25 (7.41d).

## Step 0 — Extract KV files with Source2Viewer-CLI

Prerequisites (current local setup; adjust paths if they move):

```bash
S2V=/Users/yaoda/Downloads/cli-macos-arm64/Source2Viewer-CLI
VPK="$HOME/Library/Application Support/Steam/steamapps/common/dota 2 beta/game/dota/pak01_dir.vpk"
PATCH=7.41d   # the patch you are snapshotting
RAW=data/raw/game_files/$PATCH   # gitignored; run from repo root
```

Make sure Steam has fully updated Dota before extracting — check
`.../game/dota/steam.inf` (`VersionDate`) matches the patch release.

Only the KV text files are needed, not the full VPK:

```bash
mkdir -p "$RAW"

# npc scripts: heroes, abilities (+ per-hero ability files), items,
# neutral items, ability IDs (~150 small files)
"$S2V" -i "$VPK" -f "scripts/npc/" -o "$RAW"

# localization files per locale (abilities_, items_, dota_)
"$S2V" -i "$VPK" -f "resource/localization/abilities_english.txt,resource/localization/items_english.txt,resource/localization/dota_english.txt,resource/localization/abilities_schinese.txt,resource/localization/items_schinese.txt,resource/localization/dota_schinese.txt" -o "$RAW"

# in-game changelog: note text per locale, plus the patch manifest
# (structured per patch -> hero/item/ability -> note token; needs -d to
# decompile the compiled .vdpn_c resource)
"$S2V" -i "$VPK" -f "resource/localization/patchnotes/patchnotes_english.txt,resource/localization/patchnotes/patchnotes_schinese.txt" -o "$RAW"
"$S2V" -i "$VPK" -f "patchnotes/patchnotes.vdpn_c" -d -o "$RAW"
```

The changelog covers the full patch history shipped in the client (7.06d
through 7.41d as of the first extraction) and is itself knowledge — it is
the source for "when did X change/get removed" questions and for detecting
mechanics the current files still describe but the game removed.

The extractor preserves VPK paths (`scripts/npc/...`), but the snapshot
command expects `npc/` at the source root and discovers localization at
`<source>/resource/localization/`. Reshape once:

```bash
mv "$RAW/scripts/npc" "$RAW/npc" && rmdir "$RAW/scripts"
```

Useful while debugging: `-l` with the same `-f` filter lists matching VPK
entries without extracting; `--help` shows all flags.

## Step 1 — Build the snapshot

The command expects either a repo/root containing `npc/` or the `npc/` directory
itself:

```bash
uv run invoker snapshot-game-files \
  --vpk "$RAW" \
  --out data/invoker-game-data \
  --patch "$PATCH" \
  --locale english \
  --locale schinese
```

(`data/invoker-game-data` is the current `INVOKER_GAME_DATA_DIR` from `.env`;
pass whatever root you use.)

The command prints entity counts on success. For reference, 7.41d produced:
128 heroes, 1953 abilities, 544 items, 2 neutral item sections. Numbers in
that ballpark mean a healthy snapshot; a drastic drop means the extraction is
incomplete. Spot-check `snapshot.json` in the new patch directory — it should
list both locales and the relative source-file inventory.

Then point invoker at the snapshot root:

```bash
export INVOKER_GAME_DATA_DIR=/path/to/invoker-game-data
```

Expected output:

```text
<root>/<patch>/
  heroes.json
  abilities.json
  hero_abilities.json
  items.json
  neutral_items.json
  localization/english.json
  localization/schinese.json
  changelog.json        (when the patchnotes files from Step 0 are present)
  snapshot.json
```

By default the command auto-discovers and merges these files when they exist:

- `npc/npc_ability_ids.txt` for source-backed ability and item IDs
- `resource/localization/abilities_english.txt`
- `resource/localization/items_english.txt`
- `resource/localization/dota_english.txt`

If you want to use one specific localization KV file instead, pass it explicitly:

```bash
uv run invoker snapshot-game-files \
  --vpk /path/to/extracted-dota-files \
  --out /path/to/invoker-game-data \
  --patch 7.41b \
  --localization /path/to/dota_english.txt
```

`--localization` is only valid for a single `--locale` value. For normal patch
refreshes, prefer repeated `--locale` options so the snapshot records every
locale in one patch directory.

Snapshot metadata records generic source labels and relative source-file
inventory. It must not be treated as a place to store local absolute paths.

To produce the compact downstream identity/localization artifact:

```bash
uv run invoker export-identity-localization \
  --patch 7.41c \
  --locale english \
  --locale schinese \
  --out /tmp/identity_localization_7.41c.json
```

For downstream consumers that want separate resource files, produce split
localized resources:

```bash
uv run invoker export-localized-resources \
  --patch 7.41c \
  --locale english \
  --locale schinese \
  --out-dir /tmp/invoker_741c_resources
```

This writes:

```text
/tmp/invoker_741c_resources/
  hero_identity_localization.json
  item_identity_localization.json
  ability_localization.json
```

For the preferred downstream bundle shape, export game resources:

```bash
uv run invoker export-game-resources \
  --patch 7.41c \
  --locale english \
  --locale schinese \
  --out-dir /tmp/invoker_741c_bundle
```

This writes:

```text
/tmp/invoker_741c_bundle/
  bundle.json
  heroes.json
  items.json
  index.json
```

Do not commit generated snapshots or raw extracted Valve files to this repo.
