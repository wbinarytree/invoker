from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class Config:
    stratz_token: str | None
    data_dir: Path
    game_data_dir: Path | None
    log_level: str
    dev_heroes: frozenset[str] | None  # name or numeric-id tokens; None = no filter

    @classmethod
    def load(cls) -> Config:
        load_dotenv()
        data_dir = Path(os.environ.get("INVOKER_DATA_DIR", "data"))
        if not data_dir.is_absolute():
            data_dir = PROJECT_ROOT / data_dir
        game_data_dir_raw = os.environ.get("INVOKER_GAME_DATA_DIR") or None
        game_data_dir = Path(game_data_dir_raw) if game_data_dir_raw else None
        if game_data_dir is not None and not game_data_dir.is_absolute():
            game_data_dir = PROJECT_ROOT / game_data_dir
        raw_dev = os.environ.get("INVOKER_DEV_HEROES") or None
        dev_heroes = (
            frozenset(t.strip() for t in raw_dev.split(",") if t.strip())
            if raw_dev
            else None
        )
        return cls(
            stratz_token=os.environ.get("STRATZ_API_TOKEN") or None,
            data_dir=data_dir,
            game_data_dir=game_data_dir,
            log_level=os.environ.get("INVOKER_LOG_LEVEL", "INFO"),
            dev_heroes=dev_heroes,
        )
