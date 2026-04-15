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
        for cell in soup.find_all(["th", "td"]):
            label = cell.get_text(strip=True).lower().rstrip(":")
            if label in {"role", "roles"}:
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
        """Extract ability names + first spelldesc of their descriptions from spellcard sections."""
        html = page.get("parse", {}).get("text", {}).get("*", "")
        if not html:
            return []
        soup = BeautifulSoup(html, "html.parser")
        abilities: list[dict[str, str]] = []
        skip = {"ability", "talent", "talents", "aghanim's", "hero model", "seaborn sentinel"}
        for heading_div in soup.find_all("div", class_="mw-heading3"):
            h3 = heading_div.find("h3")
            if not h3:
                continue
            name = re.sub(r"\s+", " ", h3.get_text()).strip()
            if not name or name.lower() in skip:
                continue
            card = heading_div.find_next_sibling("div", class_="spellcard-wrapper")
            if not card:
                continue
            desc_el = card.find("div", class_="spelldesc")
            if desc_el:
                text = re.sub(r"\s+", " ", desc_el.get_text()).strip()
                if text:
                    abilities.append({"name": name, "text": text})
        return abilities

    async def close(self) -> None:
        await self.client.close()
