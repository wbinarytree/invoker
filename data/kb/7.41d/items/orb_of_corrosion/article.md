---
title: Orb of Corrosion
kind: item
patch: 7.41d
card:
  entity: orb_of_corrosion
  sentences:
  - text: Orb of Corrosion is a rare item costing 1050 gold that grants 7 Agility;
      its attacks apply Corrosion for 3.0, inflicting -2 Corruption Armor, -8% Slow
      Melee or -16% Slow Ranged, and 16% Heal Reduction.
    marks:
    - gamefile:items/item_orb_of_corrosion#cost
    - gamefile:items/item_orb_of_corrosion#attribs
    - loc:DOTA_Tooltip_Ability_item_orb_of_corrosion_Description
  - text: Its build formula is Band of Elvenskin (450 gold) + Orb of Frost (300 gold)
      + Orb of Blight (300 gold).
    marks:
    - gamefile:items/item_orb_of_corrosion#components
  - text: Its behavior is passive.
    marks:
    - gamefile:items/item_orb_of_corrosion#mechanics
  - text: Its effect is dispellable.
    marks:
    - gamefile:items/item_orb_of_corrosion#mechanics
  - text: Seepage from the wounds of a warrior deity, sealed in an arcanist’s orb
      following a campaign of vicious slaughter.
    marks:
    - loc:DOTA_Tooltip_Ability_item_orb_of_corrosion_Lore
---

# Orb of Corrosion

Orb of Corrosion is a rare item that grants Agility and applies Corruption Armor, Slow Melee, Slow Ranged, and Heal Reduction through Corrosion. [gamefile:items/item_orb_of_corrosion#cost] [gamefile:items/item_orb_of_corrosion#attribs] [loc:DOTA_Tooltip_Ability_item_orb_of_corrosion_Description]

## Stats

| Stat | Value |
|---|---:|
| Agility | 7 |
| Corruption Armor | -2 |
| Duration | 3.0 |
| Heal Reduction | 16% |
| Slow Melee | -8% |
| Slow Ranged | -16% |

[gamefile:items/item_orb_of_corrosion#attribs]

## Components

| Component | Gold cost |
|---|---:|
| Band of Elvenskin | 450 gold |
| Orb of Frost | 300 gold |
| Orb of Blight | 300 gold |
| **Orb of Corrosion** | **1050 gold** |

[gamefile:items/item_orb_of_corrosion#components] [gamefile:items/item_orb_of_corrosion#cost]

## Mechanics

Corrosion is applied by attacks, reducing the target’s armor and movement speed, with a different slow against melee targets, while also reducing Health Restoration for a duration. [loc:DOTA_Tooltip_Ability_item_orb_of_corrosion_Description]

Its behavior is passive, and the effect is dispellable. [gamefile:items/item_orb_of_corrosion#mechanics]

*Seepage from the wounds of a warrior deity, sealed in an arcanist’s orb following a campaign of vicious slaughter.* [loc:DOTA_Tooltip_Ability_item_orb_of_corrosion_Lore]