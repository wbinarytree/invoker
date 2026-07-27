"""KB exposure slice: bundle export + KnowledgeService ladder.

Spec: docs/specs/2026-07-27-kb-exposure-service-and-bundle.md.
"""

import hashlib
import json
from typing import Literal

import pytest

from invoker.gen.artifacts import (
    CardSentence,
    EntityArtifact,
    EntityCard,
    article_file_text,
    write_entity_artifact,
)
from invoker.gen.client import GenerationError, GenerationProvenance
from invoker.service import KnowledgeService, KnowledgeServiceError
from invoker.service.http import handle_http_request
from invoker.service.kb_bundle import KbExportError, export_kb_bundle
from invoker.service.mcp import KnowledgeMCPAdapter
from tests.invoker.service.test_knowledge_service import _write_bundle

PATCH = "7.41b"


def _provenance(prompt_name: str) -> GenerationProvenance:
    return GenerationProvenance(
        model="fake-model",
        transport="claude-cli",
        prompt_name=prompt_name,
        prompt_version="1",
        request_sha256="0" * 64,
        input_tokens=1,
        output_tokens=1,
        stop_reason="end_turn",
        generated_at="2026-07-27T00:00:00+00:00",
    )


def _write_entity(
    kb_root,
    *,
    kind: Literal["concept", "item", "hero"],
    class_dir: str,
    slug: str,
    title: str,
    identity_line: str,
    body: str,
    patch: str = PATCH,
) -> None:
    card = EntityCard(
        entity=slug,
        sentences=[
            CardSentence(text=identity_line, marks=["corpus:host/page@1#anchor"]),
            CardSentence(text="Second card sentence.", marks=["corpus:host/page@1#anchor"]),
        ],
    )
    file_text = article_file_text(title=title, kind=kind, patch=patch, card=card, body=body)
    artifact = EntityArtifact(
        kind=kind,
        slug=slug,
        title=title,
        patch=patch,
        article_file="article.md",
        article_sha256=hashlib.sha256(file_text.encode()).hexdigest(),
        card=card,
        citations=["corpus:host/page@1#anchor"],
        packet_sha256="0" * 64,
        article_provenance=_provenance(f"{kind}-article"),
        card_provenance=_provenance(f"{kind}-card"),
    )
    write_entity_artifact(kb_root / class_dir / slug, artifact, file_text)


def _write_kb_source(tmp_path):
    kb_root = tmp_path / "kb-source"
    _write_entity(
        kb_root,
        kind="concept",
        class_dir="concepts",
        slug="evasion",
        title="Evasion",
        identity_line="Evasion makes attacks miss with a listed probability.",
        body="Evasion article body. [corpus:host/page@1#anchor]",
    )
    _write_entity(
        kb_root,
        kind="item",
        class_dir="items",
        slug="blink",
        title="Blink Dagger",
        identity_line="Blink Dagger teleports its holder 1200 units for 2250 gold.",
        body="Blink article body. [corpus:host/page@1#anchor]",
    )
    return kb_root


def _write_changelog(bundle) -> None:
    changelog = {
        "schema_version": 1,
        "patches": [
            {
                "name": "7.41",
                "date": "2026-05-22",
                "generic": [
                    {
                        "section": "General",
                        "notes": [
                            {
                                "token": "facets_removed",
                                "text": {"english": "Facets removed from the game."},
                            }
                        ],
                    }
                ],
                "items": {},
                "neutral_items": {},
                "neutral_creeps": {},
                "heroes": {},
            }
        ],
    }
    path = bundle / "game_constants" / PATCH / "changelog.json"
    path.write_text(json.dumps(changelog, indent=2))


def _exported_bundle(tmp_path):
    bundle = _write_bundle(tmp_path)
    kb_root = _write_kb_source(tmp_path)
    export_kb_bundle(kb_root, PATCH, bundle)
    return bundle, kb_root


# --- export ---


def test_export_writes_entities_index_and_sources(tmp_path):
    bundle, _ = _exported_bundle(tmp_path)
    kb_dir = bundle / "kb" / PATCH
    assert (kb_dir / "concepts" / "evasion" / "article.md").exists()
    assert (kb_dir / "items" / "blink" / "artifact.json").exists()
    index = json.loads((kb_dir / "index.json").read_text())
    assert index["patch"] == PATCH
    assert index["artifact_count"] == 2
    assert [entry["id"] for entry in index["entries"]] == ["concept/evasion", "item/blink"]
    assert index["entries"][0]["identity_line"].startswith("Evasion makes attacks miss")
    sources = json.loads((kb_dir / "sources.json").read_text())
    host = sources["hosts"]["liquipedia_dota2"]
    assert host["page_base_url"].startswith("https://liquipedia.net/")
    assert "CC-BY-SA" in host["license"]
    metadata = json.loads((bundle / "bundle.json").read_text())
    assert metadata["schema_version"] == 2
    assert metadata["kb_patches"] == [PATCH]


