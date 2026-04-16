# Invoker Phase 1 — Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use `superpowers:subagent-driven-development` (recommended) or `superpowers:executing-plans` to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

> **Workflow note:** This project does **not** follow TDD. Tasks are structured as implement → test → commit. Tests are required for behavior that matters (validators, schema compat, query API); tests are *not* required for trivial plumbing. See `CLAUDE.md`.

**Goal:** Build the Phase 1 Invoker knowledge pipeline: fetch Dota 2 data from OpenDota / STRATZ / Liquipedia, extract mechanical tags via LLM with provenance, derive pro-bracket statistical layer, emit per-hero JSON + LLM-injectable summaries, ship a NetworkX graph and an internal reader API.

**Architecture:** A fresh clone has zero data. `invoker bootstrap --patch <v>` runs seven idempotent phases (fetch → validate-raw → extract → reason → derive → summarize → manifest → index) that cache aggressively and short-circuit on unchanged inputs. JSON under `data/derived/<patch>/` is the source of truth; NetworkX cache and internal reader are derived from JSON.

**Tech Stack:** Python 3.11+, `uv`, `ruff`, `pyright`, `httpx`, `pydantic` v2, `networkx`, `google-generativeai`, `typer`, `pyyaml`, `pytest`.

**Spec:** `docs/specs/2026-04-14-invoker-architecture-design.md`

---

## File Structure

Created during Phase 1:

```
pyproject.toml
.env.example
src/invoker/
  __init__.py
  config.py                      # env loading, source-of-truth for all settings
  cli.py                         # Typer entrypoint
  paths.py                       # canonical path helpers (data/raw/..., data/derived/..., etc.)
  taxonomy.py                    # loads + validates taxonomy.yaml
  http/
    __init__.py
    client.py                    # rate-limited httpx client + file cache
    ratelimit.py                 # token bucket
  sources/
    __init__.py
    opendota.py                  # OpenDota fetcher
    stratz.py                    # STRATZ GraphQL fetcher
    liquipedia.py                # Liquipedia MediaWiki fetcher
  schemas/
    __init__.py
    raw.py                       # pydantic models for raw responses
    derived.py                   # pydantic models for derived per-hero files
  llm/
    __init__.py
    client.py                    # LLMClient Protocol
    gemini.py                    # GeminiClient
    manual.py                    # ManualClient (file-based paste workflow)
  prompts/
    __init__.py
    loader.py                    # prompt file loading + hashing
    taxonomy.yaml                # closed tag taxonomy (seed)
    extract_mechanical_tags.md
    synergy_reason.md
    counter_reason.md
  pipeline/
    __init__.py
    fetch.py                     # orchestrates source fetchers
    extract.py                   # mechanical extraction
    reason.py                    # synergy/counter reasons
    derive.py                    # statistical rollup (pro bracket)
    summarize.py                 # .txt generator
    manifest.py                  # manifest writer
    validators.py                # derived-side validators
  graph/
    __init__.py
    builder.py                   # NetworkX graph from derived files
  kb.py                          # public KnowledgeBase reader API
tests/
  fixtures/
    opendota/                    # recorded responses
    stratz/
    liquipedia/
    gold/                        # 15–20 hand-labeled heroes for regression
  test_http.py
  test_opendota.py
  test_stratz.py
  test_liquipedia.py
  test_taxonomy.py
  test_validators.py
  test_extract.py
  test_reason.py
  test_derive.py
  test_graph.py
  test_kb.py
  test_bootstrap_smoke.py
```

Files *not* in this list (team/player/archetype/vector) are explicitly deferred.

---

## Task 1: Project scaffolding

**Files:**
- Create: `pyproject.toml`, `.env.example`, `src/invoker/__init__.py`, `src/invoker/cli.py`, `src/invoker/config.py`, `src/invoker/paths.py`
- Create: `tests/__init__.py`

- [ ] **Step 1: Init uv project and deps**

```bash
cd /Users/yaoda/Projects/invoker
uv init --package invoker --python 3.11
uv add httpx pydantic networkx google-generativeai typer pyyaml "beautifulsoup4>=4.12"
uv add --dev pytest pytest-asyncio ruff pyright
```

- [ ] **Step 2: Write `pyproject.toml` tool config**

Append to `pyproject.toml`:

```toml
[tool.ruff]
line-length = 100
target-version = "py311"

[tool.ruff.lint]
select = ["E", "F", "W", "I", "N", "UP", "B", "SIM"]

[tool.pyright]
include = ["src", "tests"]
pythonVersion = "3.11"
typeCheckingMode = "basic"

[tool.pytest.ini_options]
testpaths = ["tests"]
addopts = "-ra --strict-markers"
asyncio_mode = "auto"
```

- [ ] **Step 3: Write `.env.example`**

```
# Invoker environment template. Copy to .env and fill in.

# Required for STRATZ GraphQL access. Phase 1 runs without it (thinner pro coverage).
STRATZ_API_TOKEN=

# Required for Gemini extraction (free tier is fine).
GOOGLE_API_KEY=

# Optional overrides
INVOKER_DATA_DIR=data
INVOKER_LLM_CLIENT=gemini           # gemini | manual | anthropic | openai
INVOKER_LOG_LEVEL=INFO
```

- [ ] **Step 4: Write `src/invoker/config.py`**

```python
from __future__ import annotations

import os
from dataclasses import dataclass
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parents[2]


@dataclass(frozen=True)
class Config:
    stratz_token: str | None
    google_api_key: str | None
    data_dir: Path
    llm_client: str
    log_level: str

    @classmethod
    def load(cls) -> "Config":
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
```

- [ ] **Step 5: Write `src/invoker/paths.py`**

```python
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
```

- [ ] **Step 6: Write `src/invoker/cli.py`**

```python
from __future__ import annotations

import typer

app = typer.Typer(help="Invoker — Dota 2 knowledge framework")


@app.command()
def version() -> None:
    """Print Invoker version."""
    from invoker import __version__
    typer.echo(f"invoker {__version__}")


if __name__ == "__main__":
    app()
```

- [ ] **Step 7: Write `src/invoker/__init__.py`**

```python
__version__ = "0.1.0"
```

- [ ] **Step 8: Verify**

```bash
uv run invoker version
uv run ruff check src tests
uv run pyright
```

Expected: prints `invoker 0.1.0`; ruff and pyright clean.

- [ ] **Step 9: Commit**

```bash
git add pyproject.toml uv.lock .env.example src tests
git commit -m "feat: scaffold Python project with CLI stub"
```

---

## Task 2: Tag taxonomy

**Files:**
- Create: `src/invoker/prompts/taxonomy.yaml`, `src/invoker/taxonomy.py`
- Test: `tests/test_taxonomy.py`

- [ ] **Step 1: Seed `src/invoker/prompts/taxonomy.yaml`**

Starter set of ~40 tags with quantitative thresholds. This file is the controlled vocabulary for mechanical extraction.

```yaml
# Taxonomy version. Bump on any structural change.
version: 1

tags:
  # Damage archetypes
  big_burst:
    definition: "Single-cast magical damage window ≥200 at max level, or combo ≥400 within 2s."
    examples: [Lina, Lion, Zeus]
  sustained_magical:
    definition: "Continuous magical DPS over ≥3s per cast window."
    examples: [Zeus, Jakiro]
  physical_carry:
    definition: "Late-game right-click carry with scaling physical damage."
    examples: ["Phantom Assassin", Juggernaut]

  # Disable
  single_target_disable:
    definition: "Single-target hard disable (stun/hex/sleep) ≥1.2s."
    examples: [Lion, Bane]
  aoe_disable:
    definition: "Area hard disable ≥1.0s hitting ≥2 heroes reliably."
    examples: [Magnus, Tidehunter]
  long_disable:
    definition: "Single-target hard disable ≥3.0s at any level."
    examples: [Bane, Shadow Shaman]

  # Amplifiers / utility
  armor_reduction:
    definition: "Reduces enemy armor by ≥6 via debuff or passive for ≥10s."
    examples: [Slardar, Dazzle]
  physical_damage_amplifier:
    definition: "Increases physical damage taken on target or dealt by ally."
    examples: [Slardar, Chen]
  magic_amplifier:
    definition: "Increases magic damage taken on target."
    examples: [Veno, "Ancient Apparition"]
  silence:
    definition: "Prevents spellcasting for ≥2s."
    examples: [Silencer, Drow]

  # Mobility
  blink:
    definition: "Built-in short-range teleport or dash on ≤18s cooldown."
    examples: [AM, QOP]
  global_presence:
    definition: "Map-wide ability (teleport, ult, or passive) influencing any lane."
    examples: [Zeus, Spectre, Io]

  # Initiation / saves
  initiation:
    definition: "Engages fights via blink/charge/teleport with follow-up disable."
    examples: [Magnus, Tidehunter, Slardar]
  save:
    definition: "Targeted ally protection (shield / dispel / invuln) on ≤40s cooldown."
    examples: [Dazzle, Oracle, Io]

  # Sustain / push
  sustain:
    definition: "Ally healing or regen throughput ≥60 HP/s at max level."
    examples: [Dazzle, Omni, Io]
  siege:
    definition: "Objective damage via splash, mini-stuns, or ranged AoE."
    examples: [Leshrac, "Death Prophet"]
  pusher:
    definition: "Fast creep-wave clear leading to ≥1-tower advantage in lane."
    examples: ["Death Prophet", Leshrac]

  # Vision / control
  vision_control:
    definition: "Grants vision or True Sight via ability, passive, or summon."
    examples: [Slardar, "Bounty Hunter", Zeus]
  summons:
    definition: "Controllable units with combat utility beyond hero itself."
    examples: ["Lone Druid", Meepo, Beastmaster]

  # Defensive
  magic_immunity_source:
    definition: "Grants allies or self spell immunity / high magic resistance."
    examples: [AA, Juggernaut]
  evasion:
    definition: "Passive or active physical evasion ≥30%."
    examples: [PA, Riki]
  high_base_armor:
    definition: "Base armor ≥5 at level 1 with natural tankiness."
    examples: [Timbersaw, Centaur]

  # Economy / scaling
  tempo:
    definition: "Mid-game spike windows where hero out-paces opponents 15–30 min."
    examples: [Storm, QOP]
  late_game_scaling:
    definition: "Significant power per minute after 40:00 via stacks or items."
    examples: [Medusa, Spectre]
  farming_acceleration:
    definition: "Self-farm acceleration via split-push, jungle, or ranged clear."
    examples: [AM, Sven]

  # More as we iterate
```

- [ ] **Step 2: Write `src/invoker/taxonomy.py`**

```python
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
        name: TagDefinition(name=name, definition=d["definition"], examples=tuple(d.get("examples", [])))
        for name, d in raw["tags"].items()
    }
    return Taxonomy(version=int(raw["version"]), tags=tags)
```

- [ ] **Step 3: Write `tests/test_taxonomy.py`**

```python
from invoker.taxonomy import load_taxonomy


def test_taxonomy_loads():
    t = load_taxonomy()
    assert t.version >= 1
    assert t.has("armor_reduction")
    assert "Corrosive" not in t.as_prompt_block()  # taxonomy is generic, no hero specifics beyond examples


def test_taxonomy_has_minimum_coverage():
    t = load_taxonomy()
    required = {"single_target_disable", "armor_reduction", "initiation", "save", "sustain"}
    assert required <= set(t.tags)
```

- [ ] **Step 4: Run**

```bash
uv run pytest tests/test_taxonomy.py -v
```

Expected: both tests pass.

- [ ] **Step 5: Commit**

```bash
git add src/invoker/prompts/taxonomy.yaml src/invoker/taxonomy.py tests/test_taxonomy.py
git commit -m "feat: add closed tag taxonomy with loader"
```

---

## Task 3: Rate-limited HTTP client with file cache

**Files:**
- Create: `src/invoker/http/__init__.py`, `src/invoker/http/ratelimit.py`, `src/invoker/http/client.py`
- Test: `tests/test_http.py`

- [ ] **Step 1: Write `src/invoker/http/ratelimit.py`**

