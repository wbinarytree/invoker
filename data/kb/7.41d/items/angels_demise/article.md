---
title: Khanda
kind: item
patch: 7.41d
card:
  entity: angels_demise
  sentences:
  - text: Khanda is a 5600-gold common item whose Empower Spell passive has a Cooldown
      of 9 and makes the next Unit Target spell cast on an enemy deal 250 separate
      additional damage, disable passives, and apply 30% Movement Speed Slow for a
      Slow Duration of 4.
    marks:
    - gamefile:items/item_angels_demise#cost
    - gamefile:items/item_angels_demise#attribs
    - gamefile:items/item_angels_demise#mechanics
    - loc:DOTA_Tooltip_Ability_item_angels_demise_Description
  - text: It grants 8 All Attributes, 450 Health, 7 Health Regeneration, 450 Mana,
      3 Mana Regeneration, 250 Bonus Spell Damage, 30% Slow, and 4 Slow Duration.
    marks:
    - gamefile:items/item_angels_demise#attribs
  - text: Empower Spell is dispellable.
    marks:
    - gamefile:items/item_angels_demise#mechanics
  - text: Its build formula is Phylactery (2600 gold) + Soul Booster (3000 gold) =
      Khanda (5600 gold).
    marks:
    - gamefile:items/item_angels_demise#components
    - gamefile:items/item_angels_demise#cost
  - text: “A blade sharp enough to slice through magic itself.”
    marks:
    - loc:DOTA_Tooltip_Ability_item_angels_demise_Lore
---

# Khanda

Khanda is a common item that grants All Attributes, Health, Health Regeneration, Mana, Mana Regeneration, Bonus Spell Damage, Slow, and Slow Duration, while its Empower Spell passive deals separate additional damage, disables passives, and slows Movement Speed with the next Unit Target spell cast on an enemy. [gamefile:items/item_angels_demise#cost] [gamefile:items/item_angels_demise#attribs] [loc:DOTA_Tooltip_Ability_item_angels_demise_Description]

## Stats

| Stat | Value |
|---|---:|
| All Attributes | 8 |
| Health | 450 |
| Health Regeneration | 7 |
| Mana | 450 |
| Mana Regeneration | 3 |
| Bonus Spell Damage | 250 |
| Slow | 30% |
| Slow Duration | 4 |

[gamefile:items/item_angels_demise#attribs]

## Components

| Part | Gold cost |
|---|---:|
| Phylactery | 2600 gold |
| Soul Booster | 3000 gold |
| Khanda | 5600 gold |

[gamefile:items/item_angels_demise#components] [gamefile:items/item_angels_demise#cost]

## Empower Spell

| Property | Value |
|---|---:|
| Behavior | Passive |
| Dispellable | Yes |
| Cooldown | 9 |

[gamefile:items/item_angels_demise#mechanics]

Empower Spell applies to the next Unit Target spell cast on an enemy, dealing its additional damage separately, disabling the target’s passives, and slowing their Movement Speed. [loc:DOTA_Tooltip_Ability_item_angels_demise_Description]

*A blade sharp enough to slice through magic itself.* [loc:DOTA_Tooltip_Ability_item_angels_demise_Lore]