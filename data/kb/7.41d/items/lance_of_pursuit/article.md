---
title: Lance of Pursuit
kind: item
patch: 7.41d
card:
  entity: lance_of_pursuit
  sentences:
  - text: Lance of Pursuit is a 0-gold item with 200 Mana and 0 Bonus Strength whose
      passive Hound triggers on attacks from behind, with 90 Backstab Angle, 20 Backstab
      Damage, 16% Slow Pct Melee or 8% Slow Pct Ranged, and 2 Slow Duration.
    marks:
    - gamefile:items/item_lance_of_pursuit#cost
    - gamefile:items/item_lance_of_pursuit#attribs
    - loc:DOTA_Tooltip_Ability_item_lance_of_pursuit_Description
  - text: Its build formula lists Item cost at 0 gold.
    marks:
    - gamefile:items/item_lance_of_pursuit#cost
  - text: Ability behavior is Passive.
    marks:
    - gamefile:items/item_lance_of_pursuit#mechanics
  - text: Hound triggers when attacking an enemy from behind.
    marks:
    - loc:DOTA_Tooltip_Ability_item_lance_of_pursuit_Description
  - text: Backstab Angle is 90.
    marks:
    - gamefile:items/item_lance_of_pursuit#attribs
  - text: Backstab Damage is 20.
    marks:
    - gamefile:items/item_lance_of_pursuit#attribs
  - text: Mana is 200.
    marks:
    - gamefile:items/item_lance_of_pursuit#attribs
  - text: Bonus Strength is 0.
    marks:
    - gamefile:items/item_lance_of_pursuit#attribs
  - text: Slow Duration is 2.
    marks:
    - gamefile:items/item_lance_of_pursuit#attribs
  - text: Slow Pct Melee is 16%.
    marks:
    - gamefile:items/item_lance_of_pursuit#attribs
  - text: Slow Pct Ranged is 8%.
    marks:
    - gamefile:items/item_lance_of_pursuit#attribs
  - text: The gleaming weapon of a tarnished knight haunted by his duties to an unworthy
      king.
    marks:
    - loc:DOTA_Tooltip_Ability_item_lance_of_pursuit_Lore
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