from __future__ import annotations

import json
import shutil
import tarfile
from pathlib import Path

import pytest
import yaml

from invoker.kg.reader import write_relations
from invoker.paths import hero_file, manifest_file, relations_file
from invoker.pipeline.orchestrator import run_bootstrap
from invoker.pipeline.release import ReleaseError, create_release_bundle, sha256_file

from ...support.factories import make_relation

FIXTURE_SNAPSHOT = Path("tests/fixtures/game_snapshot/7.41b")


def _write_authored_hero(
    data_dir: Path,
    *,
    filename: str = "testhero.yaml",
    hero_id: int = 120,
    hero_slug: str = "testhero",
    localized_name: str = "Test Hero",
) -> None:
    authored = data_dir / "authored"
    authored.mkdir(parents=True, exist_ok=True)
    authored.joinpath(filename).write_text(
        yaml.safe_dump(
            {
                "hero_id": hero_id,
                "hero_slug": hero_slug,
                "localized_name": localized_name,
                "capabilities": [
                    {
                        "type": "mobility",
                        "score": 0.8,
                        "evidence": ["test evidence"],
                    }
                ],
                "requirements": [],
                "liabilities": [],
                "targets": [],
                "role_distribution": {},
                "provenance": {
                    "authored_by": "human",
                    "authored_at": "2026-04-28",
                    "assist_model": None,
                },
            },
            sort_keys=False,
        )
    )


def _write_game_snapshot(root: Path) -> Path:
    game_root = root / "game"
    shutil.copytree(FIXTURE_SNAPSHOT, game_root / "7.41b")
    return game_root


def _build_release_inputs(tmp_path: Path) -> Path:
    _write_authored_hero(tmp_path)
    run_bootstrap(tmp_path, "7.41b", "invoker@test")
    return _write_game_snapshot(tmp_path)


def test_release_metadata_shape_and_file_hashes(tmp_path: Path):
    game_root = _build_release_inputs(tmp_path)

    result = create_release_bundle(
        tmp_path,
        "7.41b",
        tmp_path / "dist",
        invoker_version="0.1.test",
        game_data_dir=game_root,
    )

    release_json = json.loads(result.release_dir.joinpath("release.json").read_text())
    assert release_json["schema_version"] == 1
    assert release_json["patch"] == "7.41b"
    assert release_json["invoker_version"] == "0.1.test"
    assert release_json["game_snapshot"] == {
        "patch": "7.41b",
        "source": "fixture",
        "generated_at": "2026-04-27T00:00:00+00:00",
    }
    assert release_json["authored"]["hero_count"] == 1
    assert release_json["derived"]["manifest_path"] == "derived/manifest.json"
    assert release_json["checks"]["validate"] == "pass"
    assert release_json["checks"]["vocab_audit"] == {
        "status": "pass",
        "warnings_blocking": False,
    }

    authored_entry = release_json["authored"]["files"][0]
    authored_path = result.release_dir / authored_entry["path"]
    assert authored_entry["sha256"] == sha256_file(authored_path)
    assert len(authored_entry["sha256"]) == 64


def test_missing_derived_artifacts_fail_before_release_creation(tmp_path: Path):
    _write_authored_hero(tmp_path)
    game_root = _write_game_snapshot(tmp_path)
    out_dir = tmp_path / "dist"

    with pytest.raises(ReleaseError, match="bootstrap"):
        create_release_bundle(
            tmp_path,
            "7.41b",
            out_dir,
            invoker_version="0.1.test",
            game_data_dir=game_root,
        )

    assert not out_dir.exists()


def test_failed_derived_validation_prevents_release_creation(tmp_path: Path):
    game_root = _build_release_inputs(tmp_path)
    out_dir = tmp_path / "dist"
    hero_path = hero_file(tmp_path, "7.41b", 120)
    raw = json.loads(hero_path.read_text())
    raw["role_distribution"] = {"mid": 0.8, "offlane": 0.4}
    hero_path.write_text(json.dumps(raw))
    manifest = json.loads(manifest_file(tmp_path, "7.41b").read_text())
    manifest["heroes"][0]["content_hash"] = f"sha256:{sha256_file(hero_path)}"
    manifest_file(tmp_path, "7.41b").write_text(json.dumps(manifest))

    with pytest.raises(ReleaseError, match="derived validation failed"):
        create_release_bundle(
            tmp_path,
            "7.41b",
            out_dir,
            invoker_version="0.1.test",
            game_data_dir=game_root,
        )

    assert not out_dir.exists()


def test_stale_manifest_hash_prevents_release_creation(tmp_path: Path):
    game_root = _build_release_inputs(tmp_path)
    out_dir = tmp_path / "dist"
    hero_path = hero_file(tmp_path, "7.41b", 120)
    raw = json.loads(hero_path.read_text())
    raw["localized_name"] = "Renamed Test Hero"
    hero_path.write_text(json.dumps(raw))

    with pytest.raises(ReleaseError, match="content_hash mismatch"):
        create_release_bundle(
            tmp_path,
            "7.41b",
            out_dir,
            invoker_version="0.1.test",
            game_data_dir=game_root,
        )

    assert not out_dir.exists()


