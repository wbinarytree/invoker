---
title: Spell Lifesteal
kind: concept
patch: 7.41d
card:
  entity: spell_lifesteal
  sentences:
  - text: Spell lifesteal heals a hero for a percentage of the actual spell damage
      dealt to units, limits overkill healing to the target’s remaining health, and
      has 20% of its hero value against creeps.
    marks:
    - corpus:liquipedia_dota2/spell_lifesteal@2383668
    - corpus:liquipedia_dota2/spell_lifesteal@2383668#Sources
  - text: It does not interact with pure spell-damage sources.
    marks:
    - corpus:liquipedia_dota2/spell_lifesteal@2383668
  - text: Multiple instances from the same source do not stack, while different sources
      stack additively.
    marks:
    - corpus:liquipedia_dota2/spell_lifesteal@2383668#Sources
  - text: Most sources treat Creep-Heroes as heroes and Roshan as a creep.
    marks:
    - corpus:liquipedia_dota2/spell_lifesteal@2383668#Sources
  - text: The listed item sources from Voodoo Mask, Bloodstone, Revenant's Brooch,
      and Vampiric Enchantment do not restore health against illusions.
    marks:
    - corpus:liquipedia_dota2/spell_lifesteal@2383668#Items
  - text: Talent-granted spell lifesteal works on spell damage dealt to enemy or allied
      units, but not buildings, wards, or self.
    marks:
    - corpus:liquipedia_dota2/spell_lifesteal@2383668#Details
  - text: It heals from all 3 damage types after all reductions.
    marks:
    - corpus:liquipedia_dota2/spell_lifesteal@2383668#Details
  - text: Damage dealt by summons, including wards, does not spell lifesteal.
    marks:
    - corpus:liquipedia_dota2/spell_lifesteal@2383668#Details
  - text: Existing hero values are 6%/8%/10%/12%/13%/15%/20%/25%/30%/40%/50%/60%/70%,
      while creep values are 1.2%/1.6%/2%/2.4%/2.6%/3%/4%/5%/6%/8%/10%/12%/14%.
    marks:
    - corpus:liquipedia_dota2/spell_lifesteal@2383668#Details
  - text: Instant-kill effects marked 1 trigger spell lifesteal based on the killed
      unit’s remaining health.
    marks:
    - corpus:liquipedia_dota2/spell_lifesteal@2383668#Working
  - text: Some spell-damage and HP Removal abilities cannot use spell lifesteal, and
      attack-damage abilities require regular lifesteal instead.
    marks:
    - corpus:liquipedia_dota2/spell_lifesteal@2383668#Not_Working
  - text: Version 7.27 added spell lifesteal manipulation as a separate mechanic on
      2020-06-28.
    marks:
    - corpus:liquipedia_dota2/spell_lifesteal@2383668#Recent_Changes
---

# Spell Lifesteal

## Overview

Spell lifesteal heals a hero from spell damage they deal. Like attack-damage lifesteal, it is calculated as a percentage of the actual damage dealt to units. Unlike attack-damage lifesteal, it does not heal from overkill damage: when damage exceeds a target’s current health and kills it, healing is based on the target’s remaining health. It does not interact with pure spell-damage sources. [corpus:liquipedia_dota2/spell_lifesteal@2383668]

## Sources

