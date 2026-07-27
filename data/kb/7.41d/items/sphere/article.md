---
title: Linken's Sphere
kind: item
patch: 7.41d
card:
  entity: sphere
  sentences:
  - text: Linken's Sphere is an epic item costing 4800 gold that grants 16 All Attributes,
      6.5 Health Regeneration, 4.25 Mana Regeneration, and 300 Damage Absorb, with
      passive Spellblock once every 14.0 seconds and active Transfer Spellblock for
      14.0 seconds.
    marks:
    - gamefile:items/item_sphere#cost
    - gamefile:items/item_sphere#attribs
    - loc:DOTA_Tooltip_ability_item_sphere_Description
  - text: Its Upgrade Absorb Duration is 10.0.
    marks:
    - gamefile:items/item_sphere#attribs
  - text: It is built from Perseverance for 1400 gold, Ultimate Orb for 2800 gold,
      and a Recipe for 600 gold.
    marks:
    - gamefile:items/item_sphere#components
  - text: Transfer Spellblock is unit-targeted with 700 cast range.
    marks:
    - gamefile:items/item_sphere#mechanics
  - text: Its active cooldown is 14.0.
    marks:
    - gamefile:items/item_sphere#mechanics
  - text: Spellblock blocks most targeted spells.
    marks:
    - loc:DOTA_Tooltip_ability_item_sphere_Description
  - text: Transfer Spellblock temporarily removes Spellblock from the owner and transfers
      it to an allied unit.
    marks:
    - loc:DOTA_Tooltip_ability_item_sphere_Description
---

Linken's Sphere is an epic item that provides All Attributes, Health Regeneration, Mana Regeneration, Damage Absorb, passive Spellblock, and active Transfer Spellblock. [gamefile:items/item_sphere#cost] [gamefile:items/item_sphere#attribs] [loc:DOTA_Tooltip_ability_item_sphere_Description]

## Stats

| Stat | Value |
|---|---:|
| Cost | 4800 gold |
[gamefile:items/item_sphere#cost]

| Stat | Value |
|---|---:|
| Block Cooldown | 14.0 |
| All Attributes | 16 |
| Health Regeneration | 6.5 |
| Mana Regeneration | 4.25 |
| Damage Absorb | 300 |
| Upgrade Absorb Duration | 10.0 |
[gamefile:items/item_sphere#attribs]

## Components

| Component | Gold cost |
|---|---:|
| Perseverance | 1400 gold |
| Ultimate Orb | 2800 gold |
| Recipe | 600 gold |
[gamefile:items/item_sphere#components]

## Mechanics

| Property | Value |
|---|---:|
| Behavior | Unit Target |
| Cast range | 700 |
| Cooldown | 14.0 |
[gamefile:items/item_sphere#mechanics]

Spellblock blocks most targeted spells. Transfer Spellblock temporarily removes Spellblock from the item's owner and transfers it to an allied unit. [loc:DOTA_Tooltip_ability_item_sphere_Description]

| Effect | Duration or interval |
|---|---:|
| Spellblock | Once every 14.0 seconds |
| Transfer Spellblock | 14.0 seconds |
[loc:DOTA_Tooltip_ability_item_sphere_Description]

*This magical sphere once protected one of the most famous heroes in history.* [loc:DOTA_Tooltip_ability_item_sphere_Lore]