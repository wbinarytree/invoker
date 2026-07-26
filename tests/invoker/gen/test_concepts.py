import json

import pytest

from invoker.gen.artifacts import CardSentence, EntityCard
from invoker.gen.checks import check_coverage, extract_marks
from invoker.gen.client import (
    GenerationError,
    GenerationProvenance,
    GenerationResult,
    StructuredResult,
)
from invoker.gen.concepts import build_packet, generate_concept

# reuse the corpus store fixture helpers from the sections tests
from tests.invoker.corpus.test_sections import make_store

KEY = "testwiki/evasion@42#Uphill_Miss_Chance"
DEF_KEY = "testwiki/evasion@42#Definition"
LEAD_KEY = "testwiki/evasion@42"
ALL_KEYS = [f"corpus:{LEAD_KEY}", f"corpus:{DEF_KEY}", f"corpus:{KEY}"]


def provenance(prompt_name: str) -> GenerationProvenance:
    return GenerationProvenance(
        model="claude-opus-5",
        transport="claude-cli",
        prompt_name=prompt_name,
        prompt_version="1",
        request_sha256="0" * 64,
        input_tokens=1,
        output_tokens=1,
        stop_reason="end_turn",
        generated_at="2026-07-25T00:00:00+00:00",
    )


class FakeBackend:
    model = "claude-opus-5"

    def __init__(self, article_text: str, card: EntityCard):
        self.article_text = article_text
        self.card = card
        self.calls: list[dict] = []

    def generate(self, **kwargs) -> GenerationResult:
        self.calls.append(kwargs)
        return GenerationResult(
            text=self.article_text, provenance=provenance(kwargs["prompt_name"])
        )

    def generate_structured(self, output_type, **kwargs) -> StructuredResult:
        self.calls.append(kwargs)
        return StructuredResult(output=self.card, provenance=provenance(kwargs["prompt_name"]))


def good_card(mark: str = f"corpus:{KEY}") -> EntityCard:
    return EntityCard(
        entity="evasion",
        sentences=[CardSentence(text="Uphill ranged attacks miss 25% of the time.", marks=[mark])],
    )


def good_article() -> str:
    # cites every packet section — the coverage check demands lossless
    # compression, so a fixture article must cover the whole packet
    return (
        "# Evasion\n\n"
        f"Evasion is a mechanic that causes attacks to miss. [corpus:{LEAD_KEY}]\n\n"
        f"Attacks have a chance to miss, rounded down. [corpus:{DEF_KEY}]\n\n"
        f"Ranged attacks from low ground miss 25% of the time. [corpus:{KEY}]"
    )


def test_build_packet_keys_and_stable_hash(tmp_path):
    from invoker.corpus.sections import load_sections
    from invoker.corpus.store import CorpusStore

    make_store(tmp_path)
    sections = load_sections(CorpusStore(tmp_path), "testwiki", "evasion")
    packet, text_by_mark, digest = build_packet(sections)
    assert f"corpus:{KEY}" in text_by_mark
    assert f"corpus:{LEAD_KEY}" in text_by_mark  # lead section is citable
    assert f"[{KEY}]" in packet
    _, _, digest2 = build_packet(sections)
    assert digest == digest2
    # heading-only sections (no body text) are not packet targets
    assert f"corpus:{LEAD_KEY}#Cleave_&_Splash" not in text_by_mark


def test_extract_marks_dedupes_in_order():
    text = f"A. [corpus:{KEY}] B. [corpus:{LEAD_KEY}] C. [corpus:{KEY}]"
    assert extract_marks(text) == [f"corpus:{KEY}", f"corpus:{LEAD_KEY}"]


def run_generate(tmp_path, backend, rejected_dir=None):
    from invoker.corpus.store import CorpusStore

    make_store(tmp_path)
    return generate_concept(
        CorpusStore(tmp_path),
        backend,
        host_key="testwiki",
        slug="evasion",
        patch="7.41d",
        kb_dir=tmp_path / "kb" / "7.41d",
        rejected_dir=rejected_dir,
    )


