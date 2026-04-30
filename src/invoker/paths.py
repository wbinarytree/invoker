from __future__ import annotations

from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]


def docs_dir() -> Path:
    return PROJECT_ROOT / "docs"


def vocabulary_notes_file() -> Path:
    return docs_dir() / "specs" / "kg-vocabulary-notes.md"


def authored_dir(data_dir: Path) -> Path:
    return data_dir / "authored"


def vocab_gaps_file(data_dir: Path) -> Path:
    return authored_dir(data_dir) / "vocab-gaps.yaml"


def vocab_gap_review_file(data_dir: Path) -> Path:
    return authored_dir(data_dir) / "vocab-gap-review.yaml"


def vocab_gap_review_log_file(data_dir: Path) -> Path:
    return authored_dir(data_dir) / "vocab-gap-review-log.jsonl"


def vocab_review_file(data_dir: Path) -> Path:
    return authored_dir(data_dir) / "vocab-review.yaml"


def vocab_review_log_file(data_dir: Path) -> Path:
    return authored_dir(data_dir) / "vocab-review-log.jsonl"


def vocab_proposals_file(data_dir: Path) -> Path:
    return authored_dir(data_dir) / "vocab-proposals.yaml"


def team_registry_file(data_dir: Path) -> Path:
    return authored_dir(data_dir) / "teams.yaml"


def raw_dir(data_dir: Path, source: str, patch: str) -> Path:
    return data_dir / "raw" / source / patch


def derived_patch_dir(data_dir: Path, patch: str) -> Path:
    return data_dir / "derived" / patch


def hero_file(data_dir: Path, patch: str, hero_id: int) -> Path:
    return derived_patch_dir(data_dir, patch) / "heroes" / f"{hero_id}.json"


def relations_file(data_dir: Path, patch: str) -> Path:
    return derived_patch_dir(data_dir, patch) / "relations.json"


def summary_file(data_dir: Path, patch: str, hero_id: int) -> Path:
    return derived_patch_dir(data_dir, patch) / f"summary_{hero_id}.md"


def manifest_file(data_dir: Path, patch: str) -> Path:
    return derived_patch_dir(data_dir, patch) / "manifest.json"


def teams_dir(data_dir: Path, patch: str) -> Path:
    return derived_patch_dir(data_dir, patch) / "teams"


def team_index_file(data_dir: Path, patch: str) -> Path:
    return teams_dir(data_dir, patch) / "index.json"


def team_profile_file(data_dir: Path, patch: str, team_id: int, roster_hash: str) -> Path:
    return teams_dir(data_dir, patch) / str(team_id) / roster_hash / "profile.json"


def cache_dir(data_dir: Path, patch: str) -> Path:
    return data_dir / "cache" / "graph" / patch


def graph_file(data_dir: Path, patch: str) -> Path:
    return cache_dir(data_dir, patch) / "graph.pkl"


def llm_cache_dir(data_dir: Path) -> Path:
    return data_dir / "cache" / "llm"


def dist_file(data_dir: Path, patch: str) -> Path:
    return data_dir.parent / "dist" / f"invoker-kb-{patch}.tar.gz"
