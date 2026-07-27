---
title: Spirit Vessel
kind: item
patch: 7.41d
card:
  entity: spirit_vessel
  sentences:
  - text: Spirit Vessel is a rare item costing 2725 gold that grants 10 All Attributes,
      2 Armor, and 1.75 Mana Regeneration; its 8.0-second Soul Release reduces an
      enemy’s current health by 4% per second, reduces Health Restoration by 70%,
      and deals 25 damage per second, or provides an ally 40 health regeneration per
      second.
    marks:
    - gamefile:items/item_spirit_vessel#cost
    - gamefile:items/item_spirit_vessel#attribs
    - loc:DOTA_Tooltip_ability_item_spirit_vessel_Description
  - text: Soul Release targets a unit and doesn’t proc other abilities.
    marks:
    - gamefile:items/item_spirit_vessel#mechanics
  - text: Soul Release has 750 cast range.
    marks:
    - gamefile:items/item_spirit_vessel#mechanics
  - text: Soul Release has a 10.0 cooldown.
    marks:
    - gamefile:items/item_spirit_vessel#mechanics
  - text: Soul Release initially has 2 charges.
    marks:
    - gamefile:items/item_spirit_vessel#attribs
  - text: An enemy hero’s death within 1500 units or the user’s death grants 1 additional
      charge.
    marks:
    - gamefile:items/item_spirit_vessel#attribs
    - loc:DOTA_Tooltip_ability_item_spirit_vessel_Description
  - text: Spirit Vessel provides 0 Health.
    marks:
    - gamefile:items/item_spirit_vessel#attribs
  - text: Enemy Slow Pct is 0.
    marks:
    - gamefile:items/item_spirit_vessel#attribs
  - text: 'Build formula: Urn of Shadows (825 gold) + Diadem (1000 gold) + Recipe
      (900 gold); total cost 2725 gold.'
    marks:
    - gamefile:items/item_spirit_vessel#components
    - gamefile:items/item_spirit_vessel#cost
---

# Spirit Vessel

Spirit Vessel is a rare item that grants All Attributes, Armor, and Mana Regeneration and provides the active Soul Release, which reduces enemies’ current health and Health Restoration, deals damage to enemies, and provides health regeneration to allies. [gamefile:items/item_spirit_vessel#cost] [gamefile:items/item_spirit_vessel#attribs] [loc:DOTA_Tooltip_ability_item_spirit_vessel_Description]

## Stats

| Stat | Value |
|---|---:|
| All Attributes | 10 |
| Armor | 2 |
| Health | 0 |
| Mana Regeneration | 1.75 |
| Duration | 8.0 seconds |
| Enemy HP Drain | 4% of current health per second |
| Enemy Slow Pct | 0 |
| Restoration Reduction Enemy | 70% |
| Soul Additional Charges | 1 |
| Soul Damage Amount | 25 damage per second |
| Soul Heal Amount | 40 health regeneration per second |
| Soul Initial Charge | 2 |
| Soul Radius | 1500 units |

[gamefile:items/item_spirit_vessel#attribs] [loc:DOTA_Tooltip_ability_item_spirit_vessel_Description]

## Soul Release

| Property | Value |
|---|---|
| Classification | Active |
| Behavior | Unit Target, Doesn't Proc Other Abilities |
| Cast range | 750 |
| Cooldown | 10.0 |

[gamefile:items/item_spirit_vessel#mechanics] [loc:DOTA_Tooltip_ability_item_spirit_vessel_Description]

Against an enemy, Soul Release applies the current-health reduction, Health Restoration reduction, and damage for its duration; on an ally, it applies health regeneration for its duration. It gains charges whenever an enemy hero dies within the stated range or the user dies. [loc:DOTA_Tooltip_ability_item_spirit_vessel_Description]

## Components

| Component | Gold cost |
|---|---:|
| Urn of Shadows | 825 gold |
| Diadem | 1000 gold |
| Recipe | 900 gold |
| **Total cost** | **2725 gold** |

[gamefile:items/item_spirit_vessel#components] [gamefile:items/item_spirit_vessel#cost]