---
title: Dagon
kind: item
patch: 7.41d
card:
  entity: dagon_4
  sentences:
  - text: 'Dagon is a rare item costing 6300 gold that provides the upgradable Unit
      Target active Energy Burst: 640 Active Cast Range, 400/500/600/700/800 magical
      Damage, 0 Damage Delay, 120/140/160/180/200 Mana Cost, and 27/24/21/18/15 Cooldown.'
    marks:
    - gamefile:items/item_dagon_4#cost
    - gamefile:items/item_dagon_4#mechanics
    - loc:DOTA_Tooltip_ability_item_dagon_4_Description
  - text: Dagon grants 6/7/8/9/10 All Attributes.
    marks:
    - gamefile:items/item_dagon_4#attribs
  - text: It grants 200/210/220/230/240 Health.
    marks:
    - gamefile:items/item_dagon_4#attribs
  - text: It grants 350/375/400/425/450 Mana.
    marks:
    - gamefile:items/item_dagon_4#attribs
  - text: It grants 60/90/120/150/180 Cast Range.
    marks:
    - gamefile:items/item_dagon_4#attribs
  - text: 'Build formula: Dagon (item_dagon_3) (5200 gold) + item_recipe_dagon (item_recipe_dagon)
      (—); builds into Dagon (item_dagon_5).'
    marks:
    - gamefile:items/item_dagon_4#components
---

# Dagon

Dagon is a rare item [gamefile:items/item_dagon_4#cost] that grants All Attributes, Health, Mana, and Cast Range [gamefile:items/item_dagon_4#attribs] and provides the unit-target active Energy Burst, which deals magical Damage to a targeted enemy unit and is upgradable [gamefile:items/item_dagon_4#mechanics] [loc:DOTA_Tooltip_ability_item_dagon_4_Description].

## Cost

| Item | Gold cost |
|---|---:|
| Dagon (item_dagon_4) | 6300 gold |

[gamefile:items/item_dagon_4#cost]

## Components

| Relationship | Item | Gold cost |
|---|---|---:|
| Component | Dagon (item_dagon_3) | 5200 gold |
| Component | item_recipe_dagon (item_recipe_dagon) | — |
| Builds into | Dagon (item_dagon_5) | 7400 gold |

[gamefile:items/item_dagon_4#components]

## Stats and Mechanics

| Property | Value |
|---|---|
| All Attributes | 6/7/8/9/10 |
| Health | 200/210/220/230/240 |
| Mana | 350/375/400/425/450 |
| Cast Range | 60/90/120/150/180 |
| Damage | 400/500/600/700/800 |
| Damage Delay | 0 |
| Mana Cost / Mana Cost Tooltip | 120/140/160/180/200 |
| Behavior | Unit Target |
| Active Cast Range | 640 |
| Cooldown | 27/24/21/18/15 |

[gamefile:items/item_dagon_4#attribs] [gamefile:items/item_dagon_4#mechanics] [loc:DOTA_Tooltip_ability_item_dagon_4_Description]

*A lesser wand that grows in power the longer it is used, it brings magic to the fingertips of the user.* [loc:DOTA_Tooltip_ability_item_dagon_4_Lore]