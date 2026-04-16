import json

from invoker.llm.client import LLMResponse
from invoker.pipeline.extract import HeroExtractionInput, extract_mechanical


class FakeClient:
    model_name = "fake"

    def complete_json(self, prompt: str, *, prompt_version: int) -> LLMResponse:
        return LLMResponse(
            text=json.dumps(
                {
                    "functional_tags": ["armor_reduction", "single_target_disable"],
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
                    ],
                }
            ),
            model="fake",
            prompt_version=prompt_version,
        )


def test_extract_returns_parsed_tags():
    inp = HeroExtractionInput(
        hero_id=28,
        hero_name="Slardar",
        roles=["Initiator", "Disabler"],
        abilities=[
            {"name": "Slithereen Crush", "text": "AoE stun"},
            {"name": "Corrosive Haze", "text": "Armor reduction"},
        ],
    )
    result = extract_mechanical(inp, FakeClient())
    assert "armor_reduction" in result.functional_tags
    assert result.input_hash.startswith("sha256:")
    assert result.prompt_version >= 1
