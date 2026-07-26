---
title: Ethereal
kind: concept
patch: 7.41d
card:
  entity: ethereal
  sentences:
  - text: Ethereal, or ghost form, is a status effect that disarms a unit while granting
      attack immunity and immunity to all physical damage, and it usually reduces
      magic resistance.
    marks:
    - corpus:liquipedia_dota2/ethereal@2309507
  - text: Magic-resistance reductions from multiple ethereal effects do not stack;
      the higher reduction takes priority.
    marks:
    - corpus:liquipedia_dota2/ethereal@2309507
  - text: Abilities and spell damage can affect ethereal units, but physical damage
      cannot.
    marks:
    - corpus:liquipedia_dota2/ethereal@2309507
  - text: Slithereen Crush still stuns and slows an ethereal unit but cannot damage
      it.
    marks:
    - corpus:liquipedia_dota2/ethereal@2309507
  - text: Entering ethereal form does not dispel anything.
    marks:
    - corpus:liquipedia_dota2/ethereal@2309507
  - text: While a unit is debuff immune, most ethereal effects provide no attack immunity,
      physical-damage immunity, or magic-resistance reduction.
    marks:
    - corpus:liquipedia_dota2/ethereal@2309507
  - text: Some ethereal effects are dispelled by spell immunity.
    marks:
    - corpus:liquipedia_dota2/ethereal@2309507
  - text: Sources include Ether Blast, Ghost Form, Nihilism, Pierce the Veil, Ghost
      Shroud, and Decrepify.
    marks:
    - corpus:liquipedia_dota2/ethereal@2309507#Sources
  - text: Pierce the Veil’s ethereal effect is not prevented by debuff immunity.
    marks:
    - corpus:liquipedia_dota2/ethereal@2309507#Sources
  - text: Ghost Shroud’s ethereal effect is dispelled by spell immunity.
    marks:
    - corpus:liquipedia_dota2/ethereal@2309507#Sources
---

# Ethereal

## Overview

Ethereal, sometimes called **ghost form**, is a status effect that grants attack immunity and immunity to all physical damage while disarming the affected unit. It usually—but not always—reduces magic resistance, causing additional magical damage to be taken. Every other aspect of the unit remains controllable. [corpus:liquipedia_dota2/ethereal@2309507]

Magic-resistance reductions from multiple ethereal effects do not stack; the higher value takes priority:

`Ethereal Magic Resistance Reduction = (1 + MAX Ethereal Magic Resistance Reduction)` [corpus:liquipedia_dota2/ethereal@2309507]

Ethereal units can be affected by abilities or spell damage, but physical damage does not apply. **Slithereen Crush**, for example, cannot damage an ethereal unit but still stuns and slows it. Entering ethereal form does not dispel anything. [corpus:liquipedia_dota2/ethereal@2309507]

Most ethereal effects do not stack with debuff immunity. While debuff immune, an affected unit loses the attack immunity and physical-damage immunity and receives no magic-resistance reduction. Some ethereal effects do not stack with spell immunity and are consequently dispelled by it. [corpus:liquipedia_dota2/ethereal@2309507]

## Definition

