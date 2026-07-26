---
title: Break
kind: concept
patch: 7.41d
card:
  entity: break
  sentences:
  - text: Break is a status effect that fully disables passive abilities but, with
      some exceptions, does not disable item passives or talents.
    marks:
    - corpus:liquipedia_dota2/break@2404623#Definition
  - text: Break works completely independently from mute and silence.
    marks:
    - corpus:liquipedia_dota2/break@2404623
  - text: It disables affected abilities’ proc chances, innate cooldowns, attack modifiers,
      and permanent bonuses.
    marks:
    - corpus:liquipedia_dota2/break@2404623#Mechanics
  - text: Buffs, debuffs, and stacks already applied by a passive usually remain,
      while Break prevents new applications or stacks.
    marks:
    - corpus:liquipedia_dota2/break@2404623#Mechanics
  - text: An aura source under Break continues applying the aura, but its buff or
      debuff is disabled for the duration and any HUD status icon shows 0.
    marks:
    - corpus:liquipedia_dota2/break@2404623#Mechanics
  - text: There is no set rule determining which passive abilities Break disables.
    marks:
    - corpus:liquipedia_dota2/break@2404623#Mechanics
  - text: Most passives that depend on another ability, such as Grow and Divided We
      Stand, are not nullified.
    marks:
    - corpus:liquipedia_dota2/break@2404623#Mechanics
  - text: On-death passives such as Reincarnation and direct-synergy passives such
      as Caustic Finale with Burrowstrike are generally not disabled.
    marks:
    - corpus:liquipedia_dota2/break@2404623#Definition
  - text: Break sources include Khanda’s Empower Spell, Hoodwink’s Sharpshooter, Silver
      Edge’s Shadow Walk, and Viper Strike.
    marks:
    - corpus:liquipedia_dota2/break@2404623#Sources
  - text: Abilities completely disabled by Break include Counter Helix, Dispersion,
      Berserker’s Blood, Multicast, and Coup de Grace.
    marks:
    - corpus:liquipedia_dota2/break@2404623#Disabled_by_Break
  - text: Abilities not disabled include Grow, Divided We Stand, Mana Shield, and
      Reincarnation.
    marks:
    - corpus:liquipedia_dota2/break@2404623#Not_Disabled_by_Break
  - text: Break did not exist as a mechanic before version 6.84.
    marks:
    - corpus:liquipedia_dota2/break@2404623#Trivia
---

# Break

Break is a status effect that disables passive abilities. It does not disable passive components from items, such as Talisman of Evasion’s evasion, or talents unless stated otherwise. Break works completely independently from mute and silence. [corpus:liquipedia_dota2/break@2404623]

## Definition

| Status | Disabled aspect / definition | Example |
|---|---|---|
| Silence | Fully prevents active ability orders except item casts. Autocast abilities currently set to Autocast have their functionality disabled. Toggled abilities are stuck in their current On/Off state for the duration, but their functionality is not disabled. | Global Silence |
| Break | Fully disables passive abilities but does not disable item passives or talents, with some exceptions. On-death passives, such as Reincarnation, and direct-synergy passives, such as Caustic Finale with Burrowstrike, are generally not disabled. | Viper Strike |
| Mute | Fully prevents item-cast orders except ability casts. | Doom |

