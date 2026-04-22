from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass, field
from datetime import UTC, datetime
from pathlib import Path

from invoker.paths import hero_file, manifest_file


@dataclass
class HeroManifestEntry:
    hero_id: int
    content_hash: str


@dataclass
class Manifest:
    schema_version: int
    patch: str
    generated_at: str
    status: str  # "partial" | "complete"
    heroes: list[HeroManifestEntry] = field(default_factory=list)


def _sha256_file(p: Path) -> str:
    return "sha256:" + hashlib.sha256(p.read_bytes()).hexdigest()


def build_manifest(
    data_dir: Path,
    patch: str,
    hero_ids: list[int],
    complete: bool,
) -> Manifest:
    entries: list[HeroManifestEntry] = []
    for hid in hero_ids:
        p = hero_file(data_dir, patch, hid)
        if not p.exists():
            continue
        entries.append(
            HeroManifestEntry(
                hero_id=hid,
                content_hash=_sha256_file(p),
            )
        )
    return Manifest(
        schema_version=1,
        patch=patch,
        generated_at=datetime.now(UTC).isoformat(timespec="seconds"),
        status="complete" if complete else "partial",
        heroes=entries,
    )


def write_manifest(data_dir: Path, manifest: Manifest) -> Path:
    path = manifest_file(data_dir, manifest.patch)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(asdict(manifest), indent=2))
    return path
