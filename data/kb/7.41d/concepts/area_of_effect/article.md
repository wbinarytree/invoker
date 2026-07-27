---
title: Area of Effect
kind: concept
patch: 7.41d
card:
  entity: area_of_effect
  sentences:
  - text: Area of Effect (AoE) Radius increases spell width and radius through the
      AoE bonus stat without affecting lengths or ranges already increased by Aether
      Lens.
    marks:
    - corpus:liquipedia_dota2/area_of_effect@2377200
  - text: Listed AoE bonus sources are Dezun Bloodrite’s Blood Invocation, Gleipnir,
      Leshrac’s Defilement, Primal Beast’s Colossal, and Rubick’s Curiosity.
    marks:
    - corpus:liquipedia_dota2/area_of_effect@2377200#Sources
  - text: AoE bonus affects most circular-radius No Target and Target Area abilities.
    marks:
    - corpus:liquipedia_dota2/area_of_effect@2377200#AoE_bonus_mechanics
  - text: AoE bonus affects all auras and Cleave sources.
    marks:
    - corpus:liquipedia_dota2/area_of_effect@2377200#AoE_bonus_mechanics
  - text: Most line-shaped and cone-shaped Target Point abilities receive wider hitboxes.
    marks:
    - corpus:liquipedia_dota2/area_of_effect@2377200#AoE_bonus_mechanics
  - text: Meat Hook and Timber Chain do not receive AoE bonus.
    marks:
    - corpus:liquipedia_dota2/area_of_effect@2377200#AoE_bonus_mechanics
  - text: Earth Spike and Impale gain AoE Radius without increasing their Effect Radius
      or Hitbox Radius.
    marks:
    - corpus:liquipedia_dota2/area_of_effect@2377200#AoE_bonus_mechanics
  - text: Most Target Unit spells are unaffected, except some with an area effect
      or an extra projectile.
    marks:
    - corpus:liquipedia_dota2/area_of_effect@2377200#Ability_is_not_affected_by_AoE_Bonus
  - text: Target Unit abilities with a secondary-projectile Search Radius or an area
      effect are always affected.
    marks:
    - corpus:liquipedia_dota2/area_of_effect@2377200#AoE_bonus_mechanics
  - text: Cast Range bonuses extend the cast range of all Vector Targeting spells,
      while AoE Radius bonuses extend the effect range of almost all of them.
    marks:
    - corpus:liquipedia_dota2/area_of_effect@2377200#AoE_bonus_mechanics
  - text: With Gleipnir, Swashbuckle gains 75 Slash width, while Aether Remnant gains
      75 Remnant Watch width and 75 Remnant Search range.
    marks:
    - corpus:liquipedia_dota2/area_of_effect@2377200#AoE_bonus_mechanics
  - text: Impale’s AoE bonus is fixed when the ability is leveled and updates only
      when the ability is upgraded.
    marks:
    - corpus:liquipedia_dota2/area_of_effect@2377200#Unchanged_Effect_Radius
---

# Area of Effect

## AoE Radius

AoE Radius affects areas of effect by increasing spell width and radius. It does not affect lengths and ranges already increased by Aether Lens. AoE Radius is affected by the **AoE bonus** stat. [corpus:liquipedia_dota2/area_of_effect@2377200]

## Sources

| Source | AoE bonus |
|---|---|
| Dezun Bloodrite | Blood Invocation |
| Gleipnir | AoE bonus |
| Leshrac | Defilement |
| Primal Beast | Colossal |
| Rubick | Curiosity |

