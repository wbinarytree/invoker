from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


class GameFilesSourceError(ValueError):
    pass


class GameFilesSource:
    """JSON-only consumer for game-file snapshots."""

    def __init__(self, root: Path, patch: str, locale: str = "english") -> None:
        self.patch_dir = root / patch
        self.locale = locale
        if not self.patch_dir.exists():
            raise GameFilesSourceError(f"game snapshot does not exist: {self.patch_dir}")
        self._heroes_raw = self._read_json("heroes.json")
        self._abilities_raw = self._read_json("abilities.json")
        self._hero_abilities = self._read_json("hero_abilities.json")
        self._items_raw = self._read_json("items.json")
        self._neutral_items_raw = self._read_json("neutral_items.json")
        self._localization = self._read_json(f"localization/{locale}.json")
        self._talent_replacements = _build_talent_replacements(self._abilities_raw)
        self._talent_names = _build_talent_names(self._abilities_raw, self._talent_replacements)

    def heroes(self) -> list[dict[str, Any]]:
        """Full hero list with base metadata in the OpenDota constants shape."""
        records = [
            _hero_record(name, raw, self._localization)
            for name, raw in self._heroes_raw.items()
            if isinstance(raw, dict) and _is_live_hero(raw)
        ]
        return sorted(records, key=lambda h: h["id"])

    def abilities(self) -> dict[str, Any]:
        """Ability descriptions keyed by internal name in the OpenDota constants shape."""
        records = {
            name: _ability_record(
                name,
                raw,
                self._localization,
                self._talent_names,
                self._talent_replacements,
            )
            for name, raw in self._abilities_raw.items()
            if isinstance(raw, dict)
        }
        for hero_data in self._hero_abilities.values():
            if not isinstance(hero_data, dict):
                continue
            for talent in hero_data.get("talents", []):
                if not isinstance(talent, dict):
                    continue
                name = talent.get("name")
                if (
                    isinstance(name, str)
                    and name.startswith("special_bonus_")
                    and name not in records
                ):
                    records[name] = _ability_record(
                        name,
                        {},
                        self._localization,
                        self._talent_names,
                        self._talent_replacements,
                    )
        return records

    def hero_abilities_map(self) -> dict[str, Any]:
        """Maps hero internal name to ability and talent lists."""
        return self._hero_abilities

    def hero_stats(self) -> dict[str, Any]:
        """Hero stat constants keyed by hero id string, matching OpenDota constants."""
        stats: dict[str, Any] = {}
        for name, raw in self._heroes_raw.items():
            if not isinstance(raw, dict) or not _is_live_hero(raw):
                continue
            record = _hero_record(name, raw, self._localization)
            hero_id = str(record["id"])
            stats[hero_id] = {
                "id": record["id"],
                "name": name,
                "localized_name": record["localized_name"],
                "primary_attr": record["primary_attr"],
                "attack_type": record["attack_type"],
                "roles": record["roles"],
                "base_str": _num(raw.get("AttributeBaseStrength")),
                "base_agi": _num(raw.get("AttributeBaseAgility")),
                "base_int": _num(raw.get("AttributeBaseIntelligence")),
                "str_gain": _num(raw.get("AttributeStrengthGain")),
                "agi_gain": _num(raw.get("AttributeAgilityGain")),
                "int_gain": _num(raw.get("AttributeIntelligenceGain")),
                "base_armor": _num(raw.get("ArmorPhysical")),
                "base_attack_min": _num(raw.get("AttackDamageMin")),
                "base_attack_max": _num(raw.get("AttackDamageMax")),
                "base_attack_speed": _num(raw.get("BaseAttackSpeed", 100)),
                "base_attack_time": _num(raw.get("AttackRate")),
                "attack_animation_point": _num(raw.get("AttackAnimationPoint")),
                "attack_acquisition_range": _num(raw.get("AttackAcquisitionRange")),
                "attack_range": _num(raw.get("AttackRange")),
                "move_speed": _num(raw.get("MovementSpeed")),
            }
        return stats

    def items(self) -> dict[str, Any]:
        return self._items_raw

    def item_records(self) -> dict[str, Any]:
        """Item records with localization joins, keyed by internal name.

        Recipes are folded into their result item (`components`,
        `recipe_cost`) rather than emitted as records of their own.
        """
        records: dict[str, Any] = {}
        recipes: dict[str, tuple[list[str], int]] = {}
        for name, raw in self._items_raw.items():
            if not isinstance(raw, dict):
                continue
            if raw.get("ItemRecipe") == "1":
                result = raw.get("ItemResult")
                requirements = raw.get("ItemRequirements")
                if isinstance(result, str) and isinstance(requirements, dict) and requirements:
                    first_variant = requirements[min(requirements)]
                    components = [
                        part.rstrip("*") for part in str(first_variant).split(";") if part.strip()
                    ]
                    recipes[result] = (components, _int_or_zero(raw.get("ItemCost")))
                continue
            records[name] = _item_record(name, raw, self._localization)
        for result, (components, recipe_cost) in recipes.items():
            record = records.get(result)
            if record is None:
                continue
            record["components"] = components
            if recipe_cost:
                record["recipe_cost"] = recipe_cost
        return records

    def neutral_items(self) -> dict[str, Any]:
        return self._neutral_items_raw

    def _read_json(self, relative_path: str) -> Any:
        path = self.patch_dir / relative_path
        if not path.exists():
            raise GameFilesSourceError(f"missing game snapshot file: {path}")
        return json.loads(path.read_text())


