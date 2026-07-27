---
title: Specialist's Array
kind: item
patch: 7.41d
card:
  entity: specialists_array
  sentences:
  - text: Specialist's Array is a rare 2550-gold item granting 15 Agility and passive
      Splitshot, which gives ranged attacks a 30% chance to fire 2 additional projectiles
      within 150 bonus range and a 120-degree forward angle; each deals 20 base damage
      plus 75% normal attack damage, while the primary attack uses 100%.
    marks:
    - gamefile:items/item_specialists_array#cost
    - gamefile:items/item_specialists_array#attribs
    - loc:DOTA_Tooltip_Ability_item_specialists_array_Description
  - text: Splitshot is passive, costs 0 mana, and has a 0.0 cooldown.
    marks:
    - gamefile:items/item_specialists_array#mechanics
  - text: Additional projectiles do not trigger on-hit effects.
    marks:
    - loc:DOTA_Tooltip_Ability_item_specialists_array_Description
  - text: Its build formula is Blade of Alacrity for 1000 gold, Broadsword for 1000
      gold, and a Recipe for 550 gold; it builds into Hydra's Breath.
    marks:
    - gamefile:items/item_specialists_array#components
  - text: An impressive kit of trigger enhancements born in an aging assassin's idle
      mind.
    marks:
    - loc:DOTA_Tooltip_Ability_item_specialists_array_Lore
---

# Specialist's Array

Specialist's Array is a rare item that grants Agility and provides the passive Splitshot. [gamefile:items/item_specialists_array#cost] [gamefile:items/item_specialists_array#attribs] [loc:DOTA_Tooltip_Ability_item_specialists_array_Description]

## Stats

| Stat | Value |
|---|---:|
| Cost | 2550 gold |
[gamefile:items/item_specialists_array#cost]

| Attribute | Value |
|---|---:|
| AGILITY | 15 |
| ALL ATTRIBUTES | 0 |
| BASE PROC DMG | 20 |
| COUNT | 2 |
| DAMAGE | 20 |
| PROC CHANCE | 30% |
| PROC DMG PCT | 75% |
| PROC DMG PCT PRIMARY TOOLTIP | 100% |
| SECONDARY TARGET ANGLE | 120 |
| SECONDARY TARGET RANGE BONUS | 150 |
[gamefile:items/item_specialists_array#attribs]

| Mechanic | Value |
|---|---:|
| Behavior | Passive |
| Mana cost | 0 |
| Cooldown | 0.0 |
[gamefile:items/item_specialists_array#mechanics]

## Splitshot

Ranged attacks can fire additional projectiles at nearby enemies within an extended range and an angle in front of the attacker. Additional projectiles deal a base amount plus a percentage of normal attack damage and do not trigger on-hit effects; the primary attack uses its own damage percentage. [loc:DOTA_Tooltip_Ability_item_specialists_array_Description]

## Components

| Formula | Item | Gold cost |
|---|---|---:|
| Component | Blade of Alacrity | 1000 gold |
| Component | Broadsword | 1000 gold |
| Recipe | Recipe | 550 gold |
| Builds into | Hydra's Breath | 5900 gold |
[gamefile:items/item_specialists_array#components]

*An impressive kit of trigger enhancements born in an aging assassin's idle mind.* [loc:DOTA_Tooltip_Ability_item_specialists_array_Lore]