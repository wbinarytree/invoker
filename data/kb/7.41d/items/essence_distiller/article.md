---
title: Essence Distiller
kind: item
patch: 7.41d
card:
  entity: essence_distiller
  sentences:
  - text: Essence Distiller is a rare 1775-gold item that grants 3 All Attributes,
      6 Armor, 150 Mana, and 1.75 Mana Regeneration and provides Soul Release, which
      regenerates allied health or deals 25 damage per second to enemies.
    marks:
    - gamefile:items/item_essence_distiller#cost
    - gamefile:items/item_essence_distiller#attribs
    - loc:DOTA_Tooltip_ability_item_essence_distiller_Description
  - text: Its build formula is Urn of Shadows (825 gold), Chainmail (500 gold), Wizard
      Hat (250 gold), and Recipe (200 gold).
    marks:
    - gamefile:items/item_essence_distiller#components
    - gamefile:items/item_essence_distiller#cost
  - text: Soul Release has a cast range of 1000.
    marks:
    - gamefile:items/item_essence_distiller#mechanics
  - text: Soul Release has a cooldown of 10.0.
    marks:
    - gamefile:items/item_essence_distiller#mechanics
  - text: On an ally, Soul Release provides health regeneration with a Soul Heal Amount
      of 40.
    marks:
    - loc:DOTA_Tooltip_ability_item_essence_distiller_Description
    - gamefile:items/item_essence_distiller#attribs
  - text: When ground targeted, Soul Release lies dormant for a Ground Duration of
      15.0.
    marks:
    - loc:DOTA_Tooltip_ability_item_essence_distiller_Description
    - gamefile:items/item_essence_distiller#attribs
  - text: It attaches to the first enemy that enters its 450 Latch Range.
    marks:
    - loc:DOTA_Tooltip_ability_item_essence_distiller_Description
    - gamefile:items/item_essence_distiller#attribs
  - text: On an enemy, Soul Release deals 25 damage per second.
    marks:
    - loc:DOTA_Tooltip_ability_item_essence_distiller_Description
    - gamefile:items/item_essence_distiller#attribs
  - text: On enemies, it provides True Sight and shares their vision with the wearer's
      team.
    marks:
    - loc:DOTA_Tooltip_ability_item_essence_distiller_Description
  - text: Soul Release has a Duration of 8.0.
    marks:
    - gamefile:items/item_essence_distiller#attribs
  - text: It gains 1 additional charge whenever an enemy hero dies within its 1500
      Soul Radius.
    marks:
    - loc:DOTA_Tooltip_ability_item_essence_distiller_Description
    - gamefile:items/item_essence_distiller#attribs
  - text: Soul Release starts with 2 charges.
    marks:
    - gamefile:items/item_essence_distiller#attribs
---

# Essence Distiller

Essence Distiller is a rare item that grants All Attributes, Armor, Mana, and Mana Regeneration and provides the Soul Release active. [gamefile:items/item_essence_distiller#cost] [gamefile:items/item_essence_distiller#attribs] [loc:DOTA_Tooltip_ability_item_essence_distiller_Description]

## Components

| Component | Gold cost |
|---|---:|
| Urn of Shadows | 825 gold |
| Chainmail | 500 gold |
| Wizard Hat | 250 gold |
| Recipe | 200 gold |
| **Essence Distiller** | **1775 gold** |

[gamefile:items/item_essence_distiller#components] [gamefile:items/item_essence_distiller#cost]

## Stats

| Stat | Value |
|---|---:|
| ALL ATTRIBUTES | 3 |
| ARMOR | 6 |
| MANA | 150 |
| DURATION | 8.0 |
| GROUND DURATION | 15.0 |
| LATCH RANGE | 450 |
| LATCH VISION | 450 |
| LINGER AFTER LATCH DURATION | 0.5 |
| MANA REGENERATION | 1.75 |
| SOUL ADDITIONAL CHARGES | 1 |
| SOUL DAMAGE AMOUNT | 25 |
| SOUL HEAL AMOUNT | 40 |
| SOUL INITIAL CHARGE | 2 |
| SOUL RADIUS | 1500 |

[gamefile:items/item_essence_distiller#attribs]

| Property | Value |
|---|---:|
| Behavior | Point Target, Unit Target, AOE, DOTA_ABILITY_BEHAVIOR_DONT_PROC_OTHER_ABILITIES |
| Cast range | 1000 |
| Cooldown | 10.0 |

[gamefile:items/item_essence_distiller#mechanics]

## Soul Release

Soul Release provides health regeneration when cast on allies. It can instead be ground targeted, lying dormant and attaching to the first enemy that enters its latch radius. On enemies, it deals damage per second, provides True Sight over them, and shares their vision with the wearer's team. The effect lasts for its duration and gains charges whenever an enemy hero dies within its soul radius. [loc:DOTA_Tooltip_ability_item_essence_distiller_Description]