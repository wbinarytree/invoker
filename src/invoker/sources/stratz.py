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
