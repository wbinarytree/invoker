---
title: Shadow Blade
kind: item
patch: 7.41d
card:
  entity: invis_sword
  sentences:
  - text: Shadow Blade is an epic item costing 3250 gold that grants 35 Attack Speed
      and 25 Damage; its Shadow Walk active costs 75 mana, has a 25.0 cooldown, and
      provides up to 17.0 seconds of invisibility, 20% movement speed, and 175 bonus
      physical damage when ended by an attack.
    marks:
    - gamefile:items/item_invis_sword#cost
    - gamefile:items/item_invis_sword#attribs
    - gamefile:items/item_invis_sword#mechanics
    - loc:DOTA_Tooltip_ability_item_invis_sword_Description
  - text: Shadow Walk has a 0.3 fade time.
    marks:
    - gamefile:items/item_invis_sword#attribs
  - text: Shadow Walk is immediate, requires no target, and ignores channeling.
    marks:
    - gamefile:items/item_invis_sword#mechanics
  - text: Its invisibility ends when its duration expires or the user attacks or casts
      a spell.
    marks:
    - loc:DOTA_Tooltip_ability_item_invis_sword_Description
  - text: While active, Shadow Walk allows movement through units.
    marks:
    - loc:DOTA_Tooltip_ability_item_invis_sword_Description
  - text: Shadow Blade is built from Claymore (1350 gold), Blitz Knuckles (1000 gold),
      and Shadow Amulet (900 gold), and builds into Silver Edge.
    marks:
    - gamefile:items/item_invis_sword#components
  - text: “The blade of a fallen king, it allows you to move unseen and strike from
      the shadows.”
    marks:
    - loc:DOTA_Tooltip_ability_item_invis_sword_Lore
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