```python
from __future__ import annotations

import asyncio
import time
from dataclasses import dataclass, field


@dataclass
class TokenBucket:
    """Simple token bucket. Refills continuously at `rate` tokens per second."""
    rate: float
    capacity: float
    _tokens: float = field(init=False)
    _last: float = field(init=False)

    def __post_init__(self) -> None:
        self._tokens = self.capacity
        self._last = time.monotonic()

    async def acquire(self, amount: float = 1.0) -> None:
        while True:
            now = time.monotonic()
            elapsed = now - self._last
            self._tokens = min(self.capacity, self._tokens + elapsed * self.rate)
            self._last = now
            if self._tokens >= amount:
                self._tokens -= amount
                return
            deficit = amount - self._tokens
            await asyncio.sleep(deficit / self.rate)
```

- [ ] **Step 2: Write `src/invoker/http/client.py`**

```python
from __future__ import annotations

import hashlib
import json
from dataclasses import dataclass
from pathlib import Path
from typing import Any

import httpx

from invoker.http.ratelimit import TokenBucket


@dataclass
class SourceLimits:
    """Declared rate caps per source. Per-minute is the narrower gate for us."""
    name: str
    per_minute: int
    per_day: int | None = None


OPENDOTA = SourceLimits("opendota", per_minute=60, per_day=3000)
STRATZ = SourceLimits("stratz", per_minute=250, per_day=10_000)
LIQUIPEDIA = SourceLimits("liquipedia", per_minute=30)  # ≤0.5/sec, polite


def _cache_key(method: str, url: str, params: dict[str, Any] | None, body: Any) -> str:
    blob = json.dumps(
        {"m": method, "u": url, "p": params or {}, "b": body}, sort_keys=True
    ).encode()
    return hashlib.sha256(blob).hexdigest()[:16]


class CachedClient:
    """
    httpx-based client with a per-source token bucket and on-disk cache
    keyed on (source, method, url, params, body).
    """

    def __init__(
        self,
        source: SourceLimits,
        cache_root: Path,
        patch: str,
        headers: dict[str, str] | None = None,
        timeout: float = 30.0,
    ) -> None:
        self.source = source
        self.cache_root = cache_root / source.name / patch
        self.cache_root.mkdir(parents=True, exist_ok=True)
        self.bucket = TokenBucket(rate=source.per_minute / 60.0, capacity=source.per_minute)
        self._client = httpx.AsyncClient(headers=headers or {}, timeout=timeout)

    async def close(self) -> None:
        await self._client.aclose()

    async def get(self, url: str, params: dict[str, Any] | None = None, *, force: bool = False) -> Any:
        return await self._request("GET", url, params=params, body=None, force=force)

    async def post(self, url: str, body: Any, *, force: bool = False) -> Any:
        return await self._request("POST", url, params=None, body=body, force=force)

    async def _request(
        self,
        method: str,
        url: str,
        *,
        params: dict[str, Any] | None,
        body: Any,
        force: bool,
    ) -> Any:
        key = _cache_key(method, url, params, body)
        cache_path = self.cache_root / f"{key}.json"
        if not force and cache_path.exists():
            return json.loads(cache_path.read_text())

        await self.bucket.acquire()
        r = await self._client.request(method, url, params=params, json=body)
        r.raise_for_status()
        payload = r.json()
        cache_path.write_text(json.dumps(payload, ensure_ascii=False))
        return payload
```

- [ ] **Step 3: Write `src/invoker/http/__init__.py`**

```python
from invoker.http.client import CachedClient, LIQUIPEDIA, OPENDOTA, STRATZ, SourceLimits
from invoker.http.ratelimit import TokenBucket

__all__ = ["CachedClient", "LIQUIPEDIA", "OPENDOTA", "STRATZ", "SourceLimits", "TokenBucket"]
```

- [ ] **Step 4: Write `tests/test_http.py`**

```python
import asyncio
import time

import pytest

from invoker.http.ratelimit import TokenBucket


@pytest.mark.asyncio
async def test_bucket_paces_calls():
    bucket = TokenBucket(rate=10, capacity=2)  # 10/sec, burst of 2
    start = time.monotonic()
    for _ in range(5):
        await bucket.acquire()
    elapsed = time.monotonic() - start
    # 2 free, then 3 paced at 10/sec = at least 0.3s
    assert elapsed >= 0.25
```

- [ ] **Step 5: Run**

```bash
uv run pytest tests/test_http.py -v
```

Expected: pass.

- [ ] **Step 6: Commit**

```bash
git add src/invoker/http tests/test_http.py
git commit -m "feat: rate-limited HTTP client with file cache"
```

---

## Task 4: OpenDota fetcher

**Files:**
- Create: `src/invoker/sources/__init__.py`, `src/invoker/sources/opendota.py`
- Test: `tests/test_opendota.py`, `tests/fixtures/opendota/heroes.json` (hand-trimmed sample)

- [ ] **Step 1: Write `src/invoker/sources/opendota.py`**

```python
from __future__ import annotations

from pathlib import Path
from typing import Any

from invoker.http import OPENDOTA, CachedClient

BASE = "https://api.opendota.com/api"


class OpenDotaFetcher:
    def __init__(self, cache_root: Path, patch: str) -> None:
        self.client = CachedClient(OPENDOTA, cache_root, patch)

    async def heroes(self) -> list[dict[str, Any]]:
        """Full hero list with base stats and roles."""
        return await self.client.get(f"{BASE}/heroes")

    async def abilities(self) -> dict[str, Any]:
        """All ability descriptions keyed by internal name."""
        return await self.client.get(f"{BASE}/constants/abilities")

    async def hero_abilities_map(self) -> dict[str, Any]:
        """Maps hero internal name → list of ability internal names."""
        return await self.client.get(f"{BASE}/constants/hero_abilities")

    async def matchups(self, hero_id: int) -> list[dict[str, Any]]:
        return await self.client.get(f"{BASE}/heroes/{hero_id}/matchups")

    async def pro_matches(self, less_than_match_id: int | None = None) -> list[dict[str, Any]]:
        params = {}
        if less_than_match_id is not None:
            params["less_than_match_id"] = less_than_match_id
        return await self.client.get(f"{BASE}/proMatches", params=params or None)

    async def close(self) -> None:
        await self.client.close()
```

- [ ] **Step 2: Record a fixture**

Save a trimmed `/heroes` response (first 3 heroes, all fields) to `tests/fixtures/opendota/heroes.json`. Trim by hand; do not commit the full response.

- [ ] **Step 3: Write `tests/test_opendota.py`**

```python
import json
from pathlib import Path

FIXTURE = Path(__file__).parent / "fixtures" / "opendota" / "heroes.json"


def test_heroes_fixture_shape():
    data = json.loads(FIXTURE.read_text())
    assert isinstance(data, list)
    assert len(data) >= 3
    h = data[0]
    for key in ("id", "localized_name", "name", "primary_attr", "roles"):
        assert key in h, f"missing {key}"
```

(Integration against live OpenDota is optional — omit unless you want a `@pytest.mark.live` suite.)

- [ ] **Step 4: Run**

```bash
uv run pytest tests/test_opendota.py -v
```

Expected: pass.

- [ ] **Step 5: Commit**

```bash
git add src/invoker/sources tests/test_opendota.py tests/fixtures/opendota
git commit -m "feat: OpenDota fetcher with cached endpoints"
```

---

## Task 5: STRATZ fetcher

**Files:**
- Create: `src/invoker/sources/stratz.py`
- Test: `tests/test_stratz.py`

- [ ] **Step 1: Write `src/invoker/sources/stratz.py`**

```python
from __future__ import annotations

from pathlib import Path
from typing import Any

from invoker.http import STRATZ, CachedClient

ENDPOINT = "https://api.stratz.com/graphql"


SYNERGY_QUERY = """
query HeroSynergy($heroId: Short!, $bracket: [RankBracketBasicEnum!], $isTournament: Boolean) {
  heroStats {
    heroVsHeroMatchup(heroId: $heroId, bracketBasicIds: $bracket, isTournament: $isTournament) {
      advantage { heroId1 heroId2 synergy winsAverage matchCount }
      disadvantage { heroId1 heroId2 synergy winsAverage matchCount }
    }
  }
}
"""


class StratzFetcher:
    def __init__(self, cache_root: Path, patch: str, token: str | None) -> None:
        headers = {"Authorization": f"Bearer {token}"} if token else {}
        self.client = CachedClient(STRATZ, cache_root, patch, headers=headers)
        self.available = token is not None

    async def synergies(self, hero_id: int, *, tournament: bool = True) -> dict[str, Any] | None:
        if not self.available:
            return None
        payload = {
            "query": SYNERGY_QUERY,
            "variables": {"heroId": hero_id, "isTournament": tournament},
        }
        return await self.client.post(ENDPOINT, body=payload)

    async def close(self) -> None:
        await self.client.close()
```

> **Note on GraphQL schema:** the exact field names / enum values above may need minor adjustment against the current STRATZ schema. Adjust on first real-token test run; the caching layer means no wasted requests.

- [ ] **Step 2: Write `tests/test_stratz.py`**

```python
import asyncio
from pathlib import Path

from invoker.sources.stratz import StratzFetcher


def test_missing_token_returns_none(tmp_path: Path):
    fetcher = StratzFetcher(cache_root=tmp_path, patch="test", token=None)
    result = asyncio.run(fetcher.synergies(28))
    assert result is None
    asyncio.run(fetcher.close())
```

- [ ] **Step 3: Run**

```bash
uv run pytest tests/test_stratz.py -v
```

Expected: pass.

- [ ] **Step 4: Commit**

```bash
git add src/invoker/sources/stratz.py tests/test_stratz.py
git commit -m "feat: STRATZ GraphQL fetcher with no-token fallback"
```

---

## Task 6: Liquipedia fetcher

**Files:**
- Create: `src/invoker/sources/liquipedia.py`
- Test: `tests/test_liquipedia.py`, `tests/fixtures/liquipedia/slardar.json` (one recorded page)

- [ ] **Step 1: Write `src/invoker/sources/liquipedia.py`**

```python
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from bs4 import BeautifulSoup

from invoker.http import LIQUIPEDIA, CachedClient

API = "https://liquipedia.net/dota2/api.php"
USER_AGENT = "InvokerKnowledgeBase/0.1 (contact: https://github.com/wbinarytree/invoker)"


class LiquipediaFetcher:
    def __init__(self, cache_root: Path, patch: str) -> None:
        self.client = CachedClient(
            LIQUIPEDIA, cache_root, patch, headers={"User-Agent": USER_AGENT}
        )

    async def hero_page(self, hero_name: str) -> dict[str, Any]:
        """Return the parsed page payload for a hero."""
        return await self.client.get(
            API,
            params={
                "action": "parse",
                "page": hero_name,
                "format": "json",
                "prop": "text|wikitext",
            },
        )

    @staticmethod
    def extract_roles(page: dict[str, Any]) -> list[str]:
        """Extract the Liquipedia-curated role labels from the parsed HTML."""
        html = page.get("parse", {}).get("text", {}).get("*", "")
        if not html:
            return []
        soup = BeautifulSoup(html, "html.parser")
        roles: list[str] = []
        # Role row lives in the hero infobox. Look for the label cell then grab sibling links.
        for cell in soup.find_all(["th", "td"]):
            if cell.get_text(strip=True).lower() in {"role", "roles"}:
                nxt = cell.find_next_sibling("td") or cell.find_next("td")
                if nxt:
                    for a in nxt.find_all("a"):
                        text = a.get_text(strip=True)
                        if text and text not in roles:
                            roles.append(text)
                    if roles:
                        break
        return roles

    @staticmethod
    def extract_abilities(page: dict[str, Any]) -> list[dict[str, str]]:
        """Extract ability names + first paragraph of their descriptions."""
        html = page.get("parse", {}).get("text", {}).get("*", "")
        if not html:
            return []
        soup = BeautifulSoup(html, "html.parser")
        abilities: list[dict[str, str]] = []
        # Ability blocks follow a consistent header pattern. Minimal heuristic for Phase 1.
        for header in soup.find_all(["h3", "h4"]):
            name = header.get_text(strip=True)
            if not name or "ability" in name.lower() or "talent" in name.lower():
                continue
            desc_el = header.find_next("p")
            if desc_el and desc_el.get_text(strip=True):
                abilities.append({"name": name, "text": re.sub(r"\s+", " ", desc_el.get_text()).strip()})
        return abilities

    async def close(self) -> None:
        await self.client.close()
```

