import asyncio
from pathlib import Path

from invoker.sources.stratz import StratzFetcher


def test_missing_token_returns_none(tmp_path: Path):
    fetcher = StratzFetcher(cache_root=tmp_path, patch="test", token=None)
    result = asyncio.run(fetcher.synergies(28))
    assert result is None
    asyncio.run(fetcher.close())
