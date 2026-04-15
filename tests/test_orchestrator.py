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
                text=json.dumps(
                    {
                        "functional_tags": [
                            "armor_reduction",
                            "single_target_disable",
                            "initiation",
                        ],
                        "tag_sources": [
                            {
                                "tag": "armor_reduction",
                                "ability": "Corrosive Haze",
                                "evidence": "reduces armor",
                            },
                            {
                                "tag": "single_target_disable",
                                "ability": "Slithereen Crush",
                                "evidence": "stuns 1.6s",
                            },
                            {
                                "tag": "initiation",
                                "ability": "Slithereen Crush",
                                "evidence": "blink-in AoE stun",
                            },
                        ],
                    }
                ),
                model="scripted",
                prompt_version=prompt_version,
            )
        if "synergy" in prompt.lower():
            return LLMResponse(
                text=json.dumps({"reason": "Armor reduction amplifies physical damage output."}),
                model="scripted",
                prompt_version=prompt_version,
            )
        return LLMResponse(
            text=json.dumps({"reason": "Natural single_target_disable resists ganks."}),
            model="scripted",
            prompt_version=prompt_version,
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
