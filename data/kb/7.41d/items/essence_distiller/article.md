---
title: Essence Distiller
kind: item
patch: 7.41d
card:
  entity: essence_distiller
  sentences:
  - text: Essence Distiller is a rare 1775-gold item that grants 3 All Attributes,
      6 Armor, 150 Mana, and 1.75 Mana Regeneration and provides the Soul Release
      active, which provides health regeneration to allies with Soul Heal Amount 40
      and deals damage per second to enemies with Soul Damage Amount 25.
    marks:
    - gamefile:items/item_essence_distiller#cost
    - gamefile:items/item_essence_distiller#attribs
    - loc:DOTA_Tooltip_ability_item_essence_distiller_Description
  - text: It is built from Urn of Shadows for 825 gold, Chainmail for 500 gold, Wizard
      Hat for 250 gold, and a recipe costing 200 gold.
    marks:
    - gamefile:items/item_essence_distiller#components
    - gamefile:items/item_essence_distiller#cost
  - text: Soul Release has 1000 cast range.
    marks:
    - gamefile:items/item_essence_distiller#mechanics
  - text: Soul Release has a 10.0 cooldown.
    marks:
    - gamefile:items/item_essence_distiller#mechanics
  - text: Soul Release has 8.0 Duration.
    marks:
    - gamefile:items/item_essence_distiller#attribs
  - text: When ground targeted, Soul Release lies dormant and attaches to the first
      enemy that enters its latch radius.
    marks:
    - loc:DOTA_Tooltip_ability_item_essence_distiller_Description
  - text: Its Ground Duration is 15.0.
    marks:
    - gamefile:items/item_essence_distiller#attribs
  - text: Its Latch Range is 450.
    marks:
    - gamefile:items/item_essence_distiller#attribs
  - text: On enemies, Soul Release provides True Sight over them.
    marks:
    - loc:DOTA_Tooltip_ability_item_essence_distiller_Description
  - text: On enemies, Soul Release shares their vision with the wearer's team.
    marks:
    - loc:DOTA_Tooltip_ability_item_essence_distiller_Description
  - text: Soul Release has 2 Soul Initial Charges.
    marks:
    - gamefile:items/item_essence_distiller#attribs
  - text: It gains 1 Soul Additional Charge whenever an enemy hero dies within its
      1500 Soul Radius.
    marks:
    - gamefile:items/item_essence_distiller#attribs
    - loc:DOTA_Tooltip_ability_item_essence_distiller_Description
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