def test_export_is_byte_stable(tmp_path):
    bundle, kb_root = _exported_bundle(tmp_path)
    kb_dir = bundle / "kb" / PATCH
    before = {
        path.relative_to(kb_dir): path.read_bytes()
        for path in sorted(kb_dir.rglob("*"))
        if path.is_file()
    }
    export_kb_bundle(kb_root, PATCH, bundle)
    after = {
        path.relative_to(kb_dir): path.read_bytes()
        for path in sorted(kb_dir.rglob("*"))
        if path.is_file()
    }
    assert before == after


def test_export_refuses_drifted_article(tmp_path):
    bundle = _write_bundle(tmp_path)
    kb_root = _write_kb_source(tmp_path)
    article = kb_root / "concepts" / "evasion" / "article.md"
    article.write_text(article.read_text() + "\nhand edit\n")
    with pytest.raises(GenerationError, match="drifted"):
        export_kb_bundle(kb_root, PATCH, bundle)


def test_export_refuses_unknown_entity_class(tmp_path):
    bundle = _write_bundle(tmp_path)
    kb_root = _write_kb_source(tmp_path)
    (kb_root / "pairs" / "a__b").mkdir(parents=True)
    with pytest.raises(KbExportError, match="pairs"):
        export_kb_bundle(kb_root, PATCH, bundle)


def test_export_refuses_patch_mismatch(tmp_path):
    bundle = _write_bundle(tmp_path)
    kb_root = tmp_path / "kb-source"
    _write_entity(
        kb_root,
        kind="concept",
        class_dir="concepts",
        slug="evasion",
        title="Evasion",
        identity_line="Identity line.",
        body="Body. [corpus:host/page@1#anchor]",
        patch="7.41c",
    )
    with pytest.raises(KbExportError, match="patch"):
        export_kb_bundle(kb_root, PATCH, bundle)


def test_export_refuses_game_resource_bundle_target(tmp_path):
    out = tmp_path / "game-resource-bundle"
    out.mkdir()
    (out / "bundle.json").write_text(
        json.dumps({"schema_version": 2, "patch": PATCH, "locales": ["english"], "files": {}})
    )
    kb_root = _write_kb_source(tmp_path)
    with pytest.raises(KbExportError, match="game-resource"):
        export_kb_bundle(kb_root, PATCH, out)


def test_kb_only_bundle_resolves_patch_without_claiming_game_data(tmp_path):
    out = tmp_path / "kb-only-bundle"
    kb_root = _write_kb_source(tmp_path)
    export_kb_bundle(kb_root, PATCH, out)
    service = KnowledgeService(out)
    assert service.kb_catalog()["data"]["count"] == 2
    patches = service.list_bundle_patches()["data"]
    assert patches["kb_patches"] == [PATCH]
    assert patches["patches"] == []
    with pytest.raises(KnowledgeServiceError) as excinfo:
        service.get_hero_constants("invoker")
    assert excinfo.value.code == "missing_game_constants"


def test_export_replaces_stale_entities(tmp_path):
    import shutil

    bundle, kb_root = _exported_bundle(tmp_path)
    shutil.rmtree(kb_root / "items" / "blink")
    export_kb_bundle(kb_root, PATCH, bundle)
    assert not (bundle / "kb" / PATCH / "items").exists()
    index = json.loads((bundle / "kb" / PATCH / "index.json").read_text())
    assert [entry["id"] for entry in index["entries"]] == ["concept/evasion"]


# --- service ladder ---


def test_kb_catalog_lists_and_filters(tmp_path):
    bundle, _ = _exported_bundle(tmp_path)
    service = KnowledgeService(bundle)
    response = service.kb_catalog()
    assert response["kind"] == "kb_catalog"
    assert response["data"]["count"] == 2
    assert response["source"]["artifact"] == "kb_index"
    assert response["source"]["kb_sha256"]
    items = service.kb_catalog(kind="item")
    assert [entry["id"] for entry in items["data"]["entries"]] == ["item/blink"]
    with pytest.raises(KnowledgeServiceError) as excinfo:
        service.kb_catalog(kind="hero")
    assert excinfo.value.code == "invalid_kb_kind"


