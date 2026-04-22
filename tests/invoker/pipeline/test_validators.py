import pytest

from invoker.pipeline.validators import ValidationContext, ValidationError, validate_hero

from ...support.factories import make_hero

CTX = ValidationContext(roster_hero_ids={28, 120, 96})


def test_valid_hero_passes():
    validate_hero(make_hero(), CTX)


def test_duplicate_feature_rejected():
    h = make_hero()
    h.capabilities.append(h.capabilities[0])
    with pytest.raises(ValidationError, match="duplicate"):
        validate_hero(h, CTX)


def test_score_out_of_range_rejected():
    h = make_hero()
    h.capabilities[0].score = 1.2
    with pytest.raises(ValidationError, match="score out of range"):
        validate_hero(h, CTX)


def test_role_distribution_out_of_range_rejected():
    h = make_hero()
    h.role_distribution["offlane"] = 1.2
    with pytest.raises(ValidationError, match="role_distribution"):
        validate_hero(h, CTX)


def test_role_distribution_sum_rejected():
    h = make_hero()
    h.role_distribution = {"mid": 0.8, "offlane": 0.4}
    with pytest.raises(ValidationError, match="sums to > 1"):
        validate_hero(h, CTX)


def test_unknown_hero_id_rejected():
    h = make_hero()
    h.hero_id = 9999
    with pytest.raises(ValidationError, match="not in current roster"):
        validate_hero(h, CTX)
