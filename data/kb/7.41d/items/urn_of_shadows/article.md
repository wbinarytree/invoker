---
title: Urn of Shadows
kind: item
patch: 7.41d
card:
  entity: urn_of_shadows
  sentences:
  - text: Urn of Shadows is a rare 825 gold item that grants 2 All Attributes, 2 Armor,
      and 1.25 Mana Regeneration; its active Soul Release provides 30 health regeneration
      to allies or 25 damage per second to enemies for 8.0 seconds.
    marks:
    - gamefile:items/item_urn_of_shadows#cost
    - gamefile:items/item_urn_of_shadows#attribs
    - loc:DOTA_Tooltip_ability_item_urn_of_shadows_Description
  - text: It has an initial Soul charge count of 2.
    marks:
    - gamefile:items/item_urn_of_shadows#attribs
  - text: It gains 1 additional charge whenever an enemy hero dies within 1500 units.
    marks:
    - gamefile:items/item_urn_of_shadows#attribs
  - text: Its behavior is Unit Target and Doesn't Proc Other Abilities.
    marks:
    - gamefile:items/item_urn_of_shadows#mechanics
  - text: It is dispellable.
    marks:
    - gamefile:items/item_urn_of_shadows#mechanics
  - text: Its cast range is 750.
    marks:
    - gamefile:items/item_urn_of_shadows#mechanics
  - text: Its cooldown is 10.0.
    marks:
    - gamefile:items/item_urn_of_shadows#mechanics
  - text: Its build formula is Sage's Mask (175 gold), Ring of Protection (175 gold),
      Circlet (155 gold), and Recipe (320 gold); it builds into Essence Distiller
      and Spirit Vessel.
    marks:
    - gamefile:items/item_urn_of_shadows#components
  - text: Contains the ashes of powerful demons.
    marks:
    - loc:DOTA_Tooltip_ability_item_urn_of_shadows_Lore
---

# Urn of Shadows

Urn of Shadows is a rare item that grants All Attributes, Armor, and Mana Regeneration, while its active Soul Release provides health regeneration to allies and damage per second to enemies. [gamefile:items/item_urn_of_shadows#cost] [gamefile:items/item_urn_of_shadows#attribs] [loc:DOTA_Tooltip_ability_item_urn_of_shadows_Description]

## Statistics

| Stat | Value |
|---|---:|
| Cost | 825 gold |
| ALL ATTRIBUTES | 2 |
| ARMOR | 2 |
| DURATION | 8.0 seconds |
| MANA REGENERATION | 1.25 |
| SOUL ADDITIONAL CHARGES | 1 |
| SOUL DAMAGE AMOUNT | 25 damage per second when cast on enemies |
| SOUL HEAL AMOUNT | 30 health regeneration when cast on allies |
| SOUL INITIAL CHARGE | 2 |
| SOUL RADIUS | Gains charges every time an enemy hero dies within 1500 units |
[gamefile:items/item_urn_of_shadows#cost] [gamefile:items/item_urn_of_shadows#attribs] [loc:DOTA_Tooltip_ability_item_urn_of_shadows_Description]

## Mechanics

| Property | Value |
|---|---|
| Behavior | Unit Target, Doesn't Proc Other Abilities |
| Dispellable | Yes |
| Cast range | 750 |
| Cooldown | 10.0 |
[gamefile:items/item_urn_of_shadows#mechanics]

## Components

| Formula role | Item | Gold cost |
|---|---|---:|
| Component | Sage's Mask | 175 gold |
| Component | Ring of Protection | 175 gold |
| Component | Circlet | 155 gold |
| Recipe | Recipe | 320 gold |
| Builds into | Essence Distiller | 1775 gold |
| Builds into | Spirit Vessel | 2725 gold |
[gamefile:items/item_urn_of_shadows#components]

*Contains the ashes of powerful demons.* [loc:DOTA_Tooltip_ability_item_urn_of_shadows_Lore]