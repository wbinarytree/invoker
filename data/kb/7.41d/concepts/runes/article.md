---
title: Runes
kind: concept
patch: 7.41d
card:
  entity: runes
  sentences:
  - text: Runes are special map power-ups spawning at designated locations and ignoring
      Impassable Terrain and Pathing Blockers; activation within 150 instantly grants
      their effect, while Power Runes begin at 6:00 and recur every 2:00.
    marks:
    - corpus:liquipedia_dota2/runes@2401387
    - corpus:liquipedia_dota2/runes@2401387#Activate
  - text: A Bottle stores a picked-up Rune; if already occupied, the new Rune activates
      immediately, while the stored Rune activates after 90 seconds.
    marks:
    - corpus:liquipedia_dota2/runes@2401387#Activate
  - text: Power Runes do not repeat within a cycle, and a cycle’s first Rune cannot
      match the previous cycle’s last.
    marks:
    - corpus:liquipedia_dota2/runes@2401387#Activate
  - text: Amplify Damage grants 80% bonus attack damage and 15% spell-damage amplification
      for 45.
    marks:
    - corpus:liquipedia_dota2/runes@2401387#Amplify_Damage
  - text: Arcane provides 25% cooldown reduction and 30% mana-loss reduction for 50.
    marks:
    - corpus:liquipedia_dota2/runes@2401387#Arcane
  - text: Haste sets movement speed to 550 and prevents slowing below that value for
      22.
    marks:
    - corpus:liquipedia_dota2/runes@2401387#Haste
  - text: Illusion creates 2 illusions dealing 35% damage for 75, with a split time
      of 0.1.
    marks:
    - corpus:liquipedia_dota2/runes@2401387#Illusion
  - text: Invisibility has a fade time of 2 and duration of 45, breaking at an attack
      point or ability cast point.
    marks:
    - corpus:liquipedia_dota2/runes@2401387#Invisibility
  - text: Regeneration restores 6% of max health and mana per second for 30; player-based
      damage above 0 reduces both rates to 1% for 3.
    marks:
    - corpus:liquipedia_dota2/runes@2401387#Regeneration
  - text: Shield grants an all-damage barrier with a max-health factor of 0.5 for
      75.
    marks:
    - corpus:liquipedia_dota2/runes@2401387#Shield
  - text: Bounty grants reliable team gold with base value 40, an increase of 6 per
      instance every 300, and Turbo Mode multiplier 2.
    marks:
    - corpus:liquipedia_dota2/runes@2401387#Bounty
  - text: Water heals 40, restores 80 mana, and spawns at both river Power Rune spots
      at 2:00 and 4:00.
    marks:
    - corpus:liquipedia_dota2/runes@2401387#Water
---

# Runes

## Overview

Runes are special power-ups that spawn at designated locations on the game map. They ignore Impassable Terrain and Pathing Blockers. [corpus:liquipedia_dota2/runes@2401387]

For runes that come with cosmetic items, see Inscribed Gem. [corpus:liquipedia_dota2/runes@2401387]

## Types