def test_duplicate_authored_hero_ids_prevent_release_creation(tmp_path: Path):
    game_root = _build_release_inputs(tmp_path)
    _write_authored_hero(
        tmp_path,
        filename="duplicate.yaml",
        hero_id=120,
        hero_slug="duplicate",
        localized_name="Duplicate",
    )
    out_dir = tmp_path / "dist"

    with pytest.raises(ReleaseError, match="duplicate authored hero_id"):
        create_release_bundle(
            tmp_path,
            "7.41b",
            out_dir,
            invoker_version="0.1.test",
            game_data_dir=game_root,
        )

    assert not out_dir.exists()


def test_duplicate_manifest_hero_ids_prevent_release_creation(tmp_path: Path):
    game_root = _build_release_inputs(tmp_path)
    out_dir = tmp_path / "dist"
    path = manifest_file(tmp_path, "7.41b")
    raw = json.loads(path.read_text())
    raw["heroes"].append(dict(raw["heroes"][0]))
    path.write_text(json.dumps(raw))

    with pytest.raises(ReleaseError, match="duplicate hero_id"):
        create_release_bundle(
            tmp_path,
            "7.41b",
            out_dir,
            invoker_version="0.1.test",
            game_data_dir=game_root,
        )

    assert not out_dir.exists()


def test_relation_endpoints_outside_roster_prevent_release_creation(tmp_path: Path):
    game_root = _build_release_inputs(tmp_path)
    out_dir = tmp_path / "dist"
    write_relations(
        relations_file(tmp_path, "7.41b"),
        [make_relation()],
        source_patch="7.41b",
        generated_at="2026-04-28T00:00:00Z",
    )

    with pytest.raises(ReleaseError, match="outside release roster"):
        create_release_bundle(
            tmp_path,
            "7.41b",
            out_dir,
            invoker_version="0.1.test",
            game_data_dir=game_root,
        )

    assert not out_dir.exists()


def test_partial_derived_manifest_prevents_release_creation(tmp_path: Path):
    _write_authored_hero(tmp_path)
    run_bootstrap(tmp_path, "7.41b", "invoker@test", heroes={"testhero"})
    game_root = _write_game_snapshot(tmp_path)
    out_dir = tmp_path / "dist"

    with pytest.raises(ReleaseError, match="without a hero filter"):
        create_release_bundle(
            tmp_path,
            "7.41b",
            out_dir,
            invoker_version="0.1.test",
            game_data_dir=game_root,
        )

    assert not out_dir.exists()


def test_vocab_audit_warnings_do_not_prevent_release_creation(tmp_path: Path):
    game_root = _build_release_inputs(tmp_path)

    result = create_release_bundle(
        tmp_path,
        "7.41b",
        tmp_path / "dist",
        invoker_version="0.1.test",
        game_data_dir=game_root,
    )

    audit_text = result.release_dir.joinpath("reports/vocab-audit.txt").read_text()
    assert "Status: pass" in audit_text
    assert "## Terms With No Consuming Rule" in audit_text


def test_successful_release_copies_contents_and_writes_tarball(tmp_path: Path):
    game_root = _build_release_inputs(tmp_path)

    result = create_release_bundle(
        tmp_path,
        "7.41b",
        tmp_path / "dist",
        invoker_version="0.1.test",
        game_data_dir=game_root,
    )

    assert result.release_dir.joinpath("vocabulary/vocabulary.yaml").exists()
    assert result.release_dir.joinpath("vocabulary/kg-vocabulary-notes.md").exists()
    assert result.release_dir.joinpath("authored/testhero.yaml").exists()
    assert result.release_dir.joinpath("derived/heroes/120.json").exists()
    assert result.release_dir.joinpath("derived/relations.json").exists()
    assert result.release_dir.joinpath("derived/summary_120.md").exists()
    assert result.release_dir.joinpath("derived/manifest.json").exists()
    assert result.release_dir.joinpath("reports/validation.txt").exists()
    assert result.archive_path.exists()

    with tarfile.open(result.archive_path, "r:gz") as tar:
        names = set(tar.getnames())
    prefix = result.release_dir.name
    assert f"{prefix}/release.json" in names
    assert f"{prefix}/authored/testhero.yaml" in names
    assert f"{prefix}/derived/manifest.json" in names


def test_missing_game_snapshot_metadata_fails(tmp_path: Path):
    _write_authored_hero(tmp_path)
    run_bootstrap(tmp_path, "7.41b", "invoker@test")

    with pytest.raises(ReleaseError, match="snapshot"):
        create_release_bundle(
            tmp_path,
            "7.41b",
            tmp_path / "dist",
            invoker_version="0.1.test",
            game_data_dir=None,
        )