def _is_live_hero(raw: dict[str, Any]) -> bool:
    hero_id = raw.get("HeroID")
    enabled = raw.get("Enabled", "1")
    return hero_id not in (None, "", "0") and enabled != "0"


def _hero_record(name: str, raw: dict[str, Any], localization: dict[str, Any]) -> dict[str, Any]:
    return {
        "id": int(str(raw["HeroID"])),
        "name": name,
        "localized_name": _localized_hero_name(name, raw, localization),
        "primary_attr": _primary_attr(raw.get("AttributePrimary")),
        "attack_type": _attack_type(raw.get("AttackCapabilities")),
        "roles": _split_csv(raw.get("Role")),
    }


def _localized_hero_name(name: str, raw: dict[str, Any], localization: dict[str, Any]) -> str:
    for key in (
        f"{name}:n",
        f"{name}__en:n",
        f"DOTA_Tooltip_Hero_{name}",
        f"dota_tooltip_hero_{name}",
    ):
        value = localization.get(key)
        if isinstance(value, str) and value:
            return value
    guide_name = raw.get("workshop_guide_name")
    if isinstance(guide_name, str) and guide_name:
        return guide_name
    return _title_from_internal(name.removeprefix("npc_dota_hero_"))


def _ability_record(
    name: str,
    raw: dict[str, Any],
    localization: dict[str, Any],
    talent_names: dict[str, str],
    talent_replacements: dict[str, dict[str, str]],
) -> dict[str, Any]:
    record: dict[str, Any] = {
        "dname": _localized_ability_name(name, localization, talent_names, talent_replacements),
        "behavior": _behavior(raw.get("AbilityBehavior")),
        "dmg_type": _damage_type(raw.get("AbilityUnitDamageType")),
        "bkbpierce": _spell_immunity(raw.get("SpellImmunityType")),
        "dispellable": _dispellable(raw.get("SpellDispellableType")),
        "desc": _localized_ability_desc(name, raw, localization),
        "attrib": _attribs(name, raw.get("AbilityValues"), localization),
    }
    if "AbilityCastRange" in raw:
        record["cast_range"] = _levels(raw["AbilityCastRange"])
    if timing := _timing(raw):
        record["timing"] = timing
    if "AbilityManaCost" in raw:
        record["mc"] = _levels(raw["AbilityManaCost"])
    if "AbilityCooldown" in raw:
        record["cd"] = _levels(raw["AbilityCooldown"])
    if raw.get("Innate") == "1":
        record["is_innate"] = True
    if raw.get("HasShardUpgrade") == "1":
        record["has_shard_upgrade"] = True
    if raw.get("HasScepterUpgrade") == "1":
        record["has_scepter_upgrade"] = True
    if raw.get("IsGrantedByShard") == "1":
        record["is_granted_by_shard"] = True
    if raw.get("IsGrantedByScepter") == "1":
        record["is_granted_by_scepter"] = True
    if scepter_desc := _localized_upgrade_desc(name, raw, localization, "scepter"):
        record["scepter_desc"] = scepter_desc
    if shard_desc := _localized_upgrade_desc(name, raw, localization, "shard"):
        record["shard_desc"] = shard_desc
    return record


