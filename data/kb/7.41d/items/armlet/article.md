---
title: Armlet of Mordiggian
kind: item
patch: 7.41d
card:
  entity: armlet
  sentences:
  - text: Armlet of Mordiggian is a 2500-gold epic item granting 6 Armor, 25 Attack
      Speed, 15 Damage, and 5 Health Regeneration; its Unholy Strength toggle grants
      4 bonus armor, 35 bonus damage, 0 slow resistance, and 25 bonus strength while
      draining 45 health per second.
    marks:
    - gamefile:items/item_armlet#cost
    - gamefile:items/item_armlet#attribs
    - loc:DOTA_Tooltip_ability_item_armlet_Description
  - text: Its build formula is Helm of Iron Will for 975 gold, Gloves of Haste for
      450 gold, Blades of Attack for 450 gold, and a Recipe for 625 gold.
    marks:
    - gamefile:items/item_armlet#components
  - text: Its Toggle Cooldown stat is 0.036.
    marks:
    - gamefile:items/item_armlet#attribs
  - text: Unholy Strength is a no-target toggle with DOTA_ABILITY_BEHAVIOR_IGNORE_CHANNEL.
    marks:
    - gamefile:items/item_armlet#mechanics
  - text: Unholy Strength has a 0.0 cooldown.
    marks:
    - gamefile:items/item_armlet#mechanics
  - text: The bearer cannot die from its health drain or from the strength loss when
      Unholy Strength is deactivated.
    marks:
    - loc:DOTA_Tooltip_ability_item_armlet_Description
---

# Armlet of Mordiggian

Armlet of Mordiggian is an epic item that grants Armor, Attack Speed, Damage, and Health Regeneration and provides the Unholy Strength toggle, with Unholy Bonus Armor, Unholy Bonus Damage, Unholy Bonus Slow Resistance, Unholy Bonus Strength, and Unholy Health Drain Per Second. [gamefile:items/item_armlet#cost] [gamefile:items/item_armlet#attribs] [loc:DOTA_Tooltip_ability_item_armlet_Description]

## Components

| Component | Gold cost |
|---|---:|
| Helm of Iron Will | 975 gold |
| Gloves of Haste | 450 gold |
| Blades of Attack | 450 gold |
| Recipe | 625 gold |
| **Item cost** | **2500 gold** |

[gamefile:items/item_armlet#components] [gamefile:items/item_armlet#cost]

## Stats

| Stat | Value |
|---|---:|
| Armor | 6 |
| Attack Speed | 25 |
| Damage | 15 |
| Health Regeneration | 5 |
| Toggle Cooldown | 0.036 |
| Unholy Bonus Armor | 4 |
| Unholy Bonus Damage | 35 |
| Unholy Bonus Slow Resistance | 0 |
| Unholy Bonus Strength | 25 |
| Unholy Health Drain Per Second | 45 |

[gamefile:items/item_armlet#attribs]

## Unholy Strength

| Property | Value |
|---|---|
| Behavior | No Target, Toggle, DOTA_ABILITY_BEHAVIOR_IGNORE_CHANNEL |
| Cooldown | 0.0 |

[gamefile:items/item_armlet#mechanics]

While active, Unholy Strength grants bonus damage, strength, and armor while continuously draining health. The bearer cannot die from this health drain or from the strength loss when Unholy Strength is deactivated. [loc:DOTA_Tooltip_ability_item_armlet_Description]

*Weapon of choice among brutes, the bearer sacrifices his life energy to gain immense strength and power.* [loc:DOTA_Tooltip_ability_item_armlet_Lore]