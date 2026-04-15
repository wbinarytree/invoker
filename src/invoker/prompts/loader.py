from __future__ import annotations

import hashlib
import re
from dataclasses import dataclass
from functools import lru_cache
from pathlib import Path

PROMPTS_DIR = Path(__file__).parent

VERSION_RE = re.compile(r"<!--\s*prompt_version:\s*(\d+)\s*-->")


@dataclass(frozen=True)
class Prompt:
    name: str
    text: str
    version: int
    sha256: str

    def render(self, **kwargs: str) -> str:
        out = self.text
        for k, v in kwargs.items():
            out = out.replace("{" + k + "}", v)
        return out


@lru_cache(maxsize=32)
def load(name: str) -> Prompt:
    path = PROMPTS_DIR / f"{name}.md"
    text = path.read_text()
    m = VERSION_RE.search(text)
    if not m:
        raise ValueError(f"prompt {name} missing <!-- prompt_version: N --> header")
    return Prompt(
        name=name,
        text=text,
        version=int(m.group(1)),
        sha256=hashlib.sha256(text.encode()).hexdigest(),
    )
