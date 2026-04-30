from pathlib import Path

import pytest

from invoker.config import Config


def test_config_reads_shared_cache_dir(monkeypatch, tmp_path):
    cache_dir = tmp_path / "cache"
    monkeypatch.setenv("CACHE_DIR", str(cache_dir))
    monkeypatch.setenv("INVOKER_DATA_DIR", str(tmp_path / "data"))
    monkeypatch.delenv("INVOKER_GAME_DATA_DIR", raising=False)
    monkeypatch.delenv("INVOKER_DEV_HEROES", raising=False)
    monkeypatch.delenv("STRATZ_API_TOKEN", raising=False)

    cfg = Config.load()

    assert cfg.cache_dir == cache_dir
    assert cfg.data_dir == tmp_path / "data"


def test_config_rejects_relative_shared_cache_dir(monkeypatch, tmp_path):
    monkeypatch.setenv("CACHE_DIR", "relative-cache")
    monkeypatch.setenv("INVOKER_DATA_DIR", str(tmp_path / "data"))

    with pytest.raises(ValueError, match="CACHE_DIR"):
        Config.load()


def test_config_uses_default_shared_cache_dir(monkeypatch, tmp_path):
    monkeypatch.delenv("CACHE_DIR", raising=False)
    monkeypatch.setenv("INVOKER_DATA_DIR", str(tmp_path / "data"))

    cfg = Config.load()

    assert cfg.cache_dir == Path.home() / ".cache" / "dota-agents"
