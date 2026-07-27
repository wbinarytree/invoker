---
title: Lance of Pursuit
kind: item
patch: 7.41d
card:
  entity: lance_of_pursuit
  sentences:
  - text: Lance of Pursuit is a 0-gold passive item that grants 200 Mana and 0 Bonus
      Strength; Hound gives attacks from behind a Backstab Angle of 90, 20 Backstab
      Damage, and a 2-second slow of 16% for melee attackers or 8% for ranged attackers.
    marks:
    - gamefile:items/item_lance_of_pursuit#cost
    - gamefile:items/item_lance_of_pursuit#attribs
    - gamefile:items/item_lance_of_pursuit#mechanics
    - loc:DOTA_Tooltip_Ability_item_lance_of_pursuit_Description
  - text: 'Build formula: item cost 0 gold.'
    marks:
    - gamefile:items/item_lance_of_pursuit#cost
---

# Lance of Pursuit

Lance of Pursuit is an item with Mana and Bonus Strength that grants passive Hound, applying Backstab Damage, Slow Pct Melee or Slow Pct Ranged, and Slow Duration when attacking from behind. [gamefile:items/item_lance_of_pursuit#attribs] [loc:DOTA_Tooltip_Ability_item_lance_of_pursuit_Description]

## Components

| Entry | Gold cost |
|---|---:|
| Item cost | 0 gold |

[gamefile:items/item_lance_of_pursuit#cost]

## Stats

| Stat | Value |
|---|---:|
| Backstab Angle | 90 |
| Backstab Damage | 20 |
| Mana | 200 |
| Bonus Strength | 0 |
| Slow Duration | 2 |
| Slow Pct Melee | 16% |
| Slow Pct Ranged | 8% |

[gamefile:items/item_lance_of_pursuit#attribs]

## Mechanics

| Behavior | Value |
|---|---|
| Ability behavior | Passive |

[gamefile:items/item_lance_of_pursuit#mechanics]

Hound triggers when attacking an enemy from behind, slowing the target and dealing additional damage. The ranged slow differs from the melee slow. [loc:DOTA_Tooltip_Ability_item_lance_of_pursuit_Description]

*The gleaming weapon of a tarnished knight haunted by his duties to an unworthy king.* [loc:DOTA_Tooltip_Ability_item_lance_of_pursuit_Lore]