---
title: Shadow Blade
kind: item
patch: 7.41d
card:
  entity: invis_sword
  sentences:
  - text: Shadow Blade is an epic item costing 3250 gold that grants 35 Attack Speed
      and 25 Damage; its Shadow Walk active costs 75 mana, has a 25.0 cooldown, provides
      up to 17.0 of invisibility after a 0.3 fade time, increases movement speed by
      20%, allows movement through units, and grants 175 bonus physical damage to
      an attack that ends invisibility.
    marks:
    - gamefile:items/item_invis_sword#cost
    - gamefile:items/item_invis_sword#attribs
    - gamefile:items/item_invis_sword#mechanics
    - loc:DOTA_Tooltip_ability_item_invis_sword_Description
  - text: Shadow Walk is an immediate, no-target ability with DOTA_ABILITY_BEHAVIOR_IGNORE_CHANNEL
      behavior.
    marks:
    - gamefile:items/item_invis_sword#mechanics
  - text: Its invisibility ends when the 17.0 duration expires or the user attacks
      or casts a spell.
    marks:
    - gamefile:items/item_invis_sword#attribs
    - loc:DOTA_Tooltip_ability_item_invis_sword_Description
  - text: The Windwalk Movement Speed value is 20%.
    marks:
    - gamefile:items/item_invis_sword#attribs
  - text: The user can move through units while Shadow Walk is active.
    marks:
    - loc:DOTA_Tooltip_ability_item_invis_sword_Description
  - text: An attack that ends the invisibility gains 175 bonus physical damage.
    marks:
    - gamefile:items/item_invis_sword#attribs
    - loc:DOTA_Tooltip_ability_item_invis_sword_Description
  - text: The build formula is Claymore (1350 gold), Blitz Knuckles (1000 gold), and
      Shadow Amulet (900 gold); Shadow Blade builds into Silver Edge.
    marks:
    - gamefile:items/item_invis_sword#components
---

# Shadow Blade

Shadow Blade is an epic item that grants Attack Speed and Damage and provides the active ability Shadow Walk. [gamefile:items/item_invis_sword#cost] [gamefile:items/item_invis_sword#attribs] [loc:DOTA_Tooltip_ability_item_invis_sword_Description]

## Stats

| Stat | Value |
|---|---:|
| Cost | 3250 gold |

[gamefile:items/item_invis_sword#cost]

| Stat | Value |
|---|---:|
| Attack Speed | 35 |
| Damage | 25 |
| Windwalk Bonus Damage | 175 |
| Windwalk Duration | 17.0 |
| Windwalk Fade Time | 0.3 |
| Windwalk Movement Speed | 20% |

[gamefile:items/item_invis_sword#attribs]

| Ability property | Value |
|---|---|
| Behavior | Immediate, No Target, DOTA_ABILITY_BEHAVIOR_IGNORE_CHANNEL |
| Mana cost | 75 |
| Cooldown | 25.0 |

[gamefile:items/item_invis_sword#mechanics]

## Components

| Component | Gold cost |
|---|---:|
| Claymore | 1350 gold |
| Blitz Knuckles | 1000 gold |
| Shadow Amulet | 900 gold |

**Builds into:** Silver Edge — 5700 gold. [gamefile:items/item_invis_sword#components]

## Shadow Walk

Shadow Walk makes the user invisible until its duration expires or the user attacks or casts a spell. While active, it increases movement speed and allows movement through units. Ending the invisibility with an attack grants that attack bonus physical damage. [loc:DOTA_Tooltip_ability_item_invis_sword_Description]

*The blade of a fallen king, it allows you to move unseen and strike from the shadows.* [loc:DOTA_Tooltip_ability_item_invis_sword_Lore]