---
title: Disable
kind: concept
patch: 7.41d
card:
  entity: disable
  sentences:
  - text: A disable, also called crowd control or CC, is an ability or status effect
      that prevents, impedes, or otherwise inhibits a Hero from acting, and most Heroes
      have access to one.
    marks:
    - corpus:liquipedia_dota2/disable@2360598
  - text: A stun stops the unit’s current order, prevents movement, attacks, ability
      casts, and item use until expiry, and interrupts all channeling abilities.
    marks:
    - corpus:liquipedia_dota2/disable@2360598#Stun
  - text: Stuns generally use three modifier types—Stunned, Bash, and Unique—and same-group
      stuns refresh duration rather than extend it.
    marks:
    - corpus:liquipedia_dota2/disable@2360598#Stun
  - text: Sleep completely disables an affected unit for its entire duration; a sleeper
      is either awakened by damage or invulnerable.
    marks:
    - corpus:liquipedia_dota2/disable@2360598#Sleep
  - text: Cyclone lifts a unit into the air, completely disables it, and makes it
      invulnerable.
    marks:
    - corpus:liquipedia_dota2/disable@2360598#Cyclone
  - text: Slows reduce movement speed by a percentage and/or attack speed by a flat
      value.
    marks:
    - corpus:liquipedia_dota2/disable@2360598#Slow
  - text: Silence fully prevents active ability orders except item casts.
    marks:
    - corpus:liquipedia_dota2/disable@2360598#Ability_and_Item_Disables
  - text: Break fully disables passive abilities but not item passives or Talents,
      with some exceptions.
    marks:
    - corpus:liquipedia_dota2/disable@2360598#Ability_and_Item_Disables
  - text: Mute fully prevents item-cast orders except ability casts.
    marks:
    - corpus:liquipedia_dota2/disable@2360598#Ability_and_Item_Disables
  - text: Hex applies silence, mute, and disarm and sets the target’s movement speed
      to a fixed value.
    marks:
    - corpus:liquipedia_dota2/disable@2360598#Hex
  - text: Forced Movement changes a unit’s position independently of movement speed
      and works while the unit is disabled.
    marks:
    - corpus:liquipedia_dota2/disable@2360598#Forced_Movement
  - text: Root prevents movement and most mobility-ability casts but not turning,
      other ability casts, or use of most items.
    marks:
    - corpus:liquipedia_dota2/disable@2360598#Root
---

# Disable

Disables, also called crowd control or CC, are abilities or status effects that prevent, impede, or otherwise inhibit a Hero from acting. They occur in many varieties, and most Heroes have access to some form of disable. “Disabled” or “fully disabled” can refer specifically to stun. [corpus:liquipedia_dota2/disable@2360598]

## Mechanics Interaction

| Disable | Movement | Attack | Ability Usage | Item Usage | Vulnerable |
|---|---|---|---|---|---|
| Stun | Prevented | Prevented | Prevented 2 | Prevented | 1 |
| Sleep / Cyclone | Prevented | Prevented | Prevented | Prevented | Situational |
| Move Speed Slow | Slowed | - | - | - | 1 |
| Attack Speed Slow | - | Slowed | - | - | 1 |
| Silence | - | - | Prevented | - | 1 |
| Break | - | - | Disables Passives | - | 1 |
| Mute | - | - | - | Prevented | 1 |
| Forced Movement | Forced | Situational | Situational | Situational | 1 |
| Root | Prevented 1 | - | Situational | Situational | 1 |
| Leash | Confined | - | Situational | Situational | 1 |
| Hex | Reduced | Prevented | Prevented | Prevented | 1 |
| Trap | Confined | - | - | - | 1 |
| Taunt | Forced | Forced | Prevented | Prevented | 1 |
| Fear | Forced | Prevented | Prevented | Prevented | 1 |
| Hide | Prevented | Prevented | Prevented | Prevented | 0 |
| Ethereal | Situational | Prevented | - | - | to Abilities |
| Disarm | - | Prevented | - | - | 1 |
| Blind | - | Misses | - | - | 1 |