def _item_record(name: str, raw: dict[str, Any], localization: dict[str, Any]) -> dict[str, Any]:
    desc, desc_token = _localized_item_desc(name, raw, localization)
    record: dict[str, Any] = {
        "dname": _localized_item_name(name, localization),
        "desc": desc,
        "behavior": _behavior(raw.get("AbilityBehavior")),
        "dmg_type": _damage_type(raw.get("AbilityUnitDamageType")),
        "dispellable": _dispellable(raw.get("SpellDispellableType")),
        "attrib": _attribs(name, raw.get("AbilityValues"), localization),
    }
    if desc_token:
        record["desc_token"] = desc_token
    if "ItemCost" in raw:
        record["cost"] = _int_or_zero(raw["ItemCost"])
    if quality := raw.get("ItemQuality"):
        record["quality"] = str(quality)
    for lore_token in (
        f"DOTA_Tooltip_ability_{name}_Lore",
        f"DOTA_Tooltip_Ability_{name}_Lore",
    ):
        lore = localization.get(lore_token)
        if isinstance(lore, str) and lore:
            record["lore"] = lore
            record["lore_token"] = lore_token
            break
    if "AbilityCastRange" in raw:
        record["cast_range"] = _levels(raw["AbilityCastRange"])
    if "AbilityManaCost" in raw:
        record["mc"] = _levels(raw["AbilityManaCost"])
    if "AbilityCooldown" in raw:
        record["cd"] = _levels(raw["AbilityCooldown"])
    return record


def _int_or_zero(value: Any) -> int:
    try:
        return int(str(value))
    except (TypeError, ValueError):
        return 0


def _localized_item_name(name: str, localization: dict[str, Any]) -> str:
    for key in (
        f"DOTA_Tooltip_Ability_{name}",
        f"DOTA_Tooltip_ability_{name}",
    ):
        value = localization.get(key)
        if isinstance(value, str) and value:
            return value
    return _title_from_internal(name.removeprefix("item_"))


def _localized_item_desc(
    name: str,
    raw: dict[str, Any],
    localization: dict[str, Any],
) -> tuple[str | None, str | None]:
    """Resolved description text plus the token that actually resolved —
    packets cite the real token, never a synthesized casing."""
    replacements = ability_value_replacements(raw.get("AbilityValues"))
    for key in (
        f"DOTA_Tooltip_ability_{name}_Description",
        f"DOTA_Tooltip_Ability_{name}_Description",
    ):
        value = localization.get(key)
        if isinstance(value, str) and value:
            return _strip_tooltip_html(resolve_percent_template(value, replacements)), key
    return None, None


_TAG_BREAK_PATTERN = re.compile(r"</h\d>|<br\s*/?>", re.IGNORECASE)
_TAG_PATTERN = re.compile(r"<[^>]+>")


def _strip_tooltip_html(text: str) -> str:
    text = _TAG_BREAK_PATTERN.sub("\n", text)
    text = _TAG_PATTERN.sub("", text)
    lines = [" ".join(line.split()) for line in text.split("\n")]
    return "\n".join(line for line in lines if line)


def _localized_upgrade_desc(
    name: str,
    raw: dict[str, Any],
    localization: dict[str, Any],
    upgrade: str,
) -> str | None:
    replacements = ability_value_replacements(raw.get("AbilityValues"))
    for key in (
        f"DOTA_Tooltip_ability_{name}_{upgrade}_description",
        f"DOTA_Tooltip_Ability_{name}_{upgrade}_description",
    ):
        value = localization.get(key)
        if isinstance(value, str) and value:
            return resolve_percent_template(value, replacements)
    return None


def _localized_ability_name(
    name: str,
    localization: dict[str, Any],
    talent_names: dict[str, str],
    talent_replacements: dict[str, dict[str, str]],
) -> str:
    for key in (
        f"DOTA_Tooltip_ability_{name}",
        f"DOTA_Tooltip_Ability_{name}",
        f"dota_tooltip_ability_{name}",
    ):
        value = localization.get(key)
        if isinstance(value, str) and value:
            return _resolve_talent_template(value, talent_replacements.get(name, {}))
    if name in talent_names:
        return talent_names[name]
    return _title_from_internal(name)


def _localized_ability_desc(
    name: str,
    raw: dict[str, Any],
    localization: dict[str, Any],
) -> str | None:
    replacements = ability_value_replacements(raw.get("AbilityValues"))
    for key in (
        f"DOTA_Tooltip_ability_{name}_Description",
        f"DOTA_Tooltip_Ability_{name}_Description",
        f"dota_tooltip_ability_{name}_description",
    ):
        value = localization.get(key)
        if isinstance(value, str) and value:
            return resolve_percent_template(value, replacements)
    return None


