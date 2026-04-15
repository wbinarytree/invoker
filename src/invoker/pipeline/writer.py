from __future__ import annotations

from pathlib import Path

from invoker.paths import hero_file
from invoker.schemas.derived import HeroDerived


def write_hero(data_dir: Path, patch: str, hero: HeroDerived) -> Path:
    path = hero_file(data_dir, patch, hero.hero_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(hero.model_dump_json(indent=2))
    return path


def read_hero(data_dir: Path, patch: str, hero_id: int) -> HeroDerived:
    path = hero_file(data_dir, patch, hero_id)
    return HeroDerived.model_validate_json(path.read_text())