def test_kb_resolve_by_slug_title_and_id(tmp_path):
    bundle, _ = _exported_bundle(tmp_path)
    service = KnowledgeService(bundle)
    for query in ("evasion", "Evasion", "concept/evasion"):
        candidates = service.kb_resolve(query)["data"]["candidates"]
        assert [candidate["id"] for candidate in candidates] == ["concept/evasion"]
    assert service.kb_resolve("no such thing")["data"]["candidates"] == []


def test_kb_resolve_item_display_name_and_alias(tmp_path):
    bundle, _ = _exported_bundle(tmp_path)
    localization = bundle / "game_constants" / PATCH / "localization" / "english.json"
    raw = json.loads(localization.read_text())
    raw["item_blink__name_alias"] = "dagger;tp dagger"
    localization.write_text(json.dumps(raw))
    service = KnowledgeService(bundle)
    response = service.kb_resolve("Blink Dagger")
    assert response["data"]["alias_source"] == "game_constants"
    candidates = response["data"]["candidates"]
    assert [candidate["id"] for candidate in candidates] == ["item/blink"]
    fields = {match["field"] for match in candidates[0]["matches"]}
    assert "display_name" in fields
    alias_hit = service.kb_resolve("dagger")["data"]["candidates"]
    assert [candidate["id"] for candidate in alias_hit] == ["item/blink"]
    assert any(
        match["field"] == "alias" and match["locale"] == "english"
        for match in alias_hit[0]["matches"]
    )


def test_kb_resolve_accepts_any_bundled_locale(tmp_path):
    # English-only content, any-locale resolution: a CJK display name from a
    # bundled locale file is a valid lookup key for the English article.
    bundle, _ = _exported_bundle(tmp_path)
    schinese = bundle / "game_constants" / PATCH / "localization" / "schinese.json"
    schinese.write_text(
        json.dumps({"DOTA_Tooltip_Ability_item_blink": "闪烁匕首"}, ensure_ascii=False)
    )
    snapshot_path = bundle / "game_constants" / PATCH / "snapshot.json"
    snapshot = json.loads(snapshot_path.read_text())
    snapshot["locales"] = ["english", "schinese"]
    snapshot_path.write_text(json.dumps(snapshot, indent=2))
    service = KnowledgeService(bundle)
    candidates = service.kb_resolve("闪烁匕首")["data"]["candidates"]
    assert [candidate["id"] for candidate in candidates] == ["item/blink"]
    assert any(
        match["field"] == "display_name" and match["locale"] == "schinese"
        for match in candidates[0]["matches"]
    )


def test_kb_resolve_ambiguity_returns_all_candidates(tmp_path):
    bundle = _write_bundle(tmp_path)
    kb_root = tmp_path / "ambiguous-kb"
    _write_entity(
        kb_root,
        kind="concept",
        class_dir="concepts",
        slug="blink",
        title="Blink",
        identity_line="Blink is instant point-to-point movement.",
        body="Concept body. [corpus:host/page@1#anchor]",
    )
    _write_entity(
        kb_root,
        kind="item",
        class_dir="items",
        slug="blink",
        title="Blink Dagger",
        identity_line="Blink Dagger teleports its holder 1200 units.",
        body="Item body. [corpus:host/page@1#anchor]",
    )
    export_kb_bundle(kb_root, PATCH, bundle)
    service = KnowledgeService(bundle)
    candidates = service.kb_resolve("blink")["data"]["candidates"]
    assert {candidate["id"] for candidate in candidates} == {"concept/blink", "item/blink"}


def test_kb_resolve_ignores_items_outside_kb(tmp_path):
    bundle, _ = _exported_bundle(tmp_path)
    service = KnowledgeService(bundle)
    assert service.kb_resolve("Perseverance")["data"]["candidates"] == []


def test_kb_resolve_without_game_constants_degrades_recorded(tmp_path):
    import shutil

    bundle, _ = _exported_bundle(tmp_path)
    shutil.rmtree(bundle / "game_constants")
    service = KnowledgeService(bundle)
    response = service.kb_resolve("blink")
    assert response["data"]["alias_source"] is None
    assert [c["id"] for c in response["data"]["candidates"]] == ["item/blink"]


