---
title: Stun
kind: concept
patch: 7.41d
card:
  entity: stun
  sentences:
  - text: Stun is a status effect with three modifier types that stops a unit’s current
      order and prevents movement, attacks, ability casts, and item use until it expires.
    marks:
    - corpus:liquipedia_dota2/stun@2405717
    - corpus:liquipedia_dota2/stun@2405717#Mechanics
    - corpus:liquipedia_dota2/stun@2405717#Definition
  - text: A stun during an attack or cast animation cancels that action and fully
      interrupts channeling abilities.
    marks:
    - corpus:liquipedia_dota2/stun@2405717#Mechanics
  - text: Stun neither disables passive abilities nor affects the unit’s attributes.
    marks:
    - corpus:liquipedia_dota2/stun@2405717#Mechanics
  - text: Affected units have a stunned animation and whirling overhead effect, while
      bash-based abilities use a yellow overhead effect.
    marks:
    - corpus:liquipedia_dota2/stun@2405717#Mechanics
  - text: Stun preserves existing orders, including ⇧ Shift-queue orders, and the
      interrupted order resumes afterward unless replaced while stunned.
    marks:
    - corpus:liquipedia_dota2/stun@2405717#Mechanics
  - text: Orders may be issued during stun and execute after it expires.
    marks:
    - corpus:liquipedia_dota2/stun@2405717#Mechanics
  - text: A non-shift-queued order replaces the canceled order, whereas a shift-queued
      order executes after that canceled order finishes.
    marks:
    - corpus:liquipedia_dota2/stun@2405717#Mechanics
  - text: Multiple cast orders queue automatically, but move and attack commands do
      not queue and cancel cast orders.
    marks:
    - corpus:liquipedia_dota2/stun@2405717#Mechanics
  - text: Stun is distinct from root, silence, mute, and disarm.
    marks:
    - corpus:liquipedia_dota2/stun@2405717#Mechanics
  - text: Stunned and Bash sources within their respective groups share a modifier
      and refresh rather than extend one another’s duration.
    marks:
    - corpus:liquipedia_dota2/stun@2405717#Definition
  - text: Unique stuns use custom modifiers, so each source places its own modifier
      on affected targets.
    marks:
    - corpus:liquipedia_dota2/stun@2405717#Definition
  - text: Caster-disabling stuns use custom modifiers and prevent their caster from
      moving while their effects apply.
    marks:
    - corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns
---

# Stun

Stun is a status effect that completely locks down affected units, disabling almost all of their capabilities. [corpus:liquipedia_dota2/stun@2405717]

## Mechanics

