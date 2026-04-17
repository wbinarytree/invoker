from invoker.taxonomy import load_taxonomy


def test_taxonomy_loads():
    t = load_taxonomy()
    assert t.version >= 1
    assert t.has("armor_reduction")
    assert "Corrosive" not in t.as_prompt_block()


def test_taxonomy_has_minimum_coverage():
    t = load_taxonomy()
    required = {"single_target_disable", "armor_reduction", "initiation", "save", "sustain"}
    assert required <= set(t.tags)
