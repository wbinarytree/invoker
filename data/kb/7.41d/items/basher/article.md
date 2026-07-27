---
title: Skull Basher
kind: item
patch: 7.41d
card:
  entity: basher
  sentences:
  - text: 'Skull Basher is an epic item costing 2875 gold that grants 30 Damage and
      10 Strength and provides Passive: Bash, which has a 25% chance for melee heroes
      and 10% for ranged heroes to trigger on hit, stun the target for 1.2 duration,
      and deal 100 bonus damage, with a 2.3 cooldown.'
    marks:
    - gamefile:items/item_basher#cost
    - gamefile:items/item_basher#attribs
    - loc:DOTA_Tooltip_ability_item_basher_Description
  - text: Its build formula is Mithril Hammer (1600 gold), Belt of Strength (450 gold),
      and Recipe (825 gold); it builds into Abyssal Blade.
    marks:
    - gamefile:items/item_basher#components
  - text: Bash's damage type is Physical.
    marks:
    - gamefile:items/item_basher#mechanics
  - text: Bash is dispellable by Strong Dispels Only.
    marks:
    - gamefile:items/item_basher#mechanics
  - text: A feared weapon in the right hands, this maul's ability to shatter the defenses
      of its opponents should not be underestimated.
    marks:
    - loc:DOTA_Tooltip_ability_item_basher_Lore
---

# Skull Basher

Skull Basher is an epic item [gamefile:items/item_basher#cost] that grants Damage and Strength [gamefile:items/item_basher#attribs] and provides Passive: Bash. [loc:DOTA_Tooltip_ability_item_basher_Description]

## Stats

| Stat | Value |
|---|---:|
| Cost | 2875 gold |
[gamefile:items/item_basher#cost]

| Stat | Value |
|---|---:|
| BASH CHANCE MELEE | 25% |
| BASH CHANCE RANGED | 10% |
| BASH COOLDOWN / Cooldown | 2.3 |
| BASH DURATION | 1.2 |
| BONUS CHANCE DAMAGE | 100 |
| DAMAGE | 30 |
| STRENGTH | 10 |
[gamefile:items/item_basher#attribs] [gamefile:items/item_basher#mechanics]

## Components

| Formula entry | Gold cost |
|---|---:|
| Mithril Hammer | 1600 gold |
| Belt of Strength | 450 gold |
| Recipe | 825 gold |
| **Builds into:** Abyssal Blade | 6250 gold |
[gamefile:items/item_basher#components]

## Mechanics

Passive: Bash can trigger on hit to stun the target and deal bonus physical damage, with different chances for melee and ranged heroes. [loc:DOTA_Tooltip_ability_item_basher_Description]

Its damage type is Physical, and it is dispellable by Strong Dispels Only. [gamefile:items/item_basher#mechanics]

*A feared weapon in the right hands, this maul's ability to shatter the defenses of its opponents should not be underestimated.* [loc:DOTA_Tooltip_ability_item_basher_Lore]