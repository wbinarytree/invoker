---
title: Dust of Appearance
kind: item
patch: 7.41d
card:
  entity: dust
  sentences:
  - text: Dust of Appearance is a consumable item costing 80 gold whose Reveal creates
      a RADIUS 1050 area for DURATION 12, reveals invisible heroes, applies MOVESPEED
      -20%, deals 25 DAMAGE to revealed invisible units, and leaves the enemy debuff
      for LINGER DURATION 8 after they exit.
    marks:
    - gamefile:items/item_dust#cost
    - gamefile:items/item_dust#attribs
    - loc:DOTA_Tooltip_ability_item_dust_Description
  - text: Its behavior is Immediate, No Target.
    marks:
    - gamefile:items/item_dust#mechanics
  - text: It is dispellable.
    marks:
    - gamefile:items/item_dust#mechanics
  - text: Its cast range is 1050.
    marks:
    - gamefile:items/item_dust#mechanics
  - text: Its mana cost is 0.
    marks:
    - gamefile:items/item_dust#mechanics
  - text: Its cooldown is 30.0.
    marks:
    - gamefile:items/item_dust#mechanics
  - text: One may hide visage, but never volume.
    marks:
    - loc:DOTA_Tooltip_ability_item_dust_Lore
---

# Dust of Appearance

Dust of Appearance is a consumable item with DAMAGE, DURATION, LINGER DURATION, MOVESPEED, and RADIUS effects. [gamefile:items/item_dust#cost] [gamefile:items/item_dust#attribs]

## Cost

| Item | Gold cost |
|---|---:|
| Dust of Appearance | 80 |
[gamefile:items/item_dust#cost]

## Stats

| Stat | Value |
|---|---:|
| DAMAGE | 25 |
| DURATION | 12 |
| LINGER DURATION | 8 |
| MOVESPEED | -20% |
| RADIUS | 1050 |
[gamefile:items/item_dust#attribs]

## Mechanics

| Property | Value |
|---|---|
| Behavior | Immediate, No Target |
| Dispellable | Yes |
| Cast range | 1050 |
| Mana cost | 0 |
| Cooldown | 30.0 |
[gamefile:items/item_dust#mechanics]

**Use: Reveal.** It creates an area where the caster was standing that reveals and slows invisible heroes. Invisible units revealed by Dust take damage, and the enemy debuff lingers after they leave the area of effect. [loc:DOTA_Tooltip_ability_item_dust_Description]

*One may hide visage, but never volume.* [loc:DOTA_Tooltip_ability_item_dust_Lore]