---
title: Blade Mail
kind: item
patch: 7.41d
card:
  entity: blade_mail
  sentences:
  - text: Blade Mail is an epic 2400-gold item granting 7 Armor and 15 Damage, with
      active Damage Return that returns all incoming damage and has 85% Active Reflection
      Pct for 5.5 seconds, plus passive Damage Return that returns 10 plus 15% of
      attack damage whenever the wielder is attacked.
    marks:
    - gamefile:items/item_blade_mail#cost
    - gamefile:items/item_blade_mail#attribs
    - loc:DOTA_Tooltip_ability_item_blade_mail_Description
  - text: Its build formula is Broadsword (1000 gold) + Splintmail (950 gold) + Recipe
      (450 gold).
    marks:
    - gamefile:items/item_blade_mail#components
  - text: It has 0 Bonus Intellect.
    marks:
    - gamefile:items/item_blade_mail#attribs
  - text: Its behavior is Immediate, No Target, and Usable While Channelling.
    marks:
    - gamefile:items/item_blade_mail#mechanics
  - text: It costs 25 mana to use.
    marks:
    - gamefile:items/item_blade_mail#mechanics
  - text: It has a 25.0-second cooldown.
    marks:
    - gamefile:items/item_blade_mail#mechanics
  - text: “A razor-sharp coat of mail, it is the choice of selfless martyrs in combat.”
    marks:
    - loc:DOTA_Tooltip_ability_item_blade_mail_Lore
---

# Blade Mail

Blade Mail is an epic item [gamefile:items/item_blade_mail#cost] that grants Armor and Damage and provides active and passive Damage Return. [gamefile:items/item_blade_mail#attribs] [loc:DOTA_Tooltip_ability_item_blade_mail_Description]

## Components

| Component | Gold cost |
|---|---:|
| Broadsword | 1000 gold |
| Splintmail | 950 gold |
| Recipe | 450 gold |
| **Blade Mail** | **2400 gold** |

[gamefile:items/item_blade_mail#components] [gamefile:items/item_blade_mail#cost]

## Stats

| Stat | Value |
|---|---:|
| Active Reflection Pct | 85% |
| Armor | 7 |
| Damage | 15 |
| Bonus Intellect | 0 |
| Duration | 5.5 |
| Passive Reflection Constant | 10 |
| Passive Reflection Pct | 15% |

[gamefile:items/item_blade_mail#attribs]

| Mechanic | Value |
|---|---|
| Behavior | Immediate, No Target, Usable While Channelling |
| Mana cost | 25 |
| Cooldown | 25.0 |

[gamefile:items/item_blade_mail#mechanics]

## Damage Return

The active Damage Return returns all incoming damage and increases the returned percentage. The passive Damage Return triggers every time you are attacked and returns a constant amount plus a percentage of the attack damage dealt to you. [loc:DOTA_Tooltip_ability_item_blade_mail_Description]

*A razor-sharp coat of mail, it is the choice of selfless martyrs in combat.* [loc:DOTA_Tooltip_ability_item_blade_mail_Lore]