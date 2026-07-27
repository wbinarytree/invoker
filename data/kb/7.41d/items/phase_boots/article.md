---
title: Phase Boots
kind: item
patch: 7.41d
card:
  entity: phase_boots
  sentences:
  - text: Phase Boots is a common item costing 1450 gold that grants 4 Armor, 0 Bonus
      Attack Speed, 18 Bonus Damage Melee, 12 Bonus Damage Range, and 50 Movement
      Speed; its Phase active has an 8.0 cooldown and, for its 3.0 Phase Duration,
      grants 20% Phase Movement Speed or 10% Phase Movement Speed Range, permits movement
      through units, and makes turning quicker.
    marks:
    - gamefile:items/item_phase_boots#cost
    - gamefile:items/item_phase_boots#attribs
    - gamefile:items/item_phase_boots#mechanics
    - loc:DOTA_Tooltip_ability_item_phase_boots_Description
  - text: Its build formula is Boots of Speed for 500 gold, Chainmail for 500 gold,
      and Blades of Attack for 450 gold.
    marks:
    - gamefile:items/item_phase_boots#components
  - text: Phase has Immediate, No Target, and DOTA_ABILITY_BEHAVIOR_IGNORE_CHANNEL
      behavior.
    marks:
    - gamefile:items/item_phase_boots#mechanics
  - text: Phase grants the larger movement-speed increase to melee heroes and the
      smaller increase to ranged heroes.
    marks:
    - loc:DOTA_Tooltip_ability_item_phase_boots_Description
  - text: Movement-speed bonuses from multiple pairs of boots do not stack.
    marks:
    - loc:DOTA_Tooltip_ability_item_phase_boots_Description
---

# Phase Boots

Phase Boots is a common item with Armor, Bonus Attack Speed, Bonus Damage Melee, Bonus Damage Range, and Movement Speed, and the active Phase, which provides Phase Movement Speed or Phase Movement Speed Range and allows movement through units and quicker turning for the Phase Duration. [gamefile:items/item_phase_boots#cost] [gamefile:items/item_phase_boots#attribs] [loc:DOTA_Tooltip_ability_item_phase_boots_Description]

## Cost

| Stat | Value |
|---|---:|
| Cost | 1450 gold |

[gamefile:items/item_phase_boots#cost]

## Components

| Component | Gold cost |
|---|---:|
| Boots of Speed | 500 gold |
| Chainmail | 500 gold |
| Blades of Attack | 450 gold |

[gamefile:items/item_phase_boots#components]

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
| Behavior | Immediate, No Target, DOTA_ABILITY_BEHAVIOR_IGNORE_CHANNEL |
| Cooldown | 8.0 |

[gamefile:items/item_phase_boots#mechanics]

Phase grants a larger movement-speed increase to melee heroes than to ranged heroes, permits movement through units, and makes turning quicker for its duration. Movement-speed bonuses from multiple pairs of boots do not stack. [loc:DOTA_Tooltip_ability_item_phase_boots_Description]

*Boots that allow the wearer to travel between the ether.* [loc:DOTA_Tooltip_ability_item_phase_boots_Lore]