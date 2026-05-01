from __future__ import annotations

from pathlib import Path

from invoker import __version__
from invoker.http import SharedOpenDotaCachedClient

BASE = "https://api.opendota.com/api"


class OpenDotaFetcher:
    def __init__(self, cache_root: Path, patch: str) -> None:
        self.client = SharedOpenDotaCachedClient(
            cache_root,
            fetched_by=f"invoker@{__version__}",
            source_patch=None,
        )

    async def matchups(self, hero_id: int) -> list[dict]:
        return await self.client.get(f"{BASE}/heroes/{hero_id}/matchups")

    async def pro_matches(self, less_than_match_id: int | None = None) -> list[dict]:
        params = {}
        if less_than_match_id is not None:
            params["less_than_match_id"] = less_than_match_id
        return await self.client.get(f"{BASE}/proMatches", params=params or None)

    async def team_matches(self, team_id: int, *, force: bool = False) -> list[dict]:
        return await self.client.get(f"{BASE}/teams/{team_id}/matches", force=force)

    async def match_detail(self, match_id: int, *, force: bool = False) -> dict:
        return await self.client.get(f"{BASE}/matches/{match_id}", force=force)

    async def constants_patch(self) -> list[dict]:
        return await self.client.get(f"{BASE}/constants/patch")

    async def close(self) -> None:
        await self.client.close()