def test_generate_concept_writes_artifact_and_article_file(tmp_path):
    backend = FakeBackend(good_article(), good_card())
    artifact, path = run_generate(tmp_path, backend)
    assert path.parent.name == "evasion"
    assert path.name == "artifact.json"
    saved = json.loads(path.read_text())
    assert saved["slug"] == "evasion"
    assert saved["title"] == "Evasion"
    assert saved["patch"] == "7.41d"
    assert saved["schema_version"] == 3
    assert saved["citations"] == ALL_KEYS
    assert saved["article_provenance"]["prompt_name"] == "concept-article"
    assert saved["card_provenance"]["prompt_name"] == "concept-card"
    assert len(saved["packet_sha256"]) == 64
    # the card's one home is the markdown frontmatter, not artifact.json
    assert "card" not in saved
    assert saved["article_file"] == "article.md"
    file_text = (path.parent / "article.md").read_text()
    assert file_text.startswith("---\n")
    assert "Uphill ranged attacks miss 25% of the time." in file_text  # card in frontmatter
    assert file_text.endswith(good_article())
    # the packet reached the model with keys inline
    article_call = backend.calls[0]
    assert f"[{KEY}]" in article_call["user_content"]
    assert "Evasion" in article_call["user_content"]


def test_load_entity_article_verifies_sha_binding(tmp_path):
    from invoker.gen.artifacts import load_entity_article

    _, path = run_generate(tmp_path, FakeBackend(good_article(), good_card()))
    artifact, article = load_entity_article(path)
    assert artifact.slug == "evasion"
    # the card round-trips through the frontmatter; the body excludes it
    assert artifact.card.sentences[0].text == good_card().sentences[0].text
    assert article == good_article()
    # a hand-edited article file fails loudly
    original = (path.parent / "article.md").read_text()
    (path.parent / "article.md").write_text(original + "\n\nEdited by hand.")
    with pytest.raises(GenerationError, match="drifted"):
        load_entity_article(path)


def test_load_entity_article_rejects_stale_schema(tmp_path):
    import json as json_module

    from invoker.gen.artifacts import load_entity_article

    _, path = run_generate(tmp_path, FakeBackend(good_article(), good_card()))
    payload = json_module.loads(path.read_text())
    payload["schema_version"] = 2
    path.write_text(json_module.dumps(payload))
    with pytest.raises(GenerationError, match="schema 2"):
        load_entity_article(path)


def test_load_entity_article_rejects_frontmatter_json_mismatch(tmp_path):
    # only reachable via json-side drift — an md-side edit trips the sha
    # first — which is exactly the migration safety net this check is
    import json as json_module

    from invoker.gen.artifacts import load_entity_article

    _, path = run_generate(tmp_path, FakeBackend(good_article(), good_card()))
    payload = json_module.loads(path.read_text())
    payload["patch"] = "7.42"
    path.write_text(json_module.dumps(payload))
    with pytest.raises(GenerationError, match="frontmatter patch"):
        load_entity_article(path)


def test_article_citing_unknown_key_fails_loudly(tmp_path):
    article = "Made-up fact. [corpus:testwiki/evasion@42#Not_A_Real_Section]"
    backend = FakeBackend(article, good_card())
    with pytest.raises(GenerationError, match="Not_A_Real_Section"):
        run_generate(tmp_path, backend)


def test_article_without_marks_fails_loudly(tmp_path):
    backend = FakeBackend("Prose without any citations.", good_card())
    with pytest.raises(GenerationError, match="no citation marks"):
        run_generate(tmp_path, backend)


def test_card_with_unknown_mark_fails_loudly(tmp_path):
    bad = good_card(mark="corpus:testwiki/evasion@42#Invented")
    backend = FakeBackend(good_article(), bad)
    with pytest.raises(GenerationError, match="Invented"):
        run_generate(tmp_path, backend)