def test_kb_card_serves_structured_card(tmp_path):
    bundle, _ = _exported_bundle(tmp_path)
    service = KnowledgeService(bundle)
    response = service.kb_card("concept/evasion")
    data = response["data"]
    assert data["title"] == "Evasion"
    assert data["identity_line"].startswith("Evasion makes attacks miss")
    sentences = data["card"]["sentences"]
    assert len(sentences) == 2
    assert sentences[0]["marks"] == ["corpus:host/page@1#anchor"]
    assert data["card_provenance"]["prompt_name"] == "concept-card"
    assert response["source"]["artifact"] == "kb_entity"


def test_kb_article_serves_verbatim_file(tmp_path):
    bundle, _ = _exported_bundle(tmp_path)
    service = KnowledgeService(bundle)
    data = service.kb_article("item/blink")["data"]
    assert data["article"].startswith("---\n")
    assert "Blink article body. [corpus:host/page@1#anchor]" in data["article"]
    assert data["citations"] == ["corpus:host/page@1#anchor"]
    assert data["article_provenance"]["prompt_name"] == "item-article"


def test_kb_article_refuses_drifted_bundle_file(tmp_path):
    bundle, _ = _exported_bundle(tmp_path)
    article = bundle / "kb" / PATCH / "items" / "blink" / "article.md"
    article.write_text(article.read_text() + "\ntamper\n")
    service = KnowledgeService(bundle)
    with pytest.raises(KnowledgeServiceError) as excinfo:
        service.kb_article("item/blink")
    assert excinfo.value.code == "invalid_kb_artifact"
    assert excinfo.value.status_code == 500


def test_kb_entity_id_errors(tmp_path):
    bundle, _ = _exported_bundle(tmp_path)
    service = KnowledgeService(bundle)
    with pytest.raises(KnowledgeServiceError) as excinfo:
        service.kb_card("concept/nope")
    assert excinfo.value.code == "kb_entity_not_found"
    with pytest.raises(KnowledgeServiceError) as excinfo:
        service.kb_card("evasion")
    assert excinfo.value.code == "invalid_kb_id"


def test_missing_kb_error_names_export_command(tmp_path):
    bundle = _write_bundle(tmp_path)
    service = KnowledgeService(bundle)
    with pytest.raises(KnowledgeServiceError) as excinfo:
        service.kb_catalog()
    assert excinfo.value.code == "missing_kb"
    assert "invoker export-kb" in excinfo.value.message


def test_list_bundle_patches_reports_kb_patches(tmp_path):
    bundle, _ = _exported_bundle(tmp_path)
    service = KnowledgeService(bundle)
    assert service.list_bundle_patches()["data"]["kb_patches"] == [PATCH]


# --- changelog ---


def test_search_changelog_hits_and_query_guard(tmp_path):
    bundle, _ = _exported_bundle(tmp_path)
    _write_changelog(bundle)
    service = KnowledgeService(bundle)
    response = service.search_changelog(grep="facets")
    assert response["data"]["count"] == 1
    hit = response["data"]["hits"][0]
    assert hit["patch"] == "7.41"
    assert hit["text"] == "Facets removed from the game."
    with pytest.raises(KnowledgeServiceError) as excinfo:
        service.search_changelog()
    assert excinfo.value.code == "changelog_query_required"


def test_search_changelog_missing_changelog_fails(tmp_path):
    bundle, _ = _exported_bundle(tmp_path)
    service = KnowledgeService(bundle)
    with pytest.raises(KnowledgeServiceError) as excinfo:
        service.search_changelog(grep="facets")
    assert excinfo.value.code == "missing_changelog"


# --- adapters ---


def test_mcp_adapter_exposes_kb_ladder(tmp_path):
    bundle, _ = _exported_bundle(tmp_path)
    adapter = KnowledgeMCPAdapter(KnowledgeService(bundle))
    names = {tool["name"] for tool in adapter.list_tools()}
    assert {"kb_catalog", "kb_resolve", "kb_card", "kb_article", "search_changelog"} <= names
    response = adapter.call_tool("kb_card", {"id": "concept/evasion"})
    assert response["data"]["title"] == "Evasion"


def test_http_routes_dispatch_kb_ladder(tmp_path):
    bundle, _ = _exported_bundle(tmp_path)
    service = KnowledgeService(bundle)
    status, payload = handle_http_request(
        service, method="GET", path=f"/kb_catalog?patch={PATCH}"
    )
    assert status == 200
    assert payload["data"]["count"] == 2
    status, payload = handle_http_request(
        service, method="GET", path="/kb_resolve?query=evasion"
    )
    assert status == 200
    assert [c["id"] for c in payload["data"]["candidates"]] == ["concept/evasion"]
    status, payload = handle_http_request(service, method="GET", path="/kb_card")
    assert status == 400
