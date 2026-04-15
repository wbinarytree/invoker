"""
Quick probe: fetch Pangolier ability data from OpenDota constants + STRATZ synergies.
Run with:  uv run python scripts/probe_pangolier.py
"""

from __future__ import annotations

import asyncio
import json
import os
from pathlib import Path

from invoker.config import Config
from invoker.sources.opendota import OpenDotaFetcher
from invoker.sources.stratz import StratzFetcher

PATCH = "7.41b"
PANGOLIER_NAME = "npc_dota_hero_pangolier"


async def main() -> None:
    cfg = Config.load()
    cache = cfg.data_dir / "raw"
    od = OpenDotaFetcher(cache, PATCH)
    strat = StratzFetcher(cache, PATCH, cfg.stratz_token)

    try:
        # --- Find Pangolier's hero_id ---
        heroes = await od.heroes()
        pango = next(h for h in heroes if "pangolier" in h["localized_name"].lower())
        hero_id = pango["id"]
        print(f"=== Pangolier hero_id={hero_id} ===\n")

        # --- OpenDota ability descriptions ---
        all_abilities = await od.abilities()
        hero_ability_map = await od.hero_abilities_map()

        ability_names = hero_ability_map.get(PANGOLIER_NAME, {}).get("abilities", [])
        print(f"Ability keys from hero_abilities_map: {ability_names}\n")

        print("--- OpenDota ability descriptions ---")
        for key in ability_names:
            a = all_abilities.get(key, {})
            print(f"\n[{key}]")
            print(f"  dname : {a.get('dname', '(none)')}")
            print(f"  desc  : {a.get('desc', '(none)')[:300]}")
            attrib = a.get("attrib", [])
            if attrib:
                print(f"  attrib: {json.dumps(attrib[:4], indent=2)}")

        # --- STRATZ synergies for Pangolier ---
        if strat.available:
            print("\n--- STRATZ synergies (tournament, top 5 by synergy score) ---")
            data = await strat.synergies(hero_id)
            if data:
                edges = (
                    data.get("data", {})
                    .get("heroStats", {})
                    .get("heroVsHeroMatchup", {})
                    .get("advantage", [])
                )
                top = sorted(edges, key=lambda e: e.get("synergy", 0), reverse=True)[:5]
                for e in top:
                    print(f"  hero_id={e.get('heroId2')}  synergy={e.get('synergy', 0):.3f}  games={e.get('matchCount')}")
        else:
            print("\n[STRATZ] No token — skipping synergy fetch.")

        # --- Matchups sample ---
        print("\n--- OpenDota matchups (top 5 counter win-rate) ---")
        matchups = await od.matchups(hero_id)
        top_counters = sorted(matchups, key=lambda m: m.get("wins", 0) / max(m.get("games_played", 1), 1))[:5]
        for m in top_counters:
            wr = m["wins"] / max(m["games_played"], 1)
            print(f"  vs hero_id={m['hero_id']}  games={m['games_played']}  win_rate={wr:.2f}")

    finally:
        await od.close()
        await strat.close()


asyncio.run(main())
