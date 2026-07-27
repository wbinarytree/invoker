---
title: Dagon
kind: item
patch: 7.41d
card:
  entity: dagon
  sentences:
  - text: Dagon is a rare 3000-gold item that grants 6/7/8/9/10 All Attributes, 200/210/220/230/240
      Health, 350/375/400/425/450 Mana, and 60/90/120/150/180 Cast Range and provides
      Energy Burst, a Unit Target active that deals 400/500/600/700/800 magical damage
      at 640 Active Cast Range.
    marks:
    - gamefile:items/item_dagon#cost
    - gamefile:items/item_dagon#attribs
    - gamefile:items/item_dagon#mechanics
    - loc:DOTA_Tooltip_ability_item_dagon_Description
  - text: Energy Burst has 0 Damage Delay.
    marks:
    - gamefile:items/item_dagon#attribs
  - text: Energy Burst costs 120/140/160/180/200 Mana.
    marks:
    - gamefile:items/item_dagon#attribs
  - text: Energy Burst has a 27/24/21/18/15-second Cooldown.
    marks:
    - gamefile:items/item_dagon#attribs
  - text: Energy Burst is upgradable.
    marks:
    - gamefile:items/item_dagon#mechanics
    - loc:DOTA_Tooltip_ability_item_dagon_Description
  - text: Dagon is built from Point Booster (1200 gold), Crown (450 gold), Wizard
      Hat (250 gold), and Recipe (1100 gold), and builds into Dagon (item_dagon_2).
    marks:
    - gamefile:items/item_dagon#components
  - text: “A lesser wand that grows in power the longer it is used, it brings magic
      to the fingertips of the user.”
    marks:
    - loc:DOTA_Tooltip_ability_item_dagon_Lore
---

# Dagon

Dagon is a rare item that grants All Attributes, Health, Mana, and Cast Range and provides the Energy Burst active. [gamefile:items/item_dagon#cost] [gamefile:items/item_dagon#attribs] [loc:DOTA_Tooltip_ability_item_dagon_Description]

## Stats

| Stat | Value |
|---|---:|
| Cost | 3000 gold |
[gamefile:items/item_dagon#cost]

| Stat | Value |
|---|---:|
| All Attributes | 6/7/8/9/10 |
| Health | 200/210/220/230/240 |
| Mana | 350/375/400/425/450 |
| Cast Range | 60/90/120/150/180 |
| Damage | 400/500/600/700/800 |
| Damage Delay | 0 |
| Mana Cost / Mana Cost Tooltip | 120/140/160/180/200 |
| Cooldown | 27/24/21/18/15 |
| Active Cast Range | 640 |
| Behavior | Unit Target |
[gamefile:items/item_dagon#attribs] [gamefile:items/item_dagon#mechanics] [loc:DOTA_Tooltip_ability_item_dagon_Description]

## Components

| Component | Cost |
|---|---:|
| Point Booster | 1200 gold |
| Crown | 450 gold |
| Wizard Hat | 250 gold |
| Recipe | 1100 gold |
| **Builds into: Dagon (item_dagon_2)** | **4100 gold** |
[gamefile:items/item_dagon#components]

## Energy Burst

Energy Burst targets an enemy unit and deals magical damage. It is upgradable. [gamefile:items/item_dagon#mechanics] [loc:DOTA_Tooltip_ability_item_dagon_Description]

*A lesser wand that grows in power the longer it is used, it brings magic to the fingertips of the user.* [loc:DOTA_Tooltip_ability_item_dagon_Lore]