from invoker.benchmark.answerer import BenchmarkAnswer
from invoker.benchmark.marks import MarkResolver
from invoker.benchmark.schemas import QACase
from invoker.benchmark.scorer import FactVerdict, TrapVerdict, score_case
from invoker.gen.client import GenerationError
from invoker.marks import parse_marks
from tests.invoker.benchmark.test_answerer import provenance
from tests.invoker.benchmark.test_marks import CHANGELOG, KEY
from tests.invoker.corpus.test_sections import make_store

FACT_25 = "Ranged attacks miss 25% when attacking uphill"
FACT_OPTIONAL = "Stacks diminishingly with other evasion sources"
TRAP = "Melee attacks suffer uphill miss chance"


class FakeJudge:
    """Canned verdicts keyed by fact/assertion text; unlisted lookups fail
    the test rather than degrade silently."""

    def __init__(self, facts=None, traps=None):
        self.facts = facts or {}
        self.traps = traps or {}
        self.calls = 0

    def fact(self, answer_text: str, fact: str):
        self.calls += 1
        verdict = FactVerdict(verdict=self.facts[fact], rationale="canned")
        return verdict, provenance("qa-judge-fact")

    def trap(self, answer_text: str, assertion: str):
        self.calls += 1
        verdict = TrapVerdict(asserted=self.traps[assertion], rationale="canned")
        return verdict, provenance("qa-judge-trap")


class BoomJudge:
    def fact(self, answer_text: str, fact: str):
        raise GenerationError("judge transport failed")

    def trap(self, answer_text: str, assertion: str):
        raise GenerationError("judge transport failed")


def make_case(**overrides) -> QACase:
    payload = {
        "id": "uphill-miss",
        "question": "What is uphill miss?",
        "patch": "7.41d",
        "category": "mechanics",
        "expected_facts": [
            {"fact": FACT_25},
            {"fact": FACT_OPTIONAL, "required": False},
        ],
        "forbidden_assertions": [{"assertion": TRAP, "why": "melee is unaffected"}],
        "expected_marks": [{"kind": "corpus", "pattern": "evasion"}],
        "max_answer_words": 120,
    }
    payload.update(overrides)
    return QACase.model_validate(payload)


def make_answer(text: str) -> BenchmarkAnswer:
    return BenchmarkAnswer(
        text=text,
        marks=parse_marks(text),
        selected_artifacts=["concept/evasion"],
        changelog_queries=[],
        provenance=[],
    )


GOOD_ANSWER = f"Ranged attacks from low ground miss 25% of the time. [corpus:{KEY}]"


def resolver(tmp_path) -> MarkResolver:
    return MarkResolver(corpus_store=make_store(tmp_path), changelog=CHANGELOG)


def all_good_judge() -> FakeJudge:
    return FakeJudge(
        facts={FACT_25: "present", FACT_OPTIONAL: "absent"},
        traps={TRAP: False},
    )


def test_passing_case(tmp_path):
    result = score_case(make_case(), make_answer(GOOD_ANSWER), all_good_judge(), resolver(tmp_path))
    assert result.passed
    assert result.failures == []
    assert result.word_count == 10
    # the optional fact's absence is reported as coverage, not a failure
    assert [fact.verdict for fact in result.facts] == ["present", "absent"]
    assert result.expected_marks[0].resolved == f"corpus:{KEY}"
    # every judge call's provenance is on the record (2 facts + 1 trap)
    assert [p.prompt_name for p in result.judge_provenance] == [
        "qa-judge-fact",
        "qa-judge-fact",
        "qa-judge-trap",
    ]


def test_required_fact_absent_fails(tmp_path):
    judge = FakeJudge(facts={FACT_25: "absent", FACT_OPTIONAL: "absent"}, traps={TRAP: False})
    result = score_case(make_case(), make_answer(GOOD_ANSWER), judge, resolver(tmp_path))
    assert not result.passed
    assert result.failures == ["fact-missing"]


def test_contradicted_optional_fact_fails(tmp_path):
    judge = FakeJudge(
        facts={FACT_25: "present", FACT_OPTIONAL: "contradicted"}, traps={TRAP: False}
    )
    result = score_case(make_case(), make_answer(GOOD_ANSWER), judge, resolver(tmp_path))
    assert result.failures == ["fact-contradicted"]


