import pytest

from invoker.gen.client import GenerationError
from invoker.site.render import render_kb_site
from tests.invoker.gen.test_concepts import FakeBackend, good_article, good_card, run_generate

KEY = "testwiki/evasion@42#Uphill_Miss_Chance"


def build_kb(tmp_path):
    run_generate(tmp_path, FakeBackend(good_article(), good_card()))
    return tmp_path / "kb" / "7.41d"


def test_render_site_produces_index_and_concept_pages(tmp_path):
    kb = build_kb(tmp_path)
    report = render_kb_site(kb, "7.41d", tmp_path / "site")
    assert report.generated == 1
    index = (tmp_path / "site" / "index.html").read_text()
    assert "Coverage — patch 7.41d" in index
    assert "concepts/evasion.html" in index
    # curated-but-ungenerated registry pages appear as missing audit rows
    assert report.missing > 0
    assert "status-missing" in index

    page = (tmp_path / "site" / "concepts" / "evasion.html").read_text()
    # marks render as anchors, never as raw bracket text; unknown hosts keep
    # the full key visible in the tooltip
    assert "[corpus:" not in page
    assert f'title="{KEY}"' in page
    # provenance footer present
    assert "prompt concept-article@1" in page or "prompt concept-article@" in page
    # card sentences render with their marks
    assert "Uphill ranged attacks miss 25% of the time." in page


def test_mark_link_builds_pinned_revision_url():
    from invoker.site.render import _mark_link

    link = _mark_link(
        {"liquipedia_dota2": "https://liquipedia.net/dota2/"},
        "liquipedia_dota2/evasion@2383969#Uphill_Miss_Chance",
    )
    assert 'href="https://liquipedia.net/dota2/index.php?oldid=2383969#Uphill_Miss_Chance"' in link


def test_render_fails_on_drifted_artifact(tmp_path):
    kb = build_kb(tmp_path)
    md = kb / "concepts" / "evasion.md"
    md.write_text(md.read_text() + "\nEdited by hand.")
    with pytest.raises(GenerationError, match="drifted"):
        render_kb_site(kb, "7.41d", tmp_path / "site")


def test_render_empty_kb_still_produces_coverage_index(tmp_path):
    report = render_kb_site(tmp_path / "kb" / "7.41d", "7.41d", tmp_path / "site")
    assert report.generated == 0
    index = (tmp_path / "site" / "index.html").read_text()
    assert "0 generated" in index