Multiple instances from the same source, such as multiple Bloodstones, do not stack. Spell lifesteal from different sources, including different items, stacks additively. Against creeps, it has 20% of its value against heroes. Most sources consider Creep-Heroes heroes and Roshan a creep. [corpus:liquipedia_dota2/spell_lifesteal@2383668#Sources]

| Hero | Source | Markers |
|---|---|---|
| Grimstroke | Ink Swell | 5 |
| Kez | Raptor Dance | 4 |
| Muerta | Pierce the Veil | 2b, 4, 5 |
| Skywrath Mage | Ruin and Restoration | — |
| Queen of Pain | Succubus | 5 |

Markers: **1** requires a talent; **2a** requires Aghanim’s Scepter; **2b** requires Aghanim’s Shard; **4** considers Creep-Heroes creeps and Spirit Bear a hero; **5** does not restore health against illusions. [corpus:liquipedia_dota2/spell_lifesteal@2383668#Sources]

### Items

| Item | Source |
|---|---|
| Voodoo Mask | Spell Lifesteal |
| Bloodstone | Spell Lifesteal |
| Bloodstone | Bloodpact |
| Revenant's Brooch | Spell Lifesteal |
| Vampiric Enchantment | Spell Lifesteal |

These item sources do not restore health against illusions. [corpus:liquipedia_dota2/spell_lifesteal@2383668#Items]

### Talents

| Property | Value |
|---|---|
| Ability | Passive |
| Affects | Self |
| Hero Spell Lifesteal | Varies |
| Creep Spell Lifesteal | Varies |

[corpus:liquipedia_dota2/spell_lifesteal@2383668#Talents]

The talent grants spell lifesteal, healing the hero from spell damage they deal. It heals from spell damage against enemy or allied units except the excluded abilities, but not from damage against buildings, wards, or self. It heals from all 3 damage types after all reductions and from most instantly killing effects. Damage dealt by summons, including wards, does not spell lifesteal. [corpus:liquipedia_dota2/spell_lifesteal@2383668#Details]

| Target class | Existing values |
|---|---|
| Hero spell lifesteal | 6%/8%/10%/12%/13%/15%/20%/25%/30%/40%/50%/60%/70% |
| Creep spell lifesteal | 1.2%/1.6%/2%/2.4%/2.6%/3%/4%/5%/6%/8%/10%/12%/14% |

The talent table uses Level 10, Level 15, Level 20, and Level 25 headings, each divided into Left and Right, and contains the following bonus entry:

| Bonus | Value |
|---|---|
| Spell Lifesteal | 8% |

[corpus:liquipedia_dota2/spell_lifesteal@2383668#Details]

## Item and Ability Interactions

Compatibility is ability-dependent: some items and abilities work with spell lifesteal, while others do not. [corpus:liquipedia_dota2/spell_lifesteal@2383668#Item_and_Abilities]

### Working

| Type | Unit or item | Ability | Marker |
|---|---|---|---|
| Unit | Abaddon | Mist Coil | — |
| Unit | Abaddon | Aphotic Shield | — |
| Unit | Alchemist | Acid Spray | — |
| Unit | Alchemist | Unstable Concoction | — |
| Unit | Ancient Apparition | Cold Feet | — |
| Unit | Ancient Apparition | Chilling Touch | — |
| Unit | Ancient Apparition | Ice Blast | 1 |
| Unit | Anti-Mage | Mana Void | — |
| Unit | Arc Warden | Flux | — |
| Unit | Arc Warden | Spark Wraith | — |
| Unit | Axe | Battle Hunger | — |
| Unit | Axe | Counter Helix | — |
| Unit | Axe | Culling Blade | 1 |
| Unit | Bane | Brain Sap | — |
| Unit | Bane | Nightmare | — |
| Unit | Bane | Fiend's Grip | — |
| Unit | Batrider | Sticky Napalm | — |
| Unit | Batrider | Flamebreak | — |
| Unit | Batrider | Firefly | — |
| Unit | Beastmaster | Wild Axes | — |
| Unit | Beastmaster | Primal Roar | — |
| Unit | Bloodseeker | Blood Rite | — |
| Unit | Bloodseeker | Rupture | — |
| Unit | Bounty Hunter | Shuriken Toss | — |
| Unit | Bounty Hunter | Shadow Walk | — |
| Unit | Brewmaster | Thunder Clap | — |
| Unit | Bristleback | Quill Spray | — |
| Unit | Broodmother | Spawn Spiderlings | — |
| Unit | Centaur Warrunner | Hoof Stomp | — |
| Unit | Centaur Warrunner | Double Edge | — |
| Unit | Centaur Warrunner | Retaliate | — |
| Unit | Centaur Warrunner | Stampede | — |
| Unit | Chaos Knight | Chaos Bolt | — |
| Unit | Clinkz | Searing Arrows | — |
| Unit | Clockwerk | Battery Assault | — |
| Unit | Clockwerk | Power Cogs | 2 |
| Unit | Clockwerk | Rocket Flare | — |
| Unit | Clockwerk | Hookshot | — |
| Unit | Crystal Maiden | Crystal Nova | — |
| Unit | Crystal Maiden | Frostbite | — |
| Unit | Crystal Maiden | Freezing Field | — |
| Unit | Dark Seer | Vacuum | — |
| Unit | Dark Seer | Ion Shell | — |
| Unit | Dark Seer | Wall of Replica | — |
| Unit | Dazzle | Poison Touch | — |
| Unit | Dazzle | Shadow Wave | — |
| Unit | Death Prophet | Crypt Swarm | — |
| Unit | Death Prophet | Spirit Siphon | — |
| Unit | Death Prophet | Exorcism | — |
| Unit | Disruptor | Thunder Strike | — |
| Unit | Disruptor | Static Storm | — |
| Unit | Doom | Devour | 1 |
| Unit | Doom | Scorched Earth | — |
| Unit | Doom | Infernal Blade | — |
| Unit | Doom | Doom | — |
| Unit | Dragon Knight | Breathe Fire | — |
| Unit | Dragon Knight | Dragon Tail | — |
| Unit | Dragon Knight | Elder Dragon Form | — |
| Unit | Earth Spirit | Boulder Smash | — |
| Unit | Earth Spirit | Rolling Boulder | — |
| Unit | Earth Spirit | Geomagnetic Grip | — |
| Unit | Earth Spirit | Magnetize | — |
| Unit | Earth Spirit | Enchant Remnant | — |
| Unit | Earthshaker | Fissure | — |
| Unit | Earthshaker | Aftershock | — |
| Unit | Earthshaker | Echo Slam | — |
| Unit | Elder Titan | Echo Stomp | — |
| Unit | Elder Titan | Astral Spirit | — |
| Unit | Elder Titan | Earth Splitter | — |
| Unit | Ember Spirit | Searing Chains | — |
| Unit | Ember Spirit | Flame Guard | — |
| Unit | Ember Spirit | Activate Fire Remnant | — |
| Unit | Enchantress | Impetus | — |
| Unit | Enigma | Malefice | — |
| Unit | Enigma | Demonic Conversion | 1 |
| Unit | Enigma | Midnight Pulse | — |
| Unit | Enigma | Black Hole | — |
| Unit | Gyrocopter | Rocket Barrage | — |
| Unit | Gyrocopter | Homing Missile | 2 |
| Unit | Gyrocopter | Call Down | — |
| Unit | Huskar | Burning Spear | — |
| Unit | Huskar | Life Break | — |
| Unit | Invoker | Cold Snap | — |
| Unit | Invoker | Ice Wall | — |
| Unit | Invoker | E.M.P. | — |
| Unit | Invoker | Tornado | — |
| Unit | Invoker | Sun Strike | — |
| Unit | Invoker | Chaos Meteor | — |
| Unit | Invoker | Deafening Blast | — |
| Unit | Io | Spirits | — |
| Unit | Jakiro | Dual Breath | — |
| Unit | Jakiro | Ice Path | — |
| Unit | Jakiro | Liquid Fire | — |
| Unit | Jakiro | Macropyre | — |
| Unit | Juggernaut | Blade Fury | — |
| Unit | Keeper of the Light | Illuminate | — |
| Unit | Kunkka | Torrent | — |
| Unit | Kunkka | Ghostship | 3 |
| Unit | Legion Commander | Overwhelming Odds | — |
| Unit | Leshrac | Split Earth | — |
| Unit | Leshrac | Diabolic Edict | — |
| Unit | Leshrac | Lightning Storm | — |
| Unit | Leshrac | Pulse Nova | — |
| Unit | Lich | Frost Blast | — |
| Unit | Lich | Chain Frost | — |
| Unit | Lifestealer | Consume | — |
| Unit | Lina | Dragon Slave | — |
| Unit | Lina | Light Strike Array | — |
| Unit | Lina | Laguna Blade | — |
| Unit | Lion | Earth Spike | — |
| Unit | Lion | Finger of Death | — |
| Unit | Luna | Lucent Beam | — |
| Unit | Luna | Eclipse | — |
| Unit | Magnus | Shockwave | — |
| Unit | Magnus | Skewer | — |
| Unit | Magnus | Reverse Polarity | — |
| Unit | Medusa | Mystic Snake | — |
| Unit | Meepo | Poof | — |
| Unit | Meepo | Ransack | — |
| Unit | Mirana | Starstorm | — |
| Unit | Mirana | Sacred Arrow | — |
| Unit | Monkey King | Primal Spring | — |
| Unit | Morphling | Waveform | — |
| Unit | Morphling | Adaptive Strike (Agility) | — |
| Unit | Naga Siren | Rip Tide | — |
| Unit | Nature's Prophet | Wrath of Nature | — |
| Unit | Necrophos | Death Pulse | — |
| Unit | Necrophos | Reaper's Scythe | — |
| Unit | Night Stalker | Void | — |
| Unit | Nyx Assassin | Impale | — |
| Unit | Nyx Assassin | Mind Flare | — |
| Unit | Nyx Assassin | Spiked Carapace | — |
| Unit | Nyx Assassin | Vendetta | — |
| Unit | Ogre Magi | Fireblast | — |
| Unit | Ogre Magi | Ignite | — |
| Unit | Ogre Magi | Unrefined Fireblast | — |
| Unit | Omniknight | Purification | — |
| Unit | Oracle | Fortune's End | — |
| Unit | Oracle | Purifying Flames | — |
| Unit | Outworld Destroyer | Arcane Orb | — |
| Unit | Outworld Destroyer | Astral Imprisonment | — |
| Unit | Outworld Destroyer | Sanity's Eclipse | — |
| Unit | Phantom Lancer | Spirit Lance | — |
| Unit | Phoenix | Icarus Dive | — |
| Unit | Phoenix | Fire Spirits | — |
| Unit | Phoenix | Sun Ray | — |
| Unit | Phoenix | Supernova | — |
| Unit | Puck | Illusory Orb | — |
| Unit | Puck | Waning Rift | — |
| Unit | Puck | Dream Coil | — |
| Unit | Pudge | Meat Hook | — |
| Unit | Pudge | Rot | — |
| Unit | Pudge | Dismember | — |
| Unit | Pugna | Nether Blast | — |
| Unit | Pugna | Life Drain | — |
| Unit | Queen of Pain | Shadow Strike | — |
| Unit | Queen of Pain | Scream of Pain | — |
| Unit | Queen of Pain | Sonic Wave | — |
| Unit | Razor | Plasma Field | — |
| Unit | Razor | Eye of the Storm | — |
| Unit | Riki | Blink Strike | — |
| Unit | Rubick | Fade Bolt | — |
| Unit | Sand King | Burrowstrike | — |
| Unit | Sand King | Sand Storm | — |
| Unit | Sand King | Caustic Finale | — |
| Unit | Sand King | Epicenter | — |
| Unit | Shadow Demon | Shadow Poison | — |
| Unit | Shadow Demon | Demonic Purge | — |
| Unit | Shadow Fiend | Shadowraze | — |
| Unit | Shadow Fiend | Requiem of Souls | — |
| Unit | Shadow Shaman | Ether Shock | — |
| Unit | Shadow Shaman | Shackles | — |
| Unit | Silencer | Arcane Curse | — |
| Unit | Silencer | Glaives of Wisdom | — |
| Unit | Silencer | Last Word | — |
| Unit | Skywrath Mage | Arcane Bolt | — |
| Unit | Skywrath Mage | Concussive Shot | — |
| Unit | Skywrath Mage | Mystic Flare | — |
| Unit | Slardar | Slithereen Crush | — |
| Unit | Slark | Dark Pact | — |
| Unit | Slark | Pounce | — |
| Unit | Sniper | Shrapnel | — |
| Unit | Sniper | Assassinate | — |
| Unit | Spectre | Spectral Dagger | — |
| Unit | Spectre | Desolate | — |
| Unit | Spirit Breaker | Greater Bash | — |
| Unit | Spirit Breaker | Nether Strike | — |
| Unit | Storm Spirit | Static Remnant | — |
| Unit | Storm Spirit | Overload | — |
| Unit | Storm Spirit | Ball Lightning | — |
| Unit | Sven | Storm Hammer | — |
| Unit | Techies | Blast Off! | — |
| Unit | Templar Assassin | Meld | — |
| Unit | Templar Assassin | Psi Blades | — |
| Unit | Tidehunter | Gush | — |
| Unit | Tidehunter | Ravage | — |
| Unit | Timbersaw | Whirling Death | — |
| Unit | Timbersaw | Timber Chain | — |
| Unit | Timbersaw | Chakram | — |
| Unit | Timbersaw | Second Chakram | — |
| Unit | Tinker | Laser | — |
| Unit | Tinker | Heat-Seeking Missile | — |
| Unit | Tiny | Avalanche | — |
| Unit | Tiny | Toss | — |
| Unit | Treant Protector | Leech Seed | — |
| Unit | Treant Protector | Overgrowth | — |
| Unit | Troll Warlord | Whirling Axes (Ranged) | — |
| Unit | Troll Warlord | Whirling Axes (Melee) | — |
| Unit | Tusk | Ice Shards | — |
| Unit | Tusk | Snowball | — |
| Unit | Undying | Decay | — |
| Unit | Undying | Soul Rip | 4 |
| Unit | Ursa | Earthshock | — |
| Unit | Vengeful Spirit | Magic Missile | — |
| Unit | Vengeful Spirit | Wave of Terror | — |
| Unit | Venomancer | Venomous Gale | — |
| Unit | Venomancer | Poison Nova | — |
| Unit | Viper | Poison Attack | — |
| Unit | Viper | Nethertoxin | — |
| Unit | Viper | Corrosive Skin | — |
| Unit | Viper | Viper Strike | — |
| Unit | Visage | Soul Assumption | — |
| Unit | Warlock | Fatal Bonds | — |
| Unit | Warlock | Shadow Word | — |
| Unit | Weaver | The Swarm | 2 |
| Unit | Weaver | Shukuchi | — |
| Unit | Windranger | Powershot | — |
| Unit | Winter Wyvern | Arctic Burn | — |
| Unit | Winter Wyvern | Splinter Blast | — |
| Unit | Witch Doctor | Paralyzing Cask | — |
| Unit | Witch Doctor | Maledict | — |
| Unit | Wraith King | Wraithfire Blast | — |
| Unit | Zeus | Arc Lightning | — |
| Unit | Zeus | Lightning Bolt | — |
| Unit | Zeus | Heavenly Jump | — |
| Unit | Zeus | Thundergod's Wrath | — |
| Unit | Centaur Conqueror | War Stomp | — |
| Unit | Harpy Stormcrafter | Chain Lightning | — |
| Unit | Hellbear Smasher | Thunder Clap | — |
| Unit | Mud Golem | Hurl Boulder | — |
| Unit | Satyr Mindstealer | Mana Burn | — |
| Unit | Satyr Tormenter | Shockwave | — |
| Unit | Spirit Bear | Entangling Claws | — |
| Item | Orb of Venom | Poison Attack | — |
| Item | Urn of Shadows | Soul Release | — |
| Item | Spirit Vessel | Soul Release | — |
| Item | Dagon | Energy Burst | — |
| Item | Eul's Scepter of Divinity | Cyclone | — |
| Item | Orchid Malevolence | Soul Burn | — |
| Item | Ethereal Blade | Ether Blast | — |
| Item | Radiance | Burn | — |
| Item | Lotus Orb | Echo Shell | — |
| Item | Shiva's Guard | Arctic Blast | — |
| Item | Meteor Hammer | Meteor Hammer | — |
| Item | Maelstrom | Chain Lightning | — |
| Item | Mjollnir | Chain Lightning | — |
| Item | Mjollnir | Static Charge | — |
| Item | Hand of Midas | Transmute | 1 |
| Item | Bloodthorn | Soul Rend | — |
| Item | Giant's Ring | Giant's Foot | — |

Marker **1** means the instant-kill effect triggers spell lifesteal, with healing based on the killed unit’s remaining health. Marker **2** means that, despite using separate units to apply their effects, the abilities treat the caster as the damage source, so spell lifesteal procs and heals. Marker **3** means Ghostship’s rum wear-off health loss does not proc spell lifesteal. Marker **4** means Soul Rip does not spell lifesteal from the area health cost and steals life only when targeting an enemy to damage it. [corpus:liquipedia_dota2/spell_lifesteal@2383668#Working]

### Not Working

Some abilities that deal spell damage or are flagged as HP Removal cannot use spell lifesteal. Abilities and items that deal attack damage also cannot use it and require regular lifesteal instead. [corpus:liquipedia_dota2/spell_lifesteal@2383668#Not_Working]

| Unit or item | Ability | Markers |
|---|---|---|
| Earthshaker | Enchant Totem | 2a |
| Kunkka | Tidebringer | 4 |
| Lion | Finger of Death | 3 |
| Magnus | Empower | — |
| Sven | Great Cleave | — |
| Underlord | Atrophy Aura | 3 |
| Battle Fury | Cleave | — |
| Luna | Moon Glaives | — |
| Necrophos | Heartstopper Aura | — |
| Oracle | False Promise | — |
| Spectre | Dispersion | — |
| Terrorblade | Sunder | — |
| Venomancer | Poison Sting | — |
| Venomancer | Poison Sting | — |
| Weaver | Time Lapse | — |
| Witch Doctor | Death Ward | 1, 2 |
| Witch Doctor | Voodoo Switcheroo | 1, 2 |
| Blade Mail | Damage Return | — |

Marker **1** requires Aghanim’s Scepter; marker **2** requires Aghanim’s Shard. [corpus:liquipedia_dota2/spell_lifesteal@2383668#Not_Working]

## Spell Lifesteal Manipulation

The source notation for spell-lifesteal-manipulation sources defines marker **1** as requiring a talent, **2a** as requiring Aghanim’s Scepter, and **2b** as requiring Aghanim’s Shard. [corpus:liquipedia_dota2/spell_lifesteal@2383668#Spell_Lifesteal_Manipulation]

## Recent Changes

| Version | Date | Description |
|---|---|---|
| 7.27 | (2020-06-28) | Lifesteal manipulation no longer affects spell lifesteal. Added spell lifesteal manipulation as a separate mechanic. |

[corpus:liquipedia_dota2/spell_lifesteal@2383668#Recent_Changes]