[corpus:liquipedia_dota2/area_of_effect@2377200#Sources]

## AoE bonus mechanics

The AoE bonus affects most circular-radius **No Target** abilities, such as Scream of Pain, and circular-radius **Target Area** abilities, such as Shrapnel. It affects all auras and Cleave sources, such as Lunar Blessing and Great Cleave. [corpus:liquipedia_dota2/area_of_effect@2377200#AoE_bonus_mechanics]

It also affects most line-shaped and cone-shaped **Target Point** abilities, such as Boundless Strike and Breathe Fire, expanding the width radius of their hitboxes. Some line-shaped Target Point abilities, including Meat Hook and Timber Chain, do not receive the bonus. Earth Spike and Impale are special cases: their Effect Radius and Hitbox Radius are not increased despite their AoE Radius increasing. [corpus:liquipedia_dota2/area_of_effect@2377200#AoE_bonus_mechanics]

**Target Unit** abilities with a Search Radius used to fire secondary projectiles, such as Fade Bolt, are always affected. Target Unit abilities with an area effect, such as Storm Hammer, are also always affected. [corpus:liquipedia_dota2/area_of_effect@2377200#AoE_bonus_mechanics]

Cast Range bonuses increase the cast range of all Vector Targeting spells but not their effect range. AoE Radius bonuses increase the effect range of almost all Vector Targeting spells. [corpus:liquipedia_dota2/area_of_effect@2377200#AoE_bonus_mechanics]

| Ability | Effect while equipped with Gleipnir |
|---|---|
| Swashbuckle | `75 Slash width` increase |
| Aether Remnant | `75 Remnant Watch width` and `75 Remnant Search range` increase |

These values have the `affected_by_aoe_increase` tag in the game key-value files. [corpus:liquipedia_dota2/area_of_effect@2377200#AoE_bonus_mechanics]

## Unchanged Effect Radius

The following ability does not have its effect radius increased despite its AoE Radius increasing, so its Effect Radius does not match the new AoE Radius. Some abilities in this category may be listed for clarification. [corpus:liquipedia_dota2/area_of_effect@2377200#Unchanged_Effect_Radius]

| Hero | Ability |
|---|---|
| Nyx Assassin | Impale＊ |

＊The AoE Radius increases only if the ability LvL is upgraded after obtaining the AoE bonus. The AoE bonus is fixed when the ability is leveled and is updated only when the ability is upgraded. [corpus:liquipedia_dota2/area_of_effect@2377200#Unchanged_Effect_Radius]

## Abilities not affected by AoE bonus

Most Target Unit spells are unaffected, except some with an area effect or an extra projectile. The following list contains the Target Point, No Target, Target Area, and Vector Targeting abilities that are not affected. [corpus:liquipedia_dota2/area_of_effect@2377200#Ability_is_not_affected_by_AoE_Bonus]

| Hero | Ability |
|---|---|
| Bristleback | Bristleback2a |
| Drow Ranger | Glacier |
| Drow Ranger | Multishot |
| Earthshaker | Fissure |
| Earth Spirit | Magnetize |
| Earth Spirit | Rolling Boulder |
| Gyrocopter | Rocket Barrage |
| Muerta | Dead Shot＊ |
| Pudge | Meat Hook |
| Timbersaw | Timber Chain |

`1` Requires talent.  
`2a` Requires Aghanim's Scepter.  
`2b` Requires Aghanim's Shard. [corpus:liquipedia_dota2/area_of_effect@2377200#Ability_is_not_affected_by_AoE_Bonus]

## Item ability AoE Radius

The following item abilities have AoE Radius: [corpus:liquipedia_dota2/area_of_effect@2377200#Item_ability_AoE_Radius]

| Item | Ability |
|---|---|
| Arcane Boots | Replenish |
| Arcane Ring | Replenish Mana |
| Assault Cuirass | Assault Aura |
| Battle Fury | Cleave |
| Blood Grenade | Throw Grenade |
| Boots of Bearing | Endurance |
| Buckler | Buckler Aura |
| Boots of Bearing | Swiftness Aura |
| Crimson Guard | Guard |
| Disperser | Suppress |
| Dust of Appearance | Reveal |
| Drum of Endurance | Swiftness Aura |
| Fallen Sky | Fallen Sky |
| Gem of True Sight | True Sight |
| Gleipnir | Eternal Chains |
| Guardian Greaves | Mend |
| Headdress | Regeneration Aura |
| Holy Locket | Energy Charge |
| Magic Wand | Energy Charge |
| Mekansm | Restore |
| Meteor Hammer | Meteor Hammer |
| Overwhelming Blink | Overwhelming Blink |
| Pipe of Insight | Barrier |
| Ring of Basilius | Basilius Aura |
| Roshan's Banner | Place Banner |
| Seeds of Serenity | Verdurous Dale |
| Shiva's Guard | Arctic Blast |
| Spirit Vessel | Soul Release |
| Telescope | Prescient Aura |
| Vladmir's Offering | Vladmir's Aura |
| Urn of Shadows | Soul Release |
| Veil of Discord | Magic Weakness |

## Hero ability AoE Radius

The following abilities have their area-of-effect radius increased when their heroes equip Gleipnir, excluding exceptions whose effect radius does not actually increase as described under **Unchanged Effect Radius**. [corpus:liquipedia_dota2/area_of_effect@2377200#Hero_ability_AoE_Radius]

| Hero | Ability or effect |
|---|---|
| Abaddon | Aphotic Shield |
| Abaddon | Mist Coil1 |
| Abaddon | Borrowed Time1 & 2a |
| Alchemist | Acid Spray |
| Alchemist | Unstable Concoction |
| Ancient Apparition | Cold Feet1 |
| Ancient Apparition | Ice Blast |
| Ancient Apparition | Ice Vortex |
| Anti-Mage | Mana Void |
| Arc Warden | Flux |
| Arc Warden | Magnetic Field |
| Arc Warden | Tempest Double |
| Axe | Berserker's Call |
| Axe | Counter Helix |
| Axe | Culling Blade |
| Bane | Brain Sap2b |
| Batrider | Sticky Napalm |
| Batrider | Firefly |
| Batrider | Flamebreak |
| Batrider | Flaming Lasso2a |
| Beastmaster | Wild Axes |
| Beastmaster | Primal Roar |
| Bloodseeker | Blood Rite |
| Bloodseeker | Blood Mist |
| Brewmaster | Thunder Clap |
| Brewmaster | Cinder Brew |
| Bristleback | Quill Spray |
| Bristleback | Hairball |
| Broodmother | Spin Web |
| Broodmother | Silken Bola1 |
| Broodmother | Spinner's Snare |
| Centaur Warrunner | Hoof Stomp |
| Centaur Warrunner | Double Edge |
| Centaur Warrunner | Stampede |
| Clinkz | Burning Barrage |
| Clinkz | Tar Bomb |
| Clockwerk | Battery Assault |
| Clockwerk | Rocket Flare |
| Clockwerk | Hookshot |
| Crystal Maiden | Crystal Clone |
| Crystal Maiden | Crystal Nova |
| Crystal Maiden | Freezing Field |
| Dark Seer | Vacuum |
| Dark Seer | Ion Shell |
| Dark Seer | Surge2b |
| Dark Seer | Wall of Replica |
| Dark Willow | Bramble Maze |
| Dark Willow | Cursed Crown |
| Dark Willow | Bedlam |
| Dark Willow | Terrorize |
| Dazzle | Shadow Wave |
| Dazzle | Poison Touch |
| Death Prophet | Crypt Swarm |
| Death Prophet | Silence |
| Death Prophet | Exorcism |
| Disruptor | Thunder Strike |
| Disruptor | Kinetic Field |
| Disruptor | Static Storm |
| Dawnbreaker | Starbreaker |
| Dawnbreaker | Celestial Hammer |
| Dawnbreaker | Solar Guardian |
| Doom | Scorched Earth |
| Doom | Doom2a |
| Dragon Knight | Breathe Fire |
| Dragon Knight | Dragon Tail 1 |
| Dragon Knight | Fireball |
| Drow Ranger | Frost Arrows2a |
| Drow Ranger | Gust |
| Earth Spirit | Boulder Smash |
| Earth Spirit | Geomagnetic Grip |
| Earth Spirit | Magnetize |
| Earth Spirit | Enchant Remnant |
| Earthshaker | Enchant Totem |
| Earthshaker | Aftershock |
| Earthshaker | Echo Slam |
| Elder Titan | Echo Stomp |
| Elder Titan | Astral Spirit |
| Elder Titan | Earth Splitter |
| Ember Spirit | Fire Remnant |
| Ember Spirit | Searing Chains |
| Ember Spirit | Sleight of Fist |
| Ember Spirit | Flame Guard |
| Enchantress | Nature's Attendants |
| Enchantress | Little Friends |
| Enigma | Midnight Pulse |
| Enigma | Black Hole |
| Faceless Void | Time Walk2a |
| Faceless Void | Time Dilation |
| Faceless Void | Chronosphere |
| Grimstroke | Stroke of Fate |
| Grimstroke | Ink Swell |
| Grimstroke | Soulbind |
| Gyrocopter | Homing Missile2b |
| Gyrocopter | Flak Cannon |
| Gyrocopter | Call Down |
| Huskar | Inner Fire |
| Hoodwink | Acorn Shot |
| Hoodwink | Bushwhack |
| Hoodwink | Scurry |
| Hoodwink | Sharpshooter |
| Hoodwink | Decoy |
| Hoodwink | Hunter's Boomerang |
| Invoker | Sun Strike |
| Invoker | Tornado |
| Invoker | Chaos Meteor |
| Invoker | E.M.P. |
| Invoker | Deafening Blast |
| Invoker | Ghost Walk |
| Invoker | Ice Wall |
| Io | Tether |
| Io | Spirits |
| Jakiro | Dual Breath |
| Jakiro | Ice Path |
| Jakiro | Liquid Frost |
| Jakiro | Liquid Fire |
| Jakiro | Macropyre |
| Juggernaut | Blade Fury |
| Juggernaut | Healing Ward |
| Juggernaut | Omnislash |
| Keeper of the Light | Will-O-Wisp |
| Keeper of the Light | Illuminate |
| Keeper of the Light | Blinding Light |
| Kunkka | Torrent |
| Kunkka | Ghostship |
| Kunkka | Tidal Wave |
| Kunkka | Torrent Storm |
| Legion Commander | Overwhelming Odds |
| Legion Commander | Press the Attack1 |
| Leshrac | Diabolic Edict |
| Leshrac | Split Earth |
| Leshrac | Lightning Storm |
| Leshrac | Pulse Nova |
| Lich | Frost Blast |
| Lich | Frost Shield |
| Lich | Sinister Gaze2s |
| Lich | Chain Frost |
| Lich | Ice Spire |
| Lifestealer | Open Wounds |
| Lifestealer | Infest |
| Lina | Dragon Slave |
| Lina | Light Strike Array |
| Lion | Earth Spike |
| Lion | Hex1 |
| Lion | Finger of Death2a |
| Lone Druid | Savage Roar |
| Luna | Lucent Beam1 |
| Luna | Eclipse |
| Lycan | Howl |
| Magnus | Horn Toss |
| Magnus | Shockwave |
| Magnus | Empower |
| Magnus | Skewer |
| Magnus | Reverse Polarity |
| Mars | Spear of Mars |
| Mars | Arena of Blood |
| Mars | God's Rebuke |
| Meepo | Earthbind |
| Meepo | Poof |
| Meepo | MegaMeepo |
| Medusa | Mystic Snake |
| Medusa | Stone Gaze |
| Mirana | Leap |
| Mirana | Starstorm |
| Mirana | Sacred Arrow2a: it does not increase Arrow Collision Radius |
| Monkey King | Boundless Strike |
| Monkey King | Wukong's Command |
| Monkey King | Primal Spring |
| Morphling | Waveform |
| Muerta | The Calling |
| Naga Siren | Rip Tide |
| Naga Siren | Reel In |
| Naga Siren | Song of the Siren |
| Nature's Prophet | Sprout |
| Nature's Prophet | Nature's Call |
| Naga Siren | Reel In |
| Nature's Prophet | Curse of the Oldgrowth |
| Necrophos | Death Pulse |
| Necrophos | Ghost Shroud |
| Night Stalker | Void |
| Night Stalker | Crippling Fear |
| Nyx Assassin | Impale |
| Ogre Magi | Bloodlust |
| Ogre Magi | Fire Shield |
| Ogre Magi | Ignite |
| Omniknight | Purification |
| Oracle | Fortune's End |
| Oracle | Rain of Destiny |
| Pangolier | Rolling Thunder |
| Pangolier | Shield Crash |
| Pangolier | Swashbuckle |
| Phantom Lancer | Spirit Lance2a |
| Phantom Lancer | Doppelganger |
| Phoenix | Icarus Dive |
| Phoenix | Fire Spirits |
| Phoenix | Supernova |
| Phoenix | Sun Ray |
| Primal Beast | Onslaught |
| Primal Beast | Trample |
| Primal Beast | Uproar |
| Primal Beast | Pulverize |
| Primal Beast | Rock Throw |
| Puck | Illusory Orb |
| Puck | Waning Rift |
| Puck | Dream Coil |
| Pudge | Rot |
| Pugna | Nether Blast |
| Pugna | Life Drain |
| Queen of Pain | Blink2b |
| Queen of Pain | Scream of Pain |
| Queen of Pain | Shadow Strike2a |
| Queen of Pain | Sonic Wave |
| Razor | Plasma Field |
| Razor | Eye of the Storm |
| Razor | Storm Surge |
| Riki | Smoke Screen |
| Riki | Tricks of the Trade |
| Rubick | Fade Bolt |
| Rubick | Telekinesis |
| Sand King | Burrowstrike |
| Sand King | Sand Storm |
| Sand King | Epicenter |
| Shadow Demon | Disseminate |
| Shadow Demon | Shadow Poison |
| Shadow Fiend | Shadowraze |
| Shadow Fiend | Requiem of Souls |
| Shadow Shaman | Ether Shock |
| Silencer | Arcane Curse |
| Silencer | Glaives of Wisdom1 |
| Silencer | Last Word2a |
| Skywrath Mage | Arcane Bolt2a |
| Skywrath Mage | Concussive Shot2a |
| Skywrath Mage | Ancient Seal2a |
| Skywrath Mage | Mystic Flare |
| Slardar | Slithereen Crush |
| Slardar | Corrosive Haze |
| Slark | Dark Pact |
| Slark | Depth Shroud |
| Snapfire | Scatterblast |
| Snapfire | Firesnap Cookie |
| Snapfire | Mortimer Kisses |
| Sniper | Shrapnel |
| Sniper | Concussive Grenade |
| Spectre | Spectral Dagger |
| Spirit Breaker | Charge of Darkness |
| Spirit Breaker | Planar Pocket |
| Storm Spirit | Static Remnant |
| Storm Spirit | Electric Vortex2a |
| Storm Spirit | Overload |
| Storm Spirit | Ball Lightning |
| Sven | Storm Hammer |
| Sven | Great Cleave |
| Sven | Warcry |
| Techies | Sticky Bomb |
| Techies | Reactive Tazer |
| Techies | Blast Off! |
| Techies | Proximity Mines |
| Templar Assassin | Psionic Trap increase Trap Vision Radius |
| Terrorblade | Reflection |
| Terrorblade | Terror Wave |
| Tidehunter | Anchor Smash |
| Tidehunter | Gush2a |
| Tidehunter | Ravage |
| Timbersaw | Chakram |
| Timbersaw | Reactive Armor2a |
| Timbersaw | Whirling Death |
| Tinker | Keen Conveyance |
| Tinker | Warp Flare |
| Tinker | Laser |
| Tinker | Heat-Seeking Missile |
| Tiny | Tree Throw |
| Tiny | Tree Grab |
| Tiny | Toss |
| Tiny | Avalanche |
| Treant Protector | Nature's Grasp |
| Treant Protector | Leech Seed |
| Treant Protector | Overgrowth |
| Treant Protector | Eyes In The Forest |
| Troll Warlord | Whirling Axes (Ranged) |
| Troll Warlord | Whirling Axes (Melee) |
| Tusk | Tag Team |
| Tusk | Walrus Kick |
| Tusk | Snowball |
| Tusk | Ice Shards |
| Underlord | Firestorm |
| Underlord | Pit of Malice |
| Undying | Tombstone |
| Undying | Decay |
| Undying | Soul Rip |
| Ursa | Earthshock |
| Vengeful Spirit | Wave of Terror |
| Venomancer | Noxious Plague |
| Venomancer | Venomous Gale |
| Viper | Nosedive |
| Viper | Nethertoxin |
| Viper | Corrosive Skin |
| Visage | Grave Chill |
| Visage | Soul Assumption |
| Void Spirit | Dissimilate |
| Void Spirit | Resonant Pulse |
| Void Spirit | Astral Step |
| Void Spirit | Aether Remnant |
| Warlock | Fatal Bonds |
| Warlock | Shadow Word |
| Warlock | Upheaval |
| Warlock | Chaotic Offering |
| Windranger | Powershot |
| Windranger | Gale Force |
| Winter Wyvern | Arctic Burn increase Tree Destruction Radius |
| Winter Wyvern | Splinter Blast |
| Winter Wyvern | Cold Embrace2b |
| Winter Wyvern | Winter's Curse |
| Witch Doctor | Paralyzing Cask |
| Witch Doctor | Voodoo Restoration |
| Witch Doctor | Death Ward 2a |
| Witch Doctor | Maledict |
| Wraith King | Reincarnation |
| Zeus | Arc Lightning |
| Zeus | Heavenly Jump |
| Zeus | Lightning Bolt |
| Zeus | Nimbus |
| Zeus | Thundergod's Wrath |

`1` Requires talent.  
`2a` Requires Aghanim's Scepter.  
`2b` Requires Aghanim's Shard. [corpus:liquipedia_dota2/area_of_effect@2377200#Hero_ability_AoE_Radius]

## Recent changes

| Version | Date | Subject | Description |
|---|---|---|---|
| 7.37 | 2024-07-31 | Tooltips | An Area of Effect icon was added to all tooltip values affected by Bloodstone and other AoE increases. |
| 7.37 | 2024-07-31 | Primal Beast — Ferocity | **REWORKED:** **OLD:** Uproar no longer grants `10%` radius bonus per stack. **NEW:** Pulverize now grants a `10-second 20%` radius bonus buff per successful slam. |
| 7.36a | 2024-05-26 | Crystal Maiden — Frozen Expanse | Now tied to Freezing Field instead of Arcane Aura. AoE Bonus rescaled from `7/8/9/10%` to `6/8/10%`. The AoE bonus now applies only to Crystal Maiden. |
| 7.36 | 2024-05-22 | AoE bonuses | AoE bonuses now affect all auras and Cleave sources. |
| 7.36 | 2024-05-22 | Crystal Maiden — Arcane Aura | Increases Crystal Maiden's cast range by `50/75/100/125` and provides `7/8/9/10%` AoE Bonus; requires the Frozen Expanse Facet. |
| 7.36 | 2024-05-22 | Necrophos — Sadist | Gains `+50` AoE Increase per current Sadist stack; requires the Profane Potency Facet. |
| 7.36 | 2024-05-22 | Primal Beast — Uproar | When activated, each stack provides `10%` AoE bonus; requires the Ferocity Facet. |
| 7.36 | 2024-05-22 | Rubick — Arcane Supremacy | Every time Rubick casts a spell, he gains `+25` AoE Spell Radius Amplification for `20s`. Multiple instances stack independently; requires the Arcane Accumulation Facet. |

[corpus:liquipedia_dota2/area_of_effect@2377200#Recent_Changes]