> **Parser caveat:** MediaWiki HTML is messy and Liquipedia's template markup evolves. The role/ability extractors are first-pass heuristics; expect to refine them against real fixtures. Keep failures observable (empty list, not exception) so bootstrap degrades gracefully.

- [ ] **Step 2: Record a fixture**

Fetch Slardar's page once (manually or via a throwaway script), save the JSON payload to `tests/fixtures/liquipedia/slardar.json`. Trim the embedded HTML to the infobox + ability sections.

- [ ] **Step 3: Write `tests/test_liquipedia.py`**

```python
import json
from pathlib import Path

from invoker.sources.liquipedia import LiquipediaFetcher

FIXTURE = Path(__file__).parent / "fixtures" / "liquipedia" / "slardar.json"


def test_extract_roles():
    page = json.loads(FIXTURE.read_text())
    roles = LiquipediaFetcher.extract_roles(page)
    assert "Initiator" in roles or "Disabler" in roles, f"expected role labels, got {roles}"


def test_extract_abilities_non_empty():
    page = json.loads(FIXTURE.read_text())
    abilities = LiquipediaFetcher.extract_abilities(page)
    assert abilities, "expected at least one ability parsed"
    assert all("name" in a and "text" in a for a in abilities)
```

- [ ] **Step 4: Run**

```bash
uv run pytest tests/test_liquipedia.py -v
```

Iterate the parser until green. If the fixture HTML format surprises you, refactor both the parser and the fixture together.

- [ ] **Step 5: Commit**

```bash
git add src/invoker/sources/liquipedia.py tests/test_liquipedia.py tests/fixtures/liquipedia
git commit -m "feat: Liquipedia fetcher with role and ability extractors"
```

---

## Task 7: Raw-layer pydantic models

**Files:**
- Create: `src/invoker/schemas/__init__.py`, `src/invoker/schemas/raw.py`

- [ ] **Step 1: Write `src/invoker/schemas/raw.py`**

Models covering the shapes Phase 1 depends on. Use `extra="ignore"` because upstream responses carry more fields than we care about.

```python
from __future__ import annotations

from pydantic import BaseModel, ConfigDict, Field


class ODHero(BaseModel):
    model_config = ConfigDict(extra="ignore")
    id: int
    name: str
    localized_name: str
    primary_attr: str
    attack_type: str
    roles: list[str] = Field(default_factory=list)


class ODMatchup(BaseModel):
    model_config = ConfigDict(extra="ignore")
    hero_id: int
    games_played: int
    wins: int


class ODProMatch(BaseModel):
    model_config = ConfigDict(extra="ignore")
    match_id: int
    radiant_team_id: int | None = None
    dire_team_id: int | None = None
    radiant_win: bool | None = None
    start_time: int | None = None
    patch: int | None = None
    picks_bans: list[dict] | None = None


class ODAbility(BaseModel):
    model_config = ConfigDict(extra="ignore")
    dname: str | None = None
    behavior: str | list[str] | None = None
    desc: str | None = None
    attrib: list[dict] | None = None


class StratzSynergyEdge(BaseModel):
    model_config = ConfigDict(extra="ignore")
    heroId1: int
    heroId2: int
    synergy: float
    winsAverage: float | None = None
    matchCount: int


class LiquipediaAbility(BaseModel):
    model_config = ConfigDict(extra="ignore")
    name: str
    text: str
```

- [ ] **Step 2: Write `src/invoker/schemas/__init__.py`**

```python
from invoker.schemas.raw import (
    LiquipediaAbility,
    ODAbility,
    ODHero,
    ODMatchup,
    ODProMatch,
    StratzSynergyEdge,
)

__all__ = [
    "LiquipediaAbility",
    "ODAbility",
    "ODHero",
    "ODMatchup",
    "ODProMatch",
    "StratzSynergyEdge",
]
```

- [ ] **Step 3: Commit**

```bash
git add src/invoker/schemas
git commit -m "feat: pydantic models for raw API responses"
```

---

## Task 8: LLM client abstraction

**Files:**
- Create: `src/invoker/llm/__init__.py`, `src/invoker/llm/client.py`, `src/invoker/llm/gemini.py`, `src/invoker/llm/manual.py`
- Test: `tests/test_llm_manual.py`

- [ ] **Step 1: Write `src/invoker/llm/client.py`**

```python
from __future__ import annotations

from dataclasses import dataclass
from typing import Protocol


@dataclass(frozen=True)
class LLMResponse:
    text: str
    model: str
    prompt_version: int


class LLMClient(Protocol):
    model_name: str

    def complete_json(self, prompt: str, *, prompt_version: int) -> LLMResponse:
        """Call the model with a prompt expected to produce JSON. Returns raw text."""
        ...


def make_client(kind: str, model: str | None = None) -> LLMClient:
    if kind == "gemini":
        from invoker.llm.gemini import GeminiClient
        return GeminiClient(model=model or "gemini-2.5-flash")
    if kind == "manual":
        from invoker.llm.manual import ManualClient
        return ManualClient()
    raise ValueError(f"unknown LLM client kind: {kind}")
```

- [ ] **Step 2: Write `src/invoker/llm/gemini.py`**

```python
from __future__ import annotations

import os

from invoker.llm.client import LLMResponse

try:
    import google.generativeai as genai
except ImportError as e:
    raise RuntimeError("google-generativeai not installed") from e


class GeminiClient:
    def __init__(self, model: str = "gemini-2.5-flash") -> None:
        key = os.environ.get("GOOGLE_API_KEY")
        if not key:
            raise RuntimeError("GOOGLE_API_KEY not set")
        genai.configure(api_key=key)
        self.model_name = model
        self._model = genai.GenerativeModel(model)

    def complete_json(self, prompt: str, *, prompt_version: int) -> LLMResponse:
        resp = self._model.generate_content(
            prompt,
            generation_config={"temperature": 0.0, "response_mime_type": "application/json"},
        )
        return LLMResponse(text=resp.text, model=self.model_name, prompt_version=prompt_version)
```

- [ ] **Step 3: Write `src/invoker/llm/manual.py`**

```python
from __future__ import annotations

import hashlib
from pathlib import Path

from invoker.llm.client import LLMResponse


class ManualClient:
    """
    File-based LLM loop for rate-limit emergencies and spot-checks.

    Writes each prompt to data/raw/manual_prompts/<hash>.md.
    Reads the response from data/raw/manual_responses/<hash>.txt.
    Raises if response is missing so you know to go paste it into ChatGPT/Claude.ai.
    """

    model_name = "manual"

    def __init__(self, inbox: Path | None = None, outbox: Path | None = None) -> None:
        self.inbox = inbox or Path("data/raw/manual_prompts")
        self.outbox = outbox or Path("data/raw/manual_responses")
        self.inbox.mkdir(parents=True, exist_ok=True)
        self.outbox.mkdir(parents=True, exist_ok=True)

    def complete_json(self, prompt: str, *, prompt_version: int) -> LLMResponse:
        h = hashlib.sha256(prompt.encode()).hexdigest()[:12]
        prompt_path = self.inbox / f"{h}.md"
        response_path = self.outbox / f"{h}.txt"
        if not prompt_path.exists():
            prompt_path.write_text(prompt)
        if not response_path.exists():
            raise FileNotFoundError(
                f"Manual response missing. Paste the JSON output for:\n  {prompt_path}\n"
                f"into:\n  {response_path}"
            )
        return LLMResponse(text=response_path.read_text(), model="manual", prompt_version=prompt_version)
```

- [ ] **Step 4: Write `src/invoker/llm/__init__.py`**

```python
from invoker.llm.client import LLMClient, LLMResponse, make_client

__all__ = ["LLMClient", "LLMResponse", "make_client"]
```

- [ ] **Step 5: Write `tests/test_llm_manual.py`**

```python
import pytest

from invoker.llm.manual import ManualClient


def test_manual_client_writes_prompt_and_raises(tmp_path):
    client = ManualClient(inbox=tmp_path / "in", outbox=tmp_path / "out")
    with pytest.raises(FileNotFoundError):
        client.complete_json("hello", prompt_version=1)
    assert any((tmp_path / "in").iterdir()), "prompt should be written"


def test_manual_client_roundtrip(tmp_path):
    client = ManualClient(inbox=tmp_path / "in", outbox=tmp_path / "out")
    try:
        client.complete_json("hello", prompt_version=1)
    except FileNotFoundError as e:
        # Extract the paths from the hint and simulate pasting the response.
        msg = str(e)
        assert "Paste the JSON output for" in msg
    # Simulate pasting
    import hashlib
    h = hashlib.sha256(b"hello").hexdigest()[:12]
    (tmp_path / "out" / f"{h}.txt").write_text('{"ok": true}')
    resp = client.complete_json("hello", prompt_version=1)
    assert resp.text == '{"ok": true}'
```

- [ ] **Step 6: Run**

```bash
uv run pytest tests/test_llm_manual.py -v
```

Expected: pass.

- [ ] **Step 7: Commit**

```bash
git add src/invoker/llm tests/test_llm_manual.py
git commit -m "feat: LLMClient protocol with Gemini + manual implementations"
```

---

## Task 9: Prompt files and loader

**Files:**
- Create: `src/invoker/prompts/extract_mechanical_tags.md`, `src/invoker/prompts/synergy_reason.md`, `src/invoker/prompts/counter_reason.md`, `src/invoker/prompts/loader.py`, `src/invoker/prompts/__init__.py`
- Test: `tests/test_prompts.py`

- [ ] **Step 1: Write `src/invoker/prompts/extract_mechanical_tags.md`**

```markdown
<!-- prompt_version: 1 -->
You are extracting structured functional tags for a Dota 2 hero from a fixed taxonomy.

## Rules
1. Pick tags ONLY from the taxonomy below. Never invent a tag.
2. Each tag you pick must be justified by quoted ability text.
3. If no ability text justifies a tag, do not pick it — even if it feels right.
4. Liquipedia's curated role labels are prior evidence. Use them as hints, but final tags must still be justified by ability text.

## Output
Return a single JSON object:

```json
{
  "functional_tags": ["tag_a", "tag_b"],
  "tag_sources": [
    {"tag": "tag_a", "ability": "Ability Name", "evidence": "quoted text from the ability"}
  ]
}
```

## Taxonomy

{TAXONOMY}

## Hero

Name: {HERO_NAME}
Liquipedia roles: {LIQUIPEDIA_ROLES}

## Abilities

{ABILITIES}
```

- [ ] **Step 2: Write `src/invoker/prompts/synergy_reason.md`**

```markdown
<!-- prompt_version: 1 -->
You are writing a one-sentence justification for a hero synergy in Dota 2.

## Rules
1. The justification MUST reference at least one functional tag from hero A or hero B.
2. Stay under 25 words.
3. Speak in mechanics, not flavor. No "they're both strong" or hype.

## Output
Return a single JSON object:

```json
{"reason": "..."}
```

## Input

Hero A: {HERO_A_NAME}
Hero A tags: {HERO_A_TAGS}
Hero B: {HERO_B_NAME}
Hero B tags: {HERO_B_TAGS}
Observed synergy: {SCORE} over {GAMES} games.
```

- [ ] **Step 3: Write `src/invoker/prompts/counter_reason.md`**

Same shape as synergy_reason but phrased as "how A is countered by B." Copy and adapt.

```markdown
<!-- prompt_version: 1 -->
You are writing a one-sentence justification for a hero counter in Dota 2.

## Rules
1. The justification MUST reference at least one functional tag from hero A or hero B.
2. Stay under 25 words.
3. Speak in mechanics, not flavor.

## Output
Return a single JSON object:

```json
{"reason": "..."}
```

## Input

Hero being countered: {HERO_A_NAME}
Hero A tags: {HERO_A_TAGS}
Counter: {HERO_B_NAME}
Hero B tags: {HERO_B_TAGS}
Observed disadvantage: {SCORE} over {GAMES} games.
```

- [ ] **Step 4: Write `src/invoker/prompts/loader.py`**

```python
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
```

