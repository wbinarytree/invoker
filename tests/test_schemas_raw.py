from invoker.schemas.raw import (
    LiquipediaAbility,
    ODAbility,
    ODHero,
    ODMatchup,
    ODProMatch,
    StratzSynergyEdge,
)


def test_smoke_models():
    ODHero(
        id=1,
        name="npc_dota_hero_antimage",
        localized_name="Anti-Mage",
        primary_attr="agi",
        attack_type="Melee",
    )
    ODMatchup(hero_id=1, games_played=100, wins=55)
    ODProMatch(match_id=123456)
    ODAbility(dname="Mana Break")
    StratzSynergyEdge(heroId1=1, heroId2=2, synergy=0.12, matchCount=500)  # noqa: N815
    LiquipediaAbility(name="Slithereen Crush", text="Slams the ground.")