A stunned unit is indicated by a special stunned animation, except on buildings and wards, and a whirling overhead effect. Bash-based abilities use a yellow overhead effect. Stun neither disables passive abilities nor affects the unit’s attributes. [corpus:liquipedia_dota2/stun@2405717#Mechanics]

Upon being stunned, a unit stops its current order and stands still until the effect expires. It cannot move, attack, cast abilities, or use items. A stun during an attack or cast animation cancels that attack or cast and therefore fully interrupts channeling abilities. [corpus:liquipedia_dota2/stun@2405717#Mechanics]

Stun does not make a unit forget its orders, including ⇧ Shift-queue orders. When the stun expires, the unit resumes its previously interrupted order unless it received another order while stunned. Any order may be given normally during the stun and is executed after the stun expires. [corpus:liquipedia_dota2/stun@2405717#Mechanics]

An order issued without ⇧ Shift-queue overrides the previously canceled order. With ⇧ Shift-queue, the new order is executed after the previously canceled order finishes. Multiple cast orders are automatically queued, but move and attack commands are not queued and cancel cast orders. Consequently, a cast order followed by a non-shift-queued move order results only in the move order being executed, while a move order followed by a cast order results only in the cast order being executed. Executing move or attack and cast orders after the stun requires ⇧ Shift-queue. [corpus:liquipedia_dota2/stun@2405717#Mechanics]

Stun is distinct from root, silence, mute, and disarm. [corpus:liquipedia_dota2/stun@2405717#Mechanics]

## Definition

There are three types of stun, each using a different modifier. Stuns within the same group use the same modifier, refresh one another’s duration based on when they affect the target, and do not extend the stun duration. [corpus:liquipedia_dota2/stun@2405717#Definition]

| Modifier type | Definition | Examples |
|---|---|---|
| Stunned | Does not place individual modifiers; sources refresh one another. | Magic Missile (Regular Stun); Lightning Bolt (Mini-Stun) [corpus:liquipedia_dota2/stun@2405717#Definition] |
| Bash | Does not place individual modifiers; sources refresh one another. | Infernal Blade [corpus:liquipedia_dota2/stun@2405717#Definition] |
| Unique | Uses custom modifiers, so each source places its own modifier on its targets. | Shackles [corpus:liquipedia_dota2/stun@2405717#Definition] |

## Abilities Castable While Stunned

| Unit | Ability |
|---|---|
| Abaddon | Borrowed Time [corpus:liquipedia_dota2/stun@2405717#Abilities_Castable_When_Stunned] |
| Bane | Nightmare End [corpus:liquipedia_dota2/stun@2405717#Abilities_Castable_When_Stunned] |
| Buildings | Glyph of Fortification [corpus:liquipedia_dota2/stun@2405717#Abilities_Castable_When_Stunned] |
| Dazzle | Nothl Projection<sup>2b</sup> [corpus:liquipedia_dota2/stun@2405717#Abilities_Castable_When_Stunned] |
| Elder Titan | Return Astral Spirit [corpus:liquipedia_dota2/stun@2405717#Abilities_Castable_When_Stunned] |
| Elder Titan | Move Astral Spirit [corpus:liquipedia_dota2/stun@2405717#Abilities_Castable_When_Stunned] |
| Lone Druid | Savage Roar<sup>2b</sup> [corpus:liquipedia_dota2/stun@2405717#Abilities_Castable_When_Stunned] |
| Spirit Bear | Savage Roar<sup>2b</sup> [corpus:liquipedia_dota2/stun@2405717#Abilities_Castable_When_Stunned] |
| Morphling | Attribute Shift<sup>2b</sup> [corpus:liquipedia_dota2/stun@2405717#Abilities_Castable_When_Stunned] |
| Roshan | Roar of Retribution [corpus:liquipedia_dota2/stun@2405717#Abilities_Castable_When_Stunned] |
| Rubick | Telekinesis Land<sup>2b, 4</sup> [corpus:liquipedia_dota2/stun@2405717#Abilities_Castable_When_Stunned] |
| Scan | Scan [corpus:liquipedia_dota2/stun@2405717#Abilities_Castable_When_Stunned] |
| Templar Assassin | Refraction<sup>2b</sup> [corpus:liquipedia_dota2/stun@2405717#Abilities_Castable_When_Stunned] |
| Troll Warlord | Battle Trance<sup>1</sup> [corpus:liquipedia_dota2/stun@2405717#Abilities_Castable_When_Stunned] |
| Ursa | Enrage<sup>2a</sup> [corpus:liquipedia_dota2/stun@2405717#Abilities_Castable_When_Stunned] |
| Visage | Stone Form [corpus:liquipedia_dota2/stun@2405717#Abilities_Castable_When_Stunned] |
| Familiar | Stone Form [corpus:liquipedia_dota2/stun@2405717#Abilities_Castable_When_Stunned] |

| Marker | Condition |
|---|---|
| 1 | Requires Talent. [corpus:liquipedia_dota2/stun@2405717#Abilities_Castable_When_Stunned] |
| 2a | Requires Aghanim's Scepter. [corpus:liquipedia_dota2/stun@2405717#Abilities_Castable_When_Stunned] |
| 2b | Requires Aghanim's Shard. [corpus:liquipedia_dota2/stun@2405717#Abilities_Castable_When_Stunned] |
| 4 | Ignores stun only if self-casted Telekinesis. [corpus:liquipedia_dota2/stun@2405717#Abilities_Castable_When_Stunned] |

## Stunned Modifier Sources

| Source | Ability |
|---|---|
| Alchemist | Unstable Concoction [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Anti-Mage | Mana Void [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Beastmaster | Primal Roar [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Bounty Hunter | Shadow Walk [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Centaur Conqueror | War Stomp [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Centaur Warrunner | Hoof Stomp [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Chaos Knight | Chaos Bolt [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Clockwerk | Battery Assault [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Clockwerk | Overclocking [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Clockwerk | Hookshot [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Dark Seer | Normal Punch [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Dark Willow | Cursed Crown [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Dawnbreaker | Solar Guardian [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Dragon Knight | Dragon Tail [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Earth | Hurl Boulder [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Earth Spirit | Rolling Boulder [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Earthshaker | Fissure Aftershock<sup>2b</sup> [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Earthshaker | Aftershock [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Enigma | Malefice [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Fallen Sky | Fallen Sky [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Familiar | Stone Form [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Grimstroke | Ink Swell [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Gyrocopter | Homing Missile [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Kunkka | Ghostship [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Leshrac | Split Earth [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Lina | Light Strike Array [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Luna | Lucent Beam [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Luna | Eclipse [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Magnus | Horn Toss [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Magnus | Reverse Polarity [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Marci | Dispose [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Marci | Rebound [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Meteor Hammer | Meteor Hammer [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Mirana | Sacred Arrow [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Mud Golem | Hurl Boulder [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Night Stalker | Void<sup>4</sup> [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Nyx Assassin | Spiked Carapace [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Ogre Bruiser | Ogre Smash! [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Ogre Magi | Fireblast [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Ogre Magi | Unrefined Fireblast [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Phoenix | Supernova [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Primal Beast | Onslaught [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Primal Beast | Pulverize [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Primal Beast | Rock Throw [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Puck | Dream Coil [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Rubick | Telekinesis [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Shard Golem | Hurl Boulder [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Slardar | Slithereen Crush [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Snapfire | Firesnap Cookie [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Snapfire | Spit Out [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Sniper | Assassinate [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Spirit Breaker | Charge of Darkness [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Sven | Storm Hammer [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Techies | Blast Off! [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Tusk | Snowball [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Vengeful Spirit | Magic Missile [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Venomancer | Venomous Gale<sup>2b</sup> [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Visage | Gravekeeper's Cloak<sup>2b</sup> [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Warlock | Chaotic Offering [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Winter Wyvern | Splinter Blast<sup>1, 5</sup> [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Witch Doctor | Paralyzing Cask [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Wraith King | Wraithfire Blast [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Zeus | Lightning Bolt [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| Zeus | Nimbus [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |

| Marker | Condition |
|---|---|
| 1 | Requires talent. [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| 2a | Requires Aghanim's Scepter. [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| 2b | Requires Aghanim's Shard. [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| 4 | Only applies stun during nighttime. [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |
| 5 | Only applies to the secondary targets. [corpus:liquipedia_dota2/stun@2405717#Stunned_Modifier_Sources] |

## Bash Modifier Sources

All these abilities use the same bashed modifier. Multiple bash sources do not stack and proc independently from each other. When multiple items with bash are obtained, only the one that has continuously remained in the inventory the longest will proc bash. [corpus:liquipedia_dota2/stun@2405717#Bash_Modifier_Sources]

| Source | Ability |
|---|---|
| Abyssal Blade | Bash [corpus:liquipedia_dota2/stun@2405717#Bash_Modifier_Sources] |
| Abyssal Blade | Overwhelm [corpus:liquipedia_dota2/stun@2405717#Bash_Modifier_Sources] |
| Doom | Infernal Blade [corpus:liquipedia_dota2/stun@2405717#Bash_Modifier_Sources] |
| Roshan | Bash [corpus:liquipedia_dota2/stun@2405717#Bash_Modifier_Sources] |
| Skull Basher | Bash [corpus:liquipedia_dota2/stun@2405717#Bash_Modifier_Sources] |
| Slardar | Bash of the Deep [corpus:liquipedia_dota2/stun@2405717#Bash_Modifier_Sources] |
| Templar Assassin | Meld<sup>1</sup> [corpus:liquipedia_dota2/stun@2405717#Bash_Modifier_Sources] |

| Marker | Condition |
|---|---|
| 1 | Requires talent. [corpus:liquipedia_dota2/stun@2405717#Bash_Modifier_Sources] |
| 2a | Requires Aghanim's Scepter. [corpus:liquipedia_dota2/stun@2405717#Bash_Modifier_Sources] |
| 2b | Requires Aghanim's Shard. [corpus:liquipedia_dota2/stun@2405717#Bash_Modifier_Sources] |

## Unique Modifier Sources

| Source | Ability |
|---|---|
| Ancient Apparition | Cold Feet [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Ancient Apparition | Ice Blast<sup>2b</sup> [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Bane | Nightmare [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Bane | Fiend's Grip [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Batrider | Flaming Lasso [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Beastmaster | Primal Roar<sup>4</sup> [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Clockwerk | Power Cogs [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Dark Seer | Vacuum [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Dawnbreaker | Starbreaker [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Earth Spirit | Enchant Remnant [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Earthshaker | Fissure [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Elder Titan | Echo Stomp [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Enigma | Black Hole [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Eul's Scepter of Divinity | Cyclone [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Faceless Void | Time Walk<sup>2a</sup> [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Faceless Void | Time Lock [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Faceless Void | Chronosphere [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Hoodwink | Bushwhack [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Hoodwink | Decoy [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Invoker | Cold Snap [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Invoker | Tornado [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Jakiro | Ice Path [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Kunkka | Torrent [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Lion | Earth Spike [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Magnus | Skewer [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Mars | Spear of Mars [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Medusa | Mystic Snake<sup>2a</sup> [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Medusa | Cold Blooded<sup>2a</sup> [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Medusa | Stone Gaze [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Monkey King | Boundless Strike [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Monkey King | Tree Dance [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Morphling | Adaptive Strike [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Naga Siren | Song of the Siren [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Necrophos | Reaper's Scythe [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Nyx Assassin | Impale [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Outworld Destroyer | Astral Imprisonment [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Pangolier | Roll Up [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Pangolier | Rolling Thunder [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Pudge | Meat Hook [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Pudge | Dismember [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Sand King | Burrowstrike [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Shadow Demon | Disruption [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Shadow Shaman | Shackles [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Spirit Breaker | Greater Bash [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Spirit Breaker | Nether Strike [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Storm | Cyclone [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Storm Spirit | Electric Vortex [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Tidehunter | Ravage [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Tiny | Avalanche [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Tiny | Toss [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Tusk | Walrus PUNCH! [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Tusk | Walrus Kick [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Windranger | Shackleshot [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Wind Waker | Cyclone [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Winter Wyvern | Cold Embrace [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| Winter Wyvern | Winter's Curse [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |

| Marker | Condition |
|---|---|
| 1 | Requires talent. [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| 2a | Requires Aghanim's Scepter. [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| 2b | Requires Aghanim's Shard. [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |
| 4 | Only applies to the secondary target. [corpus:liquipedia_dota2/stun@2405717#Unique_Modifier_Sources] |

## Caster-Disabling Stuns

These abilities disable their caster upon applying their effects, preventing the caster from moving during the effects. They all use custom modifiers. [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns]

| Source | Ability |
|---|---|
| Alchemist | Chemical Rage [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Dawnbreaker | Starbreaker [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Dawnbreaker | Solar Guardian [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Chaos Knight | Phantasm [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Earthshaker | Enchant Totem<sup>2a</sup> [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Faceless Void | Time Walk [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Faceless Void | Reverse Time Walk [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Kez | Grappling Claw [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Kez | Kazurai Katana<sup>2b</sup> [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Lone Druid | True Form [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Lycan | Wolf Bite [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Lycan | Shapeshift [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Magnus | Skewer [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Marci | Rebound [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Manta Style | Mirror Image [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Meepo | Dig [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Monkey King | Tree Dance [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Monkey King | Primal Spring [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Muerta | Pierce the Veil [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Naga Siren | Mirror Image [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Necrophos | Death Seeker [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Outworld Destroyer | Astral Imprisonment [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Pangolier | Swashbuckle [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Pangolier | Shield Crash<sup>4</sup> [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Phantom Lancer | Doppelganger [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Pudge | Meat Hook<sup>5</sup> [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Snapfire | Firesnap Cookie<sup>2a</sup> [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Sand King | Burrowstrike<sup>5</sup> [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Shadow Demon | Disruption [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Techies | Blast Off! [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Terrorblade | Metamorphosis [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Terrorblade | Terror Wave [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Tusk | Snowball [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Viper | Nosedive [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Visage | Gravekeeper's Cloak<sup>2b</sup> [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| Winter Wyvern | Cold Embrace [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |

| Marker | Condition |
|---|---|
| 1 | Requires talent. [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| 2a | Requires Aghanim's Scepter. [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| 2b | Requires Aghanim's Shard. [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| 4 | Disables the caster during the jump when not used during Rolling Thunder. [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |
| 5 | Disables the caster during the cast backswing. [corpus:liquipedia_dota2/stun@2405717#Caster_Disabling_Stuns] |