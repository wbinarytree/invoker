---
title: Magic Wand
kind: item
patch: 7.41d
card:
  entity: magic_wand
  sentences:
  - text: Magic Wand is a common 460-gold item that grants 3 All Attributes and provides
      Energy Charge, which instantly restores 15 health and mana per stored charge
      up to 20 charges.
    marks:
    - gamefile:items/item_magic_wand#cost
    - gamefile:items/item_magic_wand#attribs
    - loc:DOTA_Tooltip_ability_item_magic_wand_Description
  - text: Its charge radius is 1200.
    marks:
    - gamefile:items/item_magic_wand#attribs
  - text: Energy Charge has Immediate, No Target behavior.
    marks:
    - gamefile:items/item_magic_wand#mechanics
  - text: Energy Charge has a 15.0 cooldown.
    marks:
    - gamefile:items/item_magic_wand#mechanics
  - text: It gains a charge whenever a visible enemy in range uses an ability.
    marks:
    - loc:DOTA_Tooltip_ability_item_magic_wand_Description
  - text: It is built from Magic Stick (200 gold), Iron Branch (55 gold), Iron Branch
      (55 gold), and Recipe (150 gold), and builds into Holy Locket.
    marks:
    - gamefile:items/item_magic_wand#components
  - text: A simple wand used to channel magic energies, it is favored by apprentice
      wizards and great warlocks alike.
    marks:
    - loc:DOTA_Tooltip_ability_item_magic_wand_Lore
---

# Magic Wand

Magic Wand is a common item that grants All Attributes and provides the Energy Charge active. [gamefile:items/item_magic_wand#cost] [gamefile:items/item_magic_wand#attribs] [loc:DOTA_Tooltip_ability_item_magic_wand_Description]

| Property | Value |
|---|---:|
| Cost | 460 gold |

[gamefile:items/item_magic_wand#cost]

## Stats

| Stat | Value |
|---|---:|
| ALL ATTRIBUTES | 3 |
| CHARGE RADIUS | 1200 |
| MAX CHARGES | 20 |
| RESTORE PER CHARGE | 15 |

[gamefile:items/item_magic_wand#attribs]

## Active

| Property | Value |
|---|---|
| Behavior | Immediate, No Target |
| Cooldown | 15.0 |

[gamefile:items/item_magic_wand#mechanics]

Energy Charge instantly restores health and mana per stored charge. It gains a charge whenever a visible enemy in range uses an ability. [loc:DOTA_Tooltip_ability_item_magic_wand_Description]

## Components

| Role | Item | Gold cost |
|---|---|---:|
| Component | Magic Stick | 200 gold |
| Component | Iron Branch | 55 gold |
| Component | Iron Branch | 55 gold |
| Recipe | Recipe | 150 gold |
| Builds into | Holy Locket | 2250 gold |

[gamefile:items/item_magic_wand#components]

*A simple wand used to channel magic energies, it is favored by apprentice wizards and great warlocks alike.* [loc:DOTA_Tooltip_ability_item_magic_wand_Lore]