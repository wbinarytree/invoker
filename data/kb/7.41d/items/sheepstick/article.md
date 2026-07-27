---
title: Scythe of Vyse
kind: item
patch: 7.41d
card:
  entity: sheepstick
  sentences:
  - text: Scythe of Vyse is a rare 5200-gold item that grants 30 Intelligence and
      8.5 Mana Regeneration; its Hex turns a target into a harmless critter and silences,
      mutes, and disarms it for a Sheep Duration of 2.8 with Sheep Movement Speed
      140.
    marks:
    - gamefile:items/item_sheepstick#cost
    - gamefile:items/item_sheepstick#attribs
    - loc:DOTA_Tooltip_ability_item_sheepstick_Description
  - text: It has an Upgrade Radius of 200.
    marks:
    - gamefile:items/item_sheepstick#attribs
  - text: It is built from Mystic Staff for 2800 gold, Tiara of Selemene for 1700
      gold, and a recipe for 700 gold.
    marks:
    - gamefile:items/item_sheepstick#components
  - text: Hex is Unit Target with 800 cast range, 250 mana cost, and 20.0 cooldown.
    marks:
    - gamefile:items/item_sheepstick#mechanics
  - text: Hex is dispellable by Strong Dispels Only.
    marks:
    - gamefile:items/item_sheepstick#mechanics
  - text: Hex instantly destroys illusions.
    marks:
    - loc:DOTA_Tooltip_ability_item_sheepstick_Description
---

# Scythe of Vyse

Scythe of Vyse is a rare item [gamefile:items/item_sheepstick#cost] that grants Intelligence and Mana Regeneration [gamefile:items/item_sheepstick#attribs] and provides the active ability Hex. [loc:DOTA_Tooltip_ability_item_sheepstick_Description]

## Stats

| Stat | Value |
|---|---:|
| Cost | 5200 gold |
| Intelligence | 30 |
| Mana Regeneration | 8.5 |
| Sheep Duration | 2.8 |
| Sheep Movement Speed | 140 |
| Upgrade Radius | 200 |

[gamefile:items/item_sheepstick#cost] [gamefile:items/item_sheepstick#attribs]

## Components

| Component | Cost |
|---|---:|
| Mystic Staff | 2800 gold |
| Tiara of Selemene | 1700 gold |
| Recipe | 700 gold |

[gamefile:items/item_sheepstick#components]

## Hex

| Property | Value |
|---|---:|
| Behavior | Unit Target |
| Dispellable | Strong Dispels Only |
| Cast Range | 800 |
| Mana Cost | 250 |
| Cooldown | 20.0 |

[gamefile:items/item_sheepstick#mechanics]

Hex turns the target into a harmless critter and silences, mutes, and disarms it. It instantly destroys illusions. [loc:DOTA_Tooltip_ability_item_sheepstick_Description]

*The most guarded relic among the cult of Vyse, it is the most coveted weapon among magi.* [loc:DOTA_Tooltip_ability_item_sheepstick_Lore]