1 Does not prevent turning.  
2 Certain abilities can still be cast while stunned if stated in their ability notes, e.g. Enrage. [corpus:liquipedia_dota2/disable@2360598#Mechanics_Interaction]

## Stun

Stuns are the most common and most dependable disables. A stunned unit stops its current order and stands still until the effect expires; it cannot move, attack, cast abilities, or use items. Stun also interrupts all channeling abilities, such as using Teleport. Stuns can generally be categorized into three types, each using a different modifier. Stuns in the same group use the same modifier, so they refresh one another’s duration based on when they affect the target rather than extending the stun duration. [corpus:liquipedia_dota2/disable@2360598#Stun]

| Modifier Type | Definition | Example |
|---|---|---|
| Stunned | Do not place their own individual modifiers, but refresh each other. | Magic Missile (Regular Stun)<br>Lightning Bolt (Mini-Stun) |
| Bash | Do not place their own individual modifiers, but refresh each other. | Infernal Blade |
| Unique | Uses a custom modifier, meaning each places its own modifier on its targets. | Shackles |

Certain stun abilities require the caster to channel to stun their targets or apply negative effects to the caster. These abilities mostly use the Unique Modifier. [corpus:liquipedia_dota2/disable@2360598#Stun]

| Unique Modifier examples |
|---|
| Black Hole |
| Fiend's Grip |

[corpus:liquipedia_dota2/disable@2360598#Stun]

### Sleep

Sleep is a rare status effect that completely disables affected units for its entire duration. A sleeping unit can either be awakened by taking damage or is invulnerable. [corpus:liquipedia_dota2/disable@2360598#Sleep]

| Source | Invulnerability |
|---|---|
| Nightmare | Provides invulnerability |
| Echo Stomp | Does not provide invulnerability |

[corpus:liquipedia_dota2/disable@2360598#Sleep]

### Cyclone

Cyclone lifts affected units into the air, completely disabling them while rendering them invulnerable. Some Cyclone sources also apply a basic dispel. Other units can pass beneath a lifted unit. [corpus:liquipedia_dota2/disable@2360598#Cyclone]

| Cyclone sources |
|---|
| Tornado |
| Eul's Scepter of Divinity |

[corpus:liquipedia_dota2/disable@2360598#Cyclone]

## Slow

Slows reduce an affected unit’s movement speed by a percentage and/or its attack speed by a flat value of its current speeds. Slows from different sources generally stack, while multiple applications of the same instance instead refresh its duration, with some exceptions. [corpus:liquipedia_dota2/disable@2360598#Slow]

| Slow | Disabled Aspect / Definition | Examples |
|---|---|---|
| Move Speed Slows | Reduce a unit's movement speed by a percentage of its speed.<br><br>Currently, there are no sources of movement speed slow which reduce a unit's movement speed by a fixed value. A unit affected by a haste is immune to movement speed slowing effects. | Thunder Clap |
| Attack Speed Slows | Reduce a unit's attack speed by a fixed value and stacks additively.<br><br>Currently, there are no sources of attack speed slow which reduce a unit's attack speed by a percentage value. There is no effect which grants a unit immunity to attack speed slows either. | Liquid Fire |

[corpus:liquipedia_dota2/disable@2360598#Slow]

## Ability and Item Disables

| Disable | Disabled Aspect / Definition | Examples |
|---|---|---|
| Silence | Fully prevents active ability orders, except item casts.<br><br>Autocast abilities currently set to Autocast have their functionality disabled.<br><br>Toggled abilities remain in their current On / Off state for the duration, but their functionality is not disabled. | Global Silence |
| Break | Fully disables passive abilities but does not disable item passives or Talents, with some exceptions.<br><br>On-death passives, e.g. Reincarnation, and direct-synergy passives, e.g. Caustic Finale with Burrowstrike, are generally not disabled. | Viper Strike |
| Mute | Fully prevents item cast orders, except ability casts. | Doom |

[corpus:liquipedia_dota2/disable@2360598#Ability_and_Item_Disables]

### Hex

Hex applies silence, mute, and disarm to the affected target and sets its movement speed to a fixed value. Every source of Hex instantly destroys illusions except strong illusions. Hexed heroes are still treated as heroes by abilities. [corpus:liquipedia_dota2/disable@2360598#Hex]

| Hex sources |
|---|
| Hex |
| Scythe of Vyse |

[corpus:liquipedia_dota2/disable@2360598#Hex]

## Forced Movement

Forced Movement changes a unit’s position independently of its movement speed and works while the unit is disabled. Most Forced Movement abilities prevent the affected unit from acting, but some allow it to attack, turn, and cast abilities and items. [corpus:liquipedia_dota2/disable@2360598#Forced_Movement]

| Forced Movement | Disabled Aspect / Definition | Examples |
|---|---|---|
| Fully Disabling | Behaves like a stun, preventing the unit from performing any action, but continuing with them once the effect expires. | Meat Hook affecting enemies |
| Non-disabling | Allows the affected unit to perform any action except moving. The unit can still turn, attack depending on the situation, and cast abilities and items. | Meat Hook affecting allies |
| Upward Movement | Moves a unit upwards, changing its Z-position. | Cyclone Sources |
| Pulling | Allows the affected unit to move normally but affects its speed depending on the direction of movement. | Gale Force |

[corpus:liquipedia_dota2/disable@2360598#Forced_Movement]

## Root

Root, formerly known as Ensnare, prevents affected units from moving and casting most mobility abilities. It does not prevent them from turning, casting other abilities, or using most items. A Root that also disarms is called a Bind, formerly known as Entangle. [corpus:liquipedia_dota2/disable@2360598#Root]

| Root Type | Disabled Aspect / Definition | Examples |
|---|---|---|
| Root | Prevents movement and disables certain mobility spells.<br><br>May apply True Sight, depending on source. | Ensnare |
| Bind | Prevents movement and disables certain mobility spells.<br><br>Disarms.<br><br>May apply True Sight, depending on source. | Frostbite |

[corpus:liquipedia_dota2/disable@2360598#Root]

### Leash

Leash disables the casting of several mobility abilities, including Blink-based abilities, and shares some interactions with Root. Although Leash prevents certain abilities from being cast, it does not cancel them if Leash is applied while the ability is being cast. Leash does not interrupt channeling but always cancels the following teleports. [corpus:liquipedia_dota2/disable@2360598#Leash]

| Teleports cancelled by Leash |
|---|
| Town Portal Scroll's |
| Keen Conveyance |
| Return |

[corpus:liquipedia_dota2/disable@2360598#Leash]

Leash mechanics vary by source and are detailed in the respective ability notes. [corpus:liquipedia_dota2/disable@2360598#Leash]

| Source | Interaction |
|---|---|
| Dream Coil | Affected heroes leashed during its duration are stun if they move too far from the leashed point. |
| Pounce | Heavily slows the leashed hero when it tries to move away from the leashed point. |

[corpus:liquipedia_dota2/disable@2360598#Leash]

## Trap

A trap impedes movement similarly to a cliff. Trap abilities either create an impassable obstacle or create a barrier or leash that prevents passage by heavily slowing units that try to cross it. [corpus:liquipedia_dota2/disable@2360598#Trap]

| Trap Type | Aspect / Definition | Examples |
|---|---|---|
| Pathing Blocker | An invisible entity with a collision size that physically blocks other units walking against it, unless the caster has unobstructed movement. | Fissure |
| Temporary Fence | A force field that uses Leash to prevent a unit from leaving or entering the affected area by drastically slowing its movement speed towards 0 near the field’s edges.<br><br>This movement speed slow is not shown in the HUD. | Kinetic Field |

[corpus:liquipedia_dota2/disable@2360598#Trap]

## Taunt

Taunt forces an affected unit to drop its current order and attack the taunting unit instead. It fully cancels attack orders against other units, ability-cast orders, and channeling. If outside attack range, the taunted unit moves toward the source until it enters attack range. It uses only regular movement and does not use abilities to close the gap. [corpus:liquipedia_dota2/disable@2360598#Taunt]

| Mechanic Type | Disabled Aspect / Definition | Examples |
|---|---|---|
| Taunt | Forces the affected unit to drop its current order and attack the taunting unit instead.<br><br>If outside attack range, the unit moves toward the Taunt source until within attack range. | Winter's Curse |

When Taunt and Fear affect a unit simultaneously, Taunt takes priority. [corpus:liquipedia_dota2/disable@2360598#Taunt]

### Fear

| Sub-Type | Definition | Examples |
|---|---|---|
| Fountain Fear | Units are forced to flee towards their own fountain. | Terrorize |
| Caster Fear | Units are forced to flee from the source of the fear debuff. | Requiem of Souls |
| Hypnosis | Units are forced to approach a certain point or unit, usually but not necessarily the caster. | Wheel of Wonder |

[corpus:liquipedia_dota2/disable@2360598#Fear]

## Hide

Hide prevents a unit from moving, attacking, casting abilities, or using items. Most Hide sources also make the affected unit invulnerable. Hidden units still gain Experience and Gold. While hidden, a unit cannot be affected by abilities, with exceptions such as Shadow Poison; for example, Meat Hook passes through a hidden unit and may hit a unit behind it. [corpus:liquipedia_dota2/disable@2360598#Hide]

## Disarm

Disarm prevents an affected unit from attacking but does not prevent it from casting abilities. When ordered to attack, a disarmed unit attempts to remain within attack range of its target but cannot act. It resumes attacking normally after Disarm expires. Disarm does not prevent other units from attacking the affected unit. [corpus:liquipedia_dota2/disable@2360598#Disarm]

| Disarm sources |
|---|
| Deafening Blast |
| Heaven's Halberd |

[corpus:liquipedia_dota2/disable@2360598#Disarm]

### Ethereal

Ethereal, sometimes called ghost form, makes affected units immune to all physical damage, grants attack immunity, and disarms them. It usually, but not always, reduces their magic resistance and causes them to take additional magical damage. Affected units retain control over every other aspect of their character. [corpus:liquipedia_dota2/disable@2360598#Ethereal]

The magic-resistance reductions of multiple Ethereal effects do not stack; the higher value takes priority. It is defined as:

`Ethereal Magic Resistance Reduction = (1 + MAX Ethereal Magic Resistance Reduction)` [corpus:liquipedia_dota2/disable@2360598#Ethereal]

| Ethereal sources |
|---|
| Ghost Scepter |
| Decrepify |

[corpus:liquipedia_dota2/disable@2360598#Ethereal]

## Blind

Blind makes a unit miss when attacking other units. Blind effects stack additively and can render an affected unit unable to land any attack. Blind works fully independently from evasion. [corpus:liquipedia_dota2/disable@2360598#Blind]

| Blind sources |
|---|
| Blinding Light |
| Laser |

[corpus:liquipedia_dota2/disable@2360598#Blind]

## Disabling Orders

Stuns, including Sleep and Taunt, and some sources of Forced Movement, Invulnerable, and Hide do not prevent players from giving orders to their units. The unit executes the given order when the disable expires. Only very few abilities can be cast normally during these disables. [corpus:liquipedia_dota2/disable@2360598#Disabling_Orders]

| Abilities Castable While Disabled (Stunned/Taunted/Sleeped) |
|---|
| Abaddon – Borrowed Time |
| Bane – Nightmare End |
| Buildings – Glyph of Fortification |
| Dazzle – Nothl Projection2b |
| Elder Titan – Return Astral Spirit |
| Elder Titan – Move Astral Spirit |
| Lone Druid – Savage Roar2b |
| Spirit Bear – Savage Roar2b |
| Morphling – Attribute Shift2b |
| Roshan – Roar of Retribution |
| Rubick – Telekinesis Land 2b 4 |
| Scan – Scan |
| Templar Assassin – Refraction 2b |
| Troll Warlord – Battle Trance 1 |
| Ursa – Enrage 2a |
| Visage – Stone Form |
| Familiar – Stone Form |

1 Requires Talent.  
2a Requires Aghanim's Scepter.  
2b Requires Aghanim's Shard.  
4 Ignores stun only during Duel.  
5 Ignores stun only if self-casted Telekinesis. [corpus:liquipedia_dota2/disable@2360598#Disabling_Orders]

### Can't Act

Some disables prevent giving orders and also prevent the abilities listed above from being cast. When a targeted order is prevented, the player cannot select a target; the order remains selected, so an attempted unit-targeted ability cast while silenced stays selected until manually deselected. When orders are disabled, a red on-screen error message usually appears with an error sound to explain why the order cannot be given. The message and sound vary by disable. [corpus:liquipedia_dota2/disable@2360598#Can't_Act]

| Status Effect | Disabled Aspect / Definition | Examples |
|---|---|---|
| Ethereal | Fully prevents ordering attacks on the Ethereal Unit. | Decrepify |
| Fear | Runs away from caster towards a certain direction and fully prevents any orders. | Requiem of Souls |
| Hypnosis | Pulled towards caster and fully prevents any orders. | Sinister Gaze |
| Leash | Limited movement capabilities and fully prevents ordering certain abilities. | Pounce |
| Mute | Fully prevents item cast orders, except ability casts. | Doom |
| Root | Rooted on spot and fully prevents ordering certain abilities. | Frostbite |
| Silence | Fully prevents any ability order, except item casts. | Global Silence |

[corpus:liquipedia_dota2/disable@2360598#Can't_Act]

Preventing orders is also partly a disable of its own: several abilities fully prevent orders even though the disable used by the ability does not. [corpus:liquipedia_dota2/disable@2360598#Can't_Act]

| Can't Act (General Order Disable) |
|---|
| Astral Spirit – Echo Stomp |
| Brewmaster – Primal Split (During Transformation ONLY) |
| Dawnbreaker – Solar Guardian |
| Kez – Raptor Dance (During Cast) |
| Lifestealer – Infest |
| Magnus – Skewer (Self) |
| Monkey King – Changing of the Guard |
| Phoenix – Supernova (Ally) 2a |
| Tusk – Snowball (Ally) |
| Witch Doctor – Voodoo Switcheroo |
| Brewmaster – Cinder Brew1 |
| Dark Willow – Terrorize |
| Lone Druid – Savage Roar |
| Spirit Bear – Savage Roar |
| Death Prophet – Spirit Siphon2b |
| Muerta – Dead Shot |
| Ringmaster – Tame the Beasts |
| Shadow Fiend – Requiem of Souls |
| Spectre – Reality 2a |
| Terrorblade – Terror Wave |
| Lich – Sinister Gaze |
| Ringmaster – Wheel of Wonder |
| Void Spirit – Aether Remnant |

[corpus:liquipedia_dota2/disable@2360598#Can't_Act]

| Castable while Can't Act |
|---|
| Buildings – Glyph of Fortification |
| Lifestealer – Consume |
| Elder Titan – Move Astral Spirit |
| Elder Titan – Return Astral Spirit |
| Scan – Scan |

[corpus:liquipedia_dota2/disable@2360598#Can't_Act]

## Trivia

Pause was an effect that completely prevented its target from moving, attacking, casting spells, or using items. It disabled most passive abilities, stopped buffs and debuffs from ticking down for its duration, and prevented the target from gaining experience. [corpus:liquipedia_dota2/disable@2360598#Trivia]

| Examples of Pause |
|---|
| Chronosphere |
| Astral Imprisonment |
| Disruption |

[corpus:liquipedia_dota2/disable@2360598#Trivia]