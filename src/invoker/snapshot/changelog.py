from __future__ import annotations

from pathlib import Path
from typing import Any

from invoker.snapshot.kv import parse_kv1_file

CHANGELOG_SCHEMA_VERSION = 1

MANIFEST_RELATIVE_PATH = Path("patchnotes") / "patchnotes.vdpn"
LOCALIZATION_RELATIVE_DIR = Path("resource") / "localization" / "patchnotes"

_SECTION_MAP = (
    ("items", "items"),
    ("items_neutral", "neutral_items"),
    ("neutral_creeps", "neutral_creeps"),
)


class ChangelogError(ValueError):
    pass


def _as_list(value: Any) -> list[Any]:
    if isinstance(value, list):
        return value
    return [value]


def _token(reference: str) -> str:
    return reference.lstrip("#")


def _localized(token: str, localizations: dict[str, dict[str, str]]) -> dict[str, str]:
    return {
        locale: tokens[token]
        for locale, tokens in localizations.items()
        if token in tokens
    }


def _render_note(
    note_block: dict[str, Any],
    localizations: dict[str, dict[str, str]],
) -> dict[str, Any]:
    token = _token(str(note_block["note"]))
    entry: dict[str, Any] = {"token": token, "text": _localized(token, localizations)}
    if "indent" in note_block:
        entry["indent"] = str(note_block["indent"])
    if "info" in note_block:
        info_token = _token(str(note_block["info"]))
        entry["info"] = {"token": info_token, "text": _localized(info_token, localizations)}
    return entry


def _render_notes(
    container: dict[str, Any],
    localizations: dict[str, dict[str, str]],
) -> list[dict[str, Any]]:
    notes = container.get("note")
    if notes is None:
        return []
    rendered = []
    for note_block in _as_list(notes):
        if isinstance(note_block, dict) and "note" in note_block:
            rendered.append(_render_note(note_block, localizations))
    return rendered


def build_changelog(
    manifest_path: Path,
    localizations: dict[str, dict[str, str]],
) -> dict[str, Any]:
    parsed = parse_kv1_file(manifest_path, collect_duplicates=True)
    manifest = parsed.get("patch_manifest")
    if not isinstance(manifest, dict):
        raise ChangelogError(f"{manifest_path} does not contain a patch_manifest root")

    patches: list[dict[str, Any]] = []
    for block in _as_list(manifest.get("", [])):
        if not isinstance(block, dict):
            continue
        patch: dict[str, Any] = {
            "name": str(block.get("patch_name", "")).removeprefix("patch").strip(),
            "date": block.get("patch_date"),
            "generic": [],
            "items": {},
            "neutral_items": {},
            "heroes": {},
            "neutral_creeps": {},
        }

        generic = block.get("generic")
        if isinstance(generic, dict):
            for section_name, section in generic.items():
                if not isinstance(section, dict):
                    continue
                notes = _render_notes(section, localizations)
                if not notes:
                    continue
                rendered_section: dict[str, Any] = {"section": section_name, "notes": notes}
                if "title" in section:
                    title_token = _token(str(section["title"]))
                    rendered_section["title"] = {
                        "token": title_token,
                        "text": _localized(title_token, localizations),
                    }
                patch["generic"].append(rendered_section)

        for source_key, output_key in _SECTION_MAP:
            section = block.get(source_key)
            if not isinstance(section, dict):
                continue
            for entity, entity_block in section.items():
                if not isinstance(entity_block, dict):
                    continue
                notes = _render_notes(entity_block, localizations)
                if notes:
                    patch[output_key][entity] = notes

        heroes = block.get("heroes")
        if isinstance(heroes, dict):
            for hero, hero_block in heroes.items():
                if not isinstance(hero_block, dict):
                    continue
                per_hero: dict[str, list[dict[str, Any]]] = {}
                for sub_key, sub_block in hero_block.items():
                    if not isinstance(sub_block, dict):
                        continue
                    notes = _render_notes(sub_block, localizations)
                    if notes:
                        per_hero[sub_key] = notes
                if per_hero:
                    patch["heroes"][hero] = per_hero

        patches.append(patch)

    if not patches:
        raise ChangelogError(f"{manifest_path} produced no patch blocks")

    return {
        "schema_version": CHANGELOG_SCHEMA_VERSION,
        "locales": sorted(localizations),
        "patches": patches,
    }


def search_changelog(
    changelog: dict[str, Any],
    *,
    grep: str | None = None,
    entity: str | None = None,
    note_patch: str | None = None,
    locale: str = "english",
) -> list[dict[str, Any]]:
    """Flat search over changelog entries. All filters are AND-ed; `grep`
    matches note text (chosen locale) or token, `entity` matches the
    entity/section identifier."""
    needle = grep.lower() if grep else None
    entity_needle = entity.lower() if entity else None
    results: list[dict[str, Any]] = []

    def emit(patch: dict[str, Any], scope: str, entity_name: str, entry: dict[str, Any]) -> None:
        text = entry["text"].get(locale, "")
        matchable = f"{text.lower()}\n{entry['token'].lower()}"
        if needle is not None and needle not in matchable:
            return
        if entity_needle is not None and entity_needle not in entity_name.lower():
            return
        results.append(
            {
                "patch": patch["name"],
                "date": patch["date"],
                "scope": scope,
                "entity": entity_name,
                "token": entry["token"],
                "text": text,
            }
        )

    for patch in changelog["patches"]:
        if note_patch is not None and patch["name"] != note_patch:
            continue
        for section in patch["generic"]:
            for entry in section["notes"]:
                emit(patch, "generic", section["section"], entry)
        for scope in ("items", "neutral_items", "neutral_creeps"):
            for entity_name, notes in patch[scope].items():
                for entry in notes:
                    emit(patch, scope, entity_name, entry)
        for hero, per_hero in patch["heroes"].items():
            for sub_key, notes in per_hero.items():
                for entry in notes:
                    emit(patch, "heroes", f"{hero}/{sub_key}", entry)
    return results
