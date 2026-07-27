---
title: Dandelion Amulet
kind: item
patch: 7.41d
card:
  entity: dandelion_amulet
  sentences:
  - text: Dandelion Amulet is a 0-gold item whose passive Magical Damage Block, on
      a 12-second cooldown, blocks up to 300 magic damage from each damage instance
      exceeding 75 damage.
    marks:
    - gamefile:items/item_dandelion_amulet#cost
    - gamefile:items/item_dandelion_amulet#attribs
    - gamefile:items/item_dandelion_amulet#mechanics
    - loc:DOTA_Tooltip_ability_item_dandelion_amulet_Description
  - text: Its build formula is Dandelion Amulet (0 gold).
    marks:
    - gamefile:items/item_dandelion_amulet#cost
  - text: It provides 0 mana.
    marks:
    - gamefile:items/item_dandelion_amulet#attribs
  - text: It provides 0 move speed.
    marks:
    - gamefile:items/item_dandelion_amulet#attribs
---

# Dandelion Amulet

Dandelion Amulet is an item with the passive Magical Damage Block, governed by MAGIC BLOCK, MIN DAMAGE, and COOLDOWN. [gamefile:items/item_dandelion_amulet#attribs] [gamefile:items/item_dandelion_amulet#mechanics] [loc:DOTA_Tooltip_ability_item_dandelion_amulet_Description]

## Components

| Entry | Gold cost |
|---|---:|
| Dandelion Amulet | 0 |
[gamefile:items/item_dandelion_amulet#cost]

## Stats

| Stat | Value |
|---|---:|
| MAGIC BLOCK | 300 |
| MANA | 0 |
| MIN DAMAGE | 75 |
| MOVE SPEED | 0 |
[gamefile:items/item_dandelion_amulet#attribs]

| Mechanic | Value |
|---|---:|
| Behavior | Passive |
| Cooldown | 12 |
[gamefile:items/item_dandelion_amulet#mechanics]

## Magical Damage Block

On each cooldown, the passive blocks magic damage from damage instances exceeding MIN DAMAGE, up to MAGIC BLOCK. [loc:DOTA_Tooltip_ability_item_dandelion_amulet_Description]