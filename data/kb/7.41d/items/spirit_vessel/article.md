---
title: Spirit Vessel
kind: item
patch: 7.41d
card:
  entity: spirit_vessel
  sentences:
  - text: Spirit Vessel is a rare 2725-gold item that grants 10 All Attributes, 2
      Armor, and 1.75 Mana Regeneration; its 8.0-second Soul Release drains 4% of
      an enemy’s current Health, reduces Health Restoration by 70%, and deals 25 damage,
      or grants an ally 40 Health Regeneration.
    marks:
    - gamefile:items/item_spirit_vessel#cost
    - gamefile:items/item_spirit_vessel#attribs
    - loc:DOTA_Tooltip_ability_item_spirit_vessel_Description
  - text: Its build formula is Urn of Shadows (825 gold) + Diadem (1000 gold) + Recipe
      (900 gold).
    marks:
    - gamefile:items/item_spirit_vessel#components
  - text: Soul Release is unit-targeted.
    marks:
    - gamefile:items/item_spirit_vessel#mechanics
  - text: Soul Release has a cast range of 750.
    marks:
    - gamefile:items/item_spirit_vessel#mechanics
  - text: Soul Release has a 10.0 cooldown.
    marks:
    - gamefile:items/item_spirit_vessel#mechanics
  - text: Spirit Vessel starts with 2 Soul charges.
    marks:
    - gamefile:items/item_spirit_vessel#attribs
  - text: It gains 1 Soul charge when an enemy hero dies within 1500 range or when
      its user dies.
    marks:
    - gamefile:items/item_spirit_vessel#attribs
    - loc:DOTA_Tooltip_ability_item_spirit_vessel_Description
---

# Spirit Vessel

Spirit Vessel is a rare item that grants All Attributes, Armor, and Mana Regeneration and provides Soul Release, which reduces enemies’ current Health and Health Restoration while dealing damage, or grants Health Regeneration to allies. [gamefile:items/item_spirit_vessel#cost] [gamefile:items/item_spirit_vessel#attribs] [loc:DOTA_Tooltip_ability_item_spirit_vessel_Description]

## Cost

| Stat | Value |
|---|---:|
| Cost | 2725 gold |

[gamefile:items/item_spirit_vessel#cost]

## Components

| Component | Cost |
|---|---:|
| Urn of Shadows | 825 gold |
| Diadem | 1000 gold |
| Recipe | 900 gold |

[gamefile:items/item_spirit_vessel#components]

## Stats

| Stat | Value |
|---|---:|
| All Attributes | 10 |
| Armor | 2 |
| Health | 0 |
| Mana Regeneration | 1.75 |
| Duration | 8.0 |
| Enemy HP Drain | 4% |
| Enemy Slow Pct | 0 |
| Restoration Reduction Enemy | 70% |
| Soul Additional Charges | 1 |
| Soul Damage Amount | 25 |
| Soul Heal Amount | 40 |
| Soul Initial Charge | 2 |
| Soul Radius | 1500 |

[gamefile:items/item_spirit_vessel#attribs]

## Soul Release

| Property | Value |
|---|---:|
| Behavior | Unit Target, DOTA_ABILITY_BEHAVIOR_DONT_PROC_OTHER_ABILITIES |
| Cast Range | 750 |
| Cooldown | 10.0 |

[gamefile:items/item_spirit_vessel#mechanics]

When used on an enemy, Soul Release reduces current Health and Health Restoration and deals damage over time; when used on an ally, it provides Health Regeneration. [loc:DOTA_Tooltip_ability_item_spirit_vessel_Description]

Spirit Vessel gains charges when an enemy hero dies within range or when its user dies. [loc:DOTA_Tooltip_ability_item_spirit_vessel_Description]