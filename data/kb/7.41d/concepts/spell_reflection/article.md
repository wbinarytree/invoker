---
title: Spell Reflection
kind: concept
patch: 7.41d
card:
  entity: spell_reflection
  sentences:
  - text: Spell Reflection is an offensive ability that causes an affected unit to
      cast most single-target spells back at their casters, including basic abilities
      and single-target ultimates.
    marks:
    - corpus:liquipedia_dota2/spell_reflection@2383953
  - text: It can activate automatically as a passive effect or operate as a temporary
      buff.
    marks:
    - corpus:liquipedia_dota2/spell_reflection@2383953#Mechanics
  - text: It reacts only upon cast and does not affect casts already in progress when
      reflection is applied.
    marks:
    - corpus:liquipedia_dota2/spell_reflection@2383953#Mechanics
  - text: It generally applies only when the affected unit is the primary target of
      a single-target spell, with very few area-of-effect exceptions.
    marks:
    - corpus:liquipedia_dota2/spell_reflection@2383953#Mechanics
  - text: A spell blocked by Spell Block is still reflected.
    marks:
    - corpus:liquipedia_dota2/spell_reflection@2383953#Mechanics
  - text: A spell can be reflected only once per cast, preventing reflection loops.
    marks:
    - corpus:liquipedia_dota2/spell_reflection@2383953#Mechanics
  - text: The reflecting hero is treated as the reflected spell’s caster, with an
      instant cast time and no interruption.
    marks:
    - corpus:liquipedia_dota2/spell_reflection@2383953#Mechanics
  - text: Scaling values such as Spell Amplification use the reflecting hero’s stats.
    marks:
    - corpus:liquipedia_dota2/spell_reflection@2383953#Mechanics
  - text: Upgrades from the original caster’s Aghanim items, Talents, and Facets persist
      in the reflected spell, while upgrades held only by the reflecting hero do not
      apply.
    marks:
    - corpus:liquipedia_dota2/spell_reflection@2383953#Mechanics
  - text: Reflected spells do not count as cast events or trigger on-cast effects.
    marks:
    - corpus:liquipedia_dota2/spell_reflection@2383953#Mechanics
  - text: The reflected spell’s effects occur before the original caster’s spell cast.
    marks:
    - corpus:liquipedia_dota2/spell_reflection@2383953#Mechanics
  - text: Projectile-based spells are usually reflected on impact rather than on cast.
    marks:
    - corpus:liquipedia_dota2/spell_reflection@2383953#Projectile
---

# Spell Reflection

Spell Reflection is an offensive ability that causes an affected unit to cast most single-target spells back at their casters, from basic abilities through powerful single-target ultimates. [corpus:liquipedia_dota2/spell_reflection@2383953]

## Definition