| Rune type | Bonus | Rune |
|---|---|---|
| River Power Runes | Grants a buff and/or various ability effects for a short period. | Amplify Damage Rune [corpus:liquipedia_dota2/runes@2401387#Definition] |
| River Power Runes | Grants a buff and/or various ability effects for a short period. | Arcane Rune [corpus:liquipedia_dota2/runes@2401387#Definition] |
| River Power Runes | Grants a buff and/or various ability effects for a short period. | Haste Rune [corpus:liquipedia_dota2/runes@2401387#Definition] |
| River Power Runes | Grants a buff and/or various ability effects for a short period. | Illusion Rune [corpus:liquipedia_dota2/runes@2401387#Definition] |
| River Power Runes | Grants a buff and/or various ability effects for a short period. | Invisibility Rune [corpus:liquipedia_dota2/runes@2401387#Definition] |
| River Power Runes | Grants a buff and/or various ability effects for a short period. | Regeneration Rune [corpus:liquipedia_dota2/runes@2401387#Definition] |
| River Power Runes | Grants a buff and/or various ability effects for a short period. | Shield Rune [corpus:liquipedia_dota2/runes@2401387#Definition] |
| Other Runes | Grants an instance of certain bonus resources upon activation. | Bounty Rune [corpus:liquipedia_dota2/runes@2401387#Definition] |
| Other Runes | Grants an instance of certain bonus resources upon activation. | Water Rune [corpus:liquipedia_dota2/runes@2401387#Definition] |

## Activation and spawning

Activate instantly redeems the corresponding Rune’s temporary power-up. The hero does not need to face the Rune. [corpus:liquipedia_dota2/runes@2401387#Activate]

| Field | Value |
|---|---:|
| Ability | Passive [corpus:liquipedia_dota2/runes@2401387#Activate] |
| Affects | Self [corpus:liquipedia_dota2/runes@2401387#Activate] |
| Cast Animation | 0 + 0 [corpus:liquipedia_dota2/runes@2401387#Activate] |
| Activate Distance | 150 [corpus:liquipedia_dota2/runes@2401387#Activate] |
| 1st Spawn Interval | 360 [corpus:liquipedia_dota2/runes@2401387#Activate] |
| Subsequent Spawn Interval | 120 [corpus:liquipedia_dota2/runes@2401387#Activate] |

Only the following units can activate a Rune: [corpus:liquipedia_dota2/runes@2401387#Activate]

| Activator |
|---|
| Heroes [corpus:liquipedia_dota2/runes@2401387#Activate] |
| Clones [corpus:liquipedia_dota2/runes@2401387#Activate] |
| Spirit Bear [corpus:liquipedia_dota2/runes@2401387#Activate] |

Heroes carrying a Bottle automatically store a picked-up Rune. If the Bottle already contains a Rune, the second Rune activates immediately without replacing the stored Rune. A Stored Rune cannot be dropped or gifted and automatically activates after 90 seconds. [corpus:liquipedia_dota2/runes@2401387#Activate]

The following are treated as River Power Runes: [corpus:liquipedia_dota2/runes@2401387#Activate]

| River Power Rune |
|---|
| Amplify Damage Rune [corpus:liquipedia_dota2/runes@2401387#Activate] |
| Arcane Rune [corpus:liquipedia_dota2/runes@2401387#Activate] |
| Haste Rune [corpus:liquipedia_dota2/runes@2401387#Activate] |
| Illusion Rune [corpus:liquipedia_dota2/runes@2401387#Activate] |
| Invisibility Rune [corpus:liquipedia_dota2/runes@2401387#Activate] |
| Regeneration Rune [corpus:liquipedia_dota2/runes@2401387#Activate] |
| Shield Rune [corpus:liquipedia_dota2/runes@2401387#Activate] |

Power Runes do not spawn at game start. The first Power Rune spawns at 6:00 at a dedicated river Rune spot; subsequent Power Runes spawn every 2:00. A Power Rune spawns at one random river Rune spot and disappears if it remains unactivated when the next spawn time arrives. [corpus:liquipedia_dota2/runes@2401387#Activate]

The first Rune granted in a new cycle cannot match the final Rune of the previous cycle. A Rune never repeats within a cycle and cannot spawn again until every other Power Rune has spawned. [corpus:liquipedia_dota2/runes@2401387#Activate]

Within Fog of War, a Rune icon appears on the minimap and remains until its river Rune spot is confirmed empty. Runes are visible within the faction’s vision radius and are always visible in spectator mode. [corpus:liquipedia_dota2/runes@2401387#Activate]

Runes have higher selection-box priority than most units, but only for orders that can target Runes. They can be destroyed with an `A` attack command; doing so is neither a last hit nor a deny. [corpus:liquipedia_dota2/runes@2401387#Activate]

Runes otherwise do not interact with abilities except through these sources: [corpus:liquipedia_dota2/runes@2401387#Activate]

| Interaction | Source |
|---|---|
| Can activate a Rune | Magnetic Field [corpus:liquipedia_dota2/runes@2401387#Activate] |
| Can transform into a Rune | Mischief [corpus:liquipedia_dota2/runes@2401387#Activate] |
| Store Rune | Store Rune [corpus:liquipedia_dota2/runes@2401387#Activate] |
| Can pull a Rune | Catchy Lick [corpus:liquipedia_dota2/runes@2401387#Activate] |
| Can pull a Rune | Meat Hook [corpus:liquipedia_dota2/runes@2401387#Activate] |
| Can target a Rune | Fetch [corpus:liquipedia_dota2/runes@2401387#Activate] |
| Can target a Rune | Toss [corpus:liquipedia_dota2/runes@2401387#Activate] |

Runes can be traced to the earliest Allstars rendition, where they are considered items, with that statement qualified as “if true.” [corpus:liquipedia_dota2/runes@2401387#Activate]

## River Power Runes

### Amplify Damage

Amplify Damage grants bonus attack damage and outgoing spell-damage amplification to the activating hero. [corpus:liquipedia_dota2/runes@2401387#Amplify_Damage]

| Field | Value |
|---|---:|
| Ability | No [corpus:liquipedia_dota2/runes@2401387#Amplify_Damage] |
| Affects | Self [corpus:liquipedia_dota2/runes@2401387#Amplify_Damage] |
| Cast Animation | 0 + 0 [corpus:liquipedia_dota2/runes@2401387#Amplify_Damage] |
| Attack Damage Bonus | 80% [corpus:liquipedia_dota2/runes@2401387#Amplify_Damage] |
| Spell Damage Amp | 15% [corpus:liquipedia_dota2/runes@2401387#Amplify_Damage] |
| Duration | 45 [corpus:liquipedia_dota2/runes@2401387#Amplify_Damage] |

Each stack grants flat bonus attack damage based on the hero’s current main attack damage. The value is checked periodically and updated immediately. It also grants generic outgoing spell-damage amplification affecting spell damage sourced to the hero; this stacks additively with other generic outgoing damage sources and does not affect HP Removal sources. Reapplying the buff refreshes its duration. [corpus:liquipedia_dota2/runes@2401387#Amplify_Damage]

| Status or affected unit |
|---|
| Amplify Damage Rune [corpus:liquipedia_dota2/runes@2401387#Amplify_Damage] |
| Stored Rune — Bottle’s Stored Rune state [corpus:liquipedia_dota2/runes@2401387#Amplify_Damage] |
| Hidden units [corpus:liquipedia_dota2/runes@2401387#Amplify_Damage] |
| Invulnerable units [corpus:liquipedia_dota2/runes@2401387#Amplify_Damage] |

| Modifier data |
|---|
| `modifier_rune_doubledamage` [corpus:liquipedia_dota2/runes@2401387#Amplify_Damage] |
| `Double Damage: Base damage increased by x%` [corpus:liquipedia_dota2/runes@2401387#Amplify_Damage] |

### Arcane

Arcane applies mana-cost and cooldown reduction to abilities and item abilities. [corpus:liquipedia_dota2/runes@2401387#Arcane]

| Field | Value |
|---|---:|
| Ability | No [corpus:liquipedia_dota2/runes@2401387#Arcane] |
| Affects | Self [corpus:liquipedia_dota2/runes@2401387#Arcane] |
| Cast Animation | 0 + 0 [corpus:liquipedia_dota2/runes@2401387#Arcane] |
| Cooldown Reduction | 25% [corpus:liquipedia_dota2/runes@2401387#Arcane] |
| Mana Loss Reduction | 30% [corpus:liquipedia_dota2/runes@2401387#Arcane] |
| Duration | 50 [corpus:liquipedia_dota2/runes@2401387#Arcane] |

The Rune grants these ability effects: [corpus:liquipedia_dota2/runes@2401387#Arcane]

| Effect |
|---|
| Percentage-based mana-cost reduction [corpus:liquipedia_dota2/runes@2401387#Arcane] |
| Percentage-based max and current mana loss [corpus:liquipedia_dota2/runes@2401387#Arcane] |
| Percentage-based cooldown reduction [corpus:liquipedia_dota2/runes@2401387#Arcane] |

These effects stack multiplicatively with other sources of the same mechanic type, after flat reduction sources. Reapplying the buff refreshes its duration. [corpus:liquipedia_dota2/runes@2401387#Arcane]

| Status or affected unit |
|---|
| Arcane Rune [corpus:liquipedia_dota2/runes@2401387#Arcane] |
| Stored Rune — Bottle’s Stored Rune state [corpus:liquipedia_dota2/runes@2401387#Arcane] |
| Hidden units [corpus:liquipedia_dota2/runes@2401387#Arcane] |
| Invulnerable units [corpus:liquipedia_dota2/runes@2401387#Arcane] |

| Modifier data |
|---|
| `modifier_rune_arcane` [corpus:liquipedia_dota2/runes@2401387#Arcane] |
| `Arcane: Reduces cooldowns by 30% and manacosts by 30%` [corpus:liquipedia_dota2/runes@2401387#Arcane] |
| `MODIFIER_PROPERTY_COOLDOWN_PERCENTAGE` [corpus:liquipedia_dota2/runes@2401387#Arcane] |
| `MODIFIER_PROPERTY_MANACOST_PERCENTAGE_STACKING` [corpus:liquipedia_dota2/runes@2401387#Arcane] |
| `MODIFIER_PROPERTY_UNIT_STATS_NEED_REFRESH` [corpus:liquipedia_dota2/runes@2401387#Arcane] |

### Haste

Haste grants haste movement and prevents the activating hero from being slowed below the haste value. It grants haste movement rather than other movement effects. [corpus:liquipedia_dota2/runes@2401387#Haste]

| Field | Value |
|---|---:|
| Ability | No [corpus:liquipedia_dota2/runes@2401387#Haste] |
| Affects | Self [corpus:liquipedia_dota2/runes@2401387#Haste] |
| Cast Animation | 0 + 0 [corpus:liquipedia_dota2/runes@2401387#Haste] |
| Haste Speed | 550 [corpus:liquipedia_dota2/runes@2401387#Haste] |
| Duration | 22 [corpus:liquipedia_dota2/runes@2401387#Haste] |

Reapplying the buff refreshes its duration. [corpus:liquipedia_dota2/runes@2401387#Haste]

| Status or affected unit |
|---|
| Haste Rune [corpus:liquipedia_dota2/runes@2401387#Haste] |
| Stored Rune — Bottle’s Stored Rune state [corpus:liquipedia_dota2/runes@2401387#Haste] |
| Hidden units [corpus:liquipedia_dota2/runes@2401387#Haste] |
| Invulnerable units [corpus:liquipedia_dota2/runes@2401387#Haste] |

| Modifier data |
|---|
| `modifier_rune_haste` [corpus:liquipedia_dota2/runes@2401387#Haste] |
| `Rune Haste: Movement speed increased to maximum.` [corpus:liquipedia_dota2/runes@2401387#Haste] |

### Illusion

Illusion creates multiple images of the activating hero under its own control. [corpus:liquipedia_dota2/runes@2401387#Illusion]

| Field | Value |
|---|---:|
| Ability | No [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| Affects | Self [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| Cast Animation | 0 + 0 [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| Split Time | 0.1 [corpus:liquipedia_dota2/runes@2401387#Illusion] |

Activation grants ground vision centered on the activation location. [corpus:liquipedia_dota2/runes@2401387#Illusion]

| Vision field | Value |
|---|---:|
| Vision Radius | 1000 [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| Duration | 0.1 [corpus:liquipedia_dota2/runes@2401387#Illusion] |

The images are illusions that deal a portion of the corresponding hero’s damage and receive additional incoming damage. [corpus:liquipedia_dota2/runes@2401387#Illusion]

| Illusion field | Value |
|---|---:|
| Number of Illusions | 2 [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| Damage Dealt | 35% [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| Damage Taken | 200% [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| Damage Taken | 300% [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| Duration | 75 [corpus:liquipedia_dota2/runes@2401387#Illusion] |

The illusion texture is distinguishable to allies only. [corpus:liquipedia_dota2/runes@2401387#Illusion]

On cast, the effect: [corpus:liquipedia_dota2/runes@2401387#Illusion]

| Cast behavior |
|---|
| Disjoints incoming projectiles [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| Creates the illusions with `modifier_invulnerable` [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| Determines which position in the illusion formation the wielder will reappear at [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| Applies the split-time `rune_illusion` effect to the caster [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| Makes the caster Hidden, Invulnerable, Stunned, and Unselectable during the split [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| Makes the caster reappear first, with its current health bar visible, at a random position in the fixed illusion formation [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| Issues the caster a stop command, cancelling all queued orders, including orders for other player-controlled units [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| Applies a basic dispel to the wielder [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| Makes the illusions reappear without health bars, facing the same direction as the caster and positioned according to the cast position and number of illusions [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| With 2 illusions: `or or or` [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| Plays the hero spawn animation on the created illusions [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| Grants illusion particle effects according to the hero model, followed by the health bars [corpus:liquipedia_dota2/runes@2401387#Illusion] |

Reactivating the Rune instantly kills and replaces every illusion from the current instance at the current ability level, regardless of who controls the illusions. [corpus:liquipedia_dota2/runes@2401387#Illusion]

| Expression | Value |
|---|---|
| Illusion Bounty | `2 × IllusionLVL` [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| Illusion Spawn Distance | `CasterColSize × (NumberOfIllusions + 2)` [corpus:liquipedia_dota2/runes@2401387#Illusion] |

| Status entry |
|---|
| Illusion Rune [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| Stored Rune — Bottle’s Stored Rune state [corpus:liquipedia_dota2/runes@2401387#Illusion] |

| Modifier | Property or state |
|---|---|
| `modifier_rune_illusion` | Hidden Modifier [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| `modifier_rune_illusion` | `MODIFIER_STATE_STUNED` [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| `modifier_rune_illusion` | `MODIFIER_STATE_INVULNERABLE` [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| `modifier_rune_illusion` | `MODIFIER_STATE_UNSELECTABLE` [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| `modifier_rune_illusion` | `MODIFIER_STATE_NO_HEALTH_BAR` [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| `modifier_rune_illusion` | `MODIFIER_STATE_OUT_OF_GAME` [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| `modifier_invulnerable (Illusion)` | Hidden Modifier [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| `modifier_invulnerable (Illusion)` | `MODIFIER_STATE_INVULNERABLE` [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| `modifier_invulnerable (Illusion)` | `MODIFIER_STATE_NO_HEALTH_BAR` [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| `modifier_illusion` | Illusion [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| `modifier_illusion` | `MODIFIER_PROPERTY_DAMAGEOUTGOING_PERCENTAGE_ILLUSION` [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| `modifier_illusion` | `MODIFIER_PROPERTY_IS_ILLUSION` [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| `modifier_illusion` | `MODIFIER_PROPERTY_ILLUSION_LABEL` [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| `modifier_illusion` | `MODIFIER_EVENT_ON_DEATH` [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| `modifier_illusion` | `MODIFIER_PROPERTY_LIFETIME_FRACTION` [corpus:liquipedia_dota2/runes@2401387#Illusion] |
| `modifier_illusion` | `MODIFIER_PROPERTY_INCOMING_DAMAGE_ILLUSION` [corpus:liquipedia_dota2/runes@2401387#Illusion] |

### Invisibility

Invisibility grants invisibility to the activating hero. [corpus:liquipedia_dota2/runes@2401387#Invisibility]

| Field | Value |
|---|---:|
| Ability | No [corpus:liquipedia_dota2/runes@2401387#Invisibility] |
| Affects | Self [corpus:liquipedia_dota2/runes@2401387#Invisibility] |
| Cast Animation | 0 + 0 [corpus:liquipedia_dota2/runes@2401387#Invisibility] |
| Fade Time | 2 [corpus:liquipedia_dota2/runes@2401387#Invisibility] |
| Duration | 45 [corpus:liquipedia_dota2/runes@2401387#Invisibility] |

During the fade time, the affected unit can still attack and cast abilities. The Rune does not grant phase movement. Invisibility breaks at an attack’s attack point or an ability’s cast point. Reapplying the buff refreshes its duration. [corpus:liquipedia_dota2/runes@2401387#Invisibility]

| Status or affected unit |
|---|
| Invisibility Rune [corpus:liquipedia_dota2/runes@2401387#Invisibility] |
| Stored Rune — Bottle’s Stored Rune state [corpus:liquipedia_dota2/runes@2401387#Invisibility] |
| Hidden units [corpus:liquipedia_dota2/runes@2401387#Invisibility] |
| Invulnerable units [corpus:liquipedia_dota2/runes@2401387#Invisibility] |

| Modifier data |
|---|
| `modifier_rune_invis` [corpus:liquipedia_dota2/runes@2401387#Invisibility] |
| `Invisible: Attacking removes invisibility.` [corpus:liquipedia_dota2/runes@2401387#Invisibility] |

### Regeneration

Regeneration grants max-health and max-mana regeneration when activated. [corpus:liquipedia_dota2/runes@2401387#Regeneration]

| Field | Value |
|---|---:|
| Ability | No [corpus:liquipedia_dota2/runes@2401387#Regeneration] |
| Affects | Self [corpus:liquipedia_dota2/runes@2401387#Regeneration] |
| Cast Animation | 0 + 0 [corpus:liquipedia_dota2/runes@2401387#Regeneration] |
| Max Health to Health Regen per Second | 6% [corpus:liquipedia_dota2/runes@2401387#Regeneration] |
| Max Mana to Mana Regen per Second | 6% [corpus:liquipedia_dota2/runes@2401387#Regeneration] |
| Duration | 30 [corpus:liquipedia_dota2/runes@2401387#Regeneration] |

Player-based damage greater than 0 after all reductions lowers the regeneration values for a set duration: [corpus:liquipedia_dota2/runes@2401387#Regeneration]

| Reduced field | Value |
|---|---:|
| Max Health to Health Regen per Second | 1% [corpus:liquipedia_dota2/runes@2401387#Regeneration] |
| Max Mana to Mana Regen per Second | 1% [corpus:liquipedia_dota2/runes@2401387#Regeneration] |
| Downtime | 3 [corpus:liquipedia_dota2/runes@2401387#Regeneration] |

A player-based damage instance applies the fixed downtime regardless of faction, and cooldown-reset sources cannot reset it. The player-based item downtime does not proc from these sources: [corpus:liquipedia_dota2/runes@2401387#Regeneration]

| Excluded source |
|---|
| Self-damage sources [corpus:liquipedia_dota2/runes@2401387#Regeneration] |
| HP Removal sources [corpus:liquipedia_dota2/runes@2401387#Regeneration] |

The effect dispels after replenishing 100% max health and max mana. Reapplying it creates another independent instance. [corpus:liquipedia_dota2/runes@2401387#Regeneration]

| Status or affected unit |
|---|
| Regeneration Rune [corpus:liquipedia_dota2/runes@2401387#Regeneration] |
| Stored Rune — Bottle’s Stored Rune state [corpus:liquipedia_dota2/runes@2401387#Regeneration] |
| Hidden units [corpus:liquipedia_dota2/runes@2401387#Regeneration] |
| Invulnerable units [corpus:liquipedia_dota2/runes@2401387#Regeneration] |

| Modifier data |
|---|
| `modifier_rune_regen` [corpus:liquipedia_dota2/runes@2401387#Regeneration] |
| `Rune Regeneration: Regenerating x HP and x mana per second.` [corpus:liquipedia_dota2/runes@2401387#Regeneration] |

### Shield

Shield grants the activating hero an all-damage barrier based on max health. [corpus:liquipedia_dota2/runes@2401387#Shield]

| Field | Value |
|---|---:|
| Ability | No [corpus:liquipedia_dota2/runes@2401387#Shield] |
| Affects | Self [corpus:liquipedia_dota2/runes@2401387#Shield] |
| Cast Animation | 0 + 0 [corpus:liquipedia_dota2/runes@2401387#Shield] |
| Max Health to Barrier Factor | 0.5 [corpus:liquipedia_dota2/runes@2401387#Shield] |
| Duration | 75 [corpus:liquipedia_dota2/runes@2401387#Shield] |

Reapplying the buff refreshes its duration but does not refresh the damage-barrier values. [corpus:liquipedia_dota2/runes@2401387#Shield]

The barrier absorbs damage instances after reductions. On-damage effects do not proc until the barrier is depleted. It stacks additively with barriers of the same damage type and independently with barriers of other damage types. When a higher-priority damage-negation source is active, the barrier does not function until that source expires. [corpus:liquipedia_dota2/runes@2401387#Shield]

| Status or affected unit |
|---|
| Shield Rune [corpus:liquipedia_dota2/runes@2401387#Shield] |
| Stored Rune — Bottle’s Stored Rune state [corpus:liquipedia_dota2/runes@2401387#Shield] |
| Hidden units [corpus:liquipedia_dota2/runes@2401387#Shield] |
| Invulnerable units [corpus:liquipedia_dota2/runes@2401387#Shield] |

| Modifier data |
|---|
| `modifier_rune_shield` [corpus:liquipedia_dota2/runes@2401387#Shield] |
| `Shielded: Protected by a barrier equal to x% of Max HP.` [corpus:liquipedia_dota2/runes@2401387#Shield] |
| Damage Barrier Type Priority [corpus:liquipedia_dota2/runes@2401387#Shield] |

## Other Runes

### Bounty

Bounty grants bonus reliable gold whose value is based on the in-game time when the Rune is created. [corpus:liquipedia_dota2/runes@2401387#Bounty]

| Field | Value |
|---|---:|
| Ability | No [corpus:liquipedia_dota2/runes@2401387#Bounty] |
| Affects | Self / Allied Heroes [corpus:liquipedia_dota2/runes@2401387#Bounty] |
| Cast Animation | 0 + 0 [corpus:liquipedia_dota2/runes@2401387#Bounty] |
| Effect Radius | Global [corpus:liquipedia_dota2/runes@2401387#Bounty] |
| Base Team Gold | 40 [corpus:liquipedia_dota2/runes@2401387#Bounty] |
| Gold Bonus Increase per Instance | 6 [corpus:liquipedia_dota2/runes@2401387#Bounty] |
| Increase Interval | 300 [corpus:liquipedia_dota2/runes@2401387#Bounty] |
| Turbo Mode Multiplier | 2 [corpus:liquipedia_dota2/runes@2401387#Bounty] |
| Team Gold Bonus | 40 [corpus:liquipedia_dota2/runes@2401387#Bounty] |
| Spawn Interval | 240 [corpus:liquipedia_dota2/runes@2401387#Bounty] |
| Charge Restore per Other Rune | 2 [corpus:liquipedia_dota2/runes@2401387#Bounty] |

The first pair spawns at the river Power Rune spots and grants a greater reliable-gold bonus. Subsequent Bounty Runes spawn at 4:00 in-game time intervals at dedicated Bounty Rune spots in each faction’s jungle. They are less effective and replenish a Bottle only to a certain extent. [corpus:liquipedia_dota2/runes@2401387#Bounty]

If a Bounty Rune is not activated before the next spawn time, the new Rune appears next to the old one. [corpus:liquipedia_dota2/runes@2401387#Bounty]

Activation grants reliable gold to every hero belonging to the activating faction. The amount granted by a subsequent Bounty Rune to each allied hero is: [corpus:liquipedia_dota2/runes@2401387#Bounty]

| Expression |
|---|
| `40 + 6 × ⌊ (In-Game Time / 5) ⌋` [corpus:liquipedia_dota2/runes@2401387#Bounty] |

A Stored Bounty Rune grants gold according to when the Rune was created, not when it was bottled. It restores 2 Regenerate charges unless the item has < 2 charges. [corpus:liquipedia_dota2/runes@2401387#Bounty]

Activation briefly produces a small golden particle burst visible to everyone and displays ally-only overhead text showing the reliable gold granted. In Turbo Mode, the gold factor applies even though the notification displays the standard granted values. [corpus:liquipedia_dota2/runes@2401387#Bounty]

| Status entry |
|---|
| Bounty Rune [corpus:liquipedia_dota2/runes@2401387#Bounty] |
| Stored Rune — Bottle’s Stored Rune state [corpus:liquipedia_dota2/runes@2401387#Bounty] |

### Water

Water instantly heals and restores mana. [corpus:liquipedia_dota2/runes@2401387#Water]

| Field | Value |
|---|---:|
| Ability | No [corpus:liquipedia_dota2/runes@2401387#Water] |
| Affects | Self [corpus:liquipedia_dota2/runes@2401387#Water] |
| Cast Animation | 0 + 0 [corpus:liquipedia_dota2/runes@2401387#Water] |
| Heal | 40 [corpus:liquipedia_dota2/runes@2401387#Water] |
| Mana Restore | 80 [corpus:liquipedia_dota2/runes@2401387#Water] |
| 1st Spawn Interval | 120 [corpus:liquipedia_dota2/runes@2401387#Water] |
| 2nd Spawn Interval | 240 [corpus:liquipedia_dota2/runes@2401387#Water] |
| Charge Restore per Other Rune | 2 [corpus:liquipedia_dota2/runes@2401387#Water] |

Water Runes spawn at 2:00 and 4:00 at both river Power Rune spots and are no longer created after those intervals. An unactivated Water Rune disappears at the next spawn time. [corpus:liquipedia_dota2/runes@2401387#Water]

Water Runes are less effective and replenish a Bottle only to a certain extent. They restore 2 Regenerate charges unless the item has < 2 charges. [corpus:liquipedia_dota2/runes@2401387#Water]

Using `-spawnrune` to force Rune spawns before 4:00 still causes both Power Rune spots to spawn Water Runes. [corpus:liquipedia_dota2/runes@2401387#Water]

| Status entry |
|---|
| Water Rune [corpus:liquipedia_dota2/runes@2401387#Water] |
| Stored Rune — Bottle’s Stored Rune state [corpus:liquipedia_dota2/runes@2401387#Water] |

## Recent changes

The main changelog article is **Runes/Changelogs**. [corpus:liquipedia_dota2/runes@2401387#Recent_Changes]

| Version | Date | Change |
|---|---|---|
| 7.40 | 2025-12-15 | Bounty Rune now has its gold value set upon creation instead of upon activation. [corpus:liquipedia_dota2/runes@2401387#Recent_Changes] |
| 7.40 | 2025-12-15 | Invisibility Rune no longer grants 25% incoming damage reduction. [corpus:liquipedia_dota2/runes@2401387#Recent_Changes] |
| 7.40 | 2025-12-15 | Haste Rune’s duration no longer increases by 3 seconds per Rune cycle. [corpus:liquipedia_dota2/runes@2401387#Recent_Changes] |
| 7.38 | 2025-02-19 | Removed Wisdom Rune and replaced it with Shrines of Wisdom. [corpus:liquipedia_dota2/runes@2401387#Recent_Changes] |
| 7.38 | 2025-02-19 | Increased Bounty Rune spawn interval from 3 to 4 minutes. [corpus:liquipedia_dota2/runes@2401387#Recent_Changes] |
| 7.38 | 2025-02-19 | Increased Bounty Rune base team gold from 36 to 40. [corpus:liquipedia_dota2/runes@2401387#Recent_Changes] |
| 7.38 | 2025-02-19 | Reduced Bounty Rune gold bonus increase per 5 minutes from 9 to 6. [corpus:liquipedia_dota2/runes@2401387#Recent_Changes] |
| 7.35 | 2023-12-14 | Renamed Double Damage Rune to Amplify Damage Rune. [corpus:liquipedia_dota2/runes@2401387#Recent_Changes] |
| 7.35 | 2023-12-14 | Reduced its attack-damage bonus from 100% to 80% of main attack damage. [corpus:liquipedia_dota2/runes@2401387#Recent_Changes] |
| 7.35 | 2023-12-14 | It now also grants 15% Spell Amplification. [corpus:liquipedia_dota2/runes@2401387#Recent_Changes] |
| 7.35 | 2023-12-14 | Regeneration Rune has its health and mana regeneration reduced to 1% of the user’s max health/mana after taking player-based damage instead of being dispelled. [corpus:liquipedia_dota2/runes@2401387#Recent_Changes] |
| 7.35 | 2023-12-14 | Reduced Arcane Rune cooldown reduction from 30% to 25%. [corpus:liquipedia_dota2/runes@2401387#Recent_Changes] |
| 7.35 | 2023-12-14 | Invisibility Rune now also grants 25% incoming damage reduction, increased by 5% per Rune cycle. [corpus:liquipedia_dota2/runes@2401387#Recent_Changes] |
| 7.35 | 2023-12-14 | Haste Rune’s duration now increases by 3 seconds per Rune cycle. [corpus:liquipedia_dota2/runes@2401387#Recent_Changes] |

## Gallery contents

| Group | Entry |
|---|---|
| Runes in-game | Amplify Damage Rune [corpus:liquipedia_dota2/runes@2401387#Gallery] |
| Runes in-game | Arcane Rune [corpus:liquipedia_dota2/runes@2401387#Gallery] |
| Runes in-game | Bounty Rune [corpus:liquipedia_dota2/runes@2401387#Gallery] |
| Runes in-game | Haste Rune [corpus:liquipedia_dota2/runes@2401387#Gallery] |
| Runes in-game | Illusion Rune [corpus:liquipedia_dota2/runes@2401387#Gallery] |
| Runes in-game | Invisibility Rune [corpus:liquipedia_dota2/runes@2401387#Gallery] |
| Runes in-game | Regeneration Rune [corpus:liquipedia_dota2/runes@2401387#Gallery] |
| Runes in-game | Shield Rune [corpus:liquipedia_dota2/runes@2401387#Gallery] |
| Runes in-game | Water Rune [corpus:liquipedia_dota2/runes@2401387#Gallery] |
| Runes in-game | Wisdom Rune [corpus:liquipedia_dota2/runes@2401387#Gallery] |
| Runes in-game | Old Bounty Rune [corpus:liquipedia_dota2/runes@2401387#Gallery] |
| Rune spots | Top river Power Rune spawn point [corpus:liquipedia_dota2/runes@2401387#Gallery] |
| Rune spots | Bottom river Power Rune spawn point [corpus:liquipedia_dota2/runes@2401387#Gallery] |
| Rune spots | Radiant secondary-jungle Bounty Rune spawn point [corpus:liquipedia_dota2/runes@2401387#Gallery] |
| Rune spots | Dire secondary-jungle Bounty Rune spawn point [corpus:liquipedia_dota2/runes@2401387#Gallery] |
| Rune models | Rune models [corpus:liquipedia_dota2/runes@2401387#Gallery] |
| Other media | Tarot card from the Dark Carnival event, Wheel of Fortune [corpus:liquipedia_dota2/runes@2401387#Gallery] |
| Other media | Regeneration, Bounty, Amplify Damage, and Invisibility Runes depicted on the wheel [corpus:liquipedia_dota2/runes@2401387#Gallery] |