[corpus:liquipedia_dota2/break@2404623#Definition]

## Mechanics

Break disables every aspect of an affected ability, including proc chances, innate cooldowns, attack modifiers, and permanent bonuses. Only abilities with passive components are affected; passive components of items and talents are not. For example, Break disables Blur but not Talisman of Evasion or its derived items.

If a passive ability places a buff or debuff, effects already in place are not nullified. If an enemy is affected by Poison Sting, its effects continue after Break is applied to the caster; Break only prevents the caster’s attacks from applying the effect. The same applies to passive abilities that grant stacks, such as Essence Shift: Break prevents new stacks but usually does not disable existing stacks.

Auras behave oppositely. The aura continues placing its buff or debuff on units, but Break on the aura’s source disables that buff or debuff for the duration. If the aura has a status icon in the HUD, it shows 0 while affected by Break.

There is no set rule determining which passive abilities Break disables. Most passive abilities that depend on another ability to function, such as Grow and Divided We Stand, are not nullified. [corpus:liquipedia_dota2/break@2404623#Mechanics]

## Sources

| Source | Break source | Conditions |
|---|---|---|
| Doom | Doom | Requires Talent. |
| Khanda | Empower Spell | — |
| Hill Troll Berserker | Break | — |
| Hoodwink | Decoy | — |
| Hoodwink | Sharpshooter | — |
| Naga Siren | Ensnare | Requires Aghanim's Scepter. |
| Nyx Assassin | Vendetta | Requires Aghanim's Shard; Pierces Debuff Immunity. |
| Phantom Assassin | Fan of Knives | Requires Aghanim's Scepter; Pierces Debuff Immunity. |
| Primal Beast | Uproar | Requires Aghanim's Scepter. |
| Shadow Demon | Demonic Purge | Requires Aghanim's Scepter; Pierces Debuff Immunity. |
| Shadow Shaman | Hex | Requires Talent. |
| Silver Edge | Shadow Walk | — |
| Viper | Viper Strike | Pierces Debuff Immunity. |

[corpus:liquipedia_dota2/break@2404623#Sources]

## Disabled by Break

The following passive abilities are completely disabled by Break. Unless stated otherwise, this includes passive cooldowns, damage counters, and other small parts of the abilities.

| Unit or hero | Ability | Qualification |
|---|---|---|
| Warlock Golem | Flaming Fists | — |
| Warlock Golem | Permanent Immolation | — |
| Earth | Demolish | — |
| Shadow Fiend | Necromastery | Does not grant stacks while disabled by Break; existing stacks still fully work. |
| Shadow Fiend | Presence of the Dark Lord | — |
| Drow Ranger | Marksmanship | Its particle effects still visually react to enemy presence, but all passive components are disabled. |
| Drow Ranger | Precision Aura | Fully disabled, even when using its active component. |
| Sven | Great Cleave | — |
| Earthshaker | Aftershock | — |
| Weaver | Geminate Attack | — |
| Weaver | Threads of Fate | — |
| Lina | Fiery Soul | Does not grant stacks while disabled by Break; existing stacks still fully work. |
| Vengeful Spirit | Vengeance Aura | — |
| Tidehunter | Kraken Shell | — |
| Axe | Counter Helix | — |
| Axe | One Man Army | — |
| Bloodseeker | Thirst | — |
| Tiny | Insurmountable | — |
| Razor | Storm Surge | — |
| Viper | Corrosive Skin | — |
| Viper | Predator | — |
| Spectre | Desolate | — |
| Spectre | Dispersion | — |
| Slardar | Bash of the Deep | — |
| Slardar | Seaborn Sentinel | — |
| Chen | Divine Favor | — |
| Nature's Prophet | Spirit of the Forest | — |
| Venomancer | Poison Sting | Plague Ward’s Poison Sting is also disabled. |
| Storm Spirit | Galvanized | — |
| Storm Spirit | Overload | Does not grant stacks while disabled by Break; existing stacks still fully work. |
| Puck | Puckish | — |
| Beastmaster | Drums of Slom | — |
| Beastmaster | Inner Beast | — |
| Night Stalker | Midnight Feast | — |
| Necrophos | Heartstopper Aura | — |
| Necrophos | Sadist | — |
| Sniper | Keen Scope (7.36 - 7.40c) | — |
| Slark | Shadow Dance (Pre 7.36) | — |
| Abaddon | Curse of Avernus (7.20 - 7.35d) | — |
| Abaddon | Borrowed Time | Its passive components are disabled. |
| Abaddon | Curse of Avernus | Allies do not gain the speed buff when attacking an already cursed enemy. |
| Dragon Knight | Dragon Blood | — |
| Dragon Knight | Wyrm's Wrath | — |
| Luna | Lunar Blessing | — |
| Luna | Moon Glaives | — |
| Lycan | Apex Predator | — |
| Lycan | Feral Impulse | — |
| Alchemist | Corrosive Weaponry | — |
| Alchemist | Greevil's Greed | — |
| Queen of Pain | Succubus | — |
| Ursa | Fury Swipes | Does not grant stacks while disabled by Break; existing stacks still fully work. |
| Ursa | Maul | — |
| Magnus | Solid Core | — |
| Riki | Backstab | — |
| Riki | Cloak and Dagger | — |
| Visage | Gravekeeper's Cloak | — |
| Elder Titan | Natural Order | Only its armor reduction is disabled. |
| Anti-Mage | Counterspell | Its passive components are disabled. |
| Anti-Mage | Mana Break | — |
| Ember Spirit | Fire Remnant | — |
| Ember Spirit | Immolation | — |
| Rubick | Arcane Supremacy | — |
| Rubick | Curiosity | — |
| Mars | Bulwark | — |
| Mars | Dauntless | — |
| Medusa | Cold Blooded | — |
| Medusa | Split Shot | — |
| Enchantress | Little Friends | — |
| Enchantress | Untouchable | — |
| Meepo | Ransack | — |
| Enigma | Event Horizon | — |
| Shadow Shaman | Fowl Play | — |
| Faceless Void | Backtrack | — |
| Faceless Void | Distortion Field | — |
| Faceless Void | Time Lock | — |
| Batrider | Smoldering Resin | — |
| Monkey King | Jingu Mastery | Neither applies new stacks nor allows existing stacks to grant bonuses during Break. |
| Silencer | Suffer In Silence | — |
| Wraith King | Mortal Strike | Does not grant stacks while disabled by Break; existing stacks still fully work. |
| Wraith King | Vampiric Spirit | — |
| Bounty Hunter | Jinada | — |
| Muerta | Gunslinger | — |
| Brewmaster | Liquid Courage | — |
| Naga Siren | Eelskin | — |
| Naga Siren | Rip Tide | — |
| Zeus | Static Field | — |
| Gyrocopter | Side Gunner | — |
| Slark | Essence Shift | Does not grant stacks while disabled by Break; existing stacks still fully work. It still grants permanent bonuses under its kill conditions while disabled. |
| Slark | Saltwater Shiv | — |
| Slark | Shadow Dance | Its passive components are disabled. |
| Nyx Assassin | Mana Burn | — |
| Hoodwink | Scurry | — |
| Snapfire | Boomstick | — |
| Huskar | Berserker's Blood | — |
| Ogre Magi | Multicast | — |
| Bristleback | Bristleback | — |
| Bristleback | Warpath | Does not grant stacks while disabled by Break; existing stacks still fully work. |
| Sniper | Headshot | — |
| Sniper | Keen Scope | — |
| Sniper | Take Aim | Its passive components are disabled. |
| Omniknight | Degen Aura | — |
| Omniknight | Hammer of Purity | — |
| Spirit Breaker | Greater Bash | Break only prevents it from proccing on attacks; it still works fully with other abilities. |
| Broodmother | Incapacitating Bite | — |
| Broodmother | Spider's Milk | — |
| Centaur Warrunner | Retaliate | Its passive components are disabled. |
| Chaos Knight | Chaos Strike | — |
| Templar Assassin | Psi Blades | — |
| Pangolier | Fortune Favors the Bold | — |
| Pangolier | Lucky Shot | — |
| Phantom Assassin | Coup de Grace | — |
| Phantom Assassin | Immaterial | — |
| Phantom Assassin | Stifling Dagger | — |
| Crystal Maiden | Arcane Aura | — |
| Crystal Maiden | Glacial Guard | — |
| Phantom Lancer | Juxtapose | — |
| Phantom Lancer | Phantom Rush | — |
| Timbersaw | Exposure Therapy | — |
| Timbersaw | Reactive Armor | Does not grant stacks while disabled by Break; existing stacks still fully work. |
| Juggernaut | Blade Dance | — |
| Juggernaut | Bladeform | — |
| Phoenix | Dying Light | — |
| Tinker | Eureka! | — |
| Keeper of the Light | Bright Speed | — |
| Dark Willow | Pixie Dust | — |
| Treant Protector | Leech Seed | — |
| Primal Beast | Uproar | — |
| Dawnbreaker | Break of Dawn | — |
| Dawnbreaker | Luminosity | — |
| Kunkka | Tidebringer | — |
| Troll Warlord | Berserker's Rage | Its passive components are disabled. |
| Troll Warlord | Fervor | Neither applies new stacks nor allows existing stacks to grant bonuses during Break. |
| Death Prophet | Exorcism | — |
| Death Prophet | Witchcraft | — |
| Legion Commander | Moment of Courage | — |
| Disruptor | Electromagnetic Repulsion | — |
| Lifestealer | Feast | — |
| Lifestealer | Ghoul Frenzy | — |
| Underlord | Atrophy Aura | Does not grant stacks while disabled by Break; existing stacks still fully work. |
| Underlord | Invading Force | — |
| Lone Druid | Spirit Link | — |
| Ghost | Frost Attack | — |
| Lycan Lane Wolf | Cripple | — |
| Minor Imp | Eldritch Explosion | — |
| Ancient Frostbitten Golem | Time Warp Aura | — |
| Kez | Kazurai Katana | — |
| Kez | Shodo Sai | — |
| Flagbearer Creep | Inspiration Aura | — |
| Super Flagbearer Creep | Inspiration Aura | — |
| Mega Flagbearer Creep | Inspiration Aura | — |
| Pollywog | Riverborn Aura | — |
| Boglet | Riverborn Aura | — |
| Croaker | Riverborn Aura | — |
| Ancient Croaker | Riverborn Aura | — |
| Marshmage Apprentice | Riverborn Aura | — |
| Marshmage | Riverborn Aura | — |
| Ancient Marshmage | Riverborn Aura | — |
| Demonic Warrior (Underlord) | Last Will | — |
| Demonic Warrior (Underlord) | Mana Break | — |
| Demonic Archer (Underlord) | Archer Aura | — |
| Demonic Archer (Book of the Dead) | Archer Aura | — |
| Demonic Warrior (Book of the Dead) | Last Will | — |
| Demonic Warrior (Book of the Dead) | Mana Break | — |
| Largo | Encore | — |
| Spirit Bear (Pre 7.40) | Demolish | — |
| Fire | Permanent Immolation | — |
| Kobold | Prospecting Aura | — |
| Kobold Soldier | Steal Weapon | — |
| Kobold Foreman | Speed Aura | — |
| Hill Troll Berserker | Break | — |
| Hill Troll Priest | Heal Amplification Aura | — |
| Vhoul Assassin | Envenomed Weapon | — |
| Centaur Courser | Cloak Aura | — |
| Alpha Wolf | Critical Strike | — |
| Alpha Wolf | Packleader's Aura | — |
| Satyr Mindstealer | Mana Aura | — |
| Mud Golem | Shard Split | — |
| Satyr Tormenter | Unholy Aura | — |
| Hellbear | Death Throe: Rush | — |
| Hellbear | Swiftness Aura | — |
| Hellbear Smasher | Death Throe: Power | — |
| Wildwing Ripper | Toughness Aura | — |
| Skeleton Warrior | Rally | — |
| Ancient Black Drake | Magic Amplification Aura | — |
| Ancient Black Dragon | Dragonhide Aura | — |
| Ancient Black Dragon | Splash Attack | — |
| Ancient Rock Golem | Weakening Aura | — |
| Ancient Rumblehide | War Drums Aura | — |
| Roshan | Bash | Break only prevents it from proccing on attacks; it still works fully with other abilities. |
| Razorback | Poison | Plague Ward’s Poison Sting is also disabled. |
| Ancient Prowler Acolyte | Prowler Aura | — |
| Spirit Bear | Demolish | — |
| Spirit Bear | Entangling Claws | — |
| Spirit Bear | Spirit Link | — |
| Lycan Wolf | Cripple | — |

[corpus:liquipedia_dota2/break@2404623#Disabled_by_Break]

## Not Disabled by Break

The following passive abilities are not disabled by Break.

| Unit or hero | Ability |
|---|---|
| Earth | Drunken Brawler |
| Earth | Earth Element |
| Astral Spirit | Invulnerability |
| Astral Spirit | Unobstructed Movement |
| Proximity Mine | Permanent Invisibility |
| Ice Spire | Spell Immunity |
| Siege Creep | Reinforced |
| Shadow Fiend | Requiem of Souls |
| Sven | Wrath of God |
| Pugna | Oblivion Savant |
| Clockwerk | Armor Power |
| Earthshaker | Slugger |
| Ancient Apparition | Bone Chill |
| Lina | Slow Burn |
| Vengeful Spirit | Retribution |
| Tidehunter | Leviathan's Catch |
| Lion | To Hell and Back |
| Morphling | Ebb and Flow |
| Doom | Lvl ? Pain |
| Bloodseeker | Sanguivore |
| Lich | Chain Frost |
| Lich | Ice Spire |
| Tiny | Grow |
| Razor | Plasma Field |
| Razor | Unstable Current |
| Viper | Nosedive |
| Leshrac | Defilement |
| Windranger | Tailwind |
| Mirana | Celestial Quiver |
| Chen | Zealot |
| Storm Spirit | Ball Lightning |
| Storm Spirit | Static Remnant |
| Puck | Dream Coil |
| Puck | Phase Shift |
| Sand King | Burrowstrike |
| Sand King | Epicenter |
| Sand King | Sand Storm |
| Necrophos | Reaper's Scythe |
| Axe | Coat of Blood |
| Pudge | Flesh Heap (6.64 - 7.35d) |
| Silencer | Glaives of Wisdom (6.15-7.35d) |
| Invoker | Mastermind |
| Skywrath Mage | Shield of the Scion (Pre 7.35d) |
| Winter Wyvern | Eldwurm Scholar |
| Ringmaster | Dark Carnival Barker |
| Abaddon | Withering Mist |
| Pudge | Flesh Heap |
| Undying | Ceaseless Dirge |
| Undying | Tombstone |
| Lycan | Shapeshift |
| Lycan | Summon Wolves |
| Magnus | Empower |
| Visage | Soul Assumption |
| Elder Titan | Momentum |
| Anti-Mage | Persecutor |
| Marci | Special Delivery |
| Marci | Unleash |
| Void Spirit | Intrinsic Edge |
| Arc Warden | Runic Infusion |
| Warlock | Chaotic Offering |
| Warlock | Eldritch Summoning |
| Medusa | Mana Shield |
| Enchantress | Enchant |
| Enchantress | Rabble-Rouser |
| Bane | Ichor of Nyctasha |
| Shadow Demon | Menace |
| Meepo | Divided We Stand |
| Meepo | Geomancy |
| Faceless Void | Time Walk |
| Batrider | Sticky Napalm |
| Silencer | Glaives of Wisdom |
| Wraith King | Wraithfire Blast |
| Bounty Hunter | Big Game Hunter |
| Bounty Hunter | Shuriken Toss |
| Grimstroke | Ink Trail |
| Skywrath Mage | Shield of the Scion |
| Muerta | Pierce the Veil |
| Muerta | Supernatural |
| Muerta | The Calling |
| Brewmaster | Drunken Brawler |
| Zeus | Lightning Hands |
| Gyrocopter | Afterburner |
| Gyrocopter | Call Down |
| Hoodwink | Mistwoods Wayfarer |
| Huskar | Blood Magic |
| Ogre Magi | Dumb Luck |
| Ogre Magi | Fireblast |
| Bristleback | Prickly |
| Sniper | Assassinate |
| Invoker | Exort |
| Invoker | Quas |
| Invoker | Wex |
| Oracle | Prognosticate |
| Centaur Warrunner | Horsepower |
| Outworld Destroyer | Essence Flux |
| Outworld Destroyer | Objurgation |
| Chaos Knight | Fundamental Forging |
| Templar Assassin | Inner Peace |
| Io | Equilibrium |
| Io | Spirits |
| Io | Tether |
| Clinkz | Infernal Shred |
| Terrorblade | Dark Unity |
| Jakiro | Double Trouble |
| Phantom Lancer | Illusory Armaments |
| Dark Seer | Normal Punch |
| Dark Seer | Quick Wit |
| Treant Protector | Nature's Guise |
| Dazzle | Weave |
| Kunkka | Admiral's Rum |
| Troll Warlord | Battle Stance |
| Legion Commander | Duel |
| Legion Commander | Outfight Them! |
| Tusk | Bitter Chill |
| Tusk | Walrus PUNCH! |
| Lone Druid | Summon Spirit Bear |
| Lone Druid | True Form |
| Undying Zombie | Deathlust |
| Undying Zombie | Spell Immunity |
| Phoenix Sun | Phase Movement |
| Phoenix Sun | Spell Immunity |
| Ghost | Piercing |
| Tornado (Wildwing) | Invulnerability |
| Tornado (Wildwing) | Tempest |
| Sticky Bomb | Invulnerability |
| Sticky Bomb | Phase Movement |
| Power Cog | Spell Immunity |
| Spiderling | Spawn Spiderite (5.66 - 7.35d) |
| Earth | Debuff Immunity |
| Storm | Drunken Brawler |
| Jex | Invulnerability |
| Jex | Phase Movement |
| Fiend's Gate | Invulnerability |
| Fiend's Gate | Spell Immunity |
| Watcher | Invulnerability |
| Mars Soldier | Invulnerability |
| Mars Soldier | Phase Movement |
| Roshan's Banner (unit) | Spell Immunity |
| Ofrenda | Invulnerability |
| Ofrenda | Phase Movement |
| Attributes | Attribute Bonus |
| Cleave | Cleave |
| Armor | Armor Corruption |
| Armor | Bonus Armor |
| Mana Break | Mana Break |
| Bash | Bash |
| Illusions | Illusions |
| [[Magic_Resistance\|\]\] | Base |
| Attack Damage | Piercing |
| Attack Damage | Reinforced |
| Attack Damage | Runty |
| Death | Reincarnation |
| Massive Serpent Ward | Piercing |
| Massive Serpent Ward | Spell Immunity |
| Ancient (Building) | Reinforced |
| Effigy Building | Reinforced |
| Attack Damage | Reinforced |
| Attack Damage | Reinforced |
| Attack Damage | Reinforced |
| Tower (Tier 4) | Reinforced |
| Twin Gate | Invulnerability |
| Twin Gate | Spell Immunity |
| Tormentor | Reflect |
| Tormentor | Unyielding Shield |
| Super Melee Creep | Runty |
| Mega Melee Creep | Runty |
| Super Ranged Creep | Piercing |
| Mega Ranged Creep | Piercing |
| Super Siege Creep | Reinforced |
| Mega Siege Creep | Reinforced |
| Flagbearer Creep | Runty |
| Super Flagbearer Creep | Runty |
| Mega Flagbearer Creep | Runty |
| Treant's Eyes | Eyes In The Forest |
| Demonic Warrior (Underlord) | Runty |
| Demonic Archer (Underlord) | Piercing |
| Demonic Archer (Book of the Dead) | Piercing |
| Demonic Warrior (Book of the Dead) | Runty |
| Minefield Sign | Phase Movement |
| Minefield Sign | Spell Immunity |
| Spirit Bear (Pre 7.40) | Return |
| M.A.D. | Permanent Invisibility |
| M.A.D. | Phase Movement |
| Keen Cannon | Spell Immunity |
| Fire | Drunken Brawler |
| Fire | Permanent Phase |
| Melee Creep | Runty |
| Ranged Creep | Piercing |
| Hill Troll Berserker | Piercing |
| Hill Troll Priest | Piercing |
| Vhoul Assassin | Piercing |
| Harpy Scout | Piercing |
| Harpy Stormcrafter | Piercing |
| Hill Troll | Piercing |
| Ancient Granite Golem | Granite Aura |
| Roshan | On The Move |
| Roshan | Spell Block |
| Roshan | Strength of the Immortal |
| Fountain | Reinforced |
| Anchor | Phase Movement |
| Anchor | Spell Immunity |
| Tombstone | Spell Immunity |
| Spiderling | Poison Sting |
| Spiderling | Spawn Spiderlings |
| Attack Damage | Reinforced |
| Attack Damage | Reinforced |
| Beetle | Phase Movement |
| Beetle | Spell Immunity |
| Attack Damage | Piercing |
| Plague Ward | Spell Immunity |
| Spirit Bear | Return |
| Courier | Passive Bonus |
| Wraith King Skeleton | Damage Tracker |
| Wraith King Skeleton | Reincarnating |
| Death Ward | Invulnerability |
| Psionic Trap | Permanent Invisibility |
| Healing Ward | Phase Movement |
| Healing Ward | Spell Immunity |
| Forged Spirit | Melting Strike |
| Familiar | Visage Innate |
| Serpent Ward | Piercing |
| Serpent Ward | Spell Immunity |
| Lycan Wolf | Invisibility |
| Homing Missile | Phase Movement |
| Phantom | Phase Movement |
| Spin Web | Invulnerability |
| Spin Web | Phase Movement |
| Ignis Fatuus | Phase Movement |

[corpus:liquipedia_dota2/break@2404623#Not_Disabled_by_Break]

## Trivia

Break did not exist as a mechanic before version 6.84. Doom—required in 6.82/6.83—Hex sources until 6.84, Duel until 6.82, and Chronosphere until 6.82 instead disabled a small portion of passive spell and item abilities.

### Disabled by all four sources

| Passive component |
|---|
| Blur [?] |
| Drunken Brawler [?] |
| Bristleback |
| Kraken Shell [?] |
| Fury Swipes |
| Shadow Dance [?] |
| Vampiric Aura [?] |
| Feast |
| Bash of the Deep |
| Berserker's Rage [?] |
| Greater Bash |
| Time Lock |
| Headshot |
| Great Cleave |
| Blade Dance |
| Chaos Strike |
| Coup de Grace |
| Jinada [?] |
| Mortal Strike |
| Shapeshift [?] |
| Mana Break |
| Butterfly's evasion |
| Heaven's Halberd's evasion |
| Talisman of Evasion's evasion |
| Gem of True Sight's aura |
| Radiance's aura [?] |
| Vladmir's Offering's lifesteal [?] |
| Helm of the Dominator's lifesteal |
| Mask of Madness' lifesteal |
| Morbid Mask's lifesteal |
| Satanic's lifesteal |
| Abyssal Blade's bash |
| Skull Basher's bash |
| Monkey King Bar's mini-bash |
| Battle Fury's cleave |
| Crystalys' critical strike |
| Daedalus' critical strike |
| Diffusal Blade's feedback |
| Diffusal Blade 2's feedback |

### Disabled only by Doom

| Passive component |
|---|
| Backtrack |
| Borrowed Time [?] |
| Berserker's Blood |
| Corrosive Skin |
| Dispersion |
| Entangling Claws |
| Juxtapose |
| Kraken Shell [?] |
| Linken's Sphere's spell block |

### Disabled only by Hexes, Duel, and Chronosphere

| Passive component |
|---|
| Stout Shield's damage block |
| Poor Man's Shield's damage block |
| Vanguard's damage block |
| Crimson Guard's damage block |

[corpus:liquipedia_dota2/break@2404623#Trivia]

## Recent changes

| Version | Date | Change |
|---|---|---|
| 7.37 | 2024-07-31 | Added: Vendetta now applies Break. |
| 7.32 | 2022-08-24 | Doom no longer applies Break. |
| 7.32 | 2022-08-24 | Nether Strike no longer applies Break. |
| 7.32 | 2022-08-24 | Added the new Decoy ability as a source of Break. |
| 7.28c | 2021-02-19 | Removed: Vendetta no longer applies Break. |

[corpus:liquipedia_dota2/break@2404623#Recent_Changes]