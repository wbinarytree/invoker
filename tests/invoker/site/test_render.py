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


def test_article_mark_with_ampersand_anchor_renders_clean_link(tmp_path):
    import hashlib
    import json

    from invoker.gen.artifacts import article_file_text

    kb = build_kb(tmp_path)
    concept_dir = kb / "concepts" / "evasion"
    article = "Cleave never misses targets. [corpus:testwiki/evasion@42#Cleave_&_Splash]"
    file_text = article_file_text(
        title="Evasion", kind="concept", patch="7.41d", card=good_card(), body=article
    )
    (concept_dir / "article.md").write_text(file_text)
    artifact = json.loads((concept_dir / "artifact.json").read_text())
    artifact["article_sha256"] = hashlib.sha256(file_text.encode()).hexdigest()
    (concept_dir / "artifact.json").write_text(json.dumps(artifact))

    render_kb_site(kb, "7.41d", tmp_path / "site")
    page = (tmp_path / "site" / "concepts" / "evasion.html").read_text()
    # single-escaped ampersand in the tooltip, no emphasis mangling, no
    # double escaping anywhere in the rendered mark
    assert 'title="testwiki/evasion@42#Cleave_&amp;_Splash"' in page
    assert "amp;amp;" not in page
    assert "<em>Splash" not in page and "&lt;em&gt;" not in page


def test_render_fails_on_drifted_artifact(tmp_path):
    kb = build_kb(tmp_path)
    md = kb / "concepts" / "evasion" / "article.md"
    md.write_text(md.read_text() + "\nEdited by hand.")
    with pytest.raises(GenerationError, match="drifted"):
        render_kb_site(kb, "7.41d", tmp_path / "site")


def test_render_empty_kb_still_produces_coverage_index(tmp_path):
    report = render_kb_site(tmp_path / "kb" / "7.41d", "7.41d", tmp_path / "site")
    assert report.generated == 0
    index = (tmp_path / "site" / "index.html").read_text()
    assert "0 generated" in index