def _build_talent_replacements(abilities: dict[str, Any]) -> dict[str, dict[str, str]]:
    replacements: dict[str, dict[str, str]] = {}
    for ability_name, raw in abilities.items():
        if not isinstance(raw, dict):
            continue
        values = raw.get("AbilityValues")
        if not isinstance(values, dict):
            continue
        if ability_name.startswith("special_bonus_"):
            for field_name, field_value in values.items():
                if isinstance(field_value, dict) and isinstance(field_value.get("value"), str):
                    replacements.setdefault(ability_name, {})[str(field_name)] = field_value[
                        "value"
                    ]
                elif isinstance(field_value, str):
                    replacements.setdefault(ability_name, {})[str(field_name)] = field_value
        for field_name, field_value in values.items():
            if not isinstance(field_value, dict):
                continue
            placeholder = f"bonus_{field_name}"
            for key, value in field_value.items():
                if key.startswith("special_bonus_") and isinstance(value, str):
                    replacements.setdefault(key, {})[placeholder] = value
    return replacements


def _build_talent_names(
    abilities: dict[str, Any],
    talent_replacements: dict[str, dict[str, str]],
) -> dict[str, str]:
    names: dict[str, str] = {}
    for talent_name, replacements in talent_replacements.items():
        for placeholder, value in replacements.items():
            field_name = placeholder.removeprefix("bonus_")
            names.setdefault(talent_name, f"{value} {_label_from_key(field_name)}")
    for ability_name in abilities:
        if ability_name.startswith("special_bonus_"):
            names.setdefault(ability_name, _special_bonus_name(ability_name))
    return names


def _resolve_talent_template(template: str, replacements: dict[str, str]) -> str:
    rendered = template
    for key, value in replacements.items():
        token = f"{{s:{key}}}"
        unsigned = value.lstrip("+-")
        rendered = rendered.replace(f"+{token}", f"+{unsigned}")
        rendered = rendered.replace(f"-{token}", f"-{unsigned}")
        rendered = rendered.replace(token, value)
    return _collapse_replaced_percent_escape(rendered)


def ability_value_replacements(values: Any) -> dict[str, str]:
    if not isinstance(values, dict):
        return {}
    replacements: dict[str, str] = {}
    for field_name, raw in values.items():
        if isinstance(raw, dict):
            if "value" not in raw:
                continue
            value = raw["value"]
        else:
            value = raw
        replacements[str(field_name)] = _template_value(value)
    return replacements


def resolve_percent_template(template: str, replacements: dict[str, str]) -> str:
    rendered = template
    for key, value in replacements.items():
        rendered = rendered.replace(f"%{key}%", value)
    return _collapse_replaced_percent_escape(rendered)


def _template_value(value: Any) -> str:
    if not isinstance(value, str):
        return str(value)
    parts = value.split()
    return "/".join(parts) if len(parts) > 1 else value


def _collapse_replaced_percent_escape(value: str) -> str:
    # KV tooltips escape a literal percent sign as "%%" ("%damage%%%" renders
    # as "40%"). Collapse only when the escape directly follows a substituted
    # numeric value: elsewhere a "%" run may straddle an unreplaced "%key%"
    # token boundary, and folding it would corrupt the token that later
    # passes (or a reader) still need to see intact.
    chars: list[str] = []
    index = 0
    while index < len(value):
        if (
            value.startswith("%%", index)
            and chars
            and (chars[-1].isdigit() or chars[-1] in {"+", "-", "."})
        ):
            chars.append("%")
            index += 2
            continue
        chars.append(value[index])
        index += 1
    return "".join(chars)


_VARIABLE_LABEL_TEMPLATE = re.compile(r"^([%+\-\s]*)\$(\w+)$")


def _attrib_label(name: str, key: str, localization: dict[str, Any]) -> tuple[str, bool]:
    """Tooltip label for one AbilityValues key, plus whether the value
    renders as a percentage.

    Tooltip tokens like '%+$spell_resist' reference shared label variables
    (dota_ability_variable_spell_resist = "Magic Resistance") — the label
    players actually see. A key-derived fallback like "bonus magical armor"
    misnames the stat, which the mage-slayer cross-reference caught."""
    for token in (
        f"DOTA_Tooltip_ability_{name}_{key}",
        f"DOTA_Tooltip_Ability_{name}_{key}",
    ):
        text = localization.get(token)
        if isinstance(text, str) and text:
            match = _VARIABLE_LABEL_TEMPLATE.match(text.strip())
            if match:
                label = localization.get(f"dota_ability_variable_{match.group(2)}")
                if isinstance(label, str) and label:
                    return label, "%" in match.group(1)
            break
    return _label_from_key(key), False


