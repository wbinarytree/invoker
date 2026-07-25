import json

import pytest

from invoker.gen.artifacts import CardSentence, ConceptCard
from invoker.gen.client import (
    GenerationError,
    GenerationProvenance,
    GenerationResult,
    StructuredResult,
)
from invoker.gen.concepts import build_packet, extract_citations, generate_concept

# reuse the corpus store fixture helpers from the sections tests
from tests.invoker.corpus.test_sections import make_store

KEY = "testwiki/evasion@42#Uphill_Miss_Chance"
LEAD_KEY = "testwiki/evasion@42"


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
    def __init__(self, article_text: str, card: ConceptCard):
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


def good_card(mark: str = f"corpus:{KEY}") -> ConceptCard:
    return ConceptCard(
        entity="evasion",
        sentences=[CardSentence(text="Uphill ranged attacks miss 25% of the time.", marks=[mark])],
    )


def good_article() -> str:
    return f"# Evasion\n\nRanged attacks from low ground miss 25% of the time. [corpus:{KEY}]"


def test_build_packet_keys_and_stable_hash(tmp_path):
    from invoker.corpus.sections import load_sections
    from invoker.corpus.store import CorpusStore

    make_store(tmp_path)
    sections = load_sections(CorpusStore(tmp_path), "testwiki", "evasion")
    packet, keys, digest = build_packet(sections)
    assert KEY in keys
    assert LEAD_KEY in keys  # lead section is citable
    assert f"[{KEY}]" in packet
    _, _, digest2 = build_packet(sections)
    assert digest == digest2
    # heading-only sections (no body text) are not packet targets
    assert f"{LEAD_KEY}#Cleave_&_Splash" not in keys


def test_extract_citations_dedupes_in_order():
    text = f"A. [corpus:{KEY}] B. [corpus:{LEAD_KEY}] C. [corpus:{KEY}]"
    assert extract_citations(text) == [KEY, LEAD_KEY]


def run_generate(tmp_path, backend):
    from invoker.corpus.store import CorpusStore

    make_store(tmp_path)
    return generate_concept(
        CorpusStore(tmp_path),
        backend,
        host_key="testwiki",
        slug="evasion",
        patch="7.41d",
        kb_dir=tmp_path / "kb" / "7.41d",
    )


def test_generate_concept_writes_artifact(tmp_path):
    backend = FakeBackend(good_article(), good_card())
    artifact, path = run_generate(tmp_path, backend)
    assert path.name == "evasion.json"
    saved = json.loads(path.read_text())
    assert saved["slug"] == "evasion"
    assert saved["title"] == "Evasion"
    assert saved["patch"] == "7.41d"
    assert saved["citations"] == [f"corpus:{KEY}"]
    assert saved["article_provenance"]["prompt_name"] == "concept-article"
    assert saved["card_provenance"]["prompt_name"] == "concept-card"
    assert len(saved["packet_sha256"]) == 64
    # the packet reached the model with keys inline
    article_call = backend.calls[0]
    assert f"[{KEY}]" in article_call["user_content"]
    assert "Evasion" in article_call["user_content"]


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
