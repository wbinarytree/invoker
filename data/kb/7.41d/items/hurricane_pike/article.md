---
title: Hurricane Pike
kind: item
patch: 7.41d
card:
  entity: hurricane_pike
  sentences:
  - text: Hurricane Pike is a 4450-gold epic item granting 130 ranged attack range,
      20 agility, 100 bonus attack speed, 200 health, 15 intelligence, and 15 strength;
      its Hurricane Thrust pushes units 600 over 0.5 seconds and permits up to 5 unrestricted-range
      attacks against an enemy for 6 seconds.
    marks:
    - gamefile:items/item_hurricane_pike#cost
    - gamefile:items/item_hurricane_pike#attribs
    - loc:DOTA_Tooltip_Ability_item_hurricane_pike_Description
  - text: It is built from Force Staff for 2200 gold, Dragon Lance for 1900 gold,
      and a Recipe for 350 gold, for a total cost of 4450 gold.
    marks:
    - gamefile:items/item_hurricane_pike#cost
    - gamefile:items/item_hurricane_pike#components
  - text: Hurricane Thrust has Unit Target behavior, 650 cast range, 150 mana cost,
      and a 19.0-second cooldown.
    marks:
    - gamefile:items/item_hurricane_pike#mechanics
  - text: Its behavior includes DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK.
    marks:
    - gamefile:items/item_hurricane_pike#mechanics
  - text: Against an enemy, Hurricane Thrust pushes the caster and target away from
      each other.
    marks:
    - loc:DOTA_Tooltip_Ability_item_hurricane_pike_Description
  - text: When used on the caster or an ally, Hurricane Thrust pushes the target in
      the direction it is facing.
    marks:
    - loc:DOTA_Tooltip_Ability_item_hurricane_pike_Description
---

# Hurricane Pike

Hurricane Pike is an epic item that grants Attack Range (Ranged Only), Agility, Bonus Attack Speed, Health, Intelligence, and Strength and provides the Hurricane Thrust active. [gamefile:items/item_hurricane_pike#cost] [gamefile:items/item_hurricane_pike#attribs] [loc:DOTA_Tooltip_Ability_item_hurricane_pike_Description]

## Components

| Item or component | Cost |
|---|---:|
| Hurricane Pike | 4450 gold |
| Force Staff | 2200 gold |
| Dragon Lance | 1900 gold |
| Recipe | 350 gold |

[gamefile:items/item_hurricane_pike#cost] [gamefile:items/item_hurricane_pike#components]

## Stats

| Stat | Value |
|---|---:|
| Attack Range (Ranged Only) | 130 |
| Agility | 20 |
| Bonus Attack Speed | 100 |
| Health | 200 |
| Intelligence | 15 |
| Strength | 15 |
| Cast Range Enemy | 425 |
| Dizzy Distance Pct | 0 |
| Dizzy Duration | 0 |
| Enemy Length | 425 |
| Max Attacks | 5 |
| Push Length | 600 |
| Push Time | 0.5 |
| Range Duration | 6 |

[gamefile:items/item_hurricane_pike#attribs]

## Hurricane Thrust

| Property | Value |
|---|---|
| Behavior | Unit Target, DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK |
| Cast range | 650 |
| Mana cost | 150 |
| Cooldown | 19.0 |

[gamefile:items/item_hurricane_pike#mechanics]

Against an enemy, Hurricane Thrust pushes the caster and target away from each other, then temporarily allows the caster to attack that target without range restrictions, subject to the listed attack limit and bonus attack speed. On self or allies, it pushes the target in the direction it is facing. [loc:DOTA_Tooltip_Ability_item_hurricane_pike_Description]

*A legendary pike once held as the royal sigil of the ancient wyvern riders.* [loc:DOTA_Tooltip_Ability_item_hurricane_pike_Lore]