- [ ] **Step 5: Write `src/invoker/prompts/__init__.py`**

```python
from invoker.prompts.loader import Prompt, load

__all__ = ["Prompt", "load"]
```

- [ ] **Step 6: Write `tests/test_prompts.py`**

```python
from invoker.prompts import load


def test_extraction_prompt_loads():
    p = load("extract_mechanical_tags")
    assert p.version >= 1
    assert "{TAXONOMY}" in p.text
    assert "{HERO_NAME}" in p.text


def test_rendering_replaces_placeholders():
    p = load("synergy_reason")
    rendered = p.render(
        HERO_A_NAME="Slardar",
        HERO_A_TAGS="armor_reduction",
        HERO_B_NAME="Pangolier",
        HERO_B_TAGS="physical_damage_amplifier",
        SCORE="0.08",
        GAMES="50",
    )
    assert "Slardar" in rendered
    assert "{HERO_A_NAME}" not in rendered
```

- [ ] **Step 7: Run**

```bash
uv run pytest tests/test_prompts.py -v
```

Expected: pass.

- [ ] **Step 8: Commit**

```bash
git add src/invoker/prompts tests/test_prompts.py
git commit -m "feat: prompt files and loader with version headers"
```

---

## Task 10: Mechanical extraction pipeline

**Files:**
- Create: `src/invoker/pipeline/__init__.py`, `src/invoker/pipeline/extract.py`
- Test: `tests/test_extract.py`

- [ ] **Step 1: Write `src/invoker/pipeline/extract.py`**

```python
from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from datetime import datetime, timezone

from invoker.llm import LLMClient
from invoker.prompts import load
from invoker.taxonomy import load_taxonomy


@dataclass
class HeroExtractionInput:
    hero_id: int
    hero_name: str
    liquipedia_roles: list[str]
    abilities: list[dict]   # [{"name": ..., "text": ...}]


@dataclass
class TagSource:
    tag: str
    ability: str
    evidence: str


@dataclass
class MechanicalExtraction:
    hero_id: int
    functional_tags: list[str]
    tag_sources: list[TagSource]
    model: str
    prompt_version: int
    prompt_hash: str
    input_hash: str
    extracted_at: str


def _input_hash(h: HeroExtractionInput) -> str:
    blob = json.dumps(asdict(h), sort_keys=True).encode()
    return "sha256:" + hashlib.sha256(blob).hexdigest()


def extract_mechanical(h: HeroExtractionInput, client: LLMClient) -> MechanicalExtraction:
    prompt = load("extract_mechanical_tags")
    tax = load_taxonomy()

    abilities_block = "\n".join(f"- {a['name']}: {a['text']}" for a in h.abilities)
    rendered = prompt.render(
        TAXONOMY=tax.as_prompt_block(),
        HERO_NAME=h.hero_name,
        LIQUIPEDIA_ROLES=", ".join(h.liquipedia_roles) or "(none)",
        ABILITIES=abilities_block,
    )
    response = client.complete_json(rendered, prompt_version=prompt.version)
    parsed = json.loads(response.text)

    return MechanicalExtraction(
        hero_id=h.hero_id,
        functional_tags=list(parsed["functional_tags"]),
        tag_sources=[TagSource(**s) for s in parsed["tag_sources"]],
        model=response.model,
        prompt_version=response.prompt_version,
        prompt_hash=prompt.sha256,
        input_hash=_input_hash(h),
        extracted_at=datetime.now(timezone.utc).isoformat(timespec="seconds"),
    )
```

- [ ] **Step 2: Write `tests/test_extract.py`**

```python
import json

from invoker.llm.client import LLMResponse
from invoker.pipeline.extract import HeroExtractionInput, extract_mechanical


class FakeClient:
    model_name = "fake"

    def complete_json(self, prompt: str, *, prompt_version: int) -> LLMResponse:
        return LLMResponse(
            text=json.dumps({
                "functional_tags": ["armor_reduction", "single_target_disable"],
                "tag_sources": [
                    {"tag": "armor_reduction", "ability": "Corrosive Haze", "evidence": "reduces armor"},
                    {"tag": "single_target_disable", "ability": "Slithereen Crush", "evidence": "stuns 1.6s"},
                ],
            }),
            model="fake",
            prompt_version=prompt_version,
        )


def test_extract_returns_parsed_tags():
    inp = HeroExtractionInput(
        hero_id=28,
        hero_name="Slardar",
        liquipedia_roles=["Initiator", "Disabler"],
        abilities=[
            {"name": "Slithereen Crush", "text": "AoE stun"},
            {"name": "Corrosive Haze", "text": "Armor reduction"},
        ],
    )
    result = extract_mechanical(inp, FakeClient())
    assert "armor_reduction" in result.functional_tags
    assert result.input_hash.startswith("sha256:")
    assert result.prompt_version >= 1
```

- [ ] **Step 3: Run**

```bash
uv run pytest tests/test_extract.py -v
```

Expected: pass.

- [ ] **Step 4: Commit**

```bash
git add src/invoker/pipeline tests/test_extract.py
git commit -m "feat: mechanical extraction with taxonomy-gated output"
```

---

## Task 11: Synergy / counter reason generation

**Files:**
- Create: `src/invoker/pipeline/reason.py`
- Test: `tests/test_reason.py`

- [ ] **Step 1: Write `src/invoker/pipeline/reason.py`**

```python
from __future__ import annotations

import json
from dataclasses import dataclass

from invoker.llm import LLMClient
from invoker.prompts import load


@dataclass
class ReasonInput:
    hero_a_id: int
    hero_a_name: str
    hero_a_tags: list[str]
    hero_b_id: int
    hero_b_name: str
    hero_b_tags: list[str]
    score: float
    games: int


@dataclass
class ReasonOutput:
    reason: str
    model: str
    prompt_version: int


def _render_and_call(prompt_name: str, inp: ReasonInput, client: LLMClient) -> ReasonOutput:
    prompt = load(prompt_name)
    rendered = prompt.render(
        HERO_A_NAME=inp.hero_a_name,
        HERO_A_TAGS=", ".join(inp.hero_a_tags) or "(no tags)",
        HERO_B_NAME=inp.hero_b_name,
        HERO_B_TAGS=", ".join(inp.hero_b_tags) or "(no tags)",
        SCORE=f"{inp.score:+.2f}",
        GAMES=str(inp.games),
    )
    response = client.complete_json(rendered, prompt_version=prompt.version)
    parsed = json.loads(response.text)
    return ReasonOutput(reason=parsed["reason"], model=response.model, prompt_version=response.prompt_version)


def generate_synergy_reason(inp: ReasonInput, client: LLMClient) -> ReasonOutput:
    return _render_and_call("synergy_reason", inp, client)


def generate_counter_reason(inp: ReasonInput, client: LLMClient) -> ReasonOutput:
    return _render_and_call("counter_reason", inp, client)


class ReasonNotGroundedError(ValueError):
    pass


def validate_grounding(reason: str, a_tags: list[str], b_tags: list[str]) -> None:
    """Reject a reason that mentions no tag from either hero."""
    text = reason.lower().replace("_", " ")
    all_tags = set(a_tags) | set(b_tags)
    for tag in all_tags:
        if tag.replace("_", " ") in text or tag in reason.lower():
            return
    raise ReasonNotGroundedError(
        f"Reason cites no tag from either hero. Reason: {reason!r}. Tags: {sorted(all_tags)}"
    )
```

- [ ] **Step 2: Write `tests/test_reason.py`**

```python
import json

import pytest

from invoker.llm.client import LLMResponse
from invoker.pipeline.reason import (
    ReasonInput,
    ReasonNotGroundedError,
    generate_synergy_reason,
    validate_grounding,
)


class CannedClient:
    def __init__(self, reason: str) -> None:
        self.reason = reason
        self.model_name = "canned"

    def complete_json(self, prompt: str, *, prompt_version: int) -> LLMResponse:
        return LLMResponse(
            text=json.dumps({"reason": self.reason}),
            model="canned",
            prompt_version=prompt_version,
        )


def test_synergy_reason_generates():
    inp = ReasonInput(
        hero_a_id=28, hero_a_name="Slardar", hero_a_tags=["armor_reduction"],
        hero_b_id=120, hero_b_name="Pangolier", hero_b_tags=["physical_damage_amplifier"],
        score=0.08, games=50,
    )
    out = generate_synergy_reason(inp, CannedClient("Armor reduction stacks with physical damage amplifier."))
    assert "armor" in out.reason.lower()


def test_validate_grounding_accepts_tag_mention():
    validate_grounding("armor reduction stacks", ["armor_reduction"], [])


def test_validate_grounding_rejects_no_mention():
    with pytest.raises(ReasonNotGroundedError):
        validate_grounding("they both win fights", ["armor_reduction"], ["physical_damage_amplifier"])
```

- [ ] **Step 3: Run**

```bash
uv run pytest tests/test_reason.py -v
```

Expected: pass.

- [ ] **Step 4: Commit**

```bash
git add src/invoker/pipeline/reason.py tests/test_reason.py
git commit -m "feat: synergy and counter reason generation with grounding check"
```

---

## Task 12: Statistical derivation (pro bracket)

**Files:**
- Create: `src/invoker/pipeline/derive.py`
- Test: `tests/test_derive.py`

- [ ] **Step 1: Write `src/invoker/pipeline/derive.py`**

```python
from __future__ import annotations

from dataclasses import dataclass


CONFIDENCE_BUCKETS = [
    (40, "high"),
    (10, "med"),
    (1, "low"),
    (0, "none"),
]


def confidence_for(games: int) -> str:
    for threshold, label in CONFIDENCE_BUCKETS:
        if games >= threshold:
            return label
    return "none"


@dataclass
class PositionStats:
    weights: dict[str, float]
    games: int
    window_days: int


def position_weights(counts_per_position: dict[str, int], floor: float = 0.03) -> dict[str, float]:
    total = sum(counts_per_position.values())
    if total == 0:
        return {str(p): 0.0 for p in range(1, 6)}
    raw = {str(p): counts_per_position.get(str(p), 0) / total for p in range(1, 6)}
    # Floor noise, then renormalize.
    above_floor = {k: v for k, v in raw.items() if v >= floor}
    floored = sum(raw[k] for k in raw if k not in above_floor)
    if above_floor:
        rescale = 1.0 / (1.0 - floored if 1.0 - floored > 0 else 1.0)
        weights = {k: (v * rescale if k in above_floor else 0.0) for k, v in raw.items()}
        # Normalize for rounding
        s = sum(weights.values()) or 1.0
        weights = {k: round(v / s, 3) for k, v in weights.items()}
    else:
        weights = {k: round(v, 3) for k, v in raw.items()}
    return weights


@dataclass
class MetaTier:
    contest_rate: float
    win_rate: float
    tier: str
    games: int


def meta_tier(contest_rate: float, win_rate: float) -> str:
    if contest_rate >= 0.5:
        return "first_phase_priority"
    if contest_rate >= 0.25:
        return "high_priority"
    if contest_rate >= 0.10:
        return "situational"
    return "niche"


@dataclass
class StatisticalEdge:
    hero_id: int
    score: float | None
    games: int
    confidence: str
    source: str
    reason: str | None = None


def merge_matchups(
    stratz_edges: list[dict] | None,
    opendota_matchups: list[dict] | None,
    *,
    hero_id: int,
) -> tuple[list[StatisticalEdge], list[StatisticalEdge]]:
    """
    Merge synergy and counter data. Preference order:
      - synergies: prefer STRATZ (signed advantage). If absent, fall back to OpenDota matchup
        win-rate delta against average.
      - counters: symmetric — negative advantage becomes a counter.
    Result: (synergies, counters) — each a list of StatisticalEdge.
    """
    synergies: dict[int, StatisticalEdge] = {}
    counters: dict[int, StatisticalEdge] = {}

    if stratz_edges:
        for edge in stratz_edges:
            other = edge["heroId2"] if edge["heroId1"] == hero_id else edge["heroId1"]
            games = int(edge["matchCount"])
            score = float(edge["synergy"])
            target = synergies if score >= 0 else counters
            target[other] = StatisticalEdge(
                hero_id=other,
                score=score,
                games=games,
                confidence=confidence_for(games),
                source="stratz",
            )

    if opendota_matchups:
        # OpenDota gives per-opponent win_rate. Convert to a signed delta vs 0.5.
        for m in opendota_matchups:
            other = int(m["hero_id"])
            if other in synergies or other in counters:
                continue
            games = int(m["games_played"])
            if games == 0:
                continue
            wr = m["wins"] / games
            score = round(wr - 0.5, 3)
            target = synergies if score >= 0 else counters
            target[other] = StatisticalEdge(
                hero_id=other,
                score=score,
                games=games,
                confidence=confidence_for(games),
                source="opendota",
            )

    return (
        sorted(synergies.values(), key=lambda e: abs(e.score or 0), reverse=True),
        sorted(counters.values(), key=lambda e: abs(e.score or 0), reverse=True),
    )
```

