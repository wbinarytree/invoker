---
title: Blood Grenade
kind: item
patch: 7.41d
card:
  entity: blood_grenade
  sentences:
  - text: Blood Grenade is a 50-gold consumable item that provides 50 Health; Throw
      Grenade has 50 Impact Damage, -15% Movespeed Slow, 15 Damage Over Time, 5 Debuff
      Duration, 1 Tick Rate, and 300 Radius.
    marks:
    - gamefile:items/item_blood_grenade#cost
    - gamefile:items/item_blood_grenade#attribs
    - loc:DOTA_Tooltip_Ability_item_blood_grenade_Description
  - text: Throw Grenade targets an area and affects enemies with its Impact Damage,
      Movespeed Slow, and periodic Damage Over Time.
    marks:
    - loc:DOTA_Tooltip_Ability_item_blood_grenade_Description
  - text: Throw Grenade has Point Target and AOE behavior, a 900 Cast range, and a
      10 Cooldown.
    marks:
    - gamefile:items/item_blood_grenade#mechanics
  - text: Throw Grenade has 1100 Speed.
    marks:
    - gamefile:items/item_blood_grenade#attribs
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