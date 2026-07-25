import hashlib

import pytest

from invoker.benchmark.answerer import (
    Answerer,
    AnswerSelection,
    KbEntry,
    load_kb_entries,
)
from invoker.benchmark.marks import Mark
from invoker.gen.artifacts import CardSentence, EntityArtifact, EntityCard
from invoker.gen.client import (
    GenerationError,
    GenerationProvenance,
    GenerationResult,
    StructuredResult,
)
from tests.invoker.benchmark.test_marks import CHANGELOG, KEY


def provenance(prompt_name: str) -> GenerationProvenance:
    return GenerationProvenance(
        model="fake-model",
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
    """Queued outputs: structured calls pop from `selections`, prose calls
    pop from `texts`. Records every call for assertions."""

    model = "fake-model"

    def __init__(self, selections=None, texts=None):
        self.selections = list(selections or [])
        self.texts = list(texts or [])
        self.calls: list[tuple[str, dict]] = []

    def generate(self, **kwargs) -> GenerationResult:
        self.calls.append(("generate", kwargs))
        return GenerationResult(
            text=self.texts.pop(0), provenance=provenance(kwargs["prompt_name"])
        )

    def generate_structured(self, output_type, **kwargs) -> StructuredResult:
        self.calls.append(("structured", kwargs))
        return StructuredResult(
            output=self.selections.pop(0), provenance=provenance(kwargs["prompt_name"])
        )


def entry(entry_id: str = "concept/evasion") -> KbEntry:
    return KbEntry(
        id=entry_id,
        title="Evasion",
        summary="Uphill ranged attacks miss 25% of the time.",
        article=f"# Evasion\n\nRanged attacks from low ground miss 25% of the time. [corpus:{KEY}]",
    )


def write_concept(kb_dir, slug: str, article: str) -> None:
    concept_dir = kb_dir / "concepts" / slug
    concept_dir.mkdir(parents=True)
    (concept_dir / "article.md").write_text(article)
    artifact = EntityArtifact(
        kind="concept",
        slug=slug,
        title=slug.replace("-", " ").title(),
        patch="7.41d",
        article_file="article.md",
        article_sha256=hashlib.sha256(article.encode()).hexdigest(),
        card=EntityCard(
            entity=slug,
            sentences=[CardSentence(text="First card sentence.", marks=[f"corpus:{KEY}"])],
        ),
        citations=[f"corpus:{KEY}"],
        packet_sha256="0" * 64,
        article_provenance=provenance("concept-article"),
        card_provenance=provenance("concept-card"),
    )
    (concept_dir / "artifact.json").write_text(artifact.model_dump_json())


def test_load_kb_entries_reads_concepts(tmp_path):
    write_concept(tmp_path, "evasion", "Article text. [corpus:x]")
    entries = load_kb_entries(tmp_path)
    assert [e.id for e in entries] == ["concept/evasion"]
    assert entries[0].title == "Evasion"
    assert entries[0].summary == "First card sentence."
    assert entries[0].article == "Article text. [corpus:x]"


def test_load_kb_entries_missing_dir_is_empty(tmp_path):
    assert load_kb_entries(tmp_path / "absent") == []


def test_load_kb_entries_unknown_entity_class_fails_loudly(tmp_path):
    (tmp_path / "heroes" / "slardar").mkdir(parents=True)
    with pytest.raises(GenerationError, match="no index loader"):
        load_kb_entries(tmp_path)


def test_load_kb_entries_drifted_article_fails_loudly(tmp_path):
    write_concept(tmp_path, "evasion", "Article text. [corpus:x]")
    (tmp_path / "concepts" / "evasion" / "article.md").write_text("edited by hand")
    with pytest.raises(GenerationError, match="drifted"):
        load_kb_entries(tmp_path)


def test_empty_selection_is_resolution_miss_without_compose_call():
    backend = FakeBackend(selections=[AnswerSelection()])
    answer = Answerer(backend, [entry()], changelog=None).answer("What is Mage Slayer?")
    assert answer.text is None
    assert answer.marks == []
    assert [name for name, _ in backend.calls] == ["structured"]
    assert len(answer.provenance) == 1


def test_unknown_artifact_id_fails_loudly():
    backend = FakeBackend(selections=[AnswerSelection(artifacts=["concept/invented"])])
    with pytest.raises(GenerationError, match="unknown artifact ids: concept/invented"):
        Answerer(backend, [entry()], changelog=None).answer("What is evasion?")


def test_selection_over_artifact_cap_fails_loudly():
    entries = [entry(f"concept/e{i}") for i in range(5)]
    backend = FakeBackend(selections=[AnswerSelection(artifacts=[e.id for e in entries])])
    with pytest.raises(GenerationError, match="limit 4"):
        Answerer(backend, entries, changelog=None).answer("What is evasion?")


def test_changelog_query_without_changelog_fails_loudly():
    backend = FakeBackend(selections=[AnswerSelection(changelog_queries=["facets removed"])])
    with pytest.raises(GenerationError, match="unavailable"):
        Answerer(backend, [entry()], changelog=None).answer("When were facets removed?")


def test_selection_over_query_cap_fails_loudly():
    backend = FakeBackend(selections=[AnswerSelection(changelog_queries=["a", "b", "c", "d"])])
    with pytest.raises(GenerationError, match="limit 3"):
        Answerer(backend, [entry()], changelog=CHANGELOG).answer("When?")


def test_compose_receives_articles_and_changelog_hits_and_answer_carries_marks():
    answer_text = (
        f"Uphill ranged attacks miss 25% of the time. [corpus:{KEY}] "
        "Facets were removed in 7.41. [changelog:DOTA_Patch_7_41_General_Global_Changes]"
    )
    backend = FakeBackend(
        selections=[
            AnswerSelection(artifacts=["concept/evasion"], changelog_queries=["facets removed"])
        ],
        texts=[answer_text],
    )
    answer = Answerer(backend, [entry()], changelog=CHANGELOG).answer(
        "What is uphill miss and when did facets go?"
    )
    assert answer.text == answer_text
    assert Mark("corpus", KEY) in answer.marks
    assert Mark("changelog", "DOTA_Patch_7_41_General_Global_Changes") in answer.marks
    assert answer.selected_artifacts == ["concept/evasion"]
    assert answer.changelog_queries == ["facets removed"]
    compose = backend.calls[1][1]
    assert "Ranged attacks from low ground miss 25%" in compose["user_content"]
    assert (
        "[changelog:DOTA_Patch_7_41_General_Global_Changes] patch 7.41 (2026-03-24) "
        "generic/global_changes: Facets removed from the game" in compose["user_content"]
    )
    assert len(answer.provenance) == 2


def test_changelog_hits_keep_the_newest_patch_when_capped():
    """First live battery: a broad query matched dozens of 7.36
    facet-introduction notes and the cap dropped the 7.41 removal note
    the question was about. The newest patch *by date* must survive the
    cap regardless of manifest order (this fixture lists newest first, so
    position-based reversal would get it wrong), with intra-patch note
    order preserved."""
    old_notes = [
        {"token": f"OLD_NOTE_{i}", "text": {"english": f"Facets introduction detail {i}"}}
        for i in range(20)
    ]
    changelog = {
        "schema_version": 1,
        "locales": ["english"],
        "patches": [
            {
                "name": "7.41",
                "date": "2026-03-24",
                "generic": [
                    {
                        "section": "global_changes",
                        "notes": [
                            {
                                "token": "REMOVAL_NOTE",
                                "text": {"english": "Facets removed from the game"},
                            }
                        ],
                    }
                ],
                "items": {},
                "neutral_items": {},
                "heroes": {},
                "neutral_creeps": {},
            },
            {
                "name": "7.36",
                "date": "2024-05-22",
                "generic": [{"section": "general", "notes": old_notes}],
                "items": {},
                "neutral_items": {},
                "heroes": {},
                "neutral_creeps": {},
            },
        ],
    }
    backend = FakeBackend(
        selections=[AnswerSelection(changelog_queries=["facets"])],
        texts=["Facets were removed in 7.41. [changelog:REMOVAL_NOTE]"],
    )
    Answerer(backend, [], changelog=changelog).answer("When were facets removed?")
    content = backend.calls[1][1]["user_content"]
    assert "[changelog:REMOVAL_NOTE] patch 7.41" in content
    # 21 matches, cap 12: the dropped 9 are the oldest, and the material says so
    omitted_line = content.splitlines()[-1]
    assert "9" in omitted_line and "older" in omitted_line and "omitted" in omitted_line
    # intra-patch order preserved: the surviving 7.36 notes read in sequence
    first_old = content.index("OLD_NOTE_0")
    second_old = content.index("OLD_NOTE_1")
    assert content.index("REMOVAL_NOTE") < first_old < second_old


def test_selection_exactly_at_caps_succeeds():
    entries = [entry(f"concept/e{i}") for i in range(4)]
    backend = FakeBackend(
        selections=[
            AnswerSelection(
                artifacts=[e.id for e in entries],
                changelog_queries=["a", "b", "c"],
            )
        ],
        texts=["Answer. [corpus:x]"],
    )
    answer = Answerer(backend, entries, changelog=CHANGELOG).answer("Question?")
    assert answer.text == "Answer. [corpus:x]"
    assert len(answer.selected_artifacts) == 4
    assert len(answer.changelog_queries) == 3


def test_select_index_lists_entries_and_changelog_availability():
    backend = FakeBackend(selections=[AnswerSelection()])
    Answerer(backend, [entry()], changelog=None).answer("What is evasion?")
    select = backend.calls[0][1]
    assert "- concept/evasion: Evasion — Uphill ranged attacks miss 25%" in select["user_content"]
    assert "Changelog: not available this run." in select["user_content"]

    backend = FakeBackend(selections=[AnswerSelection()])
    Answerer(backend, [], changelog=CHANGELOG).answer("What is evasion?")
    select = backend.calls[0][1]
    assert "(none generated yet)" in select["user_content"]
    assert "Changelog: available" in select["user_content"]
