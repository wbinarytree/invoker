"""Item article + card generator (slice 1 of the game-file-grounded
generators; spec: docs/specs/2026-07-26-game-file-grounded-generators.md).

The context packet renders an ``ItemContext`` into keyed sections under
the ``gamefile:items/<name>#<section>`` / ``loc:<token>`` mark grammar;
generation may only cite keys the packet contains, and numbers must
appear in the cited section's rendered text (same discipline as
concepts, different substrate).
"""

from __future__ import annotations

import hashlib
from pathlib import Path

from invoker.gen.artifacts import (
    EntityArtifact,
    EntityCard,
    article_file_text,
    load_entity_article,
    write_entity_artifact,
)
from invoker.gen.checks import (
    article_segments,
    check_article_numbers,
    check_coverage,
    check_marks,
    check_numbers,
    extract_marks,
)
from invoker.gen.client import GenerationError
from invoker.gen.concepts import GenerationBackend, persist_rejected
from invoker.kg.ability_context import AttribEntry
from invoker.kg.item_context import ItemContext, ItemRef, build_item_context

ITEM_PROMPT_VERSION = "7"

ITEM_ARTICLE_SYSTEM_PROMPT = """You write reference articles for a grounded Dota 2 \
encyclopedia. This article covers one item.

Rules:
- Use ONLY facts stated in the source sections the user provides. No outside \
knowledge, even when you are confident.
- Every factual statement is covered by a citation mark of the form \
[gamefile:KEY] or [loc:KEY], where KEY is one of the provided section keys, \
copied exactly. A table block or run of sentences drawn from one section \
shares a single mark at the end of the run. A mark always FOLLOWS the text \
it vouches for: a table's marks go on their own line immediately after the \
table — never on the sentence introducing it.
- Cite the single narrowest section that states the fact. When one table \
consolidates values from several sections, its trailing marks cover every \
contributing section.
- Open with a single sentence stating what the item is — name, quality, \
and its effects by their real stat names — citing the sections that state \
those facts. Concrete and plain: no flavor verbs ("burns", "cripples"), \
no vague summaries ("combines X with Y"). Its numbers live in the tables \
below, not the opener.
- Numbers live in compact markdown stat tables. Include every value row the \
cited section carries — Scepter/Shard columns too, when present — and never \
restate a table value in prose. Values shown with a % sign keep it.
- The components section is the build formula: a table with each \
component and its gold cost, the recipe row when present, and a \
builds-into line when the packet carries one. Every price the section \
states appears in the table.
- Prose is reserved for what the item does: behavior, mechanics, \
interactions, dispellability. Keep it dense; no value appears twice.
- Every qualifier a source attaches to a value survives into the article: \
a cadence ("per second"), a damage-type restriction ("magic damage only"), \
a trigger condition, an ability's active or passive classification. "Deals \
25 damage" and "deals 25 damage per second" are different facts — carry \
the source's version. When both a gamefile section and the description \
state an ability's classification, cite the gamefile section for it.
- When the sources carry lore, close the article with it as a short \
flavor line citing its section — the lore is part of the record.
- Numbers must match the cited section exactly: reproduce values as the \
source states them. Never derive, sum, convert, count, or round numbers; \
reproduce ranges and series exactly as written.
- The patch named in the request is context, not source material: never \
state the patch or its version anywhere in the article, including the title.
- If the sources do not cover something, leave it out. Never fill a gap with \
a plausible value.
- Markdown, a few short sections, no preamble, no meta-commentary about \
sources or citations."""

ITEM_CARD_SYSTEM_PROMPT = """You compress a grounded encyclopedia article into a card.

Rules:
- The card is at most 12 sentences and around 300 tokens total.
- The first sentence is the identity line: it is shown alone as the item's \
summary in an index, so it must state concretely what the item is and \
does — name, quality, cost, and its core effect with its defining \
numbers. A reader who sees only this sentence must be able to tell what \
the item is. It is the one exception to one-fact-per-sentence and carries \
the marks of every section it draws on.
- Every other sentence states one core fact, so each fact maps to its own \
source marks. Prefer dropping a minor fact over packing two facts into one \
sentence.
- State facts plainly with exact values. No flavor language: verbs like \
"burns" or "cripples" and summaries like "combines X with Y" say nothing \
checkable — write the stat names and numbers instead.
- One sentence carries the build formula: every component with its gold \
cost, and the recipe cost when the formula has one, exactly as the \
components section states them. What the item builds into is named \
without prices — those numbers belong to the target item's own page.
- Each sentence keeps the citation marks of the article text it compresses, \
as strings of the form kind:KEY (e.g. gamefile:items/item_x#attribs) copied \
exactly from the article's marks. A mark vouches only for facts its own \
section states — never attach a mark to a sentence whose facts come from \
elsewhere. Cite the narrowest key that states the fact; never pad with \
broader keys.
- Keep the load-bearing facts and exact numbers; drop narrative padding.
- When the article closes with a lore flavor line, the card's last sentence \
carries that lore as the article states it, with the lore section's mark — \
the one exception to the no-flavor rule: it is quoted record content, not \
your language.
- Every number must appear literally in the article text a sentence's marks \
cover: never count list entries or table rows yourself, and never derive, \
sum, convert, or round a value.
- Use ONLY the article text. No outside knowledge."""


