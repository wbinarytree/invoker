import json
from pathlib import Path

from invoker.kb import KnowledgeBase
from invoker.llm.client import LLMResponse
from invoker.pipeline.orchestrator import HeroRawBundle, finalize_patch, run_for_hero


class ScriptedClient:
    """LLM that returns preset outputs based on prompt content."""

    model_name = "scripted"

    def generate_json(
        self,
        prompt: str,
        *,
        prompt_version: int,
        schema: object | None = None,
        cache_tag: str | None = None,
    ) -> LLMResponse:
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
        # Batch reason prompt: extract hero_b_ids and return one reason per edge.
        import re
        ids = [int(m) for m in re.findall(r"hero_b_id=(\d+)", prompt)]
        return LLMResponse(
            text=json.dumps(
                [
                    {
                        "hero_b_id": hid,
                        "reason": (
                            "Armor reduction amplifies "
                            f"single_target_disable against {hid}."
                        ),
                    }
                    for hid in ids
                ]
            ),
            model="scripted",
            prompt_version=prompt_version,
        )


def _slardar_bundle() -> HeroRawBundle:
    return HeroRawBundle(
        hero_id=28,
        localized_name="Slardar",
        internal_name="npc_dota_hero_slardar",
        roles=["Initiator", "Disabler"],
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
    )


def test_orchestrator_produces_valid_hero(tmp_path: Path):
    bundle = _slardar_bundle()
    run_for_hero(tmp_path, "7.41b", "invoker@test", bundle, ScriptedClient())
    finalize_patch(tmp_path, "7.41b", [28, 120, 96], complete=True)

    kb = KnowledgeBase(patch="7.41b", bracket="pro", data_dir=tmp_path)
    h = kb.hero(28)
    assert h.localized_name == "Slardar"
    assert "armor_reduction" in h.functional_tags
    assert len(h.synergies["pro"]) == 1
    assert h.synergies["pro"][0].reason is not None


def test_skip_reasons_emits_no_reason_calls(tmp_path: Path):
    class CountingClient(ScriptedClient):
        def __init__(self) -> None:
            self.reason_calls = 0
            self.extract_calls = 0

        def generate_json(self, prompt, **kwargs):
            if "functional_tags" in prompt:
                self.extract_calls += 1
            else:
                self.reason_calls += 1
            return super().generate_json(prompt, **kwargs)

    client = CountingClient()
    result = run_for_hero(
        tmp_path, "7.41b", "invoker@test", _slardar_bundle(), client, skip_reasons=True
    )
    assert result.success
    assert result.reasons_written == 0
    assert client.extract_calls == 1
    assert client.reason_calls == 0
    finalize_patch(tmp_path, "7.41b", [28, 120, 96], complete=True)

    kb = KnowledgeBase(patch="7.41b", bracket="pro", data_dir=tmp_path)
    assert kb.hero(28).synergies["pro"][0].reason is None


def test_max_reason_edges_caps_candidates(tmp_path: Path):
    bundle = _slardar_bundle()
    bundle.opendota_matchups = None
    bundle.stratz_edges = [
        {"heroId1": 28, "heroId2": hid, "synergy": 0.1 - 0.001 * i, "matchCount": 50}
        for i, hid in enumerate([120, 121, 122, 123, 124, 125, 126])
    ]

    class CountingClient(ScriptedClient):
        def __init__(self) -> None:
            self.batch_edge_count = 0

        def generate_json(self, prompt, **kwargs):
            if "hero_b_id" in prompt:
                import re
                self.batch_edge_count = len(re.findall(r"hero_b_id=", prompt))
            return super().generate_json(prompt, **kwargs)

    client = CountingClient()
    run_for_hero(
        tmp_path, "7.41b", "invoker@test", bundle, client, max_edges=3
    )
    assert client.batch_edge_count == 3
