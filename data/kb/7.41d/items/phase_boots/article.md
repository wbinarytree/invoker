---
title: Phase Boots
kind: item
patch: 7.41d
card:
  entity: phase_boots
  sentences:
  - text: Phase Boots is a common item costing 1450 gold that provides 4 Armor, 18
      Bonus Damage Melee, 12 Bonus Damage Range, and 50 Movement Speed; Phase lasts
      3.0 seconds, provides 20% Phase Movement Speed and 10% Phase Movement Speed
      Range, enables movement through units, and increases turning speed.
    marks:
    - gamefile:items/item_phase_boots#cost
    - gamefile:items/item_phase_boots#attribs
    - loc:DOTA_Tooltip_ability_item_phase_boots_Description
  - text: It is built from Boots of Speed (500 gold), Chainmail (500 gold), and Blades
      of Attack (450 gold).
    marks:
    - gamefile:items/item_phase_boots#components
  - text: It provides 0 Bonus Attack Speed.
    marks:
    - gamefile:items/item_phase_boots#attribs
  - text: Phase is Immediate, No Target, and usable while channelling.
    marks:
    - gamefile:items/item_phase_boots#mechanics
  - text: Phase has an 8.0-second cooldown.
    marks:
    - gamefile:items/item_phase_boots#mechanics
  - text: Movement speed bonuses from multiple pairs of boots do not stack.
    marks:
    - loc:DOTA_Tooltip_ability_item_phase_boots_Description
  - text: Boots that allow the wearer to travel between the ether.
    marks:
    - loc:DOTA_Tooltip_ability_item_phase_boots_Lore
---

# Phase Boots

Phase Boots is a common item that provides Armor, Bonus Damage Melee, Bonus Damage Range, and Movement Speed, plus the active Phase, which provides Phase Movement Speed, unit phasing, and faster turning. [gamefile:items/item_phase_boots#cost] [gamefile:items/item_phase_boots#attribs] [loc:DOTA_Tooltip_ability_item_phase_boots_Description]

## Components

| Component | Gold cost |
|---|---:|
| Boots of Speed | 500 gold |
| Chainmail | 500 gold |
| Blades of Attack | 450 gold |
| **Phase Boots** | **1450 gold** |

[gamefile:items/item_phase_boots#components] [gamefile:items/item_phase_boots#cost]

## Stats

| Stat | Value |
|---|---:|
| Armor | 4 |
| Bonus Attack Speed | 0 |
| Bonus Damage Melee | 18 |
| Bonus Damage Range | 12 |
| Movement Speed | 50 |
| Phase Duration | 3.0 |
| Phase Movement Speed | 20% |
| Phase Movement Speed Range | 10% |

[gamefile:items/item_phase_boots#attribs]

## Phase

| Property | Value |
|---|---|
| Behavior | Immediate, No Target, Usable While Channelling |
| Cooldown | 8.0 |

[gamefile:items/item_phase_boots#mechanics]

Phase lets the user move through units and turn more quickly. Movement speed bonuses from multiple pairs of boots do not stack. [loc:DOTA_Tooltip_ability_item_phase_boots_Description]

*Boots that allow the wearer to travel between the ether.* [loc:DOTA_Tooltip_ability_item_phase_boots_Lore]