from invoker.kg.mechanism_primer import MechanismPrimerContext, load_mechanism_primer


def test_load_mechanism_primer_known_patch():
    result = load_mechanism_primer("7.41b")
    assert isinstance(result, MechanismPrimerContext)
    assert result.patch == "7.41b"
    assert len(result.mechanics) > 0
    stats = [m["stat"] for m in result.mechanics]
    assert "strength" in stats
    assert "agility" in stats
    assert "intelligence" in stats


def test_load_mechanism_primer_unknown_patch_returns_empty():
    result = load_mechanism_primer("0.00")
    assert result.patch == "0.00"
    assert result.mechanics == []
