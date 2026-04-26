import pytest

from invoker.kg.mechanism_primer import (
    MechanismPrimerContext,
    MechanismPrimerError,
    load_mechanism_primer,
)


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


def test_load_mechanism_primer_rejects_invalid_mechanics(tmp_path):
    bad = tmp_path / "mechanism_primer_test.yaml"
    bad.write_text("patch: test\nmechanics:\n  - stat: strength\n")
    import invoker.kg.mechanism_primer as mp
    original = mp._PRIMER_DIR
    mp._PRIMER_DIR = tmp_path
    try:
        with pytest.raises(MechanismPrimerError, match="contributions"):
            load_mechanism_primer("test")
    finally:
        mp._PRIMER_DIR = original
