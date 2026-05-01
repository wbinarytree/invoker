from __future__ import annotations

from pathlib import Path
from typing import Any

from invoker.http import STRATZ, CachedClient

ENDPOINT = "https://api.stratz.com/graphql"

MATCHUP_QUERY = """
query HeroMatchup($heroId: Short!, $bracket: [RankBracketBasicEnum!]) {
  heroStats {
    matchUp(heroId: $heroId, bracketBasicIds: $bracket) {
      heroId
      matchCountWith
      matchCountVs
      with { heroId1 heroId2 synergy matchCount winsAverage winRateHeroId1 winRateHeroId2 }
      vs   { heroId1 heroId2 synergy matchCount winsAverage winRateHeroId1 winRateHeroId2 }
    }
  }
}
"""

PLAYER_POSITION_QUERY = """
query PlayerPosition($steamAccountId: Long!) {
  player(steamAccountId: $steamAccountId) {
    identity { name }
    steamAccount {
      proSteamAccount { id realName name position }
    }
  }
}
"""


def _normalize_position(value: Any) -> int | None:
    if isinstance(value, bool):
        return None
    if isinstance(value, int) and 1 <= value <= 5:
        return value
    if isinstance(value, str):
        digits = "".join(c for c in value if c.isdigit())
        if digits:
            number = int(digits)
            if 1 <= number <= 5:
                return number
    return None


def flatten_edges(response: dict[str, Any], hero_id: int) -> list[dict[str, Any]]:
    """
    Flatten the matchUp response into a list of edge dicts compatible with merge_matchups.

    with entries  → positive synergy score  (synergy partners)
    vs entries    → negated synergy score   (counter/disadvantage edges)
    """
    rows = (
        response.get("data", {})
        .get("heroStats", {})
        .get("matchUp", [])
    )
    edges: list[dict[str, Any]] = []
    for row in rows:
        if row.get("heroId") != hero_id:
            continue
        for e in row.get("with", []):
            edges.append({
                "heroId1": e["heroId1"],
                "heroId2": e["heroId2"],
                "synergy": e["synergy"],
                "matchCount": e["matchCount"],
                "winsAverage": e.get("winsAverage"),
            })
        for e in row.get("vs", []):
            edges.append({
                "heroId1": e["heroId1"],
                "heroId2": e["heroId2"],
                "synergy": -e["synergy"],
                "matchCount": e["matchCount"],
                "winsAverage": e.get("winsAverage"),
            })
    return edges


class StratzFetcher:
    def __init__(self, cache_root: Path, patch: str, token: str | None) -> None:
        headers = {"User-Agent": "STRATZ_API"}
        if token:
            headers["Authorization"] = f"Bearer {token}"
        self.client = CachedClient(STRATZ, cache_root, patch, headers=headers)
        self.available = token is not None

    async def synergies(self, hero_id: int) -> list[dict[str, Any]] | None:
        """Return flat edge dicts for hero_id, or None if no token."""
        if not self.available:
            return None
        payload = {
            "query": MATCHUP_QUERY,
            "variables": {"heroId": hero_id},
        }
        response = await self.client.post(ENDPOINT, body=payload)
        return flatten_edges(response, hero_id)

    async def player_position(
        self, account_id: int, *, force: bool = False
    ) -> int | None:
        """Return STRATZ-curated pro position 1..5 for the account, or None.

        Returns None when no token is configured, when the player is not on a
        pro roster, or when STRATZ has no position recorded for them.
        """
        if not self.available:
            return None
        payload = {
            "query": PLAYER_POSITION_QUERY,
            "variables": {"steamAccountId": account_id},
        }
        response = await self.client.post(ENDPOINT, body=payload, force=force)
        if not isinstance(response, dict):
            return None
        data = response.get("data") or {}
        player = data.get("player") or {}
        steam_account = player.get("steamAccount") or {}
        pro = steam_account.get("proSteamAccount") or {}
        return _normalize_position(pro.get("position"))

    async def close(self) -> None:
        await self.client.close()
