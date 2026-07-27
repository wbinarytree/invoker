---
title: Arcanist's Armor
kind: item
patch: 7.41d
card:
  entity: force_field
  sentences:
  - text: Arcanist's Armor is a 0-gold item whose Shield passive grants all other
      allies within a 1200 radius 4 Armor and 8% Magic Resistance, and whose Mega
      Shield active grants 25% Damage Reflection for 5 seconds.
    marks:
    - gamefile:items/item_force_field#cost
    - gamefile:items/item_force_field#attribs
    - gamefile:items/item_force_field#mechanics
    - loc:DOTA_Tooltip_Ability_item_force_field_Description
  - text: It grants itself 0 Armor and 0 Magic Resistance.
    marks:
    - gamefile:items/item_force_field#attribs
  - text: Mega Shield has Immediate, No Target behavior.
    marks:
    - gamefile:items/item_force_field#mechanics
  - text: Mega Shield has a 35 cooldown.
    marks:
    - gamefile:items/item_force_field#mechanics
  - text: “An exquisite piece commissioned by a paranoid monarch who choked on a piece
      of fruit long before the item saw its intended use.”
    marks:
    - loc:DOTA_Tooltip_Ability_item_force_field_Lore
---

# Arcanist's Armor

Arcanist's Armor is an item that grants Armor and Magic Resistance to other allies and can grant Damage Reflection. [gamefile:items/item_force_field#cost] [loc:DOTA_Tooltip_Ability_item_force_field_Description]

## Stats

| Stat | Value |
|---|---:|
| ACTIVE REFLECTION PCT | 25% |
| BONUS AOE ARMOR | 4 |
| BONUS AOE MRES | 8% |
| BONUS AOE RADIUS | 1200 |
| SELF ARMOR | 0 |
| SELF MRES | 0 |

[gamefile:items/item_force_field#attribs]

## Abilities

**Mega Shield (active):** Force Field Aura grants Damage Reflection for the active’s duration. **Shield (passive):** grants Armor and Magic Resistance to all other allies within its radius. [loc:DOTA_Tooltip_Ability_item_force_field_Description]

| Property | Value |
|---|---|
| Behavior | Immediate, No Target |
| Cooldown | 35 |
| Damage Reflection duration | 5 seconds |

[gamefile:items/item_force_field#mechanics] [loc:DOTA_Tooltip_Ability_item_force_field_Description]

## Cost

| Item | Gold cost |
|---|---:|
| Arcanist's Armor | 0 gold |

[gamefile:items/item_force_field#cost]

*An exquisite piece commissioned by a paranoid monarch who choked on a piece of fruit long before the item saw its intended use.* [loc:DOTA_Tooltip_Ability_item_force_field_Lore]