def _raw_desc_template(name: str, localization: dict[str, Any]) -> str:
    """Unresolved description template — the source of the percent flag for
    keys with no tooltip label token: `%key%%%` renders as a literal % after
    the substituted value (e.g. mage_slayer's `%spell_amp_debuff%%%`)."""
    for token in (
        f"DOTA_Tooltip_ability_{name}_Description",
        f"DOTA_Tooltip_Ability_{name}_Description",
        f"dota_tooltip_ability_{name}_description",
    ):
        value = localization.get(token)
        if isinstance(value, str) and value:
            return value
    return ""


def _attribs(name: str, values: Any, localization: dict[str, Any]) -> list[dict[str, Any]]:
    if not isinstance(values, dict):
        return []
    rows: list[dict[str, Any]] = []
    desc_template = _raw_desc_template(name, localization)
    for key, raw in values.items():
        value: Any
        scepter_bonus: Any = None
        shard_bonus: Any = None
        if isinstance(raw, dict):
            value = raw.get("value")
            scepter_bonus = raw.get("special_bonus_scepter")
            shard_bonus = raw.get("special_bonus_shard")
        else:
            value = raw
        # A row with no base value can still exist purely as a Scepter/Shard
        # upgrade (e.g. shard_amp_duration: {special_bonus_shard: "5.0"}).
        if value is None and scepter_bonus is None and shard_bonus is None:
            continue
        label, percent = _attrib_label(name, str(key), localization)
        if not percent and f"%{key}%%%" in desc_template:
            percent = True
        row: dict[str, Any] = {
            "key": str(key),
            "header": label.upper() + ":",
        }
        if percent:
            row["percent"] = True
        if value is not None:
            row["value"] = _levels(value)
        if scepter_bonus is not None:
            row["scepter_bonus"] = str(scepter_bonus)
        if shard_bonus is not None:
            row["shard_bonus"] = str(shard_bonus)
        rows.append(row)
    return rows


def _timing(raw: dict[str, Any]) -> dict[str, Any]:
    fields = {
        "cast_point": "AbilityCastPoint",
        "channel_time": "AbilityChannelTime",
        "cast_animation": "AbilityCastAnimation",
        "cast_gesture_slot": "AbilityCastGestureSlot",
        "animation_playback_rate": "AnimationPlaybackRate",
    }
    timing: dict[str, Any] = {}
    for output_key, raw_key in fields.items():
        value = raw.get(raw_key)
        if isinstance(value, str) and value:
            timing[output_key] = _levels(value)
    return timing


