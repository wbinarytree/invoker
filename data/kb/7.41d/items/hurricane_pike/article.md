---
title: Hurricane Pike
kind: item
patch: 7.41d
card:
  entity: hurricane_pike
  sentences:
  - text: Hurricane Pike is an epic 4450-gold item that grants ranged heroes 130 Attack
      Range, 20 Agility, 100 Bonus Attack Speed, 200 Health, 15 Intelligence, and
      15 Strength, and provides Hurricane Thrust, a 650-cast-range, 150-mana active
      with a 19.0 cooldown that pushes units and permits up to 5 unrestricted-range
      attacks against an enemy for 6 seconds.
    marks:
    - gamefile:items/item_hurricane_pike#cost
    - gamefile:items/item_hurricane_pike#attribs
    - gamefile:items/item_hurricane_pike#mechanics
    - loc:DOTA_Tooltip_Ability_item_hurricane_pike_Description
  - text: Hurricane Pike (4450 gold) is built from Force Staff (2200 gold), Dragon
      Lance (1900 gold), and a Recipe (350 gold).
    marks:
    - gamefile:items/item_hurricane_pike#cost
    - gamefile:items/item_hurricane_pike#components
  - text: Against an enemy, Hurricane Thrust pushes the caster and target 600 away
      from each other over 0.5 seconds.
    marks:
    - gamefile:items/item_hurricane_pike#attribs
    - loc:DOTA_Tooltip_Ability_item_hurricane_pike_Description
  - text: The caster can then attack that enemy without range restrictions for 6 seconds,
      up to 5 attacks, with 100 Bonus Attack Speed.
    marks:
    - gamefile:items/item_hurricane_pike#attribs
    - loc:DOTA_Tooltip_Ability_item_hurricane_pike_Description
  - text: When cast on the user or an ally, Hurricane Thrust pushes the target in
      the direction it faces.
    marks:
    - loc:DOTA_Tooltip_Ability_item_hurricane_pike_Description
  - text: Hurricane Thrust has Unit Target and DOTA_ABILITY_BEHAVIOR_DONT_RESUME_ATTACK
      behavior.
    marks:
    - gamefile:items/item_hurricane_pike#mechanics
  - text: Its Cast Range Enemy and Enemy Length values are both 425.
    marks:
    - gamefile:items/item_hurricane_pike#attribs
  - text: Its Dizzy Distance Pct and Dizzy Duration values are both 0.
    marks:
    - gamefile:items/item_hurricane_pike#attribs
  - text: “A legendary pike once held as the royal sigil of the ancient wyvern riders.”
    marks:
    - loc:DOTA_Tooltip_Ability_item_hurricane_pike_Lore
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