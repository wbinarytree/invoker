import os
from pathlib import Path

import pytest

from ..support import FIXTURES_DIR

GOLD_DIR = FIXTURES_DIR / "gold"


@pytest.mark.skipif(not os.environ.get("INVOKER_RUN_LIVE_LLM"), reason="live LLM disabled")
@pytest.mark.parametrize("gold_file", list(GOLD_DIR.glob("*.json")))
def test_gold_hero(gold_file: Path):
    pytest.skip("live fetchers not yet wired - contract only")
