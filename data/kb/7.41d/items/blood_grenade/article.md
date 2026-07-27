---
title: Blood Grenade
kind: item
patch: 7.41d
card:
  entity: blood_grenade
  sentences:
  - text: Blood Grenade is a 50-gold consumable that provides 50 HEALTH; Throw Grenade
      deals 50 IMPACT DAMAGE and 15 DAMAGE OVER TIME at a TICK RATE of 1 for a DEBUFF
      DURATION of 5, applies -15% MOVESPEED SLOW, and has RADIUS 300.
    marks:
    - gamefile:items/item_blood_grenade#cost
    - gamefile:items/item_blood_grenade#attribs
    - loc:DOTA_Tooltip_Ability_item_blood_grenade_Description
  - text: Throw Grenade has SPEED 1100.
    marks:
    - gamefile:items/item_blood_grenade#attribs
  - text: Its behavior is Point Target, AOE, DOTA_ABILITY_BEHAVIOR_IGNORE_BACKSWING,
      and DOTA_ABILITY_BEHAVIOR_DONT_PROC_OTHER_ABILITIES.
    marks:
    - gamefile:items/item_blood_grenade#mechanics
  - text: Its cast range is 900.
    marks:
    - gamefile:items/item_blood_grenade#mechanics
  - text: Its cooldown is 10.
    marks:
    - gamefile:items/item_blood_grenade#mechanics
  - text: Both the hunter and the hunted must pay the blood price.
    marks:
    - loc:DOTA_Tooltip_Ability_item_blood_grenade_Lore
---

# Blood Grenade

Blood Grenade is a consumable item that provides Health, while Throw Grenade applies Impact Damage, Movespeed Slow, and Damage Over Time for a Debuff Duration. [gamefile:items/item_blood_grenade#cost] [gamefile:items/item_blood_grenade#attribs] [loc:DOTA_Tooltip_Ability_item_blood_grenade_Description]

## Cost

| Item | Gold cost |
|---|---:|
| Blood Grenade | 50 gold |

[gamefile:items/item_blood_grenade#cost]

## Stats

| Stat | Value |
|---|---:|
| HEALTH | 50 |
| DAMAGE OVER TIME | 15 |
| DEBUFF DURATION | 5 |
| IMPACT DAMAGE | 50 |
| MOVESPEED SLOW | -15% |
| RADIUS | 300 |
| SPEED | 1100 |
| TICK RATE | 1 |

[gamefile:items/item_blood_grenade#attribs]

## Throw Grenade

| Property | Value |
|---|---|
| Behavior | Point Target, AOE, DOTA_ABILITY_BEHAVIOR_IGNORE_BACKSWING, DOTA_ABILITY_BEHAVIOR_DONT_PROC_OTHER_ABILITIES |
| Cast range | 900 |
| Cooldown | 10 |

[gamefile:items/item_blood_grenade#mechanics]

Throw Grenade targets an area; affected enemies take Impact Damage and receive a Movespeed Slow and periodic Damage Over Time for the Debuff Duration. [loc:DOTA_Tooltip_Ability_item_blood_grenade_Description]

*Both the hunter and the hunted must pay the blood price.* [loc:DOTA_Tooltip_Ability_item_blood_grenade_Lore]