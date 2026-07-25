---
name: new-patch-snapshot
description: Extract KV files from the local Dota 2 client with Source2Viewer-CLI and build a patch-scoped game-file snapshot. Use when Valve ships a new patch (e.g. "snapshot 7.42", "new patch kicked off").
---

You are building a game-file snapshot for a new Dota 2 patch.

The canonical playbook is `docs/game-files-snapshot.md` — read it first; it is
the source of truth if this skill and the doc ever disagree.

## Inputs

Ask for the patch name if not given (e.g. `7.42`). Everything else has
defaults:

- `S2V=/Users/yaoda/Downloads/cli-macos-arm64/Source2Viewer-CLI`
- `VPK="$HOME/Library/Application Support/Steam/steamapps/common/dota 2 beta/game/dota/pak01_dir.vpk"`
- `RAW=data/raw/game_files/<patch>` (gitignored, repo-relative)
- snapshot output root: `data/invoker-game-data` (matches `INVOKER_GAME_DATA_DIR` in `.env`)
- locales: `english`, `schinese`

If the S2V binary or VPK is missing at those paths, stop and ask the user
where they moved it — do not guess or download anything.

## Steps

1. **Freshness check.** Confirm the client is actually on the new patch:
   `VersionDate` in `.../game/dota/steam.inf` should be on/after the patch
   release date. If it looks stale, tell the user to let Steam update first.
2. **Extract** (only KV text files, never the full VPK):
   - `"$S2V" -i "$VPK" -f "scripts/npc/" -o "$RAW"`
   - `"$S2V" -i "$VPK" -f "resource/localization/abilities_english.txt,resource/localization/items_english.txt,resource/localization/dota_english.txt,resource/localization/abilities_schinese.txt,resource/localization/items_schinese.txt,resource/localization/dota_schinese.txt" -o "$RAW"`
3. **Reshape** to the layout the snapshot command expects:
   `mv "$RAW/scripts/npc" "$RAW/npc" && rmdir "$RAW/scripts"`
4. **Snapshot:**
   `uv run invoker snapshot-game-files --vpk "$RAW" --out data/invoker-game-data --patch <patch> --locale english --locale schinese`
5. **Verify:**
   - Command prints entity counts. Reference (7.41d): 128 heroes,
     1953 abilities, 544 items, 2 neutral item sections. New patches should
     be in the same ballpark or slightly higher; a drastic drop means a bad
     extraction — investigate, don't proceed.
   - Check `data/invoker-game-data/<patch>/snapshot.json` lists both locales
     and the source-file inventory.
6. **Report** the counts and the snapshot path to the user.

## Hard rules

- Never commit extracted Valve files or generated snapshots (`data/` is
  gitignored — keep it that way).
- Do not extract the full VPK; the KV filters above are sufficient.
- If entity counts look wrong, surface it — do not silently accept a
  half-built snapshot.
