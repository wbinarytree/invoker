from __future__ import annotations

import json
import logging
import sys
from typing import Any


def configure_logging(level_name: str) -> None:
    level = getattr(logging, level_name.upper(), logging.INFO)
    logging.basicConfig(
        level=level,
        format="%(asctime)s %(levelname)s %(name)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
        stream=sys.stdout,
        force=True,
    )


def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)


def log_event(
    logger: logging.Logger,
    level: int,
    event: str,
    **fields: Any,
) -> None:
    parts = [f"event={event}"]
    for key, value in fields.items():
        parts.append(f"{key}={json.dumps(value, ensure_ascii=True, sort_keys=True)}")
    logger.log(level, " ".join(parts))
