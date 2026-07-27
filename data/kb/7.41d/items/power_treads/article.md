---
title: Power Treads
kind: item
patch: 7.41d
card:
  entity: power_treads
  sentences:
  - text: Power Treads is a common item costing 1400 gold that grants 25 Attack Speed,
      55 Bonus Movement Speed Melee, 45 Bonus Movement Speed Ranged, and 10 Selected
      Attribute, with the Switch Attribute active.
    marks:
    - gamefile:items/item_power_treads#cost
    - gamefile:items/item_power_treads#attribs
    - loc:DOTA_Tooltip_ability_item_power_treads_Description
  - text: It grants 0 Bonus Damage.
    marks:
    - gamefile:items/item_power_treads#attribs
  - text: Power Treads is built from Boots of Speed (500 gold), Gloves of Haste (450
      gold), and Belt of Strength (450 gold).
    marks:
    - gamefile:items/item_power_treads#cost
    - gamefile:items/item_power_treads#components
  - text: Switch Attribute is an immediate, no-target active.
    marks:
    - gamefile:items/item_power_treads#mechanics
    - loc:DOTA_Tooltip_ability_item_power_treads_Description
  - text: Switch Attribute selects Strength, Agility, or Intelligence, granting +10
      to the selected attribute.
    marks:
    - loc:DOTA_Tooltip_ability_item_power_treads_Description
  - text: Movement speed bonuses from multiple pairs of boots do not stack.
    marks:
    - loc:DOTA_Tooltip_ability_item_power_treads_Description
---

# Power Treads

Power Treads is a common item with Attack Speed, Bonus Movement Speed Melee, Bonus Movement Speed Ranged, and Selected Attribute, plus the Switch Attribute active. [gamefile:items/item_power_treads#cost] [gamefile:items/item_power_treads#attribs] [loc:DOTA_Tooltip_ability_item_power_treads_Description]

## Stats

| Stat | Value |
|---|---:|
| Attack Speed | 25 |
| Bonus Damage | 0 |
| Bonus Movement Speed Melee | 55 |
| Bonus Movement Speed Ranged | 45 |
| Selected Attribute | 10 |

[gamefile:items/item_power_treads#attribs]

## Components

| Build formula | Gold cost |
|---|---:|
| Power Treads | 1400 gold |
| Boots of Speed | 500 gold |
| Gloves of Haste | 450 gold |
| Belt of Strength | 450 gold |

[gamefile:items/item_power_treads#cost] [gamefile:items/item_power_treads#components]

## Mechanics

| Active | Behavior |
|---|---|
| Switch Attribute | Immediate, No Target |

[gamefile:items/item_power_treads#mechanics] [loc:DOTA_Tooltip_ability_item_power_treads_Description]

| Selected attribute | Bonus |
|---|---:|
| Strength | +10 |
| Agility | +10 |
| Intelligence | +10 |

[loc:DOTA_Tooltip_ability_item_power_treads_Description]

Movement speed bonuses from multiple pairs of boots do not stack. [loc:DOTA_Tooltip_ability_item_power_treads_Description]

*A pair of tough-skinned boots that change to meet the demands of the wearer.* [loc:DOTA_Tooltip_ability_item_power_treads_Lore]