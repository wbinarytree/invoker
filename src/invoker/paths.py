from __future__ import annotations

from pathlib import Path


def raw_dir(data_dir: Path, source: str, patch: str) -> Path:
    return data_dir / "raw" / source / patch


def derived_patch_dir(data_dir: Path, patch: str) -> Path:
    return data_dir / "derived" / patch


def hero_file(data_dir: Path, patch: str, hero_id: int) -> Path:
    return derived_patch_dir(data_dir, patch) / "heroes" / f"{hero_id}.json"


def summary_file(data_dir: Path, patch: str, bracket: str, hero_id: int) -> Path:
    return derived_patch_dir(data_dir, patch) / "summaries" / bracket / f"{hero_id}.txt"


def manifest_file(data_dir: Path, patch: str) -> Path:
    return derived_patch_dir(data_dir, patch) / "manifest.json"


def cache_dir(data_dir: Path, patch: str) -> Path:
    return data_dir / "cache" / patch


def graph_file(data_dir: Path, patch: str) -> Path:
    return cache_dir(data_dir, patch) / "graph.pkl"


def dist_file(data_dir: Path, patch: str) -> Path:
    return data_dir.parent / "dist" / f"invoker-kb-{patch}.tar.gz"
