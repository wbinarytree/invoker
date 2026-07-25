import pytest

from invoker.corpus.registry import PACKAGED_REGISTRY, RegistryError, load_registry


def test_packaged_registry_loads_and_validates():
    registry = load_registry()
    assert PACKAGED_REGISTRY.exists()
    assert "liquipedia_dota2" in registry.hosts
    host = registry.hosts["liquipedia_dota2"]
    assert host.api_url.startswith("https://")
    assert host.page_base_url.startswith("https://")
    assert host.pages
    assert host.max_requests_per_minute > 0


def test_missing_registry_file_raises(tmp_path):
    with pytest.raises(RegistryError, match="not found"):
        load_registry(tmp_path / "nope.yaml")


def test_invalid_registry_shape_raises(tmp_path):
    bad = tmp_path / "pages.yaml"
    bad.write_text("schema_version: 1\nhosts:\n  broken:\n    api_url: x\n")
    with pytest.raises(RegistryError, match="invalid corpus registry"):
        load_registry(bad)


def test_unknown_registry_keys_rejected(tmp_path):
    bad = tmp_path / "pages.yaml"
    bad.write_text(
        "schema_version: 1\n"
        "surprise: true\n"
        "hosts:\n"
        "  h:\n"
        "    api_url: https://example.test/api.php\n"
        "    page_base_url: https://example.test/\n"
        "    license: CC-BY-SA 3.0\n"
        "    pages: [Mechanics]\n"
    )
    with pytest.raises(RegistryError, match="invalid corpus registry"):
        load_registry(bad)
