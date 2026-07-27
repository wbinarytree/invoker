---
title: Spell Block
kind: concept
patch: 7.41d
card:
  entity: spell_block
  sentences:
  - text: Spell Block is a defensive passive effect or active buff that automatically
      blocks most offensive single-target abilities aimed at its unit, then enters
      cooldown.
    marks:
    - corpus:liquipedia_dota2/spell_block@2383952
    - corpus:liquipedia_dota2/spell_block@2383952#Mechanics
  - text: Spell Reflection returns an offensive unit-targeted ability to its caster,
      while Spell Redirection sends it to another unit.
    marks:
    - corpus:liquipedia_dota2/spell_block@2383952#Definition
  - text: Spell Block, Spell Reflection, and Spell Redirection operate independently.
    marks:
    - corpus:liquipedia_dota2/spell_block@2383952#Definition
  - text: Every Spell Block has downtime after blocking a spell, so its protection
      is not permanent.
    marks:
    - corpus:liquipedia_dota2/spell_block@2383952#Mechanics
  - text: Coming off cooldown does not cancel a single-target spell already affecting
      the unit.
    marks:
    - corpus:liquipedia_dota2/spell_block@2383952#Mechanics
  - text: With very few exceptions, Spell Block protects only the primary target,
      not units hit by area effects or as secondary targets.
    marks:
    - corpus:liquipedia_dota2/spell_block@2383952#Mechanics
  - text: Blocking a single-target spell usually completely negates its associated
      area effect and can protect nearby allies.
    marks:
    - corpus:liquipedia_dota2/spell_block@2383952#Mechanics
  - text: Changing an ability from single-target to non-targeted through another ability,
      talent, or Aghanim’s Scepter may make it unblockable.
    marks:
    - corpus:liquipedia_dota2/spell_block@2383952#Mechanics
  - text: Spell Block does not block active attack modifiers or allied abilities.
    marks:
    - corpus:liquipedia_dota2/spell_block@2383952#Mechanics
  - text: Projectile abilities are usually blocked upon impact, while hero-based projectile
      abilities are blocked upon cast.
    marks:
    - corpus:liquipedia_dota2/spell_block@2383952#Projectile
  - text: Bouncing abilities usually trigger Spell Block only on the primary target
      and continue bouncing when blocked.
    marks:
    - corpus:liquipedia_dota2/spell_block@2383952#Bounce
  - text: The passive self-only talent blocks most targeted abilities once and has
      cooldown values of 15/18/20.
    marks:
    - corpus:liquipedia_dota2/spell_block@2383952#Talents
---

# Spell Block

Spell Block is a defensive ability that protects a unit from most single-target abilities, ranging from basic small abilities to the strongest single-target ultimates. [corpus:liquipedia_dota2/spell_block@2383952]

## Definition

| Mechanic | Definition | Example |
|---|---|---|
| Spell Block | Blocks the offensive unit-targeted ability. | Spellblock |
| Spell Reflection | Reflects the offensive unit-targeted ability from the targeted unit to its caster. | Echo Shell |
| Spell Redirection | Redirects the unit-targeted ability from the intended targeted unit to another unit. | Soulbind |

