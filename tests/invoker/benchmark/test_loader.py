import pytest

from invoker.benchmark.loader import BenchmarkError, load_cases


def test_seed_cases_load_and_validate():
    cases = load_cases()
    ids = [case.id for case in cases]
    assert len(ids) == len(set(ids))
    assert {
        "uphill-miss",
        "mage-slayer",
        "corrosive-haze",
        "facet-removal",
        "pseudo-random-distribution",
    } <= set(ids)
    for case in cases:
        assert case.expected_facts
        assert case.expected_marks
        assert any(fact.required for fact in case.expected_facts), case.id


def test_traps_from_user_corrections_are_encoded():
    cases = {case.id: case for case in load_cases()}
    haze = cases["corrosive-haze"]
    assert any("facet" in trap.assertion.lower() for trap in haze.forbidden_assertions)
    assert any(
        "special_bonus_unique_slardar_3" in fact.fact and fact.required
        for fact in haze.expected_facts
    )
    facets = cases["facet-removal"]
    assert facets.category == "changelog"
    assert facets.expected_marks[0].kind == "changelog"


def test_missing_directory_raises(tmp_path):
    with pytest.raises(BenchmarkError, match="not found"):
        load_cases(tmp_path / "nope")


def test_empty_directory_raises(tmp_path):
    with pytest.raises(BenchmarkError, match="no benchmark cases"):
        load_cases(tmp_path)


def test_invalid_case_raises(tmp_path):
    (tmp_path / "bad-case.yaml").write_text("id: bad-case\nquestion: q\n")
    with pytest.raises(BenchmarkError, match="invalid benchmark case"):
        load_cases(tmp_path)


def test_id_must_match_filename(tmp_path):
    (tmp_path / "wrong-name.yaml").write_text(
        """
schema_version: 1
id: other-id
question: q?
patch: 7.41d
category: mechanics
expected_facts:
  - fact: something
expected_marks:
  - kind: corpus
    pattern: x
"""
    )
    with pytest.raises(BenchmarkError, match="must match the file name stem"):
        load_cases(tmp_path)
