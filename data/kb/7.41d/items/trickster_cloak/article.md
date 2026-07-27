---
title: Trickster Cloak
kind: item
patch: 7.41d
card:
  entity: trickster_cloak
  sentences:
  - text: Trickster Cloak is a 0-gold item with 6 Duration, 0 Evasion, and 0 Magic
      Resistance whose Cloak active grants invisibility.
    marks:
    - gamefile:items/item_trickster_cloak#cost
    - gamefile:items/item_trickster_cloak#attribs
    - loc:DOTA_Tooltip_Ability_item_trickster_cloak_Description
  - text: Cloak has Immediate, No Target, and DOTA_ABILITY_BEHAVIOR_IGNORE_CHANNEL
      behavior.
    marks:
    - gamefile:items/item_trickster_cloak#mechanics
  - text: Cloak has a 25.0 cooldown.
    marks:
    - gamefile:items/item_trickster_cloak#mechanics
---

# Trickster Cloak

Trickster Cloak is an item with Duration, Evasion, and Magic Resistance whose active, Cloak, grants invisibility. [gamefile:items/item_trickster_cloak#cost] [gamefile:items/item_trickster_cloak#attribs] [loc:DOTA_Tooltip_Ability_item_trickster_cloak_Description]

## Stats

| Stat | Value |
|---|---:|
| Duration | 6 |
| Evasion | 0 |
| Magic Resistance | 0 |

[gamefile:items/item_trickster_cloak#attribs]

## Cloak

| Property | Value |
|---|---|
| Behavior | Immediate, No Target, DOTA_ABILITY_BEHAVIOR_IGNORE_CHANNEL |
| Cooldown | 25.0 |

[gamefile:items/item_trickster_cloak#mechanics]

Cloak causes the user to become invisible. [loc:DOTA_Tooltip_Ability_item_trickster_cloak_Description]

## Cost

| Item | Gold cost |
|---|---:|
| Trickster Cloak | 0 gold |

[gamefile:items/item_trickster_cloak#cost]

*A fantastic garment immediately misplaced by its creator upon completion.* [loc:DOTA_Tooltip_Ability_item_trickster_cloak_Lore]