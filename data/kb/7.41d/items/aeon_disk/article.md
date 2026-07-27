---
title: Aeon Disk
kind: item
patch: 7.41d
card:
  entity: aeon_disk
  sentences:
  - text: Aeon Disk is an epic 3000-gold item that grants 250 Health and 300 Mana;
      its passive Combo Breaker triggers below 70% health and applies a strong dispel
      plus a 2.5-second buff that prevents all damage dealt and received and provides
      75% Status Resistance.
    marks:
    - gamefile:items/item_aeon_disk#cost
    - gamefile:items/item_aeon_disk#attribs
    - gamefile:items/item_aeon_disk#mechanics
    - loc:DOTA_Tooltip_ability_item_aeon_disk_Description
  - text: 'Build formula: Vitality Booster (1000 gold) + Energy Booster (800 gold)
      + Recipe (1200 gold) = Aeon Disk (3000 gold).'
    marks:
    - gamefile:items/item_aeon_disk#components
    - gamefile:items/item_aeon_disk#cost
  - text: Its COOLDOWN DURATION is 105.0/125.0/145.0/165.0.
    marks:
    - gamefile:items/item_aeon_disk#attribs
  - text: Its INITIAL COOLDOWN is 6.
    marks:
    - gamefile:items/item_aeon_disk#attribs
  - text: Its MAX LEVEL is 4.
    marks:
    - gamefile:items/item_aeon_disk#attribs
  - text: Only player-based damage can trigger Combo Breaker.
    marks:
    - loc:DOTA_Tooltip_ability_item_aeon_disk_Description
  - text: The cooldown increases every time Combo Breaker triggers.
    marks:
    - loc:DOTA_Tooltip_ability_item_aeon_disk_Description
---

# Aeon Disk

Aeon Disk is an epic item that provides Health and Mana and has the passive Combo Breaker, whose buff provides Status Resistance. [gamefile:items/item_aeon_disk#cost] [gamefile:items/item_aeon_disk#attribs] [gamefile:items/item_aeon_disk#mechanics] [loc:DOTA_Tooltip_ability_item_aeon_disk_Description]

## Components

| Build formula | Gold cost |
|---|---:|
| Vitality Booster | 1000 gold |
| Energy Booster | 800 gold |
| Recipe | 1200 gold |
| **Aeon Disk** | **3000 gold** |

[gamefile:items/item_aeon_disk#components] [gamefile:items/item_aeon_disk#cost]

## Stats

| Stat | Value |
|---|---:|
| HEALTH | 250 |
| MANA | 300 |
| BUFF DURATION | 2.5 seconds |
| COOLDOWN DURATION | 105.0/125.0/145.0/165.0 |
| HEALTH THRESHOLD PCT | 70% |
| INITIAL COOLDOWN | 6 |
| MAX LEVEL | 4 |
| STATUS RESISTANCE | 75% |

[gamefile:items/item_aeon_disk#attribs] [loc:DOTA_Tooltip_ability_item_aeon_disk_Description]

## Combo Breaker

Only player-based damage can trigger Combo Breaker when that damage causes the holder’s health to fall below its threshold. The trigger applies a strong dispel and grants the holder a buff. While active, the buff prevents all damage dealt and received. The cooldown increases every time Combo Breaker triggers. [loc:DOTA_Tooltip_ability_item_aeon_disk_Description]