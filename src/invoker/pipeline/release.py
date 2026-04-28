from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import tarfile
from dataclasses import dataclass
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from invoker.kg.authoring import validate_authored_file
from invoker.kg.reader import RelationsReader
from invoker.kg.vocab_audit import format_vocab_audit, run_vocab_audit
from invoker.kg.vocabulary import VOCABULARY_PATH
from invoker.paths import (
    PROJECT_ROOT,
    authored_dir,
    derived_patch_dir,
    manifest_file,
    relations_file,
    summary_file,
    vocabulary_notes_file,
)
from invoker.pipeline.validators import ValidationContext, validate_hero
from invoker.pipeline.writer import read_hero


class ReleaseError(ValueError):
    pass


@dataclass(frozen=True)
class ReleaseResult:
    release_dir: Path
    archive_path: Path
    hero_count: int
    relation_count: int


@dataclass(frozen=True)
class AuthoredReleaseFile:
    path: Path
    hero_id: int


def sha256_file(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def _canonical_authored_files(data_dir: Path) -> list[Path]:
    root = authored_dir(data_dir)
    if not root.exists():
        return []
    return [
        path
        for path in sorted(root.glob("*.yaml"))
        if not path.name.endswith(".draft.yaml") and not path.name.startswith("vocab-")
    ]


def _copy_file(src: Path, release_dir: Path, relative: str) -> dict[str, str]:
    dst = release_dir / relative
    dst.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(src, dst)
    return {"path": relative, "sha256": sha256_file(dst)}


def _run_git(args: list[str]) -> str | None:
    try:
        completed = subprocess.run(
            ["git", *args],
            cwd=PROJECT_ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except Exception:
        return None
    return completed.stdout.strip()


def _git_hash() -> str | None:
    return _run_git(["rev-parse", "HEAD"])


def _git_dirty() -> bool:
    status = _run_git(["status", "--porcelain"])
    return bool(status)


def _release_timestamps() -> tuple[str, str]:
    now = datetime.now(UTC).replace(microsecond=0)
    release_timestamp = now.isoformat().replace("+00:00", "Z")
    path_timestamp = now.strftime("%Y%m%dT%H%M%SZ")
    return release_timestamp, path_timestamp


def _load_game_snapshot(game_data_dir: Path | None, patch: str) -> dict[str, Any]:
    if game_data_dir is None:
        raise ReleaseError(
            "INVOKER_GAME_DATA_DIR is required for publish so release metadata can "
            "record the source game-file snapshot."
        )
    snapshot_path = game_data_dir / patch / "snapshot.json"
    if not snapshot_path.exists():
        raise ReleaseError(
            f"game-file snapshot metadata not found at {snapshot_path}; "
            f"run `uv run invoker snapshot-game-files --patch {patch} ...` first."
        )
    raw = json.loads(snapshot_path.read_text())
    if not isinstance(raw, dict):
        raise ReleaseError(f"{snapshot_path} must contain a JSON object")
    for key in ("patch", "source", "generated_at"):
        if key not in raw:
            raise ReleaseError(f"{snapshot_path} missing required metadata field {key!r}")
    if raw["patch"] != patch:
        raise ReleaseError(f"{snapshot_path} patch is {raw['patch']!r}, expected {patch!r}")
    return {
        "patch": raw["patch"],
        "source": raw["source"],
        "generated_at": raw["generated_at"],
    }


def _validate_authored(data_dir: Path) -> list[AuthoredReleaseFile]:
    files = _canonical_authored_files(data_dir)
    if not files:
        raise ReleaseError(
            f"no canonical authored hero YAML files found under {authored_dir(data_dir)}"
        )
    authored: list[AuthoredReleaseFile] = []
    for path in files:
        try:
            profile = validate_authored_file(path)
        except Exception as exc:
            raise ReleaseError(f"authored facts validation failed for {path}: {exc}") from exc
        authored.append(AuthoredReleaseFile(path=path, hero_id=profile.hero_id))
    return authored


def _validate_derived(data_dir: Path, patch: str) -> tuple[dict[str, Any], int]:
    patch_dir = derived_patch_dir(data_dir, patch)
    if not patch_dir.exists():
        raise ReleaseError(
            f"derived artifacts for patch {patch} are missing at {patch_dir}; "
            f"run `uv run invoker bootstrap --patch {patch}` first."
        )
    m_path = manifest_file(data_dir, patch)
    if not m_path.exists():
        raise ReleaseError(
            f"derived manifest missing at {m_path}; "
            f"run `uv run invoker bootstrap --patch {patch}` first."
        )
    r_path = relations_file(data_dir, patch)
    if not r_path.exists():
        raise ReleaseError(
            f"relations artifact missing at {r_path}; "
            f"run `uv run invoker bootstrap --patch {patch}` first."
        )

    manifest = json.loads(m_path.read_text())
    if not isinstance(manifest, dict):
        raise ReleaseError(f"{m_path} must contain a JSON object")
    entries = manifest.get("heroes", [])
    if not isinstance(entries, list) or not entries:
        raise ReleaseError(f"{m_path} must list at least one derived hero")
    if manifest.get("status") != "complete":
        raise ReleaseError(
            f"{m_path} status is {manifest.get('status')!r}; "
            f"run `uv run invoker bootstrap --patch {patch}` without a hero filter first."
        )

    ids = {int(entry["hero_id"]) for entry in entries}
    ctx = ValidationContext(roster_hero_ids=ids)
    for entry in entries:
        hero_id = int(entry["hero_id"])
        try:
            validate_hero(read_hero(data_dir, patch, hero_id), ctx)
        except Exception as exc:
            raise ReleaseError(f"derived validation failed for hero {hero_id}: {exc}") from exc
        s_path = summary_file(data_dir, patch, hero_id)
        if not s_path.exists():
            raise ReleaseError(
                f"summary artifact missing at {s_path}; "
                f"run `uv run invoker bootstrap --patch {patch}` first."
            )

    try:
        relations = RelationsReader.load(r_path)
    except Exception as exc:
        raise ReleaseError(f"relations validation failed for {r_path}: {exc}") from exc
    return manifest, len(relations.all())


def _validate_release_completeness(
    authored_files: list[AuthoredReleaseFile],
    manifest: dict[str, Any],
) -> None:
    authored_ids = {entry.hero_id for entry in authored_files}
    derived_ids = {int(entry["hero_id"]) for entry in manifest["heroes"]}
    if authored_ids == derived_ids:
        return

    details: list[str] = []
    missing = sorted(authored_ids - derived_ids)
    extra = sorted(derived_ids - authored_ids)
    if missing:
        details.append(f"missing derived hero ids: {missing}")
    if extra:
        details.append(f"derived hero ids without authored YAML: {extra}")
    raise ReleaseError("derived manifest does not match authored corpus; " + "; ".join(details))


def _derived_files(data_dir: Path, patch: str, manifest: dict[str, Any]) -> list[tuple[Path, str]]:
    files: list[tuple[Path, str]] = []
    for entry in sorted(manifest["heroes"], key=lambda item: int(item["hero_id"])):
        hero_id = int(entry["hero_id"])
        files.append(
            (
                derived_patch_dir(data_dir, patch) / "heroes" / f"{hero_id}.json",
                f"derived/heroes/{hero_id}.json",
            )
        )
        files.append((summary_file(data_dir, patch, hero_id), f"derived/summary_{hero_id}.md"))
    files.append((relations_file(data_dir, patch), "derived/relations.json"))
    files.append((manifest_file(data_dir, patch), "derived/manifest.json"))
    return files


def _write_reports(
    release_dir: Path,
    *,
    patch: str,
    manifest: dict[str, Any],
    relation_count: int,
    vocab_audit_text: str,
) -> None:
    reports_dir = release_dir / "reports"
    reports_dir.mkdir(parents=True, exist_ok=True)
    hero_count = len(manifest["heroes"])
    validation_text = "\n".join(
        [
            "# Release Validation",
            "",
            f"Patch: {patch}",
            "Status: pass",
            f"Heroes validated: {hero_count}/{hero_count}",
            f"Relations loaded: {relation_count}",
            "Summaries: pass",
            "",
        ]
    )
    (reports_dir / "validation.txt").write_text(validation_text)
    (reports_dir / "vocab-audit.txt").write_text(vocab_audit_text)


def create_release_bundle(
    data_dir: Path,
    patch: str,
    out_dir: Path,
    *,
    invoker_version: str,
    game_data_dir: Path | None,
    force: bool = False,
) -> ReleaseResult:
    authored_files = _validate_authored(data_dir)
    manifest, relation_count = _validate_derived(data_dir, patch)
    _validate_release_completeness(authored_files, manifest)
    game_snapshot = _load_game_snapshot(game_data_dir, patch)

    vocab_audit = run_vocab_audit(data_dir)
    vocab_audit_text = format_vocab_audit(vocab_audit)
    if not vocab_audit.passed:
        raise ReleaseError("vocab-audit found blocking errors; run `uv run invoker vocab-audit`.")

    timestamp, path_timestamp = _release_timestamps()
    release_name = f"invoker-kg-{patch}-{path_timestamp}"
    release_dir = out_dir / release_name
    archive_path = out_dir / f"{release_name}.tar.gz"

    if (release_dir.exists() or archive_path.exists()) and not force:
        raise ReleaseError(
            f"release output already exists for {release_name}; pass --force to overwrite"
        )
    if force:
        if release_dir.exists():
            shutil.rmtree(release_dir)
        if archive_path.exists():
            archive_path.unlink()

    release_dir.mkdir(parents=True, exist_ok=False)

    vocabulary_files = [
        _copy_file(VOCABULARY_PATH, release_dir, "vocabulary/vocabulary.yaml"),
        _copy_file(vocabulary_notes_file(), release_dir, "vocabulary/kg-vocabulary-notes.md"),
    ]
    authored_manifest = [
        _copy_file(entry.path, release_dir, f"authored/{entry.path.name}")
        for entry in authored_files
    ]
    derived_manifest = [
        _copy_file(src, release_dir, relative)
        for src, relative in _derived_files(data_dir, patch, manifest)
    ]
    _write_reports(
        release_dir,
        patch=patch,
        manifest=manifest,
        relation_count=relation_count,
        vocab_audit_text=vocab_audit_text,
    )

    release_json = {
        "schema_version": 1,
        "patch": patch,
        "timestamp": timestamp,
        "invoker_version": invoker_version,
        "git_hash": _git_hash(),
        "git_dirty": _git_dirty(),
        "game_snapshot": game_snapshot,
        "vocabulary": {
            "schema_version": 1,
            "files": vocabulary_files,
        },
        "authored": {
            "hero_count": len(authored_manifest),
            "files": authored_manifest,
        },
        "derived": {
            "manifest_path": "derived/manifest.json",
            "files": derived_manifest,
        },
        "checks": {
            "validate": "pass",
            "vocab_audit": {
                "status": "pass",
                "warnings_blocking": False,
            },
        },
    }
    (release_dir / "release.json").write_text(json.dumps(release_json, indent=2) + "\n")

    archive_path.parent.mkdir(parents=True, exist_ok=True)
    with tarfile.open(archive_path, "w:gz") as tar:
        tar.add(release_dir, arcname=release_dir.name)

    return ReleaseResult(
        release_dir=release_dir,
        archive_path=archive_path,
        hero_count=len(authored_manifest),
        relation_count=relation_count,
    )
