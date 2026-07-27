---
title: Vladmir's Offering
kind: item
patch: 7.41d
card:
  entity: vladmir
  sentences:
  - text: Vladmir's Offering is a rare 2200-gold item that provides 1 Armor and 0.75
      Mana Regeneration; its 1200-radius Vladmir's Aura grants nearby allies 20% Lifesteal,
      18% Bonus Damage, 1 Mana Regeneration, and 2.0 Armor.
    marks:
    - gamefile:items/item_vladmir#cost
    - gamefile:items/item_vladmir#attribs
    - loc:DOTA_Tooltip_ability_item_vladmir_Description
  - text: It is passive and has a cast range of 1200.
    marks:
    - gamefile:items/item_vladmir#mechanics
  - text: Its Damage Self value is 0.
    marks:
    - gamefile:items/item_vladmir#attribs
  - text: Its Lifesteal Self value is 0.
    marks:
    - gamefile:items/item_vladmir#attribs
  - text: Its Lifesteal Creeps Tooltip value is 12.
    marks:
    - gamefile:items/item_vladmir#attribs
  - text: Its build formula is Buckler (425 gold), Ring of Basilius (425 gold), Morbid
      Mask (900 gold), and Blades of Attack (450 gold); it builds into Wraith Pact.
    marks:
    - gamefile:items/item_vladmir#cost
    - gamefile:items/item_vladmir#components
  - text: An eerie mask that is haunted with the malice of a fallen vampire.
    marks:
    - loc:DOTA_Tooltip_ability_item_vladmir_Lore
---

# Vladmir's Offering

Vladmir's Offering is a rare item that provides Armor and Mana Regeneration, while Vladmir's Aura grants nearby allies Lifesteal, Bonus Damage, Mana Regeneration, and Armor. [gamefile:items/item_vladmir#cost] [gamefile:items/item_vladmir#attribs] [loc:DOTA_Tooltip_ability_item_vladmir_Description]

## Stats

| Stat | Value |
|---|---:|
| ARMOR | 1 |
| ARMOR AURA | 2.0 |
| AURA RADIUS | 1200 |
| DAMAGE AURA | 18% |
| DAMAGE SELF | 0 |
| LIFESTEAL AURA | 20% |
| LIFESTEAL CREEPS TOOLTIP | 12 |
| LIFESTEAL SELF | 0 |
| MANA REGENERATION | 0.75 |
| MANA REGEN AURA | 1 |

[gamefile:items/item_vladmir#attribs] [loc:DOTA_Tooltip_ability_item_vladmir_Description]

## Mechanics

| Property | Value |
|---|---:|
| Behavior | Passive |
| Cast range | 1200 |

[gamefile:items/item_vladmir#mechanics]

The passive is named Vladmir's Aura and applies its listed effects to nearby allies. [loc:DOTA_Tooltip_ability_item_vladmir_Description]

## Components

| Formula entry | Gold cost |
|---|---:|
| Vladmir's Offering | 2200 gold |
| Buckler | 425 gold |
| Ring of Basilius | 425 gold |
| Morbid Mask | 900 gold |
| Blades of Attack | 450 gold |
| Builds into: Wraith Pact | 3800 gold |

[gamefile:items/item_vladmir#cost] [gamefile:items/item_vladmir#components]

*An eerie mask that is haunted with the malice of a fallen vampire.* [loc:DOTA_Tooltip_ability_item_vladmir_Lore]