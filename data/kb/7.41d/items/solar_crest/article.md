---
title: Solar Crest
kind: item
patch: 7.41d
card:
  entity: solar_crest
  sentences:
  - text: Solar Crest is a rare 2575-gold item granting 7 armor, 200 health, 200 mana,
      and 25 movement speed; Shine gives an ally 5 armor, 60 attack speed, 15% movement
      speed, and a 350 physical-damage barrier for 7 seconds.
    marks:
    - gamefile:items/item_solar_crest#cost
    - gamefile:items/item_solar_crest#attribs
    - loc:DOTA_Tooltip_ability_item_solar_crest_Description
  - text: It is built from Pavise (1350 gold), Chainmail (500 gold), Wind Lace (225
      gold), and a Recipe (500 gold).
    marks:
    - gamefile:items/item_solar_crest#components
    - gamefile:items/item_solar_crest#cost
  - text: Shine has Unit Target, Immediate behavior.
    marks:
    - gamefile:items/item_solar_crest#mechanics
  - text: Shine is dispellable.
    marks:
    - gamefile:items/item_solar_crest#mechanics
  - text: Shine has 1000 cast range.
    marks:
    - gamefile:items/item_solar_crest#mechanics
  - text: Shine costs 100 mana.
    marks:
    - gamefile:items/item_solar_crest#mechanics
  - text: Shine has a 16.0 cooldown.
    marks:
    - gamefile:items/item_solar_crest#mechanics
  - text: When used on its owner, Shine does not grant its 5 armor, 15% movement speed,
      or 60 attack speed bonuses.
    marks:
    - loc:DOTA_Tooltip_ability_item_solar_crest_Description
    - gamefile:items/item_solar_crest#attribs
---

# Solar Crest

Solar Crest is a rare item that provides armor, health, mana, and movement speed, while its active, Shine, grants an ally armor, attack speed, movement speed, and a physical damage barrier. [gamefile:items/item_solar_crest#cost][gamefile:items/item_solar_crest#attribs][loc:DOTA_Tooltip_ability_item_solar_crest_Description]

## Components

| Component | Gold cost |
|---|---:|
| Pavise | 1350 gold |
| Chainmail | 500 gold |
| Wind Lace | 225 gold |
| Recipe | 500 gold |
| **Solar Crest** | **2575 gold** |

[gamefile:items/item_solar_crest#components][gamefile:items/item_solar_crest#cost]

## Stats

| Stat | Value |
|---|---:|
| Absorb amount | 350 |
| All attributes | 0 |
| Armor | 7 |
| Health | 200 |
| Mana | 200 |
| Duration | 7 |
| Movement speed | 25 |
| Target armor | 5 |
| Target attack speed | 60 |
| Target movement speed | 15% |

[gamefile:items/item_solar_crest#attribs]

## Shine

| Property | Value |
|---|---|
| Behavior | Unit Target, Immediate |
| Dispellable | Yes |
| Cast range | 1000 |
| Mana cost | 100 |
| Cooldown | 16.0 |

[gamefile:items/item_solar_crest#mechanics]

When used on self, Shine does not grant its bonus armor, movement speed, or attack speed. [loc:DOTA_Tooltip_ability_item_solar_crest_Description]

*A talisman forged to honor the daytime sky.* [loc:DOTA_Tooltip_ability_item_solar_crest_Lore]