def _item_ref_line(ref: ItemRef) -> str:
    cost = f" — {ref.cost} gold" if ref.cost is not None else ""
    return f"- {ref.name} ({ref.internal_name}){cost}"


def _value_text(value: str | list[str] | None, percent: bool) -> str | None:
    if value is None:
        return None
    rendered = "/".join(value) if isinstance(value, list) else value
    return f"{rendered}%" if percent else rendered


def _attrib_line(attrib: AttribEntry) -> str:
    value = _value_text(attrib.value, attrib.percent)
    head = f"{attrib.header} {value}" if value is not None else f"{attrib.header} (upgrade only)"
    parts = [head]
    if attrib.scepter_bonus is not None:
        parts.append(f"Scepter: {attrib.scepter_bonus}")
    if attrib.shard_bonus is not None:
        parts.append(f"Shard: {attrib.shard_bonus}")
    return " | ".join(parts)


def build_item_packet(context: ItemContext) -> tuple[str, dict[str, str], str]:
    """Render an ItemContext into the keyed-section generation packet.

    Returns (packet_text, section text by mark string, packet sha256) —
    the dict doubles as the valid-mark set and the number-check source."""
    base = f"gamefile:items/{context.internal_name}"
    sections: list[tuple[str, str]] = []

    cost_lines = [f"{context.name} ({context.internal_name})"]
    if context.quality:
        cost_lines.append(f"Quality: {context.quality}")
    if context.cost is not None:
        cost_lines.append(f"Cost: {context.cost} gold")
    sections.append((f"{base}#cost", "\n".join(cost_lines)))

    # the recipe graph, both directions: the build formula with each
    # component's price (the recipe rides here, not #cost — it is part of
    # the formula), and what this item builds into
    recipe_lines: list[str] = []
    if context.components:
        recipe_lines.append("Components:")
        recipe_lines.extend(_item_ref_line(ref) for ref in context.components)
        if context.recipe_cost is not None:
            recipe_lines.append(f"- Recipe — {context.recipe_cost} gold")
    if context.builds_into:
        recipe_lines.append("Builds into:")
        recipe_lines.extend(_item_ref_line(ref) for ref in context.builds_into)
    if recipe_lines:
        sections.append((f"{base}#components", "\n".join(recipe_lines)))

    if context.attribs:
        sections.append(
            (f"{base}#attribs", "\n".join(_attrib_line(attrib) for attrib in context.attribs))
        )

    mechanics_lines = []
    # bare Passive on a record with no ability (no description) is engine
    # boilerplate, not game information (quality-followups spec)
    boilerplate_passive = context.behavior == ["Passive"] and context.description is None
    if context.behavior and not boilerplate_passive:
        mechanics_lines.append(f"Behavior: {', '.join(context.behavior)}")
    if context.damage_type:
        mechanics_lines.append(f"Damage type: {context.damage_type}")
    if context.dispellable:
        mechanics_lines.append(f"Dispellable: {context.dispellable}")
    # the KV stores some values twice (e.g. AbilityCooldown and an
    # AbilityValues cooldown key); a value already carried by an attribs
    # row is a duplicate, not a second fact (quality-followups spec)
    attrib_values = {_value_text(a.value, a.percent) for a in context.attribs}
    for label, value in (
        ("Cast range", context.cast_range),
        ("Mana cost", context.mana_cost),
        ("Cooldown", context.cooldown),
    ):
        if value is None:
            continue
        rendered = _value_text(value, False)
        if rendered not in attrib_values:
            mechanics_lines.append(f"{label}: {rendered}")
    if mechanics_lines:
        sections.append((f"{base}#mechanics", "\n".join(mechanics_lines)))

    # loc marks cite the token that actually resolved, never a synthesized
    # casing — a description without its token is a substrate inconsistency
    # and gets no section rather than a fabricated citation
    if context.description and context.description_token:
        sections.append((f"loc:{context.description_token}", context.description))
    if context.lore and context.lore_token:
        sections.append((f"loc:{context.lore_token}", context.lore))

    packet = "\n\n".join(f"## [{mark}]\n{text}" for mark, text in sections)
    text_by_mark = dict(sections)
    return packet, text_by_mark, hashlib.sha256(packet.encode()).hexdigest()


