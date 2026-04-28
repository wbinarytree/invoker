# Release Process for Authored KG Artifacts

Date: 2026-04-28
Status: draft
Stage: Stage 4.5, between vocabulary review and Stage 5 rule expansion

## Why

Invoker now has a usable local authoring loop, game-file-backed context, and
derived KG artifacts. The next implementation stages will expand vocabulary,
rules, and evidence. Before those stages make the artifact surface larger, the
project needs a repeatable release checkpoint.

The release process should answer:

- exactly which authored facts and derived artifacts are being published;
- which patch, source snapshot, and invoker version produced them;
- how another checkout can verify and consume the artifact;
- how a bad release is diagnosed or replaced.

This is now important enough to sit before Stage 5. Rule expansion should build
on an artifact layout that can be packaged, checked, and handed to consumers.

## Goals

1. Produce a versioned local release directory or archive from current authored
   facts and derived patch artifacts.
2. Include release metadata that ties together:
   - Dota patch;
   - invoker package version or git commit;
   - source game-file snapshot metadata;
   - authored corpus manifest;
   - derived artifact manifest;
   - generation timestamp.
3. Add a verification command or validation mode that checks a release before it
   is considered publishable.
4. Keep authored local data explicit. A release can include a copy of authored
   YAML, but it must not silently turn `data/authored/` into tracked repo
   source.
5. Keep the first release process local-first. Publishing to GitHub Releases,
   object storage, or another registry is a later policy decision.

## Non-Goals

- No public hosting or installer in the first PR.
- No automatic download of releases by `invoker`.
- No migration framework for old release schemas beyond a clear schema version.
- No raw Valve game files or generated game-file snapshots committed to this
  repo.
- No evidence-attachment or rule-expansion work in this stage.

## Release Contents

First release bundle shape:

```text
dist/invoker-kg-<patch>-<timestamp>/
  release.json
  authored/
    *.yaml
  derived/
    heroes/<hero_id>.json
    relations.json
    summary_<hero_id>.md
    manifest.json
  reports/
    validation.txt
    vocab-audit.txt
```

`release.json` should include:

```json
{
  "schema_version": 1,
  "patch": "7.41b",
  "invoker_version": "0.1.0",
  "git_commit": "...",
  "generated_at": "2026-04-28T00:00:00Z",
  "game_snapshot": {
    "patch": "7.41b",
    "source": "...",
    "generated_at": "..."
  },
  "authored": {
    "hero_count": 11,
    "files": [
      {"path": "authored/alchemist.yaml", "sha256": "..."}
    ]
  },
  "derived": {
    "manifest_path": "derived/manifest.json",
    "files": [
      {"path": "derived/relations.json", "sha256": "..."}
    ]
  },
  "checks": {
    "validate": "pass",
    "vocab_audit": "pass"
  }
}
```

## CLI Shape

Use the existing `publish` command name, but make its behavior concrete:

```bash
uv run invoker publish --patch 7.41b --out dist/
```

Expected behavior:

1. require `data/authored/*.yaml` to pass authored-facts validation;
2. require derived artifacts for the patch to exist, or fail with a clear
   instruction to run `bootstrap`;
3. run derived-artifact validation;
4. run `vocab-audit`;
5. copy authored and derived artifacts into the release directory;
6. write `release.json`;
7. print the release path and a short checklist.

Optional flags can be added only when needed:

- `--archive`: also write `.tar.gz`;
- `--force`: overwrite an existing local release path;
- `--include-summaries/--no-include-summaries`: if summary payload size becomes
  a problem.

## Verification

Minimum commands for the first release-process PR:

```bash
uv run pytest
uv run pyright
uv run ruff check
uv run invoker vocab-audit
uv run invoker validate --patch 7.41b
uv run invoker publish --patch 7.41b --out dist/
```

The PR should include tests for:

- release metadata shape;
- file hashing;
- missing derived artifact failure;
- failed validation prevents release creation;
- successful local release copies authored and derived artifacts.

## Phasing

### PR 1 — Local Release Bundle

- Implement concrete `publish --patch --out`.
- Add `release.json` schema and tests.
- Update `docs/cli.md` and `docs/architecture.md`.
- Keep output local under `dist/`, which should remain untracked.

### PR 2 — Release Verification / Inspection

- Add `invoker inspect-release PATH` or equivalent validation mode only if the
  first bundle proves hard to inspect manually.
- Add documentation for consumer handoff.

### Later — Distribution Policy

- Decide whether release artifacts live in GitHub Releases, an object store, or
  a separate data repository.
- Decide whether `invoker` should fetch a release automatically.

## Open Questions

- Should authored YAML be included in every release, or should the release only
  ship derived artifacts plus enough metadata to trace back to the local corpus?
- Should release naming use invoker version, git commit, timestamp, or all
  three?
- Should `publish` require a clean git worktree, or only record dirty state in
  `release.json`?
- Should `vocab-audit` warnings be recorded as warnings, or should specific
  warning categories become release blockers?
