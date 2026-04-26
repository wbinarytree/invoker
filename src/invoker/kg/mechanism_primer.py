from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from typing import Any

import yaml

_PRIMER_DIR = Path(__file__).parent


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
    return MechanismPrimerContext(
        patch=str(raw.get("patch", patch)),
        mechanics=list(raw.get("mechanics", [])),
    )