def generate_item(
    game_data_dir: Path,
    backend: GenerationBackend,
    *,
    item: str,
    patch: str,
    kb_dir: Path,
    effort: str | None = None,
    rejected_dir: Path | None = None,
) -> tuple[EntityArtifact, Path]:
    """Generate one item article + card from the game-file snapshot and
    write the artifact under <kb_dir>/items/<slug>/."""
    try:
        context = build_item_context(game_data_dir, item, patch=patch)
    except (KeyError, ValueError) as exc:
        raise GenerationError(f"{item}: {exc}") from exc
    slug = context.internal_name.removeprefix("item_")
    packet, text_by_mark, packet_sha256 = build_item_packet(context)
    valid_marks = set(text_by_mark)

    article = backend.generate(
        prompt_name="item-article",
        prompt_version=ITEM_PROMPT_VERSION,
        system=ITEM_ARTICLE_SYSTEM_PROMPT,
        user_content=(f"Item: {context.name} (patch {patch})\n\nSource sections:\n\n{packet}"),
        effort=effort,
    )
    card = None
    try:
        citations = extract_marks(article.text)
        check_marks(citations, valid_marks, "article", slug)
        check_coverage(citations, valid_marks, "article", slug)
        check_article_numbers(article.text, text_by_mark, slug)

        card = backend.generate_structured(
            EntityCard,
            prompt_name="item-card",
            prompt_version=ITEM_PROMPT_VERSION,
            system=ITEM_CARD_SYSTEM_PROMPT,
            user_content=f"Entity: {slug}\n\nArticle:\n\n{article.text}",
            effort=effort,
        )
        card_marks = [mark for sentence in card.output.sentences for mark in sentence.marks]
        check_marks(card_marks, valid_marks, "card", slug)
        for position, sentence in enumerate(card.output.sentences, start=1):
            cited_text = "\n".join(text_by_mark.get(mark, "") for mark in sentence.marks)
            check_numbers(sentence.text, cited_text, f"card sentence {position}", slug)

        file_text = article_file_text(
            title=context.name,
            kind="item",
            patch=patch,
            card=card.output,
            body=article.text,
        )
        artifact = EntityArtifact(
            kind="item",
            slug=slug,
            title=context.name,
            patch=patch,
            article_file="article.md",
            article_sha256=hashlib.sha256(file_text.encode()).hexdigest(),
            card=card.output,
            citations=citations,
            packet_sha256=packet_sha256,
            article_provenance=article.provenance,
            card_provenance=card.provenance,
        )
        path = write_entity_artifact(kb_dir / "items" / slug, artifact, file_text)
    except Exception as exc:
        persist_rejected(
            rejected_dir,
            kind="items",
            slug=slug,
            article_text=article.text,
            card=card.output if card is not None else None,
            error=exc,
        )
        raise
    return artifact, path


def regenerate_item_card(
    backend: GenerationBackend,
    *,
    artifact_path: Path,
    effort: str | None = None,
) -> tuple[EntityArtifact, Path]:
    """Regenerate only the card from the stored article, leaving the
    article untouched (card-lore pass, quality-followups spec).

    Card marks and numbers validate against the article's own citation
    structure, not today's packet: the card compresses the article, and
    the packet may legitimately have changed since the article was
    generated. A failed check propagates and writes nothing — the stored
    artifact stays as it was."""
    artifact, body = load_entity_article(artifact_path)
    if artifact.kind != "item":
        raise GenerationError(f"{artifact.slug}: card regeneration is item-only")
    card = backend.generate_structured(
        EntityCard,
        prompt_name="item-card",
        prompt_version=ITEM_PROMPT_VERSION,
        system=ITEM_CARD_SYSTEM_PROMPT,
        user_content=f"Entity: {artifact.slug}\n\nArticle:\n\n{body}",
        effort=effort,
    )
    text_by_mark: dict[str, str] = {}
    for text, marks in article_segments(body):
        for mark in marks:
            text_by_mark[mark] = f"{text_by_mark.get(mark, '')}\n{text}"
    card_marks = [mark for sentence in card.output.sentences for mark in sentence.marks]
    check_marks(card_marks, set(artifact.citations), "card", artifact.slug)
    for position, sentence in enumerate(card.output.sentences, start=1):
        cited_text = "\n".join(text_by_mark.get(mark, "") for mark in sentence.marks)
        check_numbers(sentence.text, cited_text, f"card sentence {position}", artifact.slug)

    file_text = article_file_text(
        title=artifact.title,
        kind="item",
        patch=artifact.patch,
        card=card.output,
        body=body,
    )
    updated = artifact.model_copy(
        update={
            "article_sha256": hashlib.sha256(file_text.encode()).hexdigest(),
            "card": card.output,
            "card_provenance": card.provenance,
        }
    )
    path = write_entity_artifact(artifact_path.parent, updated, file_text)
    return updated, path