- [ ] **Step 2: Write `tests/test_derive.py`**

```python
from invoker.pipeline.derive import (
    confidence_for,
    merge_matchups,
    meta_tier,
    position_weights,
)


def test_confidence_bucketing():
    assert confidence_for(0) == "none"
    assert confidence_for(5) == "low"
    assert confidence_for(20) == "med"
    assert confidence_for(100) == "high"


def test_position_weights_floor_and_normalize():
    w = position_weights({"1": 0, "2": 40, "3": 40, "4": 1, "5": 1})
    assert w["2"] > 0.4
    assert w["3"] > 0.4
    assert w["4"] == 0.0
    assert w["5"] == 0.0
    assert abs(sum(w.values()) - 1.0) < 0.01


def test_meta_tier_thresholds():
    assert meta_tier(0.6, 0.55) == "first_phase_priority"
    assert meta_tier(0.30, 0.52) == "high_priority"
    assert meta_tier(0.15, 0.50) == "situational"
    assert meta_tier(0.05, 0.50) == "niche"


def test_merge_matchups_prefers_stratz():
    stratz = [{"heroId1": 28, "heroId2": 120, "synergy": 0.08, "matchCount": 50}]
    od = [{"hero_id": 120, "games_played": 100, "wins": 52}]
    syn, cnt = merge_matchups(stratz, od, hero_id=28)
    assert syn and syn[0].hero_id == 120
    assert syn[0].source == "stratz"
    assert syn[0].score == 0.08
    assert not cnt


def test_merge_matchups_falls_back_to_opendota():
    syn, cnt = merge_matchups(None, [{"hero_id": 120, "games_played": 100, "wins": 40}], hero_id=28)
    assert not syn
    assert cnt and cnt[0].source == "opendota"
    assert cnt[0].score == -0.1
```

- [ ] **Step 3: Run**

```bash
uv run pytest tests/test_derive.py -v
```

Expected: pass.

- [ ] **Step 4: Commit**

```bash
git add src/invoker/pipeline/derive.py tests/test_derive.py
git commit -m "feat: pro-bracket statistical derivation with confidence bucketing"
```

---

## Task 13: Per-hero file writer + summary generator

**Files:**
- Create: `src/invoker/pipeline/summarize.py`, `src/invoker/schemas/derived.py`, `src/invoker/pipeline/writer.py`
- Test: `tests/test_summarize.py`

- [ ] **Step 1: Write `src/invoker/schemas/derived.py`**

```python
from __future__ import annotations

from pydantic import BaseModel, ConfigDict


class PositionBlock(BaseModel):
    model_config = ConfigDict(extra="forbid")
    weights: dict[str, float]
    games: int
    window_days: int


class StatEdge(BaseModel):
    model_config = ConfigDict(extra="forbid")
    hero_id: int
    score: float | None
    games: int
    confidence: str
    source: str
    reason: str | None = None
    reason_provenance: dict | None = None


class MetaBlock(BaseModel):
    model_config = ConfigDict(extra="forbid")
    contest_rate: float
    win_rate: float
    tier: str
    games: int


class MetaHistoryEntry(BaseModel):
    model_config = ConfigDict(extra="forbid")
    patch: str
    bracket: str
    contest_rate: float
    win_rate: float
    tier: str


class TagSource(BaseModel):
    model_config = ConfigDict(extra="forbid")
    tag: str
    ability: str
    evidence: str


class Provenance(BaseModel):
    model_config = ConfigDict(extra="forbid")
    mechanical: dict
    statistical: dict


class HeroDerived(BaseModel):
    model_config = ConfigDict(extra="forbid")
    schema_version: int
    generator_version: str
    source_patch: str
    generated_at: str

    hero_id: int
    localized_name: str
    internal_name: str
    liquipedia_roles: list[str]

    functional_tags: list[str]
    tag_sources: list[TagSource]

    positions: dict[str, PositionBlock]
    synergies: dict[str, list[StatEdge]]
    counters: dict[str, list[StatEdge]]
    meta: dict[str, MetaBlock]
    meta_history: list[MetaHistoryEntry]

    provenance: Provenance
```

- [ ] **Step 2: Write `src/invoker/pipeline/writer.py`**

```python
from __future__ import annotations

import json
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
```

- [ ] **Step 3: Write `src/invoker/pipeline/summarize.py`**

```python
from __future__ import annotations

from pathlib import Path

from invoker.paths import summary_file
from invoker.schemas.derived import HeroDerived


def summarize(hero: HeroDerived, bracket: str) -> str:
    pos = hero.positions.get(bracket)
    pos_label = (
        "-".join(p for p, w in (pos.weights.items() if pos else {}) if w > 0)
        if pos else "unknown"
    )
    tags = ", ".join(hero.functional_tags)
    syns = [e for e in hero.synergies.get(bracket, []) if e.confidence in ("med", "high")][:3]
    cnts = [e for e in hero.counters.get(bracket, []) if e.confidence in ("med", "high")][:3]
    meta = hero.meta.get(bracket)

    history_line = ""
    if hero.meta_history:
        recent = [m for m in hero.meta_history if m.bracket == bracket][-3:]
        if len(recent) >= 2 and recent[0].tier != recent[-1].tier:
            history_line = f" [was {recent[0].tier} in {recent[0].patch}]"

    lines = [
        f"{hero.localized_name} [pos{pos_label} — {hero.functional_tags[0] if hero.functional_tags else 'n/a'}]",
        f"Functions: {tags}",
    ]
    if syns:
        lines.append(
            f"{bracket.capitalize()} synergies ({hero.source_patch}, med+): "
            + "; ".join(f"h{e.hero_id} {e.score:+.2f} ({e.games}g)" + (f" — {e.reason}" if e.reason else "") for e in syns)
        )
    if cnts:
        lines.append(
            f"{bracket.capitalize()} counters ({hero.source_patch}, med+): "
            + "; ".join(f"h{e.hero_id} {e.score:+.2f} ({e.games}g)" + (f" — {e.reason}" if e.reason else "") for e in cnts)
        )
    if meta:
        lines.append(
            f"{bracket.capitalize()} meta ({hero.source_patch}): "
            f"contest {meta.contest_rate:.0%}, win {meta.win_rate:.0%}, tier: {meta.tier}{history_line}"
        )
    return "\n".join(lines) + "\n"


def write_summary(data_dir: Path, hero: HeroDerived, bracket: str) -> Path:
    path = summary_file(data_dir, hero.source_patch, bracket, hero.hero_id)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(summarize(hero, bracket))
    return path
```

- [ ] **Step 4: Write `tests/test_summarize.py`**

Build a minimal `HeroDerived` fixture inline and check the output shape.

```python
from invoker.pipeline.summarize import summarize
from invoker.schemas.derived import (
    HeroDerived, MetaBlock, PositionBlock, Provenance, StatEdge, TagSource,
)


def _hero() -> HeroDerived:
    return HeroDerived(
        schema_version=1,
        generator_version="invoker@0.1.0",
        source_patch="7.41b",
        generated_at="2026-04-14T00:00:00Z",
        hero_id=28,
        localized_name="Slardar",
        internal_name="npc_dota_hero_slardar",
        liquipedia_roles=["Initiator"],
        functional_tags=["armor_reduction", "single_target_disable"],
        tag_sources=[TagSource(tag="armor_reduction", ability="Corrosive Haze", evidence="-20 armor")],
        positions={"pro": PositionBlock(weights={"3": 1.0}, games=34, window_days=90)},
        synergies={"pro": [StatEdge(hero_id=120, score=0.08, games=50, confidence="high", source="stratz", reason="armor reduction helps physical")]},
        counters={"pro": [StatEdge(hero_id=96, score=-0.07, games=34, confidence="med", source="opendota", reason="natural armor")]},
        meta={"pro": MetaBlock(contest_rate=0.12, win_rate=0.51, tier="situational", games=34)},
        meta_history=[],
        provenance=Provenance(mechanical={"model": "fake"}, statistical={}),
    )


def test_summary_contains_all_sections():
    s = summarize(_hero(), "pro")
    assert "Slardar" in s
    assert "armor_reduction" in s
    assert "h120" in s
    assert "h96" in s
    assert "tier: situational" in s
```

- [ ] **Step 5: Run**

```bash
uv run pytest tests/test_summarize.py -v
```

Expected: pass.

- [ ] **Step 6: Commit**

```bash
git add src/invoker/schemas/derived.py src/invoker/pipeline/writer.py src/invoker/pipeline/summarize.py tests/test_summarize.py
git commit -m "feat: derived schema, hero file writer, and summary generator"
```

---

## Task 14: Derived validators

**Files:**
- Create: `src/invoker/pipeline/validators.py`
- Test: `tests/test_validators.py`

- [ ] **Step 1: Write `src/invoker/pipeline/validators.py`**

```python
from __future__ import annotations

from dataclasses import dataclass

from invoker.pipeline.derive import confidence_for
from invoker.schemas.derived import HeroDerived
from invoker.taxonomy import load_taxonomy


class ValidationError(Exception):
    pass


@dataclass
class ValidationContext:
    roster_hero_ids: set[int]


def validate_hero(hero: HeroDerived, ctx: ValidationContext) -> None:
    _validate_tag_taxonomy(hero)
    _validate_tag_source_completeness(hero)
    _validate_reason_grounding(hero)
    _validate_statistical_sanity(hero)
    _validate_id_integrity(hero, ctx)
    _validate_bracket_consistency(hero)


def _validate_tag_taxonomy(h: HeroDerived) -> None:
    tax = load_taxonomy()
    unknown = [t for t in h.functional_tags if not tax.has(t)]
    if unknown:
        raise ValidationError(f"hero {h.hero_id}: tags not in taxonomy: {unknown}")


def _validate_tag_source_completeness(h: HeroDerived) -> None:
    cited = {s.tag for s in h.tag_sources}
    missing = [t for t in h.functional_tags if t not in cited]
    if missing:
        raise ValidationError(f"hero {h.hero_id}: tags missing tag_sources: {missing}")


def _validate_reason_grounding(h: HeroDerived) -> None:
    for bracket, edges in (("synergies", h.synergies), ("counters", h.counters)):
        for br, lst in edges.items():
            for e in lst:
                if e.reason is None:
                    continue
                text = e.reason.lower().replace("_", " ")
                hero_tags = set(h.functional_tags)
                grounded = any(tag in text or tag.replace("_", " ") in text for tag in hero_tags)
                if not grounded:
                    raise ValidationError(
                        f"hero {h.hero_id} {bracket}[{br}] vs {e.hero_id}: reason not grounded in any tag"
                    )


def _validate_statistical_sanity(h: HeroDerived) -> None:
    for dct in (h.synergies, h.counters):
        for br, lst in dct.items():
            for e in lst:
                if e.games < 0:
                    raise ValidationError(f"hero {h.hero_id}: negative games")
                if (e.score is None) != (e.games == 0):
                    raise ValidationError(
                        f"hero {h.hero_id}: score/games mismatch — score={e.score}, games={e.games}"
                    )
                expected = confidence_for(e.games)
                if e.confidence != expected:
                    raise ValidationError(
                        f"hero {h.hero_id}: confidence {e.confidence} expected {expected} for {e.games} games"
                    )


def _validate_id_integrity(h: HeroDerived, ctx: ValidationContext) -> None:
    if h.hero_id not in ctx.roster_hero_ids:
        raise ValidationError(f"hero_id {h.hero_id} not in current roster")
    for dct in (h.synergies, h.counters):
        for lst in dct.values():
            for e in lst:
                if e.hero_id not in ctx.roster_hero_ids:
                    raise ValidationError(f"hero {h.hero_id}: edge references unknown hero {e.hero_id}")


def _validate_bracket_consistency(h: HeroDerived) -> None:
    for br, block in h.positions.items():
        if block.window_days <= 0:
            raise ValidationError(f"positions[{br}]: window_days must be > 0")
    for br, block in h.meta.items():
        if block.games < 0:
            raise ValidationError(f"meta[{br}]: games negative")
```