All three mechanics work independently of each other. [corpus:liquipedia_dota2/spell_block@2383952#Definition]

## Mechanics

Spell Block is a passive effect that activates automatically when a blockable single-target spell targets the unit. It may instead be provided by a buff that protects the unit while active. All Spell Blocks have downtime and go on cooldown after blocking a spell, so they do not permanently protect against single-target spells. Spell Block only blocks upon cast; coming off cooldown does not cancel a single-target spell already affecting the unit. [corpus:liquipedia_dota2/spell_block@2383952#Mechanics]

With very few exceptions, Spell Block does not protect against area-of-effect spells or against single-target spells that hit the unit as a secondary target. The unit must be the primary target. When a single-target spell has an area effect, blocking it also completely negates that area effect and can thereby protect nearby allies, though exceptions exist. Projectile-based spells are usually blocked upon impact rather than upon cast, again with some exceptions. [corpus:liquipedia_dota2/spell_block@2383952#Mechanics]

An ability’s interaction with Spell Block may change when modified by other abilities, talents, or Aghanim’s Scepter. For example, a single-target spell changed into a non-targeted spell may cease to be blockable. Spell Block does not block active attack modifiers or allied abilities. [corpus:liquipedia_dota2/spell_block@2383952#Mechanics]

## Sources

| Source | Interaction |
|---|---|
| Anti-Mage — Counterspell | Decoy and Linken’s Sphere do not trigger while this ability is active. |
| Hoodwink — Decoy | Has higher priority than Transfer Spellblock and Spellblock. |
| Linken’s Sphere — Transfer Spellblock | Has higher priority than Spellblock. Temporarily removes Spellblock from the item’s owner and transfers the buff to an allied unit. |
| Linken’s Sphere — Spellblock | |
| Roshan — Spell Block | |
| Spirit Breaker — Planar Pocket | Has higher priority than Counterspell, Transfer Spellblock, and Spellblock. Redirected spells are still subject to all other Spell Block sources. |

[corpus:liquipedia_dota2/spell_block@2383952#Spell_Block_Sources]

### Talents

The talent is passive, affects self, blocks most targeted spells once, and is listed as “Varies.” It blocks most targeted abilities for the hero when off cooldown and has the following cooldown values: **15/18/20**. It does not block allied abilities. [corpus:liquipedia_dota2/spell_block@2383952#Talents]

Spellblock priority is **Echo Shield ➤ Transfer Spellblock ➤ Spellblock**. It does not trigger while Counterspell is active and does not stack with Planar Pocket. Its buff icon displays a cooldown when Spell Block is used. Cooldown reduction sources, such as Octarine Core, affect the cooldown, but cooldown resets do not. [corpus:liquipedia_dota2/spell_block@2383952#Talents]

Illusions receive the buff, but it does not work for them. In Ability Draft, the talent is available and is not bound to an ability. Its modifier is `modifier_special_bonus_spell_block`. [corpus:liquipedia_dota2/spell_block@2383952#Talents]

| Bonus | Level 10 Left | Level 10 Right | Level 15 Left | Level 15 Right | Level 20 Left | Level 20 Right | Level 25 Left | Level 25 Right |
|---|---|---|---|---|---|---|---|---|
| Spell Block | | | | | | | | |

[corpus:liquipedia_dota2/spell_block@2383952#Talents]

## Blocking

### Not-blocked unit-target abilities

| Category | Ability |
|---|---|
| Hero Abilities: Unit and Ground Targetable | Dragon Knight — Breathe Fire |
| Hero Abilities: Unit and Ground Targetable | Death Prophet — Crypt Swarm |
| Hero Abilities: Unit and Ground Targetable | Jakiro — Dual Breath |
| Hero Abilities: Unit and Ground Targetable | Lina — Dragon Slave |
| Hero Abilities: Unit and Ground Targetable | Lion — Earth Spike |
| Hero Abilities: Unit and Ground Targetable | Magnus — Shockwave 4 |
| Hero Abilities: Unit and Ground Targetable | Tidehunter — Gush 2a 4 |
| Hero Abilities: Unit and Ground Targetable | Tiny — Tree Throw 4 |
| Hero Abilities: Unit and Ground Targetable | Troll Warlord — Whirling Axes (Ranged) |
| Other Hero Abilities | Kez — Kazurai Katana 4 |
| Other Hero Abilities | Spectre — Spectral Dagger 6 |
| Creep Abilities 4 | Fell Spirit — Vex |
| Creep Abilities 4 | Raptor — Dive Bomb |
| Creep Abilities 4 | Satyr Tormenter — Shockwave |
| Creep Abilities 4 | Wildwing Ripper — Hurricane |
| Creep Abilities 4 | Wildwing — Tornado |
| Item Abilities | Spirit Vessel — Soul Release |
| Item Abilities | Urn of Shadows — Soul Release |
| Neutral Item Abilities 5 | |

| Marker | Meaning |
|---|---|
| 3 | Requires selecting the corresponding facet. |
| 4 | Missing from the in-game extended ability description. |
| 5 | Neutral Item abilities can’t be blocked. |
| 6 | Can be blocked only when unit-targeted and only by the main target. The in-game description is incorrect. |

[corpus:liquipedia_dota2/spell_block@2383952#Not-blocked_Unit_Target_Abilities]

Auto-cast abilities with an active attack modifier do not trigger Spell Block.

| Active Attack Modifier |
|---|
| Ancient Apparition — Chilling Touch 5 |
| Bounty Hunter — Jinada 4 5 |
| Clinkz — Searing Arrows 5 |
| Doom — Infernal Blade 7 |
| Drow Ranger — Frost Arrows |
| Enchantress — Impetus |
| Huskar — Burning Spear |
| Jakiro — Liquid Fire 5 |
| Jakiro — Liquid Frost |
| Kunkka — Tidebringer 4 7 |
| Omniknight — Hammer of Purity 4 5 |
| Outworld Destroyer — Arcane Orb |
| Silencer — Glaives of Wisdom |
| Slark — Saltwater Shiv 7 |
| Tusk — Walrus PUNCH! 5 6 |
| Treant Protector — Leech Seed 4 5 |
| Viper — Poison Attack |
| Weaver — Geminate Attack 4 |

[corpus:liquipedia_dota2/spell_block@2383952#Not-blocked_Unit_Target_Abilities]

### Bounce

Abilities that bounce between multiple targets usually trigger Spell Block only on the primary target. If blocked, they continue bouncing. [corpus:liquipedia_dota2/spell_block@2383952#Bounce]

| Blockable before the first bounce |
|---|
| Batrider — Flaming Lasso 2a |
| Dazzle — Shadow Wave |
| Grimstroke — Soulbind |
| Juggernaut — Omnislash |
| Juggernaut — Swiftslash |
| Harpy Stormcrafter — Chain Lightning |
| Hoodwink — Acorn Shot |
| Lich — Chain Frost |
| Medusa — Mystic Snake |
| Nature’s Prophet — Wrath of Nature |
| Rubick — Fade Bolt |
| Tinker — Laser 1 |
| Vengeful Spirit — Magic Missile 2b |
| Warlock — Fatal Bonds |
| Winter Wyvern — Splinter Blast 2b |
| Witch Doctor — Paralyzing Cask |
| Zeus — Arc Lightning |

| Marker | Meaning |
|---|---|
| 1 | Requires a Talent. |
| 2a | Requires Aghanim’s Scepter. |
| 2b | Requires Aghanim’s Shard. |

[corpus:liquipedia_dota2/spell_block@2383952#Bounce]

Spell Block is supposed to trigger only before the first bounce, but the following abilities are blockable on any hit:

| Blockable at any hit | Interaction |
|---|---|
| Bounty Hunter — Shuriken Toss | |
| Warpine Raider — Seed Shot 4 | Can trigger Spell Block multiple times. |

After blocking, a bounce ability is supposed to keep bouncing, but blocking prevents the following abilities from bouncing:

| Blocking prevents bounce |
|---|
| Bounty Hunter — Shuriken Toss |
| Harpy Stormcrafter — Chain Lightning |

[corpus:liquipedia_dota2/spell_block@2383952#Bounce]

### Multiple targets

The following multiple-target abilities can be blocked independently by each target:

| Ability |
|---|
| Bane — Brain Sap 2b |
| Dazzle — Poison Touch |
| Lion — Finger of Death 2a |
| Night Stalker — Void 3 |
| Nyx Assassin — Mind Flare 1 |
| Phantom Assassin — Stifling Dagger 1 |
| Skywrath Mage — Arcane Bolt 2b |
| Skywrath Mage — Ancient Seal 2a |
| Visage — Soul Assumption 1 |
| Zeus — Lightning Bolt 1 |
| Gleipnir — Eternal Chains |

| Marker | Meaning |
|---|---|
| 1 | Requires a Talent. |
| 2a | Requires Aghanim’s Scepter. |
| 2b | Requires Aghanim’s Shard. |

[corpus:liquipedia_dota2/spell_block@2383952#Multiple_Target]

### Point targets

| Blockable Ground-target Ability |
|---|
| Earth Spirit — Boulder Smash |
| Nature’s Prophet — Wrath of Nature 3 |
| Night Stalker — Void 3 |
| Zeus — Lightning Bolt 4 |
| Gleipnir — Eternal Chains |

| Not Blockable after Upgrade |
|---|
| Lion — Hex 1 |
| Lich — Sinister Gaze 2a |
| Storm Spirit — Electric Vortex 2a |
| Queen of Pain — Shadow Strike 2a |

| Marker | Meaning |
|---|---|
| 1 | Requires a Talent. |
| 2a | Requires Aghanim’s Scepter. |
| 2b | Requires Aghanim’s Shard. |
| 3 | If ground-targeted, it can still be blocked before the first bounce and continues bouncing even if blocked. |
| 4 | If ground-targeted, it can still be blocked. Vision is blocked only when unit-targeted. Bolts from Nimbus are not blocked. |

Nature’s Prophet’s **Sprout** is fully blocked only when directly targeted and is not blocked when ground-targeted. [corpus:liquipedia_dota2/spell_block@2383952#Point_Target]

### Projectiles

Projectile abilities are usually blocked upon impact. Hero-based projectile abilities are instead blocked upon cast.

| Hero-based Projectile Ability Blocked upon Cast |
|---|
| Huskar — Life Break |
| Marci — Rebound |
| Meepo — MegaMeepo Fling |
| Necrophos — Death Seeker |
| Spirit Breaker — Charge of Darkness |
| Sven — Storm Hammer (Alt-Cast) |
| Tiny — Toss |
| Tusk — Snowball |

[corpus:liquipedia_dota2/spell_block@2383952#Projectile]

### Partial blocking

| Ability | Interaction |
|---|---|
| Undying — Soul Rip | Units counted toward damage still lose health. |
| Zeus — Lightning Bolt | Vision is blocked only when unit-targeted. |

[corpus:liquipedia_dota2/spell_block@2383952#Partially_Blocking]

### Other unique interactions

| Ability | Interaction |
|---|---|
| Bane — Nightmare | Blocked upon cast and upon attacking a unit affected by an enemy Nightmare. |
| Ogre Magi — Fireblast | When blocked, ends Multicast regardless of whether the initial cast or a Multicast instance was blocked. |
| Ogre Magi — Unrefined Fireblast | When blocked, ends Multicast regardless of whether the initial cast or a Multicast instance was blocked. |

[corpus:liquipedia_dota2/spell_block@2383952#Other_Unique_Interactions]

### Fully blocked abilities

The following abilities are fully blocked by Spell Block.

#### Hero abilities

| Hero | Ability |
|---|---|
| Abaddon | Mist Coil 1 |
| Alchemist | Unstable Concoction Throw 1 2 |
| Ancient Apparition | Cold Feet 4 |
| Anti-Mage | Mana Void 3 |
| Arc Warden | Flux |
| Axe | Battle Hunger |
| Axe | Culling Blade 3 |
| Bane | Enfeeble |
| Bane | Brain Sap |
| Bane | Fiend’s Grip |
| Batrider | Flaming Lasso 3 |
| Beastmaster | Primal Roar 3 |
| Bloodseeker | Rupture |
| Bounty Hunter | Shuriken Toss 1 2 5 |
| Bounty Hunter | Track |
| Bristleback | Viscous Nasal Goo 1 4 |
| Broodmother | Spawn Spiderlings 1 |
| Centaur Warrunner | Double Edge 3 |
| Chaos Knight | Chaos Bolt 1 |
| Chaos Knight | Reality Rift |
| Chen | Penitence 1 |
| Crystal Maiden | Frostbite |
| Dark Willow | Cursed Crown |
| Dazzle | Poison Touch 3 |
| Death Prophet | Spirit Siphon |
| Disruptor | Thunder Strike 3 |
| Disruptor | Glimpse |
| Doom | Doom |
| Dragon Knight | Dragon Tail 1 |
| Earth Spirit | Boulder Smash 3 |
| Earth Spirit | Enchant Remnant |
| Enchantress | Enchant |
| Enigma | Malefice |
| Grimstroke | Phantom’s Embrace |
| Grimstroke | Soulbind 3 |
| Grimstroke | Dark Portrait |
| Gyrocopter | Homing Missile 1 |
| Huskar | Life Break 1 |
| Invoker | Cold Snap |
| Juggernaut | Omnislash 3 5 |
| Kunkka | X Marks the Spot |
| Legion Commander | Duel |
| Leshrac | Lightning Storm 3 |
| Lich | Frost Blast 3 6 |
| Lich | Sinister Gaze 4 |
| Lich | Chain Frost 1 3 5 |
| Lifestealer | Open Wounds |
| Lina | Laguna Blade 6 |
| Lion | Hex 4 |
| Lion | Mana Drain 3 |
| Lion | Finger of Death 3 6 |
| Luna | Lucent Beam |
| Medusa | Mystic Snake 1 2 5 |
| Morphling | Adaptive Strike (Agility) 1 2 |
| Morphling | Adaptive Strike (Strength) 1 2 |
| Morphling | Morph |
| Naga Siren | Ensnare 1 |
| Necrophos | Reaper’s Scythe |
| Night Stalker | Void |
| Nyx Assassin | Mind Flare |
| Ogre Magi | Ignite 1 2 |
| Oracle | Fortune’s End 1 3 |
| Oracle | Fate’s Edict |
| Oracle | Purifying Flames |
| Outworld Destroyer | Astral Imprisonment |
| Phantom Assassin | Stifling Dagger 1 2 |
| Phantom Assassin | Phantom Strike |
| Phantom Lancer | Spirit Lance 1 2 |
| Pudge | Dismember |
| Pugna | Decrepify |
| Pugna | Life Drain |
| Queen of Pain | Shadow Strike 1 3 |
| Razor | Static Link |
| Riki | Blink Strike |
| Rubick | Telekinesis 3 |
| Rubick | Fade Bolt 3 |
| Rubick | Spell Steal |
| Shadow Demon | Disruption |
| Shadow Demon | Demonic Purge |
| Shadow Shaman | Ether Shock 3 |
| Shadow Shaman | Hex |
| Shadow Shaman | Shackles |
| Silencer | Last Word 4 |
| Skywrath Mage | Arcane Bolt 1 2 |
| Skywrath Mage | Ancient Seal 3 |
| Slardar | Corrosive Haze |
| Sniper | Assassinate 1 |
| Spirit Breaker | Charge of Darkness 3 |
| Spirit Breaker | Nether Strike 3 |
| Storm Spirit | Electric Vortex 4 |
| Sven | Storm Hammer 1 3 |
| Terrorblade | Sunder |
| Tidehunter | Gush 1 4 |
| Tinker | Laser 3 |
| Treant Protector | Leech Seed |
| Tusk | Snowball |
| Tusk | Walrus Kick |
| Vengeful Spirit | Magic Missile 1 |
| Vengeful Spirit | Nether Swap |
| Viper | Viper Strike 1 |
| Visage | Grave Chill |
| Visage | Soul Assumption 1 2 |
| Warlock | Fatal Bonds 3 |
| Warlock | Shadow Word 4 |
| Windranger | Shackleshot 1 3 |
| Windranger | Focus Fire |
| Winter Wyvern | Splinter Blast 1 3 6 |
| Winter Wyvern | Winter’s Curse 3 |
| Witch Doctor | Paralyzing Cask 1 2 5 |
| Wraith King | Wraithfire Blast 1 2 |
| Zeus | Arc Lightning 3 |

[corpus:liquipedia_dota2/spell_block@2383952#Fully_blocked_abilities]

#### Item abilities

| Item | Ability |
|---|---|
| Abyssal Blade | Overwhelm |
| Bloodthorn | Soul Rend |
| Book of Shadows | Shadows |
| Dagon | Energy Burst 6 |
| Diffusal Blade | Inhibit |
| Ethereal Blade | Ether Blast 1 |
| Fae Grenade | Shadow Brand 1 |
| Eul’s Scepter of Divinity | Cyclone |
| Force Staff | Force |
| Gleipnir | Eternal Chains |
| Heaven’s Halberd | Disarm |
| Hurricane Pike | Hurricane Thrust |
| Nullifier | Nullify 1 |
| Orchid Malevolence | Soul Burn |
| Rod of Atos | Cripple 1 |
| Scythe of Vyse | Hex |
| Wind Waker | Cyclone |

[corpus:liquipedia_dota2/spell_block@2383952#Fully_blocked_abilities]

#### Unit abilities

| Unit | Ability |
|---|---|
| Hill Troll | Ensnare 1 |
| Earth | Hurl Boulder 1 |
| Harpy Stormcrafter | Chain Lightning 3 |
| Mud Golem | Hurl Boulder 1 |
| Necronomicon Archer | Purge |
| Satyr Banisher | Purge |
| Satyr Mindstealer | Mana Burn |
| Shard Golem | Hurl Boulder 1 |
| Storm | Cyclone |

| Marker | Meaning |
|---|---|
| 1 | Projectile-based abilities; blocked upon impact rather than upon cast. |
| 2 | Can hit multiple targets and are blocked for everyone they hit. |
| 3 | Can hit multiple targets but are blocked only for the primary target. When blocked, the spell is completely negated, including its area effects. |
| 4 | Can be upgraded by talents and/or Aghanim’s Scepter so that they are no longer blocked by Spell Block. |
| 5 | Bouncing spells that do not stop bouncing when blocked. |
| 6 | Despite being blocked, their particle effects still fully appear. |

[corpus:liquipedia_dota2/spell_block@2383952#Fully_blocked_abilities]

## Recent changes

| Version | Date | Change |
|---|---|---|
| 7.37 | 2024-07-31 | Earth Spike no longer triggers Spell Block. |
| 7.37 | 2024-07-31 | Burrowstrike no longer triggers Spell Block. |
| 7.32 | 2022-08-24 | Walrus Kick is now blocked by Spell Block. |
| 7.30e | 2021-10-28 | Psychic Push no longer triggers Spell Block. |

[corpus:liquipedia_dota2/spell_block@2383952#Recent_Changes]