def test_card_number_absent_from_cited_section_fails_loudly(tmp_path):
    # 25 appears under #Uphill_Miss_Chance; 77 appears nowhere
    bad = EntityCard(
        entity="evasion",
        sentences=[CardSentence(text="Attacks miss 77% of the time.", marks=[f"corpus:{KEY}"])],
    )
    backend = FakeBackend(good_article(), bad)
    with pytest.raises(GenerationError, match=r"card sentence 1.*77"):
        run_generate(tmp_path, backend)


def test_card_number_must_come_from_the_cited_section_not_any_section(tmp_path):
    # 3100 exists nowhere in the evasion fixture; even a resolvable mark
    # cannot vouch for a number its section does not contain
    bad = EntityCard(
        entity="evasion",
        sentences=[CardSentence(text="Costs 3100 gold.", marks=[f"corpus:{LEAD_KEY}"])],
    )
    backend = FakeBackend(good_article(), bad)
    with pytest.raises(GenerationError, match="3100"):
        run_generate(tmp_path, backend)


def test_article_number_absent_from_packet_fails_loudly(tmp_path):
    article = good_article().replace("25%", "42%")
    backend = FakeBackend(article, good_card())
    with pytest.raises(GenerationError, match=r"not found in the cited source: 42"):
        run_generate(tmp_path, backend)


def test_article_number_must_come_from_the_cited_section(tmp_path):
    # 25 lives in the Uphill/table sections; the lead never states it
    article = (
        f"Attacks miss 25% of the time. [corpus:{LEAD_KEY}]\n\n"
        f"Attacks have a chance to miss, rounded down. [corpus:{DEF_KEY}]\n\n"
        f"Ranged attacks from low ground miss uphill. [corpus:{KEY}]"
    )
    backend = FakeBackend(article, good_card())
    with pytest.raises(GenerationError, match=r"segment citing.*25"):
        run_generate(tmp_path, backend)


def test_article_dropping_a_packet_section_fails_loudly(tmp_path):
    # cites the lead and Uphill but drops #Definition — an uncited packet
    # section is dropped content, and generation aborts naming it
    article = (
        f"Evasion is a mechanic that causes attacks to miss. [corpus:{LEAD_KEY}]\n\n"
        f"Ranged attacks from low ground miss 25% of the time. [corpus:{KEY}]"
    )
    backend = FakeBackend(article, good_card())
    with pytest.raises(GenerationError, match=r"does not cite packet sections.*#Definition"):
        run_generate(tmp_path, backend)


def test_check_coverage_requires_anchorless_sections_and_exempts_references():
    valid = {"corpus:w/p@1", "corpus:w/p@1#Facts", "corpus:w/p@1#References"}
    # an uncited References section is boilerplate, not dropped content
    check_coverage(["corpus:w/p@1", "corpus:w/p@1#Facts"], valid, "article", "p")
    # the anchorless lead section is still required
    with pytest.raises(GenerationError, match=r"does not cite packet sections: corpus:w/p@1$"):
        check_coverage(["corpus:w/p@1#Facts", "corpus:w/p@1#References"], valid, "article", "p")
    # citing References does not excuse a dropped real section
    with pytest.raises(GenerationError, match=r"w/p@1#Facts"):
        check_coverage(["corpus:w/p@1", "corpus:w/p@1#References"], valid, "article", "p")


def test_check_coverage_exempts_batch_boilerplate_anchors():
    # anchors enumerated across the full corpus (batch KB generation
    # spec): galleries and both observed See_also case variants are
    # boilerplate; Trivia is content and must stay required
    valid = {
        "corpus:w/p@1#Facts",
        "corpus:w/p@1#Gallery",
        "corpus:w/p@1#See_Also",
        "corpus:w/p@1#See_also",
        "corpus:w/p@1#Trivia",
    }
    check_coverage(
        ["corpus:w/p@1#Facts", "corpus:w/p@1#Trivia"], valid, "article", "p"
    )
    with pytest.raises(GenerationError, match=r"w/p@1#Trivia"):
        check_coverage(["corpus:w/p@1#Facts"], valid, "article", "p")


