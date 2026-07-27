---
title: Vindicator's Axe
kind: item
patch: 7.41d
card:
  entity: vindicators_axe
  sentences:
  - text: Vindicator's Axe is a 0-gold item that grants 20 bonus armor, 35 attack
      speed, 30 bonus damage, and 20% slow resistance; its passive Vengeance effect
      provides 30 damage while the equipped hero is silenced and 20 armor while the
      hero is stunned.
    marks:
    - gamefile:items/item_vindicators_axe#attribs
    - gamefile:items/item_vindicators_axe#cost
    - gamefile:items/item_vindicators_axe#mechanics
    - loc:DOTA_Tooltip_ability_item_vindicators_axe_Description
  - text: It grants 20 bonus armor.
    marks:
    - gamefile:items/item_vindicators_axe#attribs
  - text: It grants 35 attack speed.
    marks:
    - gamefile:items/item_vindicators_axe#attribs
  - text: It grants 30 bonus damage.
    marks:
    - gamefile:items/item_vindicators_axe#attribs
  - text: It grants 20% slow resistance.
    marks:
    - gamefile:items/item_vindicators_axe#attribs
  - text: Vindicator's Axe costs 0 gold.
    marks:
    - gamefile:items/item_vindicators_axe#cost
  - text: Vengeance is passive.
    marks:
    - gamefile:items/item_vindicators_axe#mechanics
  - text: Vengeance provides 30 damage while the equipped hero is silenced.
    marks:
    - loc:DOTA_Tooltip_ability_item_vindicators_axe_Description
  - text: Vengeance provides 20 armor while the equipped hero is stunned.
    marks:
    - loc:DOTA_Tooltip_ability_item_vindicators_axe_Description
---

# Vindicator's Axe

Vindicator's Axe is an item with Bonus Armor, Attack Speed, Bonus Damage, Slow Resistance, and the passive Vengeance effect. [gamefile:items/item_vindicators_axe#attribs] [loc:DOTA_Tooltip_ability_item_vindicators_axe_Description]

## Stats

| Stat | Value |
|---|---:|
| Bonus Armor | 20 |
| Attack Speed | 35 |
| Bonus Damage | 30 |
| Slow Resistance | 20% |

[gamefile:items/item_vindicators_axe#attribs]

## Cost

| Item | Gold cost |
|---|---:|
| Vindicator's Axe | 0 gold |

[gamefile:items/item_vindicators_axe#cost]

## Vengeance

The item’s behavior is passive. [gamefile:items/item_vindicators_axe#mechanics]

| Equipped hero’s condition | Effect |
|---|---|
| Silenced | Provides 30 damage |
| Stunned | Provides 20 armor |

[loc:DOTA_Tooltip_ability_item_vindicators_axe_Description]