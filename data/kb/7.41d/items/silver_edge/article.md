---
title: Silver Edge
kind: item
patch: 7.41d
card:
  entity: silver_edge
  sentences:
  - text: Silver Edge is a 5700-gold epic item that grants 35 attack speed and 70
      damage; its Shadow Walk active grants invisibility for up to 17.0 seconds and
      22% movement speed, and an attack ending it deals 300 bonus physical damage,
      disables the target’s passive abilities, and caps its movement speed at 200
      for 5 seconds.
    marks:
    - gamefile:items/item_silver_edge#cost
    - gamefile:items/item_silver_edge#attribs
    - loc:DOTA_Tooltip_ability_item_silver_edge_Description
  - text: It is built from Shadow Blade for 3250 gold, Demon Edge for 2200 gold, and
      a Recipe for 250 gold.
    marks:
    - gamefile:items/item_silver_edge#components
    - gamefile:items/item_silver_edge#cost
  - text: Shadow Walk costs 75 mana and has a 22.0-second cooldown.
    marks:
    - gamefile:items/item_silver_edge#mechanics
  - text: Shadow Walk has a 0.3-second fade time.
    marks:
    - gamefile:items/item_silver_edge#attribs
  - text: Its behavior is Immediate, No Target, and DOTA_ABILITY_BEHAVIOR_IGNORE_CHANNEL.
    marks:
    - gamefile:items/item_silver_edge#mechanics
  - text: The invisibility ends when the wielder attacks or casts a spell.
    marks:
    - loc:DOTA_Tooltip_ability_item_silver_edge_Description
  - text: While invisible, the wielder can move through units.
    marks:
    - loc:DOTA_Tooltip_ability_item_silver_edge_Description
---

# Silver Edge

Silver Edge is an epic item that grants Attack Speed and Damage and provides the Shadow Walk active. [gamefile:items/item_silver_edge#cost] [gamefile:items/item_silver_edge#attribs] [loc:DOTA_Tooltip_ability_item_silver_edge_Description]

## Components

| Component | Cost |
|---|---:|
| Shadow Blade | 3250 gold |
| Demon Edge | 2200 gold |
| Recipe | 250 gold |
| **Silver Edge total** | **5700 gold** |

[gamefile:items/item_silver_edge#components] [gamefile:items/item_silver_edge#cost]

## Stats

| Stat | Value |
|---|---:|
| BACKSTAB DURATION | 5 |
| ATTACK SPEED | 35 |
| DAMAGE | 70 |
| BONUS INTELLECT | 0 |
| BONUS MANA REGEN | 0 |
| BONUS STRENGTH | 0 |
| MAX MOVEMENT SPEED | 200 |
| VISIBILITY RADIUS | 1025 |
| WINDWALK BONUS DAMAGE | 300 |
| WINDWALK DURATION | 17.0 |
| WINDWALK FADE TIME | 0.3 |
| WINDWALK MOVEMENT SPEED | 22% |

[gamefile:items/item_silver_edge#attribs]

## Shadow Walk

| Property | Value |
|---|---|
| Behavior | Immediate, No Target, DOTA_ABILITY_BEHAVIOR_IGNORE_CHANNEL |
| Mana cost | 75 |
| Cooldown | 22.0 |

[gamefile:items/item_silver_edge#mechanics]

Shadow Walk makes the wielder invisible until attacking or casting a spell. While invisible, the wielder moves faster and can move through units. An attack that ends the invisibility deals bonus physical damage, disables the target’s passive abilities, and caps its movement speed. [loc:DOTA_Tooltip_ability_item_silver_edge_Description]

*Once used to slay an unjust king, only to have the kingdom erupt into civil war in the aftermath.* [loc:DOTA_Tooltip_ability_item_silver_edge_Lore]