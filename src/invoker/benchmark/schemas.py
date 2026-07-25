from __future__ import annotations

from typing import Literal

from pydantic import BaseModel, ConfigDict, Field

QA_CASE_SCHEMA_VERSION = 1

Category = Literal["mechanics", "item", "ability", "hero", "changelog"]
MarkKind = Literal["gamefile", "loc", "corpus", "changelog", "stats", "human"]


class ExpectedFact(BaseModel):
    """A fact a correct answer must state. Non-required facts earn credit
    but their absence does not fail the case."""

    model_config = ConfigDict(extra="forbid")

    fact: str = Field(min_length=1)
    required: bool = True


class ForbiddenAssertion(BaseModel):
    """A trap: asserting this fails the case regardless of everything else.
    The why is mandatory — traps document how the mistake happens."""

    model_config = ConfigDict(extra="forbid")

    assertion: str = Field(min_length=1)
    why: str = Field(min_length=1)


class ExpectedMark(BaseModel):
    """A source mark class a grounded answer should cite. `pattern` is a
    substring the cited key/doc id must contain."""

    model_config = ConfigDict(extra="forbid")

    kind: MarkKind
    pattern: str = Field(min_length=1)


class QACase(BaseModel):
    model_config = ConfigDict(extra="forbid")

    schema_version: int = QA_CASE_SCHEMA_VERSION
    id: str = Field(pattern=r"^[a-z0-9]+(-[a-z0-9]+)*$")
    question: str = Field(min_length=1)
    patch: str = Field(min_length=1)
    category: Category
    expected_facts: list[ExpectedFact] = Field(min_length=1)
    forbidden_assertions: list[ForbiddenAssertion] = Field(default_factory=list)
    expected_marks: list[ExpectedMark] = Field(min_length=1)
    max_answer_words: int | None = Field(default=None, gt=0)
    notes: str | None = None
