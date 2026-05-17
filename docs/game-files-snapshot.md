# Game-File Snapshot Playbook

Use this when Valve ships a patch and you have already extracted the VPK files
to a local directory.

The command expects either a repo/root containing `npc/` or the `npc/` directory
itself:

```bash
uv run invoker snapshot-game-files \
  --vpk /path/to/extracted-dota-files \
  --out /path/to/invoker-game-data \
  --patch 7.41c \
  --locale english \
  --locale schinese
```

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
  snapshot.json
```

By default the command auto-discovers and merges these files when they exist:

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
