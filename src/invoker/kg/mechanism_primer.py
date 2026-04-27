from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

_PRIMER_DIR = Path(__file__).parent

ACTIVE_PATCH = "7.41b"


class MechanismPrimerError(ValueError):
    pass


@dataclass(frozen=True)
class MechanismPrimerContext:
    patch: str
    mechanics: list[dict[str, Any]]


def load_mechanism_primer(patch: str) -> MechanismPrimerContext:
    """Load the per-patch mechanism primer. Returns empty mechanics if no file exists."""
    path = _PRIMER_DIR / f"mechanism_primer_{patch}.yaml"
    if not path.exists():
        return MechanismPrimerContext(patch=patch, mechanics=[])
    raw = yaml.safe_load(path.read_text()) or {}
    mechanics = raw.get("mechanics", [])
    if not isinstance(mechanics, list):
        raise MechanismPrimerError(f"{path}: 'mechanics' must be a list")
    for i, entry in enumerate(mechanics):
        if not isinstance(entry, dict):
            raise MechanismPrimerError(f"{path}: mechanics[{i}] must be a mapping")
        if "stat" not in entry:
            raise MechanismPrimerError(f"{path}: mechanics[{i}] missing required key 'stat'")
        if "contributions" not in entry:
            raise MechanismPrimerError(
                f"{path}: mechanics[{i}] missing required key 'contributions'"
            )
        if not isinstance(entry["contributions"], list):
            raise MechanismPrimerError(f"{path}: mechanics[{i}].contributions must be a list")
    return MechanismPrimerContext(
        patch=str(raw.get("patch", patch)),
        mechanics=mechanics,
    )


def load_active_mechanism_primer() -> MechanismPrimerContext:
    return load_mechanism_primer(ACTIVE_PATCH)