| Modifier |
|---|
| `MODIFIER_STATE_DISARMED` [corpus:liquipedia_dota2/ethereal@2309507#Definition] |
| `MODIFIER_STATE_ATTACK_IMMUNE` [corpus:liquipedia_dota2/ethereal@2309507#Definition] |
| `MODIFIER_PROPERTY_MAGICAL_RESISTANCE_DECREPIFY_UNIQUE` [corpus:liquipedia_dota2/ethereal@2309507#Definition] |

| Mechanic | Definition | Example |
|---|---|---|
| Ethereal | Grants attack immunity and self-disarms. Grants immunity to all physical damage but usually, though not always, reduces the unit’s own magic resistance. | Decrepify [corpus:liquipedia_dota2/ethereal@2309507#Definition] |
| Non-targetable | Does not includes Hide sources. Grants attack immunity and Phased. The unit is not selectable, loses its Selection Box, and cannot be targeted by allies or enemies. | Hitch A Ride [corpus:liquipedia_dota2/ethereal@2309507#Definition] |
| Misc Non-targetable | The unit can remain selectable and retain its Selection Box, but cannot be targeted by allies or enemies. | Smoke Screen [corpus:liquipedia_dota2/ethereal@2309507#Definition] |

## Sources

| Ethereal source |
|---|
| Ethereal Blade – Ether Blast [corpus:liquipedia_dota2/ethereal@2309507#Sources] |
| Ghost Scepter – Ghost Form [corpus:liquipedia_dota2/ethereal@2309507#Sources] |
| Leshrac – Nihilism [corpus:liquipedia_dota2/ethereal@2309507#Sources] |
| Muerta – Pierce the Veil¹ [corpus:liquipedia_dota2/ethereal@2309507#Sources] |
| Necrophos – Ghost Shroud² [corpus:liquipedia_dota2/ethereal@2309507#Sources] |
| Pugna – Decrepify [corpus:liquipedia_dota2/ethereal@2309507#Sources] |

¹ Pierce the Veil’s ethereal effect is not prevented by debuff immunity. [corpus:liquipedia_dota2/ethereal@2309507#Sources]

² Ghost Shroud etehereal effect is dispelled by spell immunity. [corpus:liquipedia_dota2/ethereal@2309507#Sources]

## Gallery

Ghost Scepter’s Ghost Form. [corpus:liquipedia_dota2/ethereal@2309507#Gallery]

## Version History

| Version | Date | Type | Description |
|---|---|---|---|
| 7.39e | (2025-10-02) |  | Ethereal effects are now disabled while the affected unit is debuff immune. [corpus:liquipedia_dota2/ethereal@2309507#Version_History] |
| 7.33 | (2023-04-20) | U | Ethereal effects now fully stack with Debuff Immunity. [corpus:liquipedia_dota2/ethereal@2309507#Version_History] |
| 7.32e | (2023-03-07) | ADDED | new Pierce the Veil ability that uses the Ethereal mechanic. [corpus:liquipedia_dota2/ethereal@2309507#Version_History] |
| 7.28 | (2020-12-17) | ADDED | new Nihilism ability that uses the Ethereal mechanic. [corpus:liquipedia_dota2/ethereal@2309507#Version_History] |
| 7.00 | (2016-12-12) | ADDED | new Ghost Shroud ability that uses the Ethereal mechanic. [corpus:liquipedia_dota2/ethereal@2309507#Version_History] |
| 6.87 | (2016-04-25) |  | Units affected by Duel no longer ignore disarms and ethereal state.<br>Ethereal now blocks in-flight attack projectiles fully, rather than just ones launched before entering Ethereal form. [corpus:liquipedia_dota2/ethereal@2309507#Version_History] |
| 6.84 | (2015-04-30) |  | Turning Ethereal no longer removes Ensnare and various other root debuffs.<br>Channeling a Town Portal Scroll no longer removes ethereal sources prematurely. [corpus:liquipedia_dota2/ethereal@2309507#Version_History] |
| 6.79c | (2013-12-12) |  | Units affected by Duel now fully ignore disarms and ethereal state. [corpus:liquipedia_dota2/ethereal@2309507#Version_History] |
| 6.79 | (2013-10-21) |  | Can no longer orb-attack while attack restricted (such as Ethereal or under Frostbite). [corpus:liquipedia_dota2/ethereal@2309507#Version_History] |
| 6.72d | (2011-07-22) |  | Fixed the following abilities’ interactions with ethereal sources. [corpus:liquipedia_dota2/ethereal@2309507#Version_History] |
| 6.67 | (2026-07-24) | CREATED | Ethereal Blade. [corpus:liquipedia_dota2/ethereal@2309507#Version_History] |
| 6.60 | (2026-07-24) | CREATED | Ghost Scepter. [corpus:liquipedia_dota2/ethereal@2309507#Version_History] |
| 5.62 | (2026-07-24) | ADDED | the Ethereal mechanic.<br>Decrepify is an ability that uses the Ethereal mechanic. [corpus:liquipedia_dota2/ethereal@2309507#Version_History] |

### Abilities fixed in 6.72d

| Ability |
|---|
| Culling Blade [corpus:liquipedia_dota2/ethereal@2309507#Version_History] |
| Ice Blast [corpus:liquipedia_dota2/ethereal@2309507#Version_History] |

## Patch History

| Patch | Description |
|---|---|
| 04 Feb 2011 | Fixed cases where units under Ethereal form could still take physical damage. [corpus:liquipedia_dota2/ethereal@2309507#Patch_History] |