---
title: Magic Stick
kind: item
patch: 7.41d
card:
  entity: magic_stick
  sentences:
  - text: Magic Stick is a 200-gold component item whose immediate, no-target active,
      Energy Charge, has a 17.0-second cooldown and instantly restores 15 health and
      15 mana per stored charge, up to 10 charges.
    marks:
    - gamefile:items/item_magic_stick#cost
    - gamefile:items/item_magic_stick#attribs
    - gamefile:items/item_magic_stick#mechanics
    - loc:DOTA_Tooltip_ability_item_magic_stick_Description
  - text: Its build is Magic Stick (200 gold), and it builds into Magic Wand.
    marks:
    - gamefile:items/item_magic_stick#cost
    - gamefile:items/item_magic_stick#components
  - text: Magic Stick gains a charge whenever a visible enemy within its 1200 Charge
      Radius uses an ability.
    marks:
    - gamefile:items/item_magic_stick#attribs
    - loc:DOTA_Tooltip_ability_item_magic_stick_Description
---

# Magic Stick

Magic Stick is a component item whose active, Energy Charge, restores health and mana. [gamefile:items/item_magic_stick#cost] [loc:DOTA_Tooltip_ability_item_magic_stick_Description]

## Components

| Build | Gold cost |
|---|---:|
| Magic Stick | 200 gold |
| **Builds into:** Magic Wand | 460 gold |

[gamefile:items/item_magic_stick#cost] [gamefile:items/item_magic_stick#components]

## Stats

| Stat | Value |
|---|---:|
| Charge Radius | 1200 |
| Max Charges | 10 |
| Restore per Charge | 15 |

[gamefile:items/item_magic_stick#attribs]

## Energy Charge

| Property | Value |
|---|---|
| Behavior | Immediate, No Target |
| Cooldown | 17.0 |

[gamefile:items/item_magic_stick#mechanics]

Energy Charge instantly restores health and mana for each stored charge. Magic Stick gains a charge whenever a visible enemy within its Charge Radius uses an ability. [loc:DOTA_Tooltip_ability_item_magic_stick_Description]

*A simple wand used to channel magic energies, favored by apprentice wizards and great warlocks alike.* [loc:DOTA_Tooltip_ability_item_magic_stick_Lore]