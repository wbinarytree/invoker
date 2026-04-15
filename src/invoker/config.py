from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class Config:
    stratz_token: str | None
    google_api_key: str | None
    data_dir: Path
    llm_client: str
    log_level: str

    @classmethod
    def load(cls) -> Config:
        load_dotenv()
        data_dir = Path(os.environ.get("INVOKER_DATA_DIR", "data"))
        if not data_dir.is_absolute():
            data_dir = PROJECT_ROOT / data_dir
        return cls(
            stratz_token=os.environ.get("STRATZ_API_TOKEN") or None,
            google_api_key=os.environ.get("GOOGLE_API_KEY") or None,
            data_dir=data_dir,
            llm_client=os.environ.get("INVOKER_LLM_CLIENT", "gemini"),
            log_level=os.environ.get("INVOKER_LOG_LEVEL", "INFO"),
        )
