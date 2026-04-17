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