def test_card_citing_a_subset_of_sections_passes(tmp_path):
    # coverage is article-only by design: the card is a compression and
    # may cite any subset; good_card cites exactly one of three sections
    backend = FakeBackend(good_article(), good_card())
    artifact, _ = run_generate(tmp_path, backend)
    card_marks = {m for s in artifact.card.sentences for m in s.marks}
    assert card_marks < set(ALL_KEYS)


def test_check_failure_persists_rejected_article(tmp_path):
    # coverage failure after a paid article call: the article and error
    # land in the rejected dir before the abort propagates
    article = (
        f"Evasion is a mechanic that causes attacks to miss. [corpus:{LEAD_KEY}]\n\n"
        f"Ranged attacks from low ground miss 25% of the time. [corpus:{KEY}]"
    )
    rejected = tmp_path / "rejected"
    with pytest.raises(GenerationError, match="does not cite"):
        run_generate(tmp_path, FakeBackend(article, good_card()), rejected_dir=rejected)
    (attempt,) = list((rejected / "concepts" / "evasion").iterdir())
    assert (attempt / "article.md").read_text() == article
    assert "does not cite" in (attempt / "error.txt").read_text()
    # the card call never ran, so no card is persisted
    assert not (attempt / "card.json").exists()


def test_card_failure_persists_article_and_card(tmp_path):
    bad = good_card(mark="corpus:testwiki/evasion@42#Invented")
    rejected = tmp_path / "rejected"
    with pytest.raises(GenerationError, match="Invented"):
        run_generate(tmp_path, FakeBackend(good_article(), bad), rejected_dir=rejected)
    (attempt,) = list((rejected / "concepts" / "evasion").iterdir())
    assert (attempt / "article.md").read_text() == good_article()
    assert "Invented" in (attempt / "card.json").read_text()


def test_no_rejected_dir_means_no_persistence(tmp_path):
    # default: aborts behave exactly as before, nothing extra on disk
    backend = FakeBackend("Prose without any citations.", good_card())
    with pytest.raises(GenerationError, match="no citation marks"):
        run_generate(tmp_path, backend)
    assert not (tmp_path / "rejected").exists()


def test_structural_digits_are_not_number_claims(tmp_path):
    # headings mirror source section titles ("Example 3") and ordered
    # lists carry the model's own numbering — neither is a factual claim
    article = good_article() + (
        f"\n\n## Example 99: Miss Streaks\n\n"
        f"1. Attacks can miss.\n"
        f"2. Consecutive misses happen. [corpus:{DEF_KEY}]"
    )
    artifact, _ = run_generate(tmp_path, FakeBackend(article, good_card()))
    assert artifact.slug == "evasion"


def test_inline_numbers_still_checked_after_structural_strip(tmp_path):
    # the same digit in prose (not structure) must still be vouched for
    article = good_article() + f"\n\nMisses stack 99 times. [corpus:{DEF_KEY}]"
    with pytest.raises(GenerationError, match="99"):
        run_generate(tmp_path, FakeBackend(article, good_card()))


def test_ordered_list_content_numbers_still_checked(tmp_path):
    # only the list marker is structural; the content stays checked
    article = good_article() + (
        f"\n\n1. Misses stack 99 times. [corpus:{DEF_KEY}]"
    )
    with pytest.raises(GenerationError, match="99"):
        run_generate(tmp_path, FakeBackend(article, good_card()))


def test_numbers_inside_citation_marks_are_ignored(tmp_path):
    # the revision id 42 in the mark keys must not be counted as a claim
    backend = FakeBackend(good_article(), good_card())
    artifact, _ = run_generate(tmp_path, backend)
    assert artifact.citations == ALL_KEYS


def test_unknown_slug_fails_loudly(tmp_path):
    from invoker.corpus.store import CorpusStore

    make_store(tmp_path)
    with pytest.raises(GenerationError, match="not in the testwiki corpus index"):
        generate_concept(
            CorpusStore(tmp_path),
            FakeBackend(good_article(), good_card()),
            host_key="testwiki",
            slug="missing",
            patch="7.41d",
            kb_dir=tmp_path / "kb",
        )
