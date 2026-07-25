import json

from invoker.benchmark.answerer import ANSWERER_PROMPT_VERSION, AnswerSelection
from invoker.benchmark.runner import kb_fingerprint, run_benchmark
from invoker.benchmark.schemas import QACase
from invoker.benchmark.scorer import JUDGE_PROMPT_VERSION, FactVerdict, TrapVerdict
from invoker.gen.client import GenerationError, StructuredResult
from tests.invoker.benchmark.test_answerer import FakeBackend, provenance, write_concept
from tests.invoker.benchmark.test_marks import KEY
from tests.invoker.corpus.test_sections import make_store

UPHILL_FACT = "Ranged attacks miss 25% when attacking uphill"
ANSWER_TEXT = f"Ranged attacks from low ground miss 25% of the time. [corpus:{KEY}]"


def case(case_id: str, **overrides) -> QACase:
    payload = {
        "id": case_id,
        "question": "What is uphill miss?",
        "patch": "7.41d",
        "category": "mechanics",
        "expected_facts": [{"fact": UPHILL_FACT}],
        "expected_marks": [{"kind": "corpus", "pattern": "evasion"}],
        "max_answer_words": 120,
    }
    payload.update(overrides)
    return QACase.model_validate(payload)


class JudgeBackend:
    """Judge-side backend: canned verdicts in call order."""

    model = "fake-judge"

    def __init__(self, outputs):
        self.outputs = list(outputs)

    def generate_structured(self, output_type, **kwargs):
        return StructuredResult(
            output=self.outputs.pop(0), provenance=provenance(kwargs["prompt_name"])
        )

    def generate(self, **kwargs):  # pragma: no cover - judge never composes prose
        raise AssertionError("judge backend must not be asked for prose")


def test_run_benchmark_end_to_end(tmp_path):
    store = make_store(tmp_path / "corpus")
    kb_dir = tmp_path / "kb" / "7.41d"
    write_concept(kb_dir, "evasion", ANSWER_TEXT)

    cases = [
        case("uphill-miss"),
        case("mage-slayer", question="What is Mage Slayer?"),
        case("old-patch", patch="7.41b"),
    ]
    answer_backend = FakeBackend(
        selections=[
            AnswerSelection(artifacts=["concept/evasion"]),  # uphill-miss
            AnswerSelection(),  # mage-slayer: nothing resolves
        ],
        texts=[ANSWER_TEXT],
    )
    judge_backend = JudgeBackend([FactVerdict(verdict="present", rationale="stated")])

    printed = []
    report, report_path = run_benchmark(
        cases=cases,
        patch="7.41d",
        kb_dir=kb_dir,
        corpus_store=store,
        changelog=None,
        answer_backend=answer_backend,
        judge_backend=judge_backend,
        out_dir=tmp_path / "runs",
        on_result=lambda result: printed.append(result.case_id),
    )

    assert printed == ["uphill-miss", "mage-slayer"]
    by_id = {result.case_id: result for result in report.cases}
    assert by_id["uphill-miss"].passed
    assert by_id["mage-slayer"].failures == ["resolution-miss"]
    assert [skip.case_id for skip in report.skipped] == ["old-patch"]
    assert "7.41b" in report.skipped[0].reason

    assert report.patch == "7.41d"
    assert report.answerer_model == "fake-model"
    assert report.judge_model == "fake-judge"
    assert report.answerer_prompt_version == ANSWERER_PROMPT_VERSION
    assert report.judge_prompt_version == JUDGE_PROMPT_VERSION
    assert report.kb_artifact_count == 1
    assert len(report.kb_sha256) == 64
    assert not report.changelog_available

    saved = json.loads(report_path.read_text())
    assert saved["run_id"] == report.run_id
    assert report_path == tmp_path / "runs" / report.run_id / "report.json"
    assert {c["case_id"] for c in saved["cases"]} == {"uphill-miss", "mage-slayer"}


def test_answerer_error_fails_the_case_but_not_the_run(tmp_path):
    class ExplodingBackend:
        model = "fake-model"

        def generate_structured(self, output_type, **kwargs):
            raise GenerationError("select transport died")

        def generate(self, **kwargs):
            raise AssertionError("unreachable")

    report, _ = run_benchmark(
        cases=[case("uphill-miss")],
        patch="7.41d",
        kb_dir=tmp_path / "kb",
        corpus_store=None,
        changelog=None,
        answer_backend=ExplodingBackend(),
        judge_backend=JudgeBackend([]),
        out_dir=tmp_path / "runs",
    )
    (result,) = report.cases
    assert result.failures == ["answerer-error"]
    assert result.error == "select transport died"


def test_kb_fingerprint_tracks_content(tmp_path):
    kb_dir = tmp_path / "kb"
    write_concept(kb_dir, "evasion", "Article one. [corpus:x]")
    digest_one, count_one = kb_fingerprint(kb_dir)
    assert count_one == 1
    write_concept(kb_dir, "illusions", "Article two. [corpus:y]")
    digest_two, count_two = kb_fingerprint(kb_dir)
    assert count_two == 2
    assert digest_one != digest_two
    empty_digest, empty_count = kb_fingerprint(tmp_path / "absent")
    assert empty_count == 0
    assert len(empty_digest) == 64


def test_judge_verdicts_flow_into_the_report(tmp_path):
    kb_dir = tmp_path / "kb"
    write_concept(kb_dir, "evasion", ANSWER_TEXT)
    trap_case = case(
        "uphill-miss",
        forbidden_assertions=[{"assertion": "Melee suffers it", "why": "ranged only"}],
    )
    answer_backend = FakeBackend(
        selections=[AnswerSelection(artifacts=["concept/evasion"])], texts=[ANSWER_TEXT]
    )
    judge_backend = JudgeBackend(
        [
            FactVerdict(verdict="present", rationale="stated"),
            TrapVerdict(asserted=True, rationale="says melee misses too"),
        ]
    )
    report, _ = run_benchmark(
        cases=[trap_case],
        patch="7.41d",
        kb_dir=kb_dir,
        corpus_store=make_store(tmp_path / "corpus"),
        changelog=None,
        answer_backend=answer_backend,
        judge_backend=judge_backend,
        out_dir=tmp_path / "runs",
    )
    (result,) = report.cases
    assert result.failures == ["trap-triggered"]
    assert result.traps[0].rationale == "says melee misses too"
