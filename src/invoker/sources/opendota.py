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

    async def hero_stats(self) -> dict[str, Any]:
        """Hero stat constants keyed by internal name."""
        return await self.client.get(f"{BASE}/constants/heroes")

    async def matchups(self, hero_id: int) -> list[dict[str, Any]]:
        return await self.client.get(f"{BASE}/heroes/{hero_id}/matchups")

    async def pro_matches(self, less_than_match_id: int | None = None) -> list[dict[str, Any]]:
        params = {}
        if less_than_match_id is not None:
            params["less_than_match_id"] = less_than_match_id
        return await self.client.get(f"{BASE}/proMatches", params=params or None)

    async def close(self) -> None:
        await self.client.close()
