from __future__ import annotations

import hashlib
import json
from dataclasses import asdict, dataclass
from datetime import UTC, datetime

from invoker.llm import LLMClient
from invoker.prompts import load
from invoker.taxonomy import load_taxonomy


@dataclass
class HeroExtractionInput:
    hero_id: int
    hero_name: str
    roles: list[str]
    abilities: list[dict]


@dataclass
class TagSource:
    tag: str
    ability: str
    evidence: str


@dataclass
class MechanicalExtraction:
    hero_id: int
    functional_tags: list[str]
    tag_sources: list[TagSource]
    model: str
    prompt_version: int
    prompt_hash: str
    input_hash: str
    extracted_at: str


def _input_hash(h: HeroExtractionInput) -> str:
    blob = json.dumps(asdict(h), sort_keys=True).encode()
    return "sha256:" + hashlib.sha256(blob).hexdigest()


def extract_mechanical(h: HeroExtractionInput, client: LLMClient) -> MechanicalExtraction:
    prompt = load("extract_mechanical_tags")
    tax = load_taxonomy()

    abilities_block = "\n".join(f"- {a['name']}: {a['text']}" for a in h.abilities)
    rendered = prompt.render(
        TAXONOMY=tax.as_prompt_block(),
        HERO_NAME=h.hero_name,
        ROLES=", ".join(h.roles) or "(none)",
        ABILITIES=abilities_block,
    )
    response = client.complete_json(rendered, prompt_version=prompt.version)
    parsed = json.loads(response.text)

    return MechanicalExtraction(
        hero_id=h.hero_id,
        functional_tags=list(parsed["functional_tags"]),
        tag_sources=[TagSource(**s) for s in parsed["tag_sources"]],
        model=response.model,
        prompt_version=response.prompt_version,
        prompt_hash=prompt.sha256,
        input_hash=_input_hash(h),
        extracted_at=datetime.now(UTC).isoformat(timespec="seconds"),
    )
