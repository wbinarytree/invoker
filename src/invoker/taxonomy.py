from __future__ import annotations

from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

import yaml

TAXONOMY_FILE = Path(__file__).parent / "prompts" / "taxonomy.yaml"


@dataclass(frozen=True)
class TagDefinition:
    name: str
    definition: str
    examples: tuple[str, ...]


@dataclass(frozen=True)
class Taxonomy:
    version: int
    tags: dict[str, TagDefinition]

    def has(self, tag: str) -> bool:
        return tag in self.tags

    def as_prompt_block(self) -> str:
        lines = []
        for name, d in sorted(self.tags.items()):
            ex = ", ".join(d.examples)
            lines.append(f"- {name}: {d.definition} (e.g., {ex})")
        return "\n".join(lines)


@lru_cache(maxsize=1)
def load_taxonomy(path: Path = TAXONOMY_FILE) -> Taxonomy:
    raw = yaml.safe_load(path.read_text())
    tags = {
        name: TagDefinition(
            name=name,
            definition=d["definition"],
            examples=tuple(d.get("examples", [])),
        )
        for name, d in raw["tags"].items()
    }
    return Taxonomy(version=int(raw["version"]), tags=tags)
