---
title: Radiance
kind: item
patch: 7.41d
card:
  entity: radiance
  sentences:
  - text: Radiance is an epic 4700-gold item granting 55 Damage and 25% Evasion; its
      toggleable Burn deals 60 magical damage per second within 650 radius, or 35
      damage per second when emitted by illusions.
    marks:
    - gamefile:items/item_radiance#cost
    - gamefile:items/item_radiance#attribs
    - loc:DOTA_Tooltip_ability_item_radiance_Description
  - text: Its build formula is Sacred Relic (3400 gold) + Talisman of Evasion (1300
      gold) = Radiance (4700 gold).
    marks:
    - gamefile:items/item_radiance#components
    - gamefile:items/item_radiance#cost
  - text: Burn is a no-target toggle.
    marks:
    - gamefile:items/item_radiance#mechanics
  - text: Burn does not proc other abilities.
    marks:
    - gamefile:items/item_radiance#mechanics
  - text: Burn ignores channeling and invisibility.
    marks:
    - gamefile:items/item_radiance#mechanics
  - text: BLIND PCT is 0.
    marks:
    - gamefile:items/item_radiance#attribs
  - text: ILLUSION MULTIPLIER PCT is 100.
    marks:
    - gamefile:items/item_radiance#attribs
  - text: UPGRADE DAY VISION is 250.
    marks:
    - gamefile:items/item_radiance#attribs
  - text: A divine weapon that causes damage and a bright burning effect that lays
      waste to nearby enemies.
    marks:
    - loc:DOTA_Tooltip_ability_item_radiance_Lore
---

# Radiance

Radiance is an epic item that grants Damage and Evasion and provides the toggleable Burn effect, which deals magical damage per second to enemies with a separate damage rate for illusions. [gamefile:items/item_radiance#cost] [gamefile:items/item_radiance#attribs] [loc:DOTA_Tooltip_ability_item_radiance_Description]

## Components

| Item | Cost |
|---|---:|
| Sacred Relic | 3400 gold |
| Talisman of Evasion | 1300 gold |
| **Radiance** | **4700 gold** |

[gamefile:items/item_radiance#components] [gamefile:items/item_radiance#cost]

## Stats

| Stat | Value |
|---|---:|
| AURA DAMAGE | 60 |
| AURA DAMAGE ILLUSIONS | 35 |
| AURA RADIUS | 650 |
| BLIND PCT | 0 |
| DAMAGE | 55 |
| EVASION | 25% |
| ILLUSION MULTIPLIER PCT | 100 |
| UPGRADE DAY VISION | 250 |

[gamefile:items/item_radiance#attribs]

## Behavior

Burn is a no-target toggle. Its behavior flags specify that it does not proc other abilities and ignores channeling and invisibility. [gamefile:items/item_radiance#mechanics]

When active, Burn affects enemies with magical damage per second; illusions use their separate magical damage value. [loc:DOTA_Tooltip_ability_item_radiance_Description]

*A divine weapon that causes damage and a bright burning effect that lays waste to nearby enemies.* [loc:DOTA_Tooltip_ability_item_radiance_Lore]