---
title: Phylactery
kind: item
patch: 7.41d
card:
  entity: phylactery
  sentences:
  - text: Phylactery is a common item costing 2600 gold that grants 6 All Attributes,
      5.5 Health Regeneration, 2.25 Mana Regeneration, and 150 Bonus Spell Damage;
      its passive Empower Spell has a 9.0-second cooldown and causes the next Unit
      Target spell cast on an enemy to deal separate bonus damage and apply a 30%
      slow for 3 seconds.
    marks:
    - gamefile:items/item_phylactery#cost
    - gamefile:items/item_phylactery#attribs
    - gamefile:items/item_phylactery#mechanics
    - loc:DOTA_Tooltip_Ability_item_phylactery_Description
  - text: Bonus per Kill is 0.
    marks:
    - gamefile:items/item_phylactery#attribs
  - text: Kill Bonus Window is 0.
    marks:
    - gamefile:items/item_phylactery#attribs
  - text: Max Kill Bonus is 0.
    marks:
    - gamefile:items/item_phylactery#attribs
  - text: The build formula is Perseverance for 1400 gold, Diadem for 1000 gold, and
      a Recipe for 200 gold.
    marks:
    - gamefile:items/item_phylactery#components
  - text: Phylactery builds into Khanda.
    marks:
    - gamefile:items/item_phylactery#components
  - text: “An amulet overflowing with powerful magics.”
    marks:
    - loc:DOTA_Tooltip_Ability_item_phylactery_Lore
---

# Phylactery

Phylactery is a common item with All Attributes, Health Regeneration, Mana Regeneration, Bonus per Kill, Bonus Spell Damage, Kill Bonus Window, Max Kill Bonus, Slow, and Slow Duration. [gamefile:items/item_phylactery#cost] [gamefile:items/item_phylactery#attribs]

## Cost

| Stat | Value |
|---|---:|
| Cost | 2600 gold |

[gamefile:items/item_phylactery#cost]

## Attributes

| Stat | Value |
|---|---:|
| ALL ATTRIBUTES | 6 |
| HEALTH REGENERATION | 5.5 |
| MANA REGENERATION | 2.25 |
| BONUS PER KILL | 0 |
| BONUS SPELL DAMAGE | 150 |
| KILL BONUS WINDOW | 0 |
| MAX KILL BONUS | 0 |
| SLOW | 30% |
| SLOW DURATION | 3 |

[gamefile:items/item_phylactery#attribs]

## Components

| Type | Item | Gold cost |
|---|---|---:|
| Component | Perseverance | 1400 gold |
| Component | Diadem | 1000 gold |
| Recipe | Recipe | 200 gold |
| Builds into | Khanda | 5600 gold |

[gamefile:items/item_phylactery#components]

## Empower Spell

| Stat | Value |
|---|---:|
| Behavior | Passive |
| Cooldown | 9.0 |

[gamefile:items/item_phylactery#mechanics]

Empower Spell causes the next Unit Target spell cast on an enemy to deal separate bonus damage to the target and apply a slow. [loc:DOTA_Tooltip_Ability_item_phylactery_Description]

*An amulet overflowing with powerful magics.* [loc:DOTA_Tooltip_Ability_item_phylactery_Lore]