- [ ] **Step 2: Write `tests/test_validators.py`**

```python
import pytest

from invoker.pipeline.validators import ValidationContext, ValidationError, validate_hero
from tests.test_summarize import _hero  # reuse fixture builder


CTX = ValidationContext(roster_hero_ids={28, 120, 96})


def test_valid_hero_passes():
    validate_hero(_hero(), CTX)


def test_unknown_tag_rejected():
    h = _hero()
    h.functional_tags.append("not_a_real_tag")
    with pytest.raises(ValidationError, match="taxonomy"):
        validate_hero(h, CTX)


def test_missing_tag_source_rejected():
    h = _hero()
    h.functional_tags.append("initiation")  # no tag_source entry
    with pytest.raises(ValidationError, match="tag_sources"):
        validate_hero(h, CTX)


def test_ungrounded_reason_rejected():
    h = _hero()
    h.synergies["pro"][0].reason = "they just win a lot"
    with pytest.raises(ValidationError, match="not grounded"):
        validate_hero(h, CTX)


def test_confidence_mismatch_rejected():
    h = _hero()
    h.synergies["pro"][0].games = 5  # low
    # confidence is still "high" → mismatch
    with pytest.raises(ValidationError, match="confidence"):
        validate_hero(h, CTX)


def test_unknown_hero_id_edge_rejected():
    h = _hero()
    h.synergies["pro"][0].hero_id = 9999
    with pytest.raises(ValidationError, match="unknown hero"):
        validate_hero(h, CTX)
```

- [ ] **Step 3: Run**

```bash
uv run pytest tests/test_validators.py -v
```

Expected: pass.

- [ ] **Step 4: Commit**

```bash
git add src/invoker/pipeline/validators.py tests/test_validators.py
git commit -m "feat: derived-layer validators with taxonomy and grounding checks"
```

---

## Task 15: Manifest writer

**Files:**
- Create: `src/invoker/pipeline/manifest.py`
- Test: `tests/test_manifest.py`

- [ ] **Step 1: Write `src/invoker/pipeline/manifest.py`**

```python
from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass, field
from datetime import datetime, timezone
from pathlib import Path

from invoker.paths import derived_patch_dir, hero_file, manifest_file


@dataclass
class HeroManifestEntry:
    hero_id: int
    content_hash: str
    brackets: list[str]


@dataclass
class Manifest:
    schema_version: int
    patch: str
    generated_at: str
    status: str  # "partial" | "complete"
    heroes: list[HeroManifestEntry] = field(default_factory=list)


def _sha256_file(p: Path) -> str:
    return "sha256:" + hashlib.sha256(p.read_bytes()).hexdigest()


def build_manifest(data_dir: Path, patch: str, hero_ids: list[int], brackets: list[str], complete: bool) -> Manifest:
    entries: list[HeroManifestEntry] = []
    for hid in hero_ids:
        p = hero_file(data_dir, patch, hid)
        if not p.exists():
            continue
        entries.append(
            HeroManifestEntry(
                hero_id=hid,
                content_hash=_sha256_file(p),
                brackets=list(brackets),
            )
        )
    return Manifest(
        schema_version=1,
        patch=patch,
        generated_at=datetime.now(timezone.utc).isoformat(timespec="seconds"),
        status="complete" if complete else "partial",
        heroes=entries,
    )


def write_manifest(data_dir: Path, manifest: Manifest) -> Path:
    path = manifest_file(data_dir, manifest.patch)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(asdict(manifest), indent=2))
    return path
```

- [ ] **Step 2: Write `tests/test_manifest.py`**

```python
from pathlib import Path

from invoker.paths import hero_file
from invoker.pipeline.manifest import build_manifest, write_manifest
from invoker.pipeline.writer import write_hero
from tests.test_summarize import _hero


def test_manifest_includes_present_heroes(tmp_path: Path):
    h = _hero()
    write_hero(tmp_path, "7.41b", h)
    m = build_manifest(tmp_path, "7.41b", [h.hero_id, 999], ["pro"], complete=False)
    assert len(m.heroes) == 1
    assert m.heroes[0].content_hash.startswith("sha256:")
    assert m.status == "partial"

    path = write_manifest(tmp_path, m)
    assert path.exists()
```

- [ ] **Step 3: Run**

```bash
uv run pytest tests/test_manifest.py -v
```

Expected: pass.

- [ ] **Step 4: Commit**

```bash
git add src/invoker/pipeline/manifest.py tests/test_manifest.py
git commit -m "feat: manifest writer with per-hero content hashes"
```

---

## Task 16: NetworkX graph builder

**Files:**
- Create: `src/invoker/graph/__init__.py`, `src/invoker/graph/builder.py`
- Test: `tests/test_graph.py`

- [ ] **Step 1: Write `src/invoker/graph/builder.py`**

```python
from __future__ import annotations

import pickle
from pathlib import Path

import networkx as nx

from invoker.paths import derived_patch_dir, graph_file
from invoker.pipeline.writer import read_hero


def build_graph(data_dir: Path, patch: str, hero_ids: list[int]) -> nx.MultiDiGraph:
    g = nx.MultiDiGraph()
    for hid in hero_ids:
        h = read_hero(data_dir, patch, hid)
        g.add_node(("hero", h.hero_id), name=h.localized_name, patch=patch)
        for tag in h.functional_tags:
            g.add_node(("tag", tag), kind="tag")
            g.add_edge(("hero", h.hero_id), ("tag", tag), relation="has_tag")
        for bracket, edges in h.synergies.items():
            for e in edges:
                if e.score is None:
                    continue
                g.add_edge(
                    ("hero", h.hero_id), ("hero", e.hero_id),
                    relation="synergy",
                    bracket=bracket,
                    score=e.score,
                    games=e.games,
                    confidence=e.confidence,
                )
        for bracket, edges in h.counters.items():
            for e in edges:
                if e.score is None:
                    continue
                g.add_edge(
                    ("hero", h.hero_id), ("hero", e.hero_id),
                    relation="counter",
                    bracket=bracket,
                    score=e.score,
                    games=e.games,
                    confidence=e.confidence,
                )
    return g


def cache_graph(data_dir: Path, patch: str, g: nx.MultiDiGraph) -> Path:
    path = graph_file(data_dir, patch)
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("wb") as f:
        pickle.dump(g, f)
    return path


def load_graph(data_dir: Path, patch: str) -> nx.MultiDiGraph:
    path = graph_file(data_dir, patch)
    with path.open("rb") as f:
        return pickle.load(f)
```

- [ ] **Step 2: Write `src/invoker/graph/__init__.py`**

```python
from invoker.graph.builder import build_graph, cache_graph, load_graph

__all__ = ["build_graph", "cache_graph", "load_graph"]
```

- [ ] **Step 3: Write `tests/test_graph.py`**

```python
from pathlib import Path

from invoker.graph import build_graph, cache_graph, load_graph
from invoker.pipeline.writer import write_hero
from tests.test_summarize import _hero


def test_graph_build_roundtrip(tmp_path: Path):
    h = _hero()
    write_hero(tmp_path, "7.41b", h)
    g = build_graph(tmp_path, "7.41b", [h.hero_id])
    cache_graph(tmp_path, "7.41b", g)
    loaded = load_graph(tmp_path, "7.41b")
    assert ("hero", 28) in loaded.nodes
    assert ("tag", "armor_reduction") in loaded.nodes
    # Synergy edge exists
    edges = list(loaded.out_edges(("hero", 28), data=True))
    assert any(e[2].get("relation") == "synergy" for e in edges)
```

- [ ] **Step 4: Run**

```bash
uv run pytest tests/test_graph.py -v
```

Expected: pass.

- [ ] **Step 5: Commit**

```bash
git add src/invoker/graph tests/test_graph.py
git commit -m "feat: NetworkX graph builder with pickle cache"
```

---

## Task 17: Internal reader API (KnowledgeBase)

**Files:**
- Create: `src/invoker/kb.py`
- Test: `tests/test_kb.py`

- [ ] **Step 1: Write `src/invoker/kb.py`**

```python
from __future__ import annotations

import json
from functools import cached_property
from pathlib import Path

from invoker.graph import load_graph
from invoker.paths import derived_patch_dir, manifest_file, summary_file
from invoker.pipeline.writer import read_hero
from invoker.schemas.derived import HeroDerived


class KnowledgeBase:
    def __init__(self, patch: str, bracket: str = "pro", *, data_dir: Path | None = None) -> None:
        from invoker.config import Config
        cfg = Config.load()
        self.patch = patch
        self.bracket = bracket
        self.data_dir = data_dir or cfg.data_dir
        self._heroes: dict[int, HeroDerived] = {}

    @cached_property
    def _manifest(self) -> dict:
        return json.loads(manifest_file(self.data_dir, self.patch).read_text())

    @cached_property
    def _graph(self):
        return load_graph(self.data_dir, self.patch)

    def patches(self) -> list[str]:
        root = self.data_dir / "derived"
        return sorted(p.name for p in root.iterdir() if p.is_dir()) if root.exists() else []

    def brackets(self) -> list[str]:
        # Brackets present on at least one hero's positions block.
        for entry in self._manifest.get("heroes", []):
            return entry.get("brackets", [])
        return []

    def hero(self, key: int | str) -> HeroDerived:
        if isinstance(key, str):
            return self._by_name(key)
        if key not in self._heroes:
            self._heroes[key] = read_hero(self.data_dir, self.patch, key)
        return self._heroes[key]

    def _by_name(self, name: str) -> HeroDerived:
        for entry in self._manifest.get("heroes", []):
            h = self.hero(entry["hero_id"])
            if h.localized_name.lower() == name.lower():
                return h
        raise KeyError(f"hero not found: {name}")

    def synergies(self, key: int | str, *, min_confidence: str = "med") -> list:
        order = ["none", "low", "med", "high"]
        cutoff = order.index(min_confidence)
        return [e for e in self.hero(key).synergies.get(self.bracket, []) if order.index(e.confidence) >= cutoff]

    def counters(self, key: int | str, *, min_confidence: str = "med") -> list:
        order = ["none", "low", "med", "high"]
        cutoff = order.index(min_confidence)
        return [e for e in self.hero(key).counters.get(self.bracket, []) if order.index(e.confidence) >= cutoff]

    def neighbors(self, key: int | str, *, relation: str = "synergy", top_k: int = 5) -> list:
        h = self.hero(key)
        edges = (h.synergies if relation == "synergy" else h.counters).get(self.bracket, [])
        return edges[:top_k]

    def summary(self, key: int | str) -> str:
        hid = self.hero(key).hero_id
        return summary_file(self.data_dir, self.patch, self.bracket, hid).read_text()

    def by_tag(self, tag: str) -> list[HeroDerived]:
        results: list[HeroDerived] = []
        for entry in self._manifest.get("heroes", []):
            h = self.hero(entry["hero_id"])
            if tag in h.functional_tags:
                results.append(h)
        return results
```

- [ ] **Step 2: Write `tests/test_kb.py`**

