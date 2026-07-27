---
title: Arcane Boots
kind: item
patch: 7.41d
card:
  entity: arcane_boots
  sentences:
  - text: Arcane Boots is a rare 1500-gold item that grants 125 mana, 45 movement
      speed, and 0.25 mana regeneration; its 1200-radius Basilius Aura grants allies
      1 mana regeneration, while Replenish restores 150 mana to nearby allies within
      a 1200 radius.
    marks:
    - gamefile:items/item_arcane_boots#cost
    - gamefile:items/item_arcane_boots#attribs
    - loc:DOTA_Tooltip_ability_item_arcane_boots_Description
  - text: Its build formula is Boots of Speed (500 gold), Ring of Basilius (425 gold),
      Wizard Hat (250 gold), and a 325-gold recipe; it builds into Guardian Greaves.
    marks:
    - gamefile:items/item_arcane_boots#components
  - text: Replenish is an immediate, no-target active with 0 mana cost and a 55.0-second
      cooldown.
    marks:
    - gamefile:items/item_arcane_boots#mechanics
  - text: Movement speed bonuses from multiple pairs of boots do not stack.
    marks:
    - loc:DOTA_Tooltip_ability_item_arcane_boots_Description
---

# Arcane Boots

Arcane Boots is a rare item with Mana, Movement Speed, Mana Regeneration, the Basilius Aura passive, and the Replenish active. [gamefile:items/item_arcane_boots#cost] [gamefile:items/item_arcane_boots#attribs] [loc:DOTA_Tooltip_ability_item_arcane_boots_Description]

## Cost

| Stat | Value |
|---|---:|
| Cost | 1500 gold |

[gamefile:items/item_arcane_boots#cost]

## Components

| Formula | Cost |
|---|---:|
| Boots of Speed | 500 gold |
| Ring of Basilius | 425 gold |
| Wizard Hat | 250 gold |
| Recipe | 325 gold |
| **Builds into: Guardian Greaves** | **4450 gold** |

[gamefile:items/item_arcane_boots#components]

## Stats

| Stat | Value |
|---|---:|
| Aura Mana Regen | 1 |
| Aura Radius | 1200 |
| Mana | 125 |
| Movement Speed | 45 |
| Mana Regeneration | 0.25 |
| Replenish Amount | 150 |
| Replenish Radius | 1200 |

[gamefile:items/item_arcane_boots#attribs]

## Replenish

| Stat | Value |
|---|---|
| Behavior | Immediate, No Target |
| Mana Cost | 0 |
| Cooldown | 55.0 |

[gamefile:items/item_arcane_boots#mechanics]

Replenish restores mana to nearby allies. Basilius Aura passively grants mana regeneration to allies. Movement speed bonuses from multiple pairs of boots do not stack. [loc:DOTA_Tooltip_ability_item_arcane_boots_Description]

*Magi equipped with these boots are valued in battle.* [loc:DOTA_Tooltip_ability_item_arcane_boots_Lore]