from invoker.kg.ability_context import (
    AttribEntry,
    TalentContext,
    build_ability_contexts,
)

_ABILITIES_MAP = {
    "hero_crush": {
        "dname": "Slithereen Crush",
        "behavior": "No Target",
        "dmg_type": "Physical",
        "bkbpierce": "No",
        "dispellable": "Strong Dispels Only",
        "desc": "Slams the ground.",
        "attrib": [
            {"key": "crush_damage", "header": "DAMAGE:", "value": ["75", "150", "225", "300"]},
            {"key": "stun_duration", "header": "STUN DURATION:", "value": "0.8"},
        ],
        "mc": "100",
        "cd": "7",
    },
    "hero_sprint": {
        "dname": "Guardian Sprint",
        "behavior": ["No Target", "Instant Cast"],
        "desc": "Move faster.",
        "attrib": [
            {"key": "bonus_speed", "header": "BONUS MOVE SPEED:",
             "value": ["10%", "18%", "26%", "34%"]},
        ],
        "mc": "25",
        "cd": ["29", "25", "21", "17"],
    },
    "hero_passive": {
        "dname": "Bash of the Deep",
        "behavior": "Passive",
        "dmg_type": "Physical",
        "bkbpierce": "Yes",
        "dispellable": "Strong Dispels Only",
        "desc": "Every 3 attacks bashes.",
        "attrib": [
            {"key": "bonus_damage", "header": "BONUS DAMAGE:", "value": ["35", "90", "145", "200"]},
        ],
    },
    "hero_innate": {
        "dname": "Seaborn Sentinel",
        "is_innate": True,
        "behavior": "Passive",
        "desc": "Bonuses in water.",
        "attrib": [
            {"key": "river_speed", "header": "BONUS MOVE SPEED:", "value": "18%"},
        ],
    },
    "special_bonus_hp_250": {"dname": "+250 Health"},
    "special_bonus_unique_hero": {"dname": "+2s Crush Duration"},
}

_HERO_ABILITIES_MAP = {
    "npc_dota_hero_test": {
        "abilities": ["hero_crush", "hero_sprint", "hero_passive", "generic_hidden", "hero_innate"],
        "talents": [
            {"name": "special_bonus_hp_250", "level": 1},
            {"name": "special_bonus_unique_hero", "level": 1},
        ],
    }
}


def test_base_ability_fields():
    abilities, _ = build_ability_contexts("npc_dota_hero_test", _ABILITIES_MAP, _HERO_ABILITIES_MAP)
    crush = next(a for a in abilities if a.internal_name == "hero_crush")
    assert crush.name == "Slithereen Crush"
    assert crush.source == "base_ability"
    assert crush.behavior == ["No Target"]
    assert crush.damage_type == "Physical"
    assert crush.pierces_debuff_immunity is False
    assert crush.dispellable == "Strong Dispels Only"
    assert crush.mana_cost == "100"
    assert crush.cooldown == "7"
    assert crush.attribs == [
        AttribEntry(header="DAMAGE:", value=["75", "150", "225", "300"]),
        AttribEntry(header="STUN DURATION:", value="0.8"),
    ]


def test_behavior_normalized_to_list():
    abilities, _ = build_ability_contexts("npc_dota_hero_test", _ABILITIES_MAP, _HERO_ABILITIES_MAP)
    sprint = next(a for a in abilities if a.internal_name == "hero_sprint")
    assert sprint.behavior == ["No Target", "Instant Cast"]
    assert sprint.cooldown == ["29", "25", "21", "17"]
    assert sprint.mana_cost == "25"
    assert sprint.damage_type is None
    assert sprint.dispellable is None
    assert sprint.pierces_debuff_immunity is None


def test_passive_ability_no_mc_cd():
    abilities, _ = build_ability_contexts("npc_dota_hero_test", _ABILITIES_MAP, _HERO_ABILITIES_MAP)
    passive = next(a for a in abilities if a.internal_name == "hero_passive")
    assert passive.pierces_debuff_immunity is True
    assert passive.mana_cost is None
    assert passive.cooldown is None


def test_innate_source():
    abilities, _ = build_ability_contexts("npc_dota_hero_test", _ABILITIES_MAP, _HERO_ABILITIES_MAP)
    innate = next(a for a in abilities if a.internal_name == "hero_innate")
    assert innate.source == "innate"


def test_generic_hidden_skipped():
    abilities, _ = build_ability_contexts("npc_dota_hero_test", _ABILITIES_MAP, _HERO_ABILITIES_MAP)
    names = [a.internal_name for a in abilities]
    assert "generic_hidden" not in names


def test_ability_order_preserved():
    abilities, _ = build_ability_contexts("npc_dota_hero_test", _ABILITIES_MAP, _HERO_ABILITIES_MAP)
    names = [a.internal_name for a in abilities]
    assert names == ["hero_crush", "hero_sprint", "hero_passive", "hero_innate"]


def test_talents_joined_and_leveled():
    _, talents = build_ability_contexts("npc_dota_hero_test", _ABILITIES_MAP, _HERO_ABILITIES_MAP)
    assert len(talents) == 2
    assert all(isinstance(t, TalentContext) for t in talents)
    assert talents[0].name == "+250 Health"
    assert talents[0].level == 1
    assert talents[1].name == "+2s Crush Duration"


def test_unknown_hero_returns_empty():
    abilities, talents = build_ability_contexts(
        "npc_dota_hero_nobody", _ABILITIES_MAP, _HERO_ABILITIES_MAP
    )
    assert abilities == []
    assert talents == []


def test_mc_and_cd_list_valued():
    abilities_map = {
        "hero_variable": {
            "dname": "Variable Cost Spell",
            "behavior": "No Target",
            "attrib": [],
            "mc": ["100", "95", "90", "80"],
            "cd": ["15", "13", "11", "7"],
        }
    }
    hero_abs = {
        "npc_dota_hero_test": {"abilities": ["hero_variable"], "talents": []}
    }
    abilities, _ = build_ability_contexts("npc_dota_hero_test", abilities_map, hero_abs)
    ab = abilities[0]
    assert ab.mana_cost == ["100", "95", "90", "80"]
    assert ab.cooldown == ["15", "13", "11", "7"]


def test_ability_absent_from_map_skipped():
    hero_abs = {
        "npc_dota_hero_test": {
            "abilities": ["hero_crush", "hero_does_not_exist"],
            "talents": [],
        }
    }
    abilities, _ = build_ability_contexts("npc_dota_hero_test", _ABILITIES_MAP, hero_abs)
    assert len(abilities) == 1
    assert abilities[0].internal_name == "hero_crush"
