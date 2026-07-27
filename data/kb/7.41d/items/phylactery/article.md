---
title: Phylactery
kind: item
patch: 7.41d
card:
  entity: phylactery
  sentences:
  - text: Phylactery is a common item costing 2600 gold that grants 6 all attributes,
      5.5 health regeneration, and 2.25 mana regeneration; its passive Empower Spell
      has 9.0 cooldown and makes the next Unit Target spell cast on an enemy deal
      150 separate bonus spell damage and apply 30% slow for a duration of 3.
    marks:
    - gamefile:items/item_phylactery#cost
    - gamefile:items/item_phylactery#attribs
    - gamefile:items/item_phylactery#mechanics
    - loc:DOTA_Tooltip_Ability_item_phylactery_Description
  - text: Its bonus per kill is 0.
    marks:
    - gamefile:items/item_phylactery#attribs
  - text: Its kill bonus window is 0.
    marks:
    - gamefile:items/item_phylactery#attribs
  - text: Its max kill bonus is 0.
    marks:
    - gamefile:items/item_phylactery#attribs
  - text: It is built from Perseverance for 1400 gold, Diadem for 1000 gold, and a
      recipe for 200 gold, and builds into Khanda.
    marks:
    - gamefile:items/item_phylactery#components
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