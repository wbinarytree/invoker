---
title: Boots of Bearing
kind: item
patch: 7.41d
card:
  entity: boots_of_bearing
  sentences:
  - text: Boots of Bearing is a rare item costing 4225 gold that grants 65 Movement
      Speed, 18 Health Regeneration, and 8 Strength, provides allies 15 Movement Speed
      and 2.5 Health Regeneration through Swiftness Aura, and activates Endurance
      to grant nearby allies Bonus Attack Speed Pct 50, Bonus Movement Speed Pct 15%,
      and slow immunity.
    marks:
    - gamefile:items/item_boots_of_bearing#cost
    - gamefile:items/item_boots_of_bearing#attribs
    - loc:DOTA_Tooltip_ability_item_boots_of_bearing_Description
  - text: The build formula is Tranquil Boots (900 gold), Drum of Endurance (1625
      gold), and Ring of Tarrasque (1700 gold).
    marks:
    - gamefile:items/item_boots_of_bearing#components
  - text: Endurance has Duration 6 and Radius 1200.
    marks:
    - gamefile:items/item_boots_of_bearing#attribs
  - text: Its Bonus MS Duration is 1.5.
    marks:
    - gamefile:items/item_boots_of_bearing#attribs
  - text: Endurance has a Cooldown of 30.0.
    marks:
    - gamefile:items/item_boots_of_bearing#mechanics
  - text: Its behavior is Immediate, No Target, and DOTA_ABILITY_BEHAVIOR_IGNORE_CHANNEL.
    marks:
    - gamefile:items/item_boots_of_bearing#mechanics
  - text: Affected allies are immune to slows at the start of Endurance.
    marks:
    - loc:DOTA_Tooltip_ability_item_boots_of_bearing_Description
  - text: Movement speed bonuses from multiple pairs of boots do not stack.
    marks:
    - loc:DOTA_Tooltip_ability_item_boots_of_bearing_Description
---

# Boots of Bearing

Boots of Bearing is a rare item that grants Movement Speed, Health Regeneration, and Strength, provides allied Movement Speed and Health Regeneration through Swiftness Aura, and activates Endurance to grant nearby allies Attack Speed, Movement Speed, and slow immunity. [gamefile:items/item_boots_of_bearing#cost] [gamefile:items/item_boots_of_bearing#attribs] [loc:DOTA_Tooltip_ability_item_boots_of_bearing_Description]

## Components

| Component | Gold cost |
|---|---:|
| Tranquil Boots | 900 gold |
| Drum of Endurance | 1625 gold |
| Ring of Tarrasque | 1700 gold |
| **Boots of Bearing** | **4225 gold** |

[gamefile:items/item_boots_of_bearing#components] [gamefile:items/item_boots_of_bearing#cost]

## Stats

| Stat | Value |
|---|---:|
| Aura Health Regen | 2.5 |
| Aura Movement Speed | 15 |
| Bonus Attack Speed Pct | 50 |
| Health Regeneration | 18 |
| Intelligence | 0 |
| Movement Speed | 65 |
| Bonus Movement Speed Pct | 15% |
| Bonus MS Duration | 1.5 |
| Strength | 8 |
| Duration | 6 |
| Radius | 1200 |

[gamefile:items/item_boots_of_bearing#attribs]

## Mechanics

| Property | Value |
|---|---|
| Behavior | Immediate, No Target, DOTA_ABILITY_BEHAVIOR_IGNORE_CHANNEL |
| Cooldown | 30.0 |

[gamefile:items/item_boots_of_bearing#mechanics]

Endurance affects nearby allies; at the start of its effect, affected allies are immune to slows. Swiftness Aura affects allies, and movement speed bonuses from multiple pairs of boots do not stack. [loc:DOTA_Tooltip_ability_item_boots_of_bearing_Description]

*Resplendent footwear fashioned for the ancient herald that first dared spread the glory of Stonehall beyond the original borders of its nascent claim.* [loc:DOTA_Tooltip_ability_item_boots_of_bearing_Lore]