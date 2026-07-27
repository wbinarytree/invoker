---
title: Blade Mail
kind: item
patch: 7.41d
card:
  entity: blade_mail
  sentences:
  - text: Blade Mail is an epic item costing 2400 gold that grants 7 Armor and 15
      Damage, actively returns all incoming damage with 85% Active Reflection for
      5.5 duration, and passively returns 10 damage plus 15% of attack damage.
    marks:
    - gamefile:items/item_blade_mail#cost
    - gamefile:items/item_blade_mail#attribs
    - loc:DOTA_Tooltip_ability_item_blade_mail_Description
  - text: Blade Mail is built from a Broadsword costing 1000 gold, Splintmail costing
      950 gold, and a Recipe costing 450 gold.
    marks:
    - gamefile:items/item_blade_mail#components
  - text: Its activation behavior is Immediate, No Target, and DOTA_ABILITY_BEHAVIOR_IGNORE_CHANNEL.
    marks:
    - gamefile:items/item_blade_mail#mechanics
  - text: Activation costs 25 mana.
    marks:
    - gamefile:items/item_blade_mail#mechanics
  - text: Its cooldown is 25.0.
    marks:
    - gamefile:items/item_blade_mail#mechanics
  - text: Passive Damage Return triggers every time the bearer is attacked.
    marks:
    - loc:DOTA_Tooltip_ability_item_blade_mail_Description
---

# Blade Mail

Blade Mail is an epic item that grants Armor and Damage and provides active and passive Damage Return. [gamefile:items/item_blade_mail#cost] [gamefile:items/item_blade_mail#attribs] [loc:DOTA_Tooltip_ability_item_blade_mail_Description]

| Property | Value |
|---|---:|
| Cost | 2400 gold |

[gamefile:items/item_blade_mail#cost]

## Attributes

| Stat | Value |
|---|---:|
| Active Reflection | 85% |
| Armor | 7 |
| Damage | 15 |
| Bonus Intellect | 0 |
| Duration | 5.5 |
| Passive Reflection Constant | 10 |
| Passive Reflection | 15% |

[gamefile:items/item_blade_mail#attribs]

## Components

| Component | Cost |
|---|---:|
| Broadsword | 1000 gold |
| Splintmail | 950 gold |
| Recipe | 450 gold |

[gamefile:items/item_blade_mail#components]

## Mechanics

| Property | Value |
|---|---:|
| Behavior | Immediate, No Target, DOTA_ABILITY_BEHAVIOR_IGNORE_CHANNEL |
| Mana cost | 25 |
| Cooldown | 25.0 |

[gamefile:items/item_blade_mail#mechanics]

Active Damage Return returns all incoming damage and increases the returned percentage. Passive Damage Return triggers every time the bearer is attacked, returning constant damage plus a percentage of the attack damage dealt. [loc:DOTA_Tooltip_ability_item_blade_mail_Description]

*A razor-sharp coat of mail, it is the choice of selfless martyrs in combat.* [loc:DOTA_Tooltip_ability_item_blade_mail_Lore]