def _behavior(value: Any) -> list[str]:
    if not isinstance(value, str) or not value:
        return []
    mapping = {
        "DOTA_ABILITY_BEHAVIOR_HIDDEN": "Hidden",
        "DOTA_ABILITY_BEHAVIOR_PASSIVE": "Passive",
        "DOTA_ABILITY_BEHAVIOR_NO_TARGET": "No Target",
        "DOTA_ABILITY_BEHAVIOR_UNIT_TARGET": "Unit Target",
        "DOTA_ABILITY_BEHAVIOR_POINT": "Point Target",
        "DOTA_ABILITY_BEHAVIOR_AOE": "AOE",
        "DOTA_ABILITY_BEHAVIOR_CHANNELLED": "Channelled",
        "DOTA_ABILITY_BEHAVIOR_TOGGLE": "Toggle",
        "DOTA_ABILITY_BEHAVIOR_IMMEDIATE": "Immediate",
        "DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK": "Doesn't Resume Attack",
        "DOTA_ABILITY_BEHAVIOR_SUPPRESS_ASSOCIATED_CONSUMABLE": "Suppresses Associated Consumable",
        "DOTA_ABILITY_BEHAVIOR_IGNORE_CHANNEL": "Usable While Channelling",
        "DOTA_ABILITY_BEHAVIOR_OPTIONAL_UNIT_TARGET": "Optional Unit Target",
        "DOTA_ABILITY_BEHAVIOR_ROOT_DISABLES": "Root Disables",
        "DOTA_ABILITY_BEHAVIOR_DONT_PROC_OTHER_ABILITIES": "Doesn't Proc Other Abilities",
        "DOTA_ABILITY_BEHAVIOR_DIRECTIONAL": "Directional",
        "DOTA_ABILITY_BEHAVIOR_OVERSHOOT": "Overshoot",
        "DOTA_ABILITY_BEHAVIOR_DONT_CANCEL_MOVEMENT": "Doesn't Cancel Movement",
        "DOTA_ABILITY_BEHAVIOR_UNSWAPPABLE": "Unswappable",
        "DOTA_ABILITY_BEHAVIOR_IGNORE_BACKSWING": "Ignores Backswing",
        "DOTA_ABILITY_BEHAVIOR_NOT_LEARNABLE": "Not Learnable",
        "DOTA_ABILITY_BEHAVIOR_DONT_RESUME_MOVEMENT": "Doesn't Resume Movement",
        "DOTA_ABILITY_BEHAVIOR_VECTOR_TARGETING": "Vector Targeting",
        "DOTA_ABILITY_BEHAVIOR_IGNORE_INVISIBLE": "Ignores Invisible",
        "DOTA_ABILITY_BEHAVIOR_IGNORE_PSEUDO_QUEUE": "Ignores Pseudo Queue",
        "DOTA_ABILITY_BEHAVIOR_DONT_CANCEL_CHANNEL": "Doesn't Cancel Channel",
    }

    def fallback(part: str) -> str:
        # a flag unseen in any snapshot still never reaches prose raw
        return part.removeprefix("DOTA_ABILITY_BEHAVIOR_").replace("_", " ").title()

    return [mapping.get(part.strip(), fallback(part.strip())) for part in value.split("|") if part.strip()]


def _damage_type(value: Any) -> str | None:
    return _enum_suffix(
        value,
        {
            "DAMAGE_TYPE_PHYSICAL": "Physical",
            "DAMAGE_TYPE_MAGICAL": "Magical",
            "DAMAGE_TYPE_PURE": "Pure",
        },
    )


def _spell_immunity(value: Any) -> str | None:
    if not isinstance(value, str) or not value:
        return None
    if value.endswith("_YES"):
        return "Yes"
    if value.endswith("_NO"):
        return "No"
    return None


def _dispellable(value: Any) -> str | None:
    return _enum_suffix(
        value,
        {
            "SPELL_DISPELLABLE_YES": "Yes",
            "SPELL_DISPELLABLE_NO": "No",
            "SPELL_DISPELLABLE_YES_STRONG": "Strong Dispels Only",
        },
    )


def _enum_suffix(value: Any, mapping: dict[str, str]) -> str | None:
    if not isinstance(value, str) or not value:
        return None
    return mapping.get(value)


def _primary_attr(value: Any) -> str:
    mapping = {
        "DOTA_ATTRIBUTE_STRENGTH": "str",
        "DOTA_ATTRIBUTE_AGILITY": "agi",
        "DOTA_ATTRIBUTE_INTELLECT": "int",
        "DOTA_ATTRIBUTE_INTELLIGENCE": "int",
        "DOTA_ATTRIBUTE_ALL": "all",
    }
    return mapping.get(str(value), "")


def _attack_type(value: Any) -> str:
    if value == "DOTA_UNIT_CAP_MELEE_ATTACK":
        return "Melee"
    if value == "DOTA_UNIT_CAP_RANGED_ATTACK":
        return "Ranged"
    return ""


def _split_csv(value: Any) -> list[str]:
    if not isinstance(value, str):
        return []
    return [part.strip() for part in value.split(",") if part.strip()]


def _levels(value: Any) -> str | list[str]:
    if not isinstance(value, str):
        return str(value)
    parts = value.split()
    return parts if len(parts) > 1 else value


def _num(value: Any) -> float | None:
    try:
        return float(str(value))
    except (TypeError, ValueError):
        return None


def _label_from_key(key: str) -> str:
    return key.replace("_", " ")


def _title_from_internal(name: str) -> str:
    return name.removeprefix("special_bonus_").replace("_", " ").title()


def _special_bonus_name(name: str) -> str:
    tail = name.removeprefix("special_bonus_")
    parts = tail.split("_")
    if len(parts) >= 2 and parts[-1].lstrip("-").isdigit():
        value = parts[-1]
        label = " ".join(parts[:-1]).replace("hp", "Health").replace("mp", "Mana")
        return f"+{value} {label.title()}"
    return _title_from_internal(name)