| Mechanic | Definition | Example |
|---|---|---|
| Spell Block | Blocks the offensive unit-targeted ability. | Spellblock |
| Spell Reflection | Reflects the offensive unit-targeted ability from the targeted unit to its caster. | Echo Shell |
| Spell Redirection | Redirects the unit-targeted ability from the intended target to another unit. | Soulbind [corpus:liquipedia_dota2/spell_reflection@2383953#Definition] |

All three mechanics work independently of one another. [corpus:liquipedia_dota2/spell_reflection@2383953#Definition]

## Mechanics

Spell Reflection can be a passive effect that activates automatically when a reflectable single-target spell targets the unit, or a buff that reflects spells while active. It reflects spells only upon cast and does not react to casts already in progress when reflection is applied. A spell blocked by Spell Block is still reflected. Multiple layers do not stack, so a spell can be reflected only once per cast. With very few exceptions, area-of-effect spells are not reflected. A single-target spell is not reflected when the unit is only a secondary target; the unit must be the primary target. Projectile-based spells are usually reflected on impact rather than cast, with a few exceptions. [corpus:liquipedia_dota2/spell_reflection@2383953#Mechanics]

A reflected spell is treated as though the reflecting hero literally cast it back at the enemy, with an instant cast time and without interruption. Scaling values such as Spell Amplification use the reflecting hero’s stats rather than the original caster’s. Effects applied to the target on cast are likewise applied to the reflecting hero when the spell is reflected. [corpus:liquipedia_dota2/spell_reflection@2383953#Mechanics]

Aghanim’s Scepter and Aghanim’s Shard upgrades possessed by the original caster persist in the reflected spell even if the reflecting hero lacks the corresponding item. If the original caster lacks the upgrade, the reflected spell is not upgraded even when the reflecting hero carries the item or buff. The same rule applies to upgrades from Talents and Facets. [corpus:liquipedia_dota2/spell_reflection@2383953#Mechanics]

Reflected spells do not count as cast events, do not proc on-cast effects, and do not interrupt or intercept the reflecting hero’s actions. Reflected channeling spells nevertheless require the reflecting hero to remain still, although reflection does not order the hero to stop. Reflection ignores the original spell’s actual cast range regardless of the original caster’s distance, but spells with specifically limited distances, such as Earthshaker’s Fissure, cannot exceed those limits. [corpus:liquipedia_dota2/spell_reflection@2383953#Mechanics]

The reflected spell’s effects occur before the caster’s spell cast. Consequently, reflection still occurs if the reflecting hero dies to the spell or blocks it with Spell Block, while the original spell can be canceled if its caster dies to the reflected damage. If the original and reflected casts are lethal to both units, the original caster dies first and the reflecting hero dies afterward. For example, if Culling Blade is reflected while Axe and his target are below its kill threshold, Axe dies first to the reflecting hero’s Cull, followed by the reflecting hero dying to Axe’s Cull. If damage is delayed through a modifier, as with Laguna Blade, the reflecting hero dies first. [corpus:liquipedia_dota2/spell_reflection@2383953#Mechanics]

An ability’s interaction with Spell Reflection may change when other abilities, Talents, or Aghanim’s Scepter alter it. A single-target spell that becomes non-targeted may cease to be reflectable. [corpus:liquipedia_dota2/spell_reflection@2383953#Mechanics]

Spell Reflection does not reflect active attack modifiers or allied abilities. Reflected spells cannot be reflected again, preventing reflection loops. They remain subject to Spell Block but not Spell Redirection. [corpus:liquipedia_dota2/spell_reflection@2383953#Mechanics]

## Sources of Spell Reflection

| Source | Ability | Interaction |
|---|---|---|
| Anti-Mage | Counterspell | Lotus Orb does not trigger while this ability is active. |
| Lotus Orb | Echo Shell | — |
| Spirit Breaker | Planar Pocket | Has higher priority than Counterspell and Echo Shell. Redirected spells remain subject to every other source of Spell Reflect. [corpus:liquipedia_dota2/spell_reflection@2383953#Sources_of_Spell_Reflection] |

## Not-reflected unit-target abilities

### Unit- and ground-targetable hero abilities

| Hero | Ability |
|---|---|
| Death Prophet | Crypt Swarm |
| Dragon Knight | Breathe Fire |
| Jakiro | Dual Breath |
| Lina | Dragon Slave |
| Lion | Earth Spike |
| Magnus | Shockwave<sup>4</sup> |
| Sand King | Burrowstrike |
| Spectre | Spectral Dagger |
| Tidehunter | Gush<sup>2a 4</sup> |
| Tiny | Tree Throw |
| Troll Warlord | Whirling Axes (Ranged) [corpus:liquipedia_dota2/spell_reflection@2383953#Not-reflected_Unit_Target_Abilities] |

### Hero-based projectile abilities

| Hero | Ability |
|---|---|
| Marci | Rebound |
| Meepo | MegaMeepo Fling |
| Necrophos | Death Seeker<sup>5</sup> [corpus:liquipedia_dota2/spell_reflection@2383953#Not-reflected_Unit_Target_Abilities] |

### Other hero abilities

| Hero | Ability |
|---|---|
| Kez | Kazurai Katana<sup>4</sup> |
| Lifestealer | Infest<sup>5</sup> |
| Morphling | Morph<sup>5</sup> |
| Rubick | Spell Steal<sup>5</sup> [corpus:liquipedia_dota2/spell_reflection@2383953#Not-reflected_Unit_Target_Abilities] |

### Creep abilities

| Unit | Ability |
|---|---|
| Fell Spirit | Vex |
| Raptor | Dive Bomb |
| Roshan | Throw<sup>5</sup> |
| Satyr Tormenter | Shockwave |
| Wildwing Ripper | Hurricane |
| Wildwing | Tornado [corpus:liquipedia_dota2/spell_reflection@2383953#Not-reflected_Unit_Target_Abilities] |

### Item abilities

| Item | Ability |
|---|---|
| Spirit Vessel | Soul Release |
| Urn of Shadows | Soul Release [corpus:liquipedia_dota2/spell_reflection@2383953#Not-reflected_Unit_Target_Abilities] |

Neutral-item abilities cannot be reflected.<sup>6</sup> [corpus:liquipedia_dota2/spell_reflection@2383953#Not-reflected_Unit_Target_Abilities]

| Marker | Meaning |
|---|---|
| 3 | Requires selecting the corresponding Facet. |
| 4 | Missing from the in-game extended ability description. |
| 5 | These spells are visually reflected, but no reflection actually occurs. |
| 6 | Neutral-item abilities cannot be reflected. [corpus:liquipedia_dota2/spell_reflection@2383953#Not-reflected_Unit_Target_Abilities] |

### Active attack modifiers

Auto-casting abilities with an active attack modifier do not trigger Spell Reflect. [corpus:liquipedia_dota2/spell_reflection@2383953#Not-reflected_Unit_Target_Abilities]

| Hero | Ability |
|---|---|
| Ancient Apparition | Chilling Touch<sup>5</sup> |
| Bounty Hunter | Jinada<sup>4 5</sup> |
| Clinkz | Searing Arrows<sup>5</sup> |
| Doom | Infernal Blade<sup>7</sup> |
| Drow Ranger | Frost Arrows |
| Enchantress | Impetus |
| Huskar | Burning Spear |
| Jakiro | Liquid Fire<sup>5</sup> |
| Jakiro | Liquid Frost |
| Kunkka | Tidebringer<sup>4 7</sup> |
| Omniknight | Hammer of Purity<sup>4 5</sup> |
| Outworld Destroyer | Arcane Orb |
| Silencer | Glaives of Wisdom |
| Slark | Saltwater Shiv<sup>7</sup> |
| Tusk | Walrus PUNCH!<sup>5 6</sup> |
| Treant Protector | Leech Seed<sup>4 5</sup> |
| Viper | Poison Attack |
| Weaver | Geminate Attack<sup>4</sup> [corpus:liquipedia_dota2/spell_reflection@2383953#Not-reflected_Unit_Target_Abilities] |

## Bounce abilities

Unit-target abilities that bounce between multiple targets trigger Spell Reflection only on the primary target. [corpus:liquipedia_dota2/spell_reflection@2383953#Bounce]

| Hero or unit | Ability |
|---|---|
| Batrider | Flaming Lasso<sup>2a</sup> |
| Bounty Hunter | Shuriken Toss<sup>3</sup> |
| Dazzle | Shadow Wave |
| Grimstroke | Soulbind |
| Juggernaut | Omnislash |
| Juggernaut | Swiftslash |
| Harpy Stormcrafter | Chain Lightning |
| Hoodwink | Acorn Shot |
| Lich | Chain Frost |
| Medusa | Mystic Snake |
| Nature’s Prophet | Wrath of Nature |
| Rubick | Fade Bolt |
| Tinker | Laser<sup>1</sup> |
| Vengeful Spirit | Magic Missile<sup>2b</sup> |
| Warpine Raider | Seed Shot |
| Warlock | Fatal Bonds |
| Winter Wyvern | Splinter Blast<sup>2b</sup> |
| Witch Doctor | Paralyzing Cask |
| Zeus | Arc Lightning [corpus:liquipedia_dota2/spell_reflection@2383953#Bounce] |

| Marker | Requirement |
|---|---|
| 1 | Requires a Talent. |
| 2a | Requires Aghanim’s Scepter. |
| 2b | Requires Aghanim’s Shard. |
| 3 | Requires selecting the corresponding Facet. [corpus:liquipedia_dota2/spell_reflection@2383953#Bounce] |

## Multiple-target abilities

The following multiple-target abilities are independently reflectable by each target. [corpus:liquipedia_dota2/spell_reflection@2383953#Multiple_Target]

| Hero or item | Ability |
|---|---|
| Bane | Brain Sap<sup>2b</sup> |
| Dazzle | Poison Touch |
| Lion | Finger of Death<sup>2a</sup> |
| Night Stalker | Void<sup>3</sup> |
| Nyx Assassin | Mind Flare<sup>1</sup> |
| Phantom Assassin | Stifling Dagger<sup>1</sup> |
| Skywrath Mage | Arcane Bolt<sup>2b</sup> |
| Skywrath Mage | Ancient Seal<sup>2a</sup> |
| Visage | Soul Assumption<sup>1</sup> |
| Zeus | Lightning Bolt<sup>1</sup> |
| Gleipnir | Eternal Chains [corpus:liquipedia_dota2/spell_reflection@2383953#Multiple_Target] |

| Marker | Requirement |
|---|---|
| 1 | Requires a Talent. |
| 2a | Requires Aghanim’s Scepter. |
| 2b | Requires Aghanim’s Shard. [corpus:liquipedia_dota2/spell_reflection@2383953#Multiple_Target] |

## Point-target abilities

### Reflectable

| Hero or item | Ability |
|---|---|
| Earth Spirit | Boulder Smash |
| Nature’s Prophet | Wrath of Nature<sup>4</sup> |
| Night Stalker | Void<sup>3</sup> |
| Zeus | Lightning Bolt<sup>5</sup> |
| Gleipnir | Eternal Chains [corpus:liquipedia_dota2/spell_reflection@2383953#Point_Target] |

### Not reflectable after an upgrade

| Hero | Ability |
|---|---|
| Lion | Hex<sup>1</sup> |
| Lich | Sinister Gaze<sup>2a</sup> |
| Storm Spirit | Electric Vortex<sup>2a</sup> |
| Queen of Pain | Shadow Strike<sup>2a</sup> [corpus:liquipedia_dota2/spell_reflection@2383953#Point_Target] |

| Marker | Interaction |
|---|---|
| 4 | If Wrath of Nature is ground-targeted, it can still be reflected before the first bounce. |
| 5 | If Lightning Bolt is ground-targeted, it can still be reflected. Bolts from Nimbus are not reflected. [corpus:liquipedia_dota2/spell_reflection@2383953#Point_Target] |

Nature’s Prophet’s Sprout is reflected only when unit-targeted. [corpus:liquipedia_dota2/spell_reflection@2383953#Point_Target]

## Projectile abilities

Projectile abilities reflect on impact rather than cast. Hero-based projectiles usually reflect on impact. [corpus:liquipedia_dota2/spell_reflection@2383953#Projectile]

### Reflectable on impact

| Hero | Ability |
|---|---|
| Huskar | Life Break |
| Tiny | Toss |
| Tusk | Snowball |
| Spirit Breaker | Charge of Darkness |
| Sven | Storm Hammer (Alt-Cast) [corpus:liquipedia_dota2/spell_reflection@2383953#Projectile] |

### Reflectable on cast

| Hero | Ability |
|---|---|
| Spirit Breaker | Charge of Darkness [corpus:liquipedia_dota2/spell_reflection@2383953#Projectile] |

## Usually reflected without Aghanim upgrades

These abilities require having a specific ability to apply Aghanim upgrades when reflecting. [corpus:liquipedia_dota2/spell_reflection@2383953#Usually_reflected_without_Aghanim_upgrades]

### Temp

| Hero | Ability |
|---|---|
| Bane | Fiend’s Grip<sup>1</sup> |
| Enigma | Malefice [corpus:liquipedia_dota2/spell_reflection@2383953#Usually_reflected_without_Aghanim_upgrades] |

<sup>1</sup> Creates illusions, but they instantly die. [corpus:liquipedia_dota2/spell_reflection@2383953#Usually_reflected_without_Aghanim_upgrades]

## Other unique interactions

| Hero | Ability | Interaction |
|---|---|---|
| Bane | Nightmare | Reflected on cast and when attacking a unit affected by an enemy Nightmare. |
| Chaos Knight | Chaos Bolt | Reflected on impact. Its damage and stun values are rerolled rather than copied from the original caster’s roll. |
| Chaos Knight | Reality Rift | Sets a new random position between the original caster and reflecting hero, overriding the location randomized by the original caster. |
| Crystal Maiden | Frostbite | Reflected only when manually cast, not when applied by Freezing Field. |
| Invoker | Cold Snap | The reflected Cold Snap’s level is based on Invoker’s Quas level. |
| Ogre Magi | Fireblast | Reflects each multicast instance as it occurs. |
| Ogre Magi | Unrefined Fireblast | Reflects each multicast instance as it occurs. |
| Phantom Assassin | Phantom Strike | The original caster ends at the reflecting hero’s position, not the other way around. |
| Riki | Blink Strike | The original caster ends at the reflecting hero’s position, not the other way around. |
| Spirit Breaker | Charge of Darkness | Reflected on cast rather than impact. The reflecting hero does not apply Greater Bash. |
| Spirit Breaker | Nether Strike | The original caster ends at the reflecting hero’s position, not the other way around. The reflecting hero does not apply Greater Bash. |
| Vengeful Spirit | Nether Swap | Essentially nullifies the spell completely. The swap back occurs so quickly that even distance-based effects, such as Dream Coil’s leash breaking, cannot react to it. |
| Visage | Soul Assumption | Damage depends on how many charges the original caster had for the cast. [corpus:liquipedia_dota2/spell_reflection@2383953#Other_Unique_interactions] |

## Fully reflected abilities

The following abilities are fully reflected by Spell Reflection. [corpus:liquipedia_dota2/spell_reflection@2383953#Fully_reflected_abilities]

### Hero abilities

| Hero | Ability |
|---|---|
| Abaddon | Mist Coil<sup>1</sup> |
| Ancient Apparition | Cold Feet<sup>4</sup> |
| Anti-Mage | Mana Void<sup>3</sup> |
| Arc Warden | Flux |
| Axe | Battle Hunger |
| Axe | Culling Blade |
| Bane | Enfeeble |
| Bane | Brain Sap |
| Bane | Fiend’s Grip |
| Batrider | Flaming Lasso<sup>3</sup> |
| Beastmaster | Primal Roar<sup>3</sup> |
| Bloodseeker | Bloodrage |
| Bloodseeker | Rupture |
| Bounty Hunter | Shuriken Toss<sup>1 3</sup> |
| Bounty Hunter | Track |
| Bristleback | Viscous Nasal Goo<sup>1 4</sup> |
| Broodmother | Spawn Spiderlings<sup>1</sup> |
| Centaur Warrunner | Double Edge<sup>3</sup> |
| Chen | Penitence<sup>1</sup> |
| Dark Willow | Cursed Crown |
| Dazzle | Poison Touch<sup>3 5</sup> |
| Death Prophet | Spirit Siphon |
| Disruptor | Thunder Strike |
| Disruptor | Glimpse |
| Doom | Doom |
| Dragon Knight | Dragon Tail<sup>1</sup> |
| Earth Spirit | Boulder Smash<sup>3</sup> |
| Earth Spirit | Enchant Remnant |
| Enchantress | Enchant |
| Enigma | Malefice |
| Grimstroke | Phantom’s Embrace<sup>5</sup> |
| Gyrocopter | Homing Missile<sup>1</sup> |
| Huskar | Life Break<sup>1</sup> |
| Juggernaut | Omnislash<sup>3</sup> |
| Kunkka | X Marks the Spot |
| Legion Commander | Duel |
| Leshrac | Lightning Storm<sup>3</sup> |
| Lich | Frost Blast<sup>3</sup> |
| Lich | Sinister Gaze<sup>4</sup> |
| Lich | Chain Frost<sup>1 3</sup> |
| Lifestealer | Open Wounds |
| Lina | Laguna Blade |
| Lion | Hex<sup>4</sup> |
| Lion | Mana Drain<sup>3</sup> |
| Lion | Finger of Death<sup>3</sup> |
| Luna | Lucent Beam |
| Medusa | Mystic Snake<sup>1 3</sup> |
| Morphling | Adaptive Strike (Agility)<sup>1 2</sup> |
| Morphling | Adaptive Strike (Strength)<sup>1 2</sup> |
| Naga Siren | Ensnare<sup>1</sup> |
| Necrophos | Reaper’s Scythe |
| Night Stalker | Void |
| Nyx Assassin | Mana Burn |
| Ogre Magi | Ignite<sup>1 3</sup> |
| Oracle | Fortune’s End<sup>1 3</sup> |
| Oracle | Fate’s Edict |
| Oracle | Purifying Flames |
| Outworld Destroyer | Astral Imprisonment |
| Phantom Assassin | Stifling Dagger<sup>1 2</sup> |
| Phantom Lancer | Spirit Lance<sup>1 2</sup> |
| Pudge | Dismember |
| Pugna | Decrepify |
| Pugna | Life Drain |
| Queen of Pain | Shadow Strike<sup>1 3</sup> |
| Razor | Static Link |
| Rubick | Telekinesis<sup>3</sup> |
| Rubick | Fade Bolt<sup>3</sup> |
| Shadow Demon | Disruption |
| Shadow Demon | Demonic Purge |
| Shadow Shaman | Ether Shock<sup>3</sup> |
| Shadow Shaman | Hex |
| Shadow Shaman | Shackles |
| Silencer | Last Word<sup>4</sup> |
| Skywrath Mage | Arcane Bolt<sup>1 2</sup> |
| Skywrath Mage | Ancient Seal<sup>3</sup> |
| Slardar | Corrosive Haze |
| Sniper | Assassinate<sup>1</sup> |
| Spectre | Shadow Step |
| Storm Spirit | Electric Vortex<sup>4</sup> |
| Sven | Storm Hammer<sup>1 3</sup> |
| Terrorblade | Sunder |
| Tidehunter | Gush<sup>1 4</sup> |
| Tinker | Laser<sup>3</sup> |
| Treant Protector | Leech Seed |
| Tusk | Snowball<sup>1</sup> |
| Tusk | Walrus Kick |
| Undying | Soul Rip |
| Vengeful Spirit | Magic Missile<sup>1</sup> |
| Viper | Viper Strike<sup>1</sup> |
| Visage | Grave Chill |
| Warlock | Fatal Bonds<sup>3</sup> |
| Warlock | Shadow Word<sup>4</sup> |
| Windranger | Shackleshot<sup>1 3</sup> |
| Windranger | Focus Fire |
| Winter Wyvern | Splinter Blast<sup>1 3</sup> |
| Winter Wyvern | Winter’s Curse<sup>3</sup> |
| Witch Doctor | Paralyzing Cask<sup>1 3</sup> |
| Wraith King | Wraithfire Blast<sup>1 2</sup> |
| Zeus | Arc Lightning<sup>3</sup> [corpus:liquipedia_dota2/spell_reflection@2383953#Fully_reflected_abilities] |

### Item abilities

| Item | Ability |
|---|---|
| Abyssal Blade | Overwhelm |
| Bloodthorn | Soul Rend |
| Dagon | Energy Burst |
| Diffusal Blade | Inhibit |
| Ethereal Blade | Ether Blast<sup>1</sup> |
| Eul’s Scepter of Divinity | Cyclone |
| Force Staff | Force |
| Heaven’s Halberd | Disarm |
| Hurricane Pike | Hurricane Thrust |
| Nullifier | Nullify<sup>1</sup> |
| Orchid Malevolence | Soul Burn |
| Rod of Atos | Cripple<sup>1</sup> |
| Scythe of Vyse | Hex [corpus:liquipedia_dota2/spell_reflection@2383953#Fully_reflected_abilities] |

### Unit abilities

| Unit | Ability |
|---|---|
| Hill Troll | Ensnare<sup>1</sup> |
| Earth | Hurl Boulder<sup>1</sup> |
| Harpy Stormcrafter | Chain Lightning<sup>3</sup> |
| Mud Golem | Hurl Boulder<sup>1</sup> |
| Necronomicon Archer | Purge |
| Satyr Banisher | Purge |
| Satyr Mindstealer | Mana Burn |
| Shard Golem | Hurl Boulder<sup>1</sup> |
| Storm | Cyclone [corpus:liquipedia_dota2/spell_reflection@2383953#Fully_reflected_abilities] |

| Marker | Interaction |
|---|---|
| 1 | Projectile-based abilities; reflected on impact rather than cast. |
| 2 | These abilities can hit multiple targets and are reflected by everyone they hit. |
| 3 | These abilities can hit multiple targets but are reflected only by the primary target. |
| 4 | Talents and/or Aghanim’s Scepter can upgrade these abilities so that Spell Reflection no longer reflects them. |
| 5 | Although projectile-based, these abilities are reflected on cast rather than impact. [corpus:liquipedia_dota2/spell_reflection@2383953#Fully_reflected_abilities] |

## Recent changes

| Version | Date | Change |
|---|---|---|
| 7.38 | 2025-02-19 | Reflected spells now benefit from all bonuses possessed by the original cast, including the caster’s Facet upgrades, bonuses from Talents, and Aghanim’s Shard and Aghanim’s Scepter upgrades. These upgrades previously depended on the Aghanim’s items possessed by the reflecting unit. |
| 7.30e | 2021-10-28 | Psychic Push no longer triggers Spell Reflection. |
| 7.23 | 2019-11-26 | Added the new Echo Shield ability, which uses the Spell Reflection mechanic. [corpus:liquipedia_dota2/spell_reflection@2383953#Recent_Changes] |