```python
from pathlib import Path

from invoker.graph import build_graph, cache_graph
from invoker.kb import KnowledgeBase
from invoker.pipeline.manifest import build_manifest, write_manifest
from invoker.pipeline.summarize import write_summary
from invoker.pipeline.writer import write_hero
from tests.test_summarize import _hero


def _setup(tmp_path: Path):
    h = _hero()
    write_hero(tmp_path, "7.41b", h)
    write_summary(tmp_path, h, "pro")
    m = build_manifest(tmp_path, "7.41b", [h.hero_id], ["pro"], complete=True)
    write_manifest(tmp_path, m)
    g = build_graph(tmp_path, "7.41b", [h.hero_id])
    cache_graph(tmp_path, "7.41b", g)
    return h


def test_kb_hero_lookup(tmp_path: Path):
    _setup(tmp_path)
    kb = KnowledgeBase(patch="7.41b", bracket="pro", data_dir=tmp_path)
    assert kb.hero(28).localized_name == "Slardar"
    assert kb.hero("Slardar").hero_id == 28


def test_kb_synergies_filtered_by_confidence(tmp_path: Path):
    _setup(tmp_path)
    kb = KnowledgeBase(patch="7.41b", bracket="pro", data_dir=tmp_path)
    assert len(kb.synergies(28, min_confidence="med")) == 1
    assert len(kb.synergies(28, min_confidence="high")) == 1


def test_kb_summary(tmp_path: Path):
    _setup(tmp_path)
    kb = KnowledgeBase(patch="7.41b", bracket="pro", data_dir=tmp_path)
    assert "Slardar" in kb.summary(28)
```

- [ ] **Step 3: Run**

```bash
uv run pytest tests/test_kb.py -v
```

Expected: pass.

- [ ] **Step 4: Commit**

```bash
git add src/invoker/kb.py tests/test_kb.py
git commit -m "feat: KnowledgeBase reader API with manifest + graph"
```

---

## Task 18: Bootstrap orchestrator + CLI

**Files:**
- Create: `src/invoker/pipeline/fetch.py`, `src/invoker/pipeline/assemble.py`, `src/invoker/pipeline/orchestrator.py`, update: `src/invoker/cli.py`
- Test: `tests/test_orchestrator.py` (offline, with fake LLM)

- [ ] **Step 1: Write `src/invoker/pipeline/fetch.py`**

```python
from __future__ import annotations

import asyncio
from pathlib import Path

from invoker.config import Config
from invoker.sources.liquipedia import LiquipediaFetcher
from invoker.sources.opendota import OpenDotaFetcher
from invoker.sources.stratz import StratzFetcher


async def fetch_all(cfg: Config, patch: str, *, force: bool = False) -> dict:
    cache = cfg.data_dir / "raw"
    od = OpenDotaFetcher(cache, patch)
    strat = StratzFetcher(cache, patch, cfg.stratz_token)
    liq = LiquipediaFetcher(cache, patch)
    try:
        heroes = await od.heroes()
        abilities = await od.abilities()
        hero_abilities = await od.hero_abilities_map()
        pro_matches = await od.pro_matches()
        matchups = {h["id"]: await od.matchups(h["id"]) for h in heroes}
        stratz_syn = {h["id"]: await strat.synergies(h["id"]) for h in heroes} if strat.available else {}
        liq_pages = {h["localized_name"]: await liq.hero_page(h["localized_name"]) for h in heroes}
        return {
            "heroes": heroes,
            "abilities": abilities,
            "hero_abilities": hero_abilities,
            "pro_matches": pro_matches,
            "matchups": matchups,
            "stratz_synergies": stratz_syn,
            "liquipedia_pages": liq_pages,
        }
    finally:
        await od.close()
        await strat.close()
        await liq.close()
```

> This is the naive fetch. Phase 1 does not yet parallelize across heroes or diff against prior patches — add those as optimizations if bootstrap time becomes painful.

- [ ] **Step 2: Write `src/invoker/pipeline/assemble.py`**

Assembles a `HeroDerived` from the parts produced by fetch → extract → reason → derive.

```python
from __future__ import annotations

from datetime import datetime, timezone

from invoker.pipeline.derive import StatisticalEdge
from invoker.pipeline.extract import MechanicalExtraction
from invoker.schemas.derived import (
    HeroDerived, MetaBlock, MetaHistoryEntry, PositionBlock, Provenance, StatEdge, TagSource,
)


def _stat_to_edge(e: StatisticalEdge, reason: str | None, reason_prov: dict | None) -> StatEdge:
    return StatEdge(
        hero_id=e.hero_id,
        score=e.score,
        games=e.games,
        confidence=e.confidence,
        source=e.source,
        reason=reason,
        reason_provenance=reason_prov,
    )


def assemble_hero(
    *,
    hero_id: int,
    localized_name: str,
    internal_name: str,
    source_patch: str,
    generator_version: str,
    liquipedia_roles: list[str],
    mechanical: MechanicalExtraction,
    positions_pro: PositionBlock,
    synergies_pro: list[StatisticalEdge],
    counters_pro: list[StatisticalEdge],
    reasons_by_edge: dict[tuple[str, int], tuple[str, dict]],  # (relation, other_id) -> (reason, provenance)
    meta_pro: MetaBlock,
    meta_history: list[MetaHistoryEntry],
    statistical_provenance: dict,
    liquipedia_snapshot: str,
) -> HeroDerived:
    def wrap(edges: list[StatisticalEdge], relation: str) -> list[StatEdge]:
        out: list[StatEdge] = []
        for e in edges:
            reason_tuple = reasons_by_edge.get((relation, e.hero_id))
            reason, prov = reason_tuple if reason_tuple else (None, None)
            out.append(_stat_to_edge(e, reason, prov))
        return out

    return HeroDerived(
        schema_version=1,
        generator_version=generator_version,
        source_patch=source_patch,
        generated_at=datetime.now(timezone.utc).isoformat(timespec="seconds"),
        hero_id=hero_id,
        localized_name=localized_name,
        internal_name=internal_name,
        liquipedia_roles=liquipedia_roles,
        functional_tags=mechanical.functional_tags,
        tag_sources=[TagSource(**s.__dict__) for s in mechanical.tag_sources],
        positions={"pro": positions_pro},
        synergies={"pro": wrap(synergies_pro, "synergy")},
        counters={"pro": wrap(counters_pro, "counter")},
        meta={"pro": meta_pro},
        meta_history=meta_history,
        provenance=Provenance(
            mechanical={
                "model": mechanical.model,
                "prompt_version": mechanical.prompt_version,
                "prompt_hash": mechanical.prompt_hash,
                "input_hash": mechanical.input_hash,
                "extracted_at": mechanical.extracted_at,
                "liquipedia_snapshot": liquipedia_snapshot,
            },
            statistical={"pro": statistical_provenance},
        ),
    )
```

- [ ] **Step 3: Write `src/invoker/pipeline/orchestrator.py`**

End-to-end pipeline for one patch. Accepts injected fetchers and LLM client so tests can run offline.

```python
from __future__ import annotations

import asyncio
from dataclasses import dataclass
from pathlib import Path

from invoker.graph import build_graph, cache_graph
from invoker.llm import LLMClient
from invoker.pipeline.assemble import assemble_hero
from invoker.pipeline.derive import (
    MetaTier, PositionStats, confidence_for, merge_matchups, meta_tier, position_weights,
)
from invoker.pipeline.extract import HeroExtractionInput, extract_mechanical
from invoker.pipeline.manifest import build_manifest, write_manifest
from invoker.pipeline.reason import (
    ReasonInput, generate_counter_reason, generate_synergy_reason, validate_grounding,
)
from invoker.pipeline.summarize import write_summary
from invoker.pipeline.validators import ValidationContext, validate_hero
from invoker.pipeline.writer import write_hero
from invoker.schemas.derived import MetaBlock, MetaHistoryEntry, PositionBlock


@dataclass
class HeroRawBundle:
    hero_id: int
    localized_name: str
    internal_name: str
    liquipedia_roles: list[str]
    abilities: list[dict]                       # for extraction input
    stratz_edges: list[dict] | None             # from stratz.synergies
    opendota_matchups: list[dict] | None
    position_counts: dict[str, int]
    total_pro_games: int
    window_days: int
    contest_rate: float
    win_rate: float
    meta_history: list[MetaHistoryEntry]
    liquipedia_snapshot: str


def run_for_hero(
    data_dir: Path,
    patch: str,
    generator_version: str,
    bundle: HeroRawBundle,
    client: LLMClient,
) -> None:
    mech = extract_mechanical(
        HeroExtractionInput(
            hero_id=bundle.hero_id,
            hero_name=bundle.localized_name,
            liquipedia_roles=bundle.liquipedia_roles,
            abilities=bundle.abilities,
        ),
        client,
    )

    synergies, counters = merge_matchups(
        bundle.stratz_edges, bundle.opendota_matchups, hero_id=bundle.hero_id
    )

    reasons: dict[tuple[str, int], tuple[str, dict]] = {}
    for e in synergies + counters:
        if e.confidence not in ("med", "high"):
            continue
        relation = "synergy" if e in synergies else "counter"
        inp = ReasonInput(
            hero_a_id=bundle.hero_id,
            hero_a_name=bundle.localized_name,
            hero_a_tags=mech.functional_tags,
            hero_b_id=e.hero_id,
            hero_b_name=f"hero_{e.hero_id}",
            hero_b_tags=[],
            score=e.score or 0.0,
            games=e.games,
        )
        gen = generate_synergy_reason if relation == "synergy" else generate_counter_reason
        out = gen(inp, client)
        try:
            validate_grounding(out.reason, mech.functional_tags, [])
        except Exception:
            # Skip ungrounded reasons; edge keeps reason=None.
            continue
        reasons[(relation, e.hero_id)] = (
            out.reason,
            {"model": out.model, "prompt_version": out.prompt_version},
        )

    hero = assemble_hero(
        hero_id=bundle.hero_id,
        localized_name=bundle.localized_name,
        internal_name=bundle.internal_name,
        source_patch=patch,
        generator_version=generator_version,
        liquipedia_roles=bundle.liquipedia_roles,
        mechanical=mech,
        positions_pro=PositionBlock(
            weights=position_weights(bundle.position_counts),
            games=bundle.total_pro_games,
            window_days=bundle.window_days,
        ),
        synergies_pro=synergies,
        counters_pro=counters,
        reasons_by_edge=reasons,
        meta_pro=MetaBlock(
            contest_rate=bundle.contest_rate,
            win_rate=bundle.win_rate,
            tier=meta_tier(bundle.contest_rate, bundle.win_rate),
            games=bundle.total_pro_games,
        ),
        meta_history=bundle.meta_history,
        statistical_provenance={"window_days": bundle.window_days},
        liquipedia_snapshot=bundle.liquipedia_snapshot,
    )

    write_hero(data_dir, patch, hero)
    write_summary(data_dir, hero, "pro")


def finalize_patch(
    data_dir: Path,
    patch: str,
    hero_ids: list[int],
    *,
    complete: bool = True,
) -> None:
    from invoker.pipeline.writer import read_hero

    ctx = ValidationContext(roster_hero_ids=set(hero_ids))
    for hid in hero_ids:
        validate_hero(read_hero(data_dir, patch, hid), ctx)

    m = build_manifest(data_dir, patch, hero_ids, ["pro"], complete=complete)
    write_manifest(data_dir, m)

    g = build_graph(data_dir, patch, hero_ids)
    cache_graph(data_dir, patch, g)
```

- [ ] **Step 4: Write `tests/test_orchestrator.py`**

Uses a fake LLM to exercise the full pipeline offline. No network, no real keys.

