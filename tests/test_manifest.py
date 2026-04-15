from pathlib import Path

from invoker.pipeline.manifest import build_manifest, write_manifest
from invoker.pipeline.writer import write_hero
from tests.test_summarize import _hero


def test_manifest_includes_present_heroes(tmp_path: Path):
    h = _hero()
    write_hero(tmp_path, "7.41b", h)
    m = build_manifest(tmp_path, "7.41b", [h.hero_id, 999], ["pro"], complete=False)
    assert len(m.heroes) == 1
    assert m.heroes[0].content_hash.startswith("sha256:")
    assert m.status == "partial"

    path = write_manifest(tmp_path, m)
    assert path.exists()
