import httpx
import pytest

from invoker.corpus.coverage import corpus_coverage
from invoker.corpus.schemas import CorpusDoc, CorpusHost, CorpusRegistry, OmittedPage
from invoker.corpus.store import CorpusStore


def make_registry(**host_kwargs) -> CorpusRegistry:
    defaults = dict(
        api_url="https://example.test/api.php",
        page_base_url="https://example.test/",
        license="CC-BY-SA 3.0",
        max_requests_per_minute=6000,
        pages=["Armor", "Pseudo-random Distribution"],
        coverage_categories=["Category:Mechanics"],
        omit=[OmittedPage(title="Esports Page", reason="esports meta, not game mechanics")],
    )
    defaults.update(host_kwargs)
    return CorpusRegistry(schema_version=1, hosts={"testwiki": CorpusHost(**defaults)})


def category_transport(members: list[str], *, pages: int = 1) -> httpx.MockTransport:
    calls = {"n": 0}

    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.params["list"] == "categorymembers"
        calls["n"] += 1
        page_number = calls["n"]
        chunk = members if pages == 1 else [members[page_number - 1]]
        body: dict = {
            "query": {"categorymembers": [{"ns": 0, "title": title} for title in chunk]}
        }
        if page_number < pages:
            body["continue"] = {"cmcontinue": f"page|{page_number}"}
        return httpx.Response(200, json=body)

    return httpx.MockTransport(handler)


def store_with_redirect_doc(tmp_path) -> CorpusStore:
    store = CorpusStore(tmp_path)
    store.write_doc(
        CorpusDoc(
            doc_id="testwiki:random_distribution@50",
            host_key="testwiki",
            requested_title="Pseudo-random Distribution",
            resolved_title="Random Distribution",
            page_id=3,
            revision_id=50,
            revision_timestamp="2026-07-01T00:00:00Z",
            content="prd wikitext",
            source_url="https://example.test/Random_Distribution",
            license="CC-BY-SA 3.0",
            retrieved_at="2026-07-25T00:00:00Z",
        )
    )
    return store


def test_coverage_buckets_covered_omitted_unreviewed(tmp_path):
    store = store_with_redirect_doc(tmp_path)
    members = ["Armor", "Random Distribution", "Esports Page", "Roshan"]
    reports = corpus_coverage(
        make_registry(), store, transport=category_transport(members)
    )

    report = reports[0]
    assert report.universe_size == 4
    assert sorted(report.covered) == ["Armor", "Random Distribution"]
    assert report.omitted == [("Esports Page", "esports meta, not game mechanics")]
    assert report.unreviewed == ["Roshan"]
    # "Pseudo-random Distribution" resolved into the universe via the index.
    assert report.outside_categories == []


def test_coverage_reports_registry_pages_outside_universe(tmp_path):
    store = CorpusStore(tmp_path)
    reports = corpus_coverage(
        make_registry(pages=["Armor", "Lore Page"], omit=[]),
        store,
        transport=category_transport(["Armor"]),
    )
    assert reports[0].outside_categories == ["Lore Page"]


def test_coverage_follows_category_continuation(tmp_path):
    store = CorpusStore(tmp_path)
    members = ["Armor", "Evasion", "Roshan"]
    reports = corpus_coverage(
        make_registry(pages=["Armor"], omit=[]),
        store,
        transport=category_transport(members, pages=3),
    )
    report = reports[0]
    assert report.universe_size == 3
    assert report.covered == ["Armor"]
    assert sorted(report.unreviewed) == ["Evasion", "Roshan"]


def test_host_without_categories_reports_empty_universe(tmp_path):
    reports = corpus_coverage(
        make_registry(coverage_categories=[], omit=[]),
        CorpusStore(tmp_path),
        transport=httpx.MockTransport(lambda request: httpx.Response(500)),
    )
    assert reports[0].universe_size == 0
    assert reports[0].unreviewed == []


def test_page_dropped_from_registry_resurfaces_as_unreviewed(tmp_path):
    # The doc was fetched under "Pseudo-random Distribution" (resolving to
    # "Random Distribution"), but that title is no longer in pages: the stale
    # index entry must not keep counting it as covered.
    store = store_with_redirect_doc(tmp_path)
    reports = corpus_coverage(
        make_registry(pages=["Armor"], omit=[]),
        store,
        transport=category_transport(["Armor", "Random Distribution"]),
    )
    report = reports[0]
    assert report.covered == ["Armor"]
    assert report.unreviewed == ["Random Distribution"]


def test_omit_prefix_rules_bucket_by_class(tmp_path):
    from invoker.corpus.schemas import OmitRule

    store = CorpusStore(tmp_path)
    members = ["Armor", "Archive:Axe", "Archive:Blink Dagger", "Roshan"]
    reports = corpus_coverage(
        make_registry(
            pages=["Armor"],
            omit=[],
            omit_prefixes=[OmitRule(prefix="Archive:", reason="wiki archives")],
        ),
        store,
        transport=category_transport(members),
    )
    report = reports[0]
    assert report.covered == ["Armor"]
    assert report.omitted_by_rule == [("Archive:", "wiki archives", 2)]
    assert report.unreviewed == ["Roshan"]


def test_pages_and_omit_overlap_rejected():
    with pytest.raises(ValueError, match="both pages and omit"):
        CorpusHost(
            api_url="https://example.test/api.php",
            page_base_url="https://example.test/",
            license="CC-BY-SA 3.0",
            pages=["Armor"],
            omit=[OmittedPage(title="Armor", reason="duplicate")],
        )
