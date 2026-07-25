import json

import pytest

from invoker.corpus.schemas import CorpusIndex, CorpusIndexPage
from invoker.corpus.sections import (
    CorpusSectionError,
    load_sections,
    slice_expanded_html,
)
from invoker.corpus.store import CorpusStore

_EDIT_LINK = '<span class="mw-editsection"><a href="/edit">edit</a></span>'
EXPANDED_HTML = "".join(
    [
        '<div class="mw-parser-output">',
        '<p>Evasion is a <a href="/dota2/Mechanic">mechanic</a>',
        " that causes attacks to miss.</p>",
        '<div id="toc"><h2 id="mw-toc-heading">Contents</h2>',
        "<ul><li>1 Definition</li></ul></div>",
        '<div class="mw-heading mw-heading2"><h2 id="Definition">Definition</h2>',
        f"{_EDIT_LINK}</div>",
        "<p>Attacks have a chance to miss, <b>rounded</b> down.</p>",
        '<div class="mw-heading mw-heading3">',
        '<h3 id="Uphill_Miss_Chance">Uphill Miss Chance</h3>',
        f"{_EDIT_LINK}</div>",
        '<p>For <a href="/dota2/Ranged"><img alt="Ranged" src="icon.png" /></a>',
        '<a href="/dota2/Ranged">ranged</a> units the miss chance is 25%.</p>',
        "<table><tr><th>Source</th><th>Chance</th></tr>",
        "<tr><td>Uphill</td><td>25%</td></tr></table>",
        '<div class="mw-heading mw-heading2">',
        '<h2 id="Cleave_&amp;_Splash">Cleave &amp; Splash</h2>',
        f"{_EDIT_LINK}</div>",
        "</div>",
    ]
)


def slice_fixture():
    return slice_expanded_html(EXPANDED_HTML, host_key="testwiki", slug="evasion", revision_id=42)


def test_lead_and_headed_sections_in_document_order():
    sections = slice_fixture()
    assert [s.anchor for s in sections] == [
        None,
        "Definition",
        "Uphill_Miss_Chance",
        "Cleave_&_Splash",
    ]
    lead = sections[0]
    assert lead.heading is None
    assert lead.level == 0
    assert lead.breadcrumbs == ()
    assert "Evasion is a mechanic that causes attacks to miss." in lead.text


def test_toc_and_edit_links_and_image_alts_are_stripped():
    sections = slice_fixture()
    joined = "\n".join(s.text for s in sections)
    assert "Contents" not in joined
    assert "edit" not in joined
    # image alt "Ranged" dropped; the link text "ranged" survives
    assert "Ranged ranged" not in joined
    assert "ranged units the miss chance is 25%" in joined


def test_breadcrumbs_nest_h3_under_h2():
    sections = slice_fixture()
    uphill = next(s for s in sections if s.anchor == "Uphill_Miss_Chance")
    assert uphill.level == 3
    assert uphill.breadcrumbs == ("Definition", "Uphill Miss Chance")


def test_tables_flatten_to_rows_with_cell_separators():
    sections = slice_fixture()
    uphill = next(s for s in sections if s.anchor == "Uphill_Miss_Chance")
    assert "Source | Chance" in uphill.text
    assert "Uphill | 25%" in uphill.text


def test_citation_keys_carry_revision_and_anchor():
    sections = slice_fixture()
    lead = sections[0]
    uphill = next(s for s in sections if s.anchor == "Uphill_Miss_Chance")
    assert lead.citation_key == "testwiki/evasion@42"
    assert uphill.citation_key == "testwiki/evasion@42#Uphill_Miss_Chance"


def test_entity_anchors_are_unescaped():
    sections = slice_fixture()
    cleave = sections[-1]
    assert cleave.anchor == "Cleave_&_Splash"
    assert cleave.heading == "Cleave & Splash"
    # heading-only section stays citable even with no body text
    assert cleave.text == ""


def make_store(tmp_path, revision_id=42) -> CorpusStore:
    store = CorpusStore(tmp_path)
    store.write_expanded("testwiki", "evasion", revision_id, EXPANDED_HTML)
    index = CorpusIndex(
        host_key="testwiki",
        pages={
            "evasion": CorpusIndexPage(
                requested_title="Evasion",
                resolved_title="Evasion",
                latest_revision_id=revision_id,
                retrieved_at="2026-07-25T00:00:00Z",
                source_url="https://example.test/Evasion",
            )
        },
    )
    store.index_path("testwiki").write_text(json.dumps(index.model_dump()))
    return store


def test_load_sections_defaults_to_latest_indexed_revision(tmp_path):
    store = make_store(tmp_path)
    sections = load_sections(store, "testwiki", "evasion")
    assert sections[0].revision_id == 42
    assert sections[1].citation_key == "testwiki/evasion@42#Definition"


def test_load_sections_unknown_page_fails_loudly(tmp_path):
    store = make_store(tmp_path)
    with pytest.raises(CorpusSectionError, match="not in the testwiki corpus index"):
        load_sections(store, "testwiki", "missing_page")


def test_load_sections_missing_expanded_text_fails_loudly(tmp_path):
    store = make_store(tmp_path)
    with pytest.raises(CorpusSectionError, match="run expand-corpus"):
        load_sections(store, "testwiki", "evasion", revision_id=99)
