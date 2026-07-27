---
title: Tranquil Boots
kind: item
patch: 7.41d
card:
  entity: tranquil_boots
  sentences:
  - text: Tranquil Boots is a rare 900-gold item that grants 14 Health Regeneration
      and 65 Movement Speed; its passive Break lasts 13 seconds, removes the regeneration
      bonus, and reduces Movement Speed to 40 whenever the wearer attacks a hero or
      is attacked by any unit.
    marks:
    - gamefile:items/item_tranquil_boots#cost
    - gamefile:items/item_tranquil_boots#attribs
    - loc:DOTA_Tooltip_ability_item_tranquil_boots_Description
  - text: Bonus Armor is 0.
    marks:
    - gamefile:items/item_tranquil_boots#attribs
  - text: Break Count is 1.
    marks:
    - gamefile:items/item_tranquil_boots#attribs
  - text: Break Threshold is 20.
    marks:
    - gamefile:items/item_tranquil_boots#attribs
  - text: Heal Amount is 250.
    marks:
    - gamefile:items/item_tranquil_boots#attribs
  - text: Heal Duration is 20.0.
    marks:
    - gamefile:items/item_tranquil_boots#attribs
  - text: Heal Interval is 0.334.
    marks:
    - gamefile:items/item_tranquil_boots#attribs
  - text: Break costs 0 mana.
    marks:
    - gamefile:items/item_tranquil_boots#mechanics
  - text: Break has a 13.0 cooldown.
    marks:
    - gamefile:items/item_tranquil_boots#mechanics
  - text: Tranquil Boots (900 gold) is built from Boots of Speed (500 gold), Wind
      Lace (225 gold), and Ring of Regen (175 gold), and builds into Boots of Bearing.
    marks:
    - gamefile:items/item_tranquil_boots#cost
    - gamefile:items/item_tranquil_boots#components
  - text: Movement Speed bonuses from multiple pairs of boots do not stack.
    marks:
    - loc:DOTA_Tooltip_ability_item_tranquil_boots_Description
  - text: While they increase the longevity of the wearer, this boot is not particularly
      reliable.
    marks:
    - loc:DOTA_Tooltip_ability_item_tranquil_boots_Lore
---

# Tranquil Boots

Tranquil Boots is a rare item with Health Regeneration, Movement Speed, and the passive Break. [gamefile:items/item_tranquil_boots#cost] [gamefile:items/item_tranquil_boots#attribs] [loc:DOTA_Tooltip_ability_item_tranquil_boots_Description]

## Stats

| Stat | Value |
|---|---:|
| Bonus Armor | 0 |
| Health Regeneration | 14 |
| Movement Speed | 65 |
| Break Count | 1 |
| Break Threshold | 20 |
| Break Time | 13 |
| Broken Movement Speed | 40 |
| Heal Amount | 250 |
| Heal Duration | 20.0 |
| Heal Interval | 0.334 |

[gamefile:items/item_tranquil_boots#attribs]

| Mechanic | Value |
|---|---:|
| Behavior | Passive |
| Mana cost | 0 |
| Cooldown | 13.0 |

[gamefile:items/item_tranquil_boots#mechanics]

## Components

| Role | Item | Gold cost |
|---|---|---:|
| Item | Tranquil Boots | 900 gold |
| Component | Boots of Speed | 500 gold |
| Component | Wind Lace | 225 gold |
| Component | Ring of Regen | 175 gold |
| Builds into | Boots of Bearing | 4225 gold |

[gamefile:items/item_tranquil_boots#cost] [gamefile:items/item_tranquil_boots#components]

## Break

Break triggers whenever the wearer attacks a hero or is attacked by any unit. While active, the bonus health regeneration is lost and the movement speed bonus is reduced. Movement Speed bonuses from multiple pairs of boots do not stack. [loc:DOTA_Tooltip_ability_item_tranquil_boots_Description]

*While they increase the longevity of the wearer, this boot is not particularly reliable.* [loc:DOTA_Tooltip_ability_item_tranquil_boots_Lore]