def test_trap_asserted_fails(tmp_path):
    judge = FakeJudge(facts={FACT_25: "present", FACT_OPTIONAL: "absent"}, traps={TRAP: True})
    result = score_case(make_case(), make_answer(GOOD_ANSWER), judge, resolver(tmp_path))
    assert result.failures == ["trap-triggered"]


def test_expected_mark_pattern_missing(tmp_path):
    text = "Ranged attacks miss uphill. [changelog:TITLE_TOKEN]"
    result = score_case(make_case(), make_answer(text), all_good_judge(), resolver(tmp_path))
    assert "mark-pattern-missing" in result.failures
    assert result.expected_marks[0].matched == []


def test_expected_mark_matched_but_unresolvable(tmp_path):
    text = "Ranged attacks miss uphill. [corpus:testwiki/evasion@41#Definition]"
    result = score_case(make_case(), make_answer(text), all_good_judge(), resolver(tmp_path))
    assert "mark-unresolvable" in result.failures
    mark_result = result.expected_marks[0]
    assert mark_result.matched == ["corpus:testwiki/evasion@41#Definition"]
    assert mark_result.resolved is None
    assert "not a section key" in mark_result.unresolved_reasons[0]


def test_unresolvable_marks_outside_expected_patterns_are_informational(tmp_path):
    text = f"{GOOD_ANSWER} Extra claim. [gamefile:item_mage_slayer]"
    result = score_case(make_case(), make_answer(text), all_good_judge(), resolver(tmp_path))
    assert result.passed  # non-gating (spec: pass gate covers expected marks only)
    assert len(result.unresolvable_extra_marks) == 1
    assert "gamefile:item_mage_slayer" in result.unresolvable_extra_marks[0]


def test_over_length_fails_and_marks_do_not_count(tmp_path):
    result = score_case(
        make_case(max_answer_words=9),
        make_answer(GOOD_ANSWER),  # 10 prose words + 1 mark
        all_good_judge(),
        resolver(tmp_path),
    )
    assert result.failures == ["over-length"]
    result = score_case(
        make_case(max_answer_words=10),
        make_answer(GOOD_ANSWER),
        all_good_judge(),
        resolver(tmp_path),
    )
    assert result.passed


def test_resolution_miss_short_circuits_judging(tmp_path):
    answer = BenchmarkAnswer(
        text=None, marks=[], selected_artifacts=[], changelog_queries=[], provenance=[]
    )
    result = score_case(make_case(), answer, BoomJudge(), resolver(tmp_path))
    assert result.failures == ["resolution-miss"]
    assert result.answer is None
    assert result.facts == []


def test_judge_error_is_surfaced_and_mechanical_checks_still_run(tmp_path):
    result = score_case(make_case(), make_answer(GOOD_ANSWER), BoomJudge(), resolver(tmp_path))
    assert not result.passed
    assert "judge-error" in result.failures
    assert result.error == "judge transport failed"
    # mechanical checks ran regardless
    assert result.expected_marks[0].resolved == f"corpus:{KEY}"
    assert result.word_count == 10


def test_failure_codes_are_deduped(tmp_path):
    case = make_case(
        expected_facts=[{"fact": FACT_25}, {"fact": "Second required fact"}],
        forbidden_assertions=[],
    )
    judge = FakeJudge(facts={FACT_25: "absent", "Second required fact": "absent"})
    result = score_case(case, make_answer(GOOD_ANSWER), judge, resolver(tmp_path))
    assert result.failures.count("fact-missing") == 1


def test_judge_never_sees_gold_fields():
    seen: list[str] = []

    class RecordingJudge(FakeJudge):
        def fact(self, answer_text, fact):
            seen.append(answer_text)
            return super().fact(answer_text, fact)

    judge = RecordingJudge(facts={FACT_25: "present", FACT_OPTIONAL: "absent"}, traps={TRAP: False})
    score_case(make_case(), make_answer(GOOD_ANSWER), judge, MarkResolver())
    assert seen == [GOOD_ANSWER, GOOD_ANSWER]
