---
title: Vanguard
kind: item
patch: 7.41d
card:
  entity: vanguard
  sentences:
  - text: Vanguard is an epic item costing 1700 gold that grants 250 Health, 4.5 Health
      Regeneration, and a 60% chance to block 50 damage for melee heroes or 25 for
      ranged heroes.
    marks:
    - gamefile:items/item_vanguard#cost
    - gamefile:items/item_vanguard#attribs
    - loc:DOTA_Tooltip_ability_item_vanguard_Description
  - text: Vanguard is built from Vitality Booster for 1000 gold and Ring of Health
      for 700 gold, and builds into Crimson Guard.
    marks:
    - gamefile:items/item_vanguard#components
  - text: Vanguard has passive behavior.
    marks:
    - gamefile:items/item_vanguard#mechanics
  - text: Its passive is Damage Block, which can block damage from incoming attacks
      with different amounts for melee and ranged heroes.
    marks:
    - loc:DOTA_Tooltip_ability_item_vanguard_Description
---

# Vanguard

Vanguard is an epic item that provides **Health**, **Health Regeneration**, **Block Chance**, **Block Damage Melee**, and **Block Damage Ranged**. [gamefile:items/item_vanguard#cost] [gamefile:items/item_vanguard#attribs]

## Stats

| Stat | Value |
|---|---:|
| Cost | 1700 gold |

[gamefile:items/item_vanguard#cost]

| Stat | Value |
|---|---:|
| Block Chance | 60% |
| Block Damage Melee | 50 |
| Block Damage Ranged | 25 |
| Health | 250 |
| Health Regeneration | 4.5 |

[gamefile:items/item_vanguard#attribs]

## Components

| Formula | Item | Gold cost |
|---|---|---:|
| Component | Vitality Booster | 1000 gold |
| Component | Ring of Health | 700 gold |
| Builds into | Crimson Guard | 3725 gold |

[gamefile:items/item_vanguard#components]

## Mechanics

Vanguard has passive behavior. [gamefile:items/item_vanguard#mechanics]

Its passive is **Damage Block**, which grants a chance to block damage from incoming attacks, with different block amounts for melee and ranged heroes. [loc:DOTA_Tooltip_ability_item_vanguard_Description]

*A powerful shield that defends its wielder from even the most vicious of attacks.* [loc:DOTA_Tooltip_ability_item_vanguard_Lore]