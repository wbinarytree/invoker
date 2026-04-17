import pytest

from invoker.pipeline.validators import ValidationContext, ValidationError, validate_hero

from ...support.factories import make_hero

CTX = ValidationContext(roster_hero_ids={28, 120, 96})


def test_valid_hero_passes():
    validate_hero(make_hero(), CTX)


def test_unknown_tag_rejected():
    h = make_hero()
    h.functional_tags.append("not_a_real_tag")
    with pytest.raises(ValidationError, match="taxonomy"):
        validate_hero(h, CTX)


def test_missing_tag_source_rejected():
    h = make_hero()
    h.functional_tags.append("initiation")
    with pytest.raises(ValidationError, match="tag_sources"):
        validate_hero(h, CTX)


def test_ungrounded_reason_rejected():
    h = make_hero()
    h.synergies["pro"][0].reason = "they just win a lot"
    with pytest.raises(ValidationError, match="not grounded"):
        validate_hero(h, CTX)


def test_confidence_mismatch_rejected():
    h = make_hero()
    h.synergies["pro"][0].games = 5
    with pytest.raises(ValidationError, match="confidence"):
        validate_hero(h, CTX)


def test_unknown_hero_id_edge_rejected():
    h = make_hero()
    h.synergies["pro"][0].hero_id = 9999
    with pytest.raises(ValidationError, match="unknown hero"):
        validate_hero(h, CTX)