```python
import json
from pathlib import Path

from invoker.kb import KnowledgeBase
from invoker.llm.client import LLMResponse
from invoker.pipeline.orchestrator import HeroRawBundle, finalize_patch, run_for_hero


class ScriptedClient:
    """LLM that returns preset outputs based on prompt content."""
    model_name = "scripted"

    def complete_json(self, prompt: str, *, prompt_version: int) -> LLMResponse:
        if "functional_tags" in prompt:
            return LLMResponse(
                text=json.dumps({
                    "functional_tags": ["armor_reduction", "single_target_disable", "initiation"],
                    "tag_sources": [
                        {"tag": "armor_reduction", "ability": "Corrosive Haze", "evidence": "reduces armor"},
                        {"tag": "single_target_disable", "ability": "Slithereen Crush", "evidence": "stuns 1.6s"},
                        {"tag": "initiation", "ability": "Slithereen Crush", "evidence": "blink-in AoE stun"},
                    ],
                }),
                model="scripted", prompt_version=prompt_version,
            )
        if "synergy" in prompt.lower():
            return LLMResponse(
                text=json.dumps({"reason": "Armor reduction amplifies physical damage output."}),
                model="scripted", prompt_version=prompt_version,
            )
        return LLMResponse(
            text=json.dumps({"reason": "Natural single_target_disable resists ganks."}),
            model="scripted", prompt_version=prompt_version,
        )


def test_orchestrator_produces_valid_hero(tmp_path: Path):
    bundle = HeroRawBundle(
        hero_id=28,
        localized_name="Slardar",
        internal_name="npc_dota_hero_slardar",
        liquipedia_roles=["Initiator", "Disabler"],
        abilities=[
            {"name": "Slithereen Crush", "text": "AoE stun with armor reduction"},
            {"name": "Corrosive Haze", "text": "Armor reduction debuff"},
        ],
        stratz_edges=[{"heroId1": 28, "heroId2": 120, "synergy": 0.08, "matchCount": 50}],
        opendota_matchups=[{"hero_id": 96, "games_played": 34, "wins": 12}],
        position_counts={"1": 0, "2": 0, "3": 34, "4": 0, "5": 0},
        total_pro_games=34,
        window_days=90,
        contest_rate=0.12,
        win_rate=0.51,
        meta_history=[],
        liquipedia_snapshot="liquipedia:Slardar@test",
    )
    run_for_hero(tmp_path, "7.41b", "invoker@test", bundle, ScriptedClient())
    finalize_patch(tmp_path, "7.41b", [28, 120, 96], complete=True)

    kb = KnowledgeBase(patch="7.41b", bracket="pro", data_dir=tmp_path)
    h = kb.hero(28)
    assert h.localized_name == "Slardar"
    assert "armor_reduction" in h.functional_tags
    assert len(h.synergies["pro"]) == 1
    assert h.synergies["pro"][0].reason is not None
```

- [ ] **Step 5: Replace `src/invoker/cli.py`**

```python
from __future__ import annotations

import asyncio
import json
from pathlib import Path

import typer

from invoker import __version__
from invoker.config import Config
from invoker.paths import manifest_file

app = typer.Typer(help="Invoker — Dota 2 knowledge framework")


@app.command()
def version() -> None:
    typer.echo(f"invoker {__version__}")


@app.command()
def bootstrap(
    patch: str = typer.Option(..., help="Patch string, e.g. 7.41b"),
    force: bool = typer.Option(False, help="Ignore caches and refetch."),
    heroes: str | None = typer.Option(None, help="Comma-separated hero_ids (dev: limit scope)."),
    skip_extract: bool = typer.Option(False, help="Skip LLM extraction; use last run."),
) -> None:
    """Run the full bootstrap pipeline for a patch."""
    from invoker.pipeline.fetch import fetch_all

    cfg = Config.load()
    typer.echo(f"Fetching raw data for {patch}...")
    raw = asyncio.run(fetch_all(cfg, patch, force=force))
    typer.echo(f"Fetched {len(raw['heroes'])} heroes.")

    # Assemble HeroRawBundle per hero from `raw`, then run the orchestrator per hero,
    # then finalize_patch. The bundle-assembly step is a straight mapping from raw
    # fetches to HeroRawBundle fields; implement it as a small private helper in this
    # file the first time you run against real data. Offline coverage is in
    # tests/test_orchestrator.py (Task 18 step 4).
    typer.echo(
        "Run programmatically via invoker.pipeline.orchestrator.run_for_hero + "
        "finalize_patch until the bundle-assembly helper lands."
    )


@app.command()
def status(patch: str = typer.Option(..., help="Patch to inspect.")) -> None:
    cfg = Config.load()
    p = manifest_file(cfg.data_dir, patch)
    if not p.exists():
        typer.echo(f"No manifest for {patch}.")
        raise typer.Exit(code=1)
    typer.echo(p.read_text())


@app.command()
def validate(patch: str = typer.Option(..., help="Patch to validate.")) -> None:
    from invoker.pipeline.validators import ValidationContext, validate_hero
    from invoker.pipeline.writer import read_hero

    cfg = Config.load()
    m = json.loads(manifest_file(cfg.data_dir, patch).read_text())
    ids = {e["hero_id"] for e in m.get("heroes", [])}
    ctx = ValidationContext(roster_hero_ids=ids)
    failures = 0
    for entry in m["heroes"]:
        try:
            validate_hero(read_hero(cfg.data_dir, patch, entry["hero_id"]), ctx)
        except Exception as e:
            typer.echo(f"✗ hero {entry['hero_id']}: {e}")
            failures += 1
    typer.echo(f"{len(m['heroes']) - failures}/{len(m['heroes'])} heroes validated.")
    if failures:
        raise typer.Exit(code=1)


@app.command()
def publish(patch: str = typer.Option(..., help="Patch to bundle.")) -> None:
    import tarfile
    from invoker.paths import derived_patch_dir, dist_file

    cfg = Config.load()
    src = derived_patch_dir(cfg.data_dir, patch)
    if not src.exists():
        typer.echo(f"No derived data for {patch}.")
        raise typer.Exit(code=1)
    dst = dist_file(cfg.data_dir, patch)
    dst.parent.mkdir(parents=True, exist_ok=True)
    with tarfile.open(dst, "w:gz") as tar:
        tar.add(src, arcname=f"invoker-kb-{patch}")
    typer.echo(f"Wrote {dst}")


if __name__ == "__main__":
    app()
```

> **Note:** the `bootstrap` command intentionally leaves extract/reason/derive/summarize orchestration as a placeholder for now. Task 20 wires those together end-to-end on a small hero subset; promoting that into the CLI is the first Phase 1.5 task.

- [ ] **Step 6: Run the orchestrator test and smoke the CLI**

```bash
uv run pytest tests/test_orchestrator.py -v
uv run invoker --help
uv run invoker version
```

Expected: orchestrator test passes; help text + version line.

- [ ] **Step 7: Commit**

```bash
git add src/invoker/pipeline/fetch.py src/invoker/pipeline/assemble.py src/invoker/pipeline/orchestrator.py src/invoker/cli.py tests/test_orchestrator.py
git commit -m "feat: end-to-end orchestrator + bootstrap/status/validate/publish CLI"
```

---

## Task 19: Gold-set regression harness

**Files:**
- Create: `tests/fixtures/gold/slardar.json` (example), `tests/fixtures/gold/README.md`, `tests/test_gold.py`

- [ ] **Step 1: Seed one gold file**

`tests/fixtures/gold/slardar.json`:

```json
{
  "hero_id": 28,
  "hero_name": "Slardar",
  "expected_tags": [
    "armor_reduction",
    "single_target_disable",
    "physical_damage_amplifier",
    "initiation",
    "vision_control"
  ],
  "forbidden_tags": [
    "big_burst",
    "sustained_magical"
  ]
}
```

- [ ] **Step 2: Write `tests/fixtures/gold/README.md`**

Document what a gold entry means and how to add one. Keep under 30 lines.

```markdown
# Gold Set

Each file is a hand-labeled expected mechanical extraction for one hero.
Used as a regression harness for prompt changes.

## Fields
- `hero_id`: int
- `hero_name`: display name
- `expected_tags`: tags the extractor MUST produce (missing any → regression)
- `forbidden_tags`: tags the extractor MUST NOT produce (false positive → regression)

## Adding a hero
1. Pick 1–3 heroes per archetype (carry, support, pusher, tempo mid, tank).
2. Hand-label `expected_tags` from the taxonomy.
3. Add any tags you explicitly reject under `forbidden_tags`.
4. Run `pytest tests/test_gold.py`.

## Target coverage for Phase 1
15–20 heroes across all roles.
```

- [ ] **Step 3: Write `tests/test_gold.py`**

This test is skipped by default (requires a real Gemini key) but is the regression gate for prompt changes.

```python
import json
import os
from pathlib import Path

import pytest

GOLD_DIR = Path(__file__).parent / "fixtures" / "gold"


@pytest.mark.skipif(not os.environ.get("INVOKER_RUN_LIVE_LLM"), reason="live LLM disabled")
@pytest.mark.parametrize("gold_file", [p for p in GOLD_DIR.glob("*.json")])
def test_gold_hero(gold_file: Path):
    from invoker.llm import make_client
    from invoker.pipeline.extract import HeroExtractionInput, extract_mechanical

    gold = json.loads(gold_file.read_text())
    # TODO: replace with real hero input from live data once fetchers are wired.
    # For now, this test documents the contract; it is gated behind INVOKER_RUN_LIVE_LLM.
    pytest.skip("live fetchers not yet wired — contract only")
```

- [ ] **Step 4: Commit**

```bash
git add tests/fixtures/gold tests/test_gold.py
git commit -m "feat: gold-set regression harness scaffold"
```

---

## Task 20: End-to-end smoke test

**Files:**
- Create: `tests/test_bootstrap_smoke.py`

- [ ] **Step 1: Write `tests/test_bootstrap_smoke.py`**

Exercises the pipeline on a hand-assembled hero (no live API calls, no live LLM).

```python
from pathlib import Path

from invoker.graph import build_graph, cache_graph
from invoker.kb import KnowledgeBase
from invoker.pipeline.manifest import build_manifest, write_manifest
from invoker.pipeline.summarize import write_summary
from invoker.pipeline.validators import ValidationContext, validate_hero
from invoker.pipeline.writer import write_hero
from tests.test_summarize import _hero


def test_full_pipeline_on_one_hero(tmp_path: Path):
    h = _hero()

    # Write per-hero file
    write_hero(tmp_path, "7.41b", h)

    # Validate it
    ctx = ValidationContext(roster_hero_ids={28, 120, 96})
    validate_hero(h, ctx)

    # Summarize
    summary_path = write_summary(tmp_path, h, "pro")
    assert summary_path.exists()

    # Manifest
    m = build_manifest(tmp_path, "7.41b", [h.hero_id], ["pro"], complete=True)
    write_manifest(tmp_path, m)

    # Graph
    g = build_graph(tmp_path, "7.41b", [h.hero_id])
    cache_graph(tmp_path, "7.41b", g)

    # KB
    kb = KnowledgeBase(patch="7.41b", bracket="pro", data_dir=tmp_path)
    assert kb.hero(28).localized_name == "Slardar"
    assert len(kb.synergies(28, min_confidence="med")) == 1
    assert "Slardar" in kb.summary(28)
```

- [ ] **Step 2: Run**

```bash
uv run pytest tests/test_bootstrap_smoke.py -v
```

Expected: pass. This proves the offline pipeline is wired end-to-end.

- [ ] **Step 3: Commit**

```bash
git add tests/test_bootstrap_smoke.py
git commit -m "test: end-to-end smoke test of offline pipeline"
```

---

## Task 21: README

**Files:**
- Create: `README.md`

- [ ] **Step 1: Write `README.md`**

```markdown
# Invoker

Knowledge base framework for Dota 2 fundamentals — structured, patch-aware, LLM-consumable knowledge for downstream drafting and replay agents.

## What's here

The repo ships as a framework with **no data**. All knowledge is bootstrapped from public sources (OpenDota, STRATZ, Liquipedia) and enriched with LLM-extracted mechanical tags.

## Quick start

```bash
uv sync
cp .env.example .env                # fill in keys
uv run invoker --help
uv run invoker bootstrap --patch 7.41b
```

## Docs

- `GUIDELINES.md` — project rules (living)
- `CLAUDE.md` — AI collaboration rules
- `docs/specs/` — architecture design docs
- `docs/plans/` — implementation plans

## License

Private.
```

- [ ] **Step 2: Commit**

```bash
git add README.md
git commit -m "docs: README"
```

---

## Completion

When every task above is checked:

```bash
uv run pytest                    # full suite should pass
uv run ruff check src tests      # clean
uv run pyright                   # clean
git log --oneline                # history should tell a clean story
git push
```

Phase 1 is complete when:
- `uv run invoker --help` shows bootstrap / status / validate / publish.
- The offline smoke test (Task 20) passes.
- Individual pipeline modules are exercised by their own tests.
- The full `invoker bootstrap --patch <v>` flow, running against live APIs and a live LLM, is deferred to the first Phase 1.5 task (wiring the orchestrator).
- A later roadmap phase should add self-evolving support for downstream drafting agents: `invoker` should emit stable critique/evidence artifacts that can feed agent self-review and proposal generation, but any learned update path must remain human-reviewed and reproducible.
