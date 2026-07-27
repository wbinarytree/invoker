---
title: Headdress
kind: item
patch: 7.41d
card:
  entity: headdress
  sentences:
  - text: Headdress is a rare 425-gold item that provides 0.5 Health Regeneration
      and passively grants allies 2.0 Aura Health Regen within a 1200 radius.
    marks:
    - gamefile:items/item_headdress#cost
    - gamefile:items/item_headdress#attribs
    - loc:DOTA_Tooltip_ability_item_headdress_Description
  - text: Its build formula is Ring of Regen (175 gold) plus a Recipe (250 gold).
    marks:
    - gamefile:items/item_headdress#components
  - text: It builds into Drum of Endurance and Mekansm.
    marks:
    - gamefile:items/item_headdress#components
---

# Headdress

Headdress is a rare item that provides Health Regeneration and has Regeneration Aura, a passive effect that grants Aura Health Regen to allies. [gamefile:items/item_headdress#cost] [gamefile:items/item_headdress#attribs] [loc:DOTA_Tooltip_ability_item_headdress_Description]

## Stats

| Stat | Value |
|---|---:|
| Cost | 425 gold |
[gamefile:items/item_headdress#cost]

| Stat | Value |
|---|---:|
| Aura Health Regen | 2.0 |
| Aura Radius | 1200 |
| Health Regeneration | 0.5 |
[gamefile:items/item_headdress#attribs] [loc:DOTA_Tooltip_ability_item_headdress_Description]

| Property | Value |
|---|---:|
| Behavior | Passive |
| Cast range | 1200 |
[gamefile:items/item_headdress#mechanics]

Regeneration Aura grants health regeneration to allies. [loc:DOTA_Tooltip_ability_item_headdress_Description]

## Components

| Component | Gold cost |
|---|---:|
| Ring of Regen | 175 gold |
| Recipe | 250 gold |
[gamefile:items/item_headdress#components]

**Builds into:** Drum of Endurance — 1625 gold; Mekansm — 1775 gold. [gamefile:items/item_headdress#components]

*Creates a soothing aura that restores allies in battle.* [loc:DOTA_Tooltip_ability_item_headdress_Lore]