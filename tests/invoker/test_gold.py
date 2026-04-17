import json
import os
from pathlib import Path

import pytest
import yaml

from ..support import FIXTURES_DIR

GOLD_DIR = FIXTURES_DIR / "gold"
TAXONOMY_FILE = Path("src/invoker/prompts/taxonomy.yaml")


def _taxonomy_tags() -> set[str]:
    data = yaml.safe_load(TAXONOMY_FILE.read_text())
    return set(data["tags"].keys())


@pytest.mark.parametrize("gold_file", sorted(GOLD_DIR.glob("*.json")))
def test_gold_file_shape(gold_file: Path):
    data = json.loads(gold_file.read_text())
    for key in ("hero_id", "hero_name", "expected_tags", "forbidden_tags"):
        assert key in data, f"{gold_file.name}: missing {key}"
    assert isinstance(data["expected_tags"], list)
    assert isinstance(data["forbidden_tags"], list)


@pytest.mark.parametrize("gold_file", sorted(GOLD_DIR.glob("*.json")))
def test_gold_tags_in_taxonomy(gold_file: Path):
    data = json.loads(gold_file.read_text())
    vocab = _taxonomy_tags()
    for tag in data["expected_tags"]:
        assert tag in vocab, f"{gold_file.name}: expected tag {tag!r} not in taxonomy"
    for tag in data["forbidden_tags"]:
        assert tag in vocab, f"{gold_file.name}: forbidden tag {tag!r} not in taxonomy"


@pytest.mark.parametrize("gold_file", sorted(GOLD_DIR.glob("*.json")))
def test_gold_no_tag_overlap(gold_file: Path):
    data = json.loads(gold_file.read_text())
    overlap = set(data["expected_tags"]) & set(data["forbidden_tags"])
    assert not overlap, f"{gold_file.name}: tags in both lists: {overlap}"


@pytest.mark.skipif(not os.environ.get("INVOKER_RUN_LIVE_LLM"), reason="live LLM disabled")
@pytest.mark.parametrize("gold_file", list(GOLD_DIR.glob("*.json")))
def test_gold_hero(gold_file: Path):
    pytest.skip("live fetchers not yet wired - contract only")
