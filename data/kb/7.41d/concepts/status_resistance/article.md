---
title: Status Resistance
kind: concept
patch: 7.41d
card:
  entity: status_resistance
  sentences:
  - text: Status Resistance is a hero attribute that reduces the duration of most
      status debuffs, and every unit has base status resistance 0 by default.
    marks:
    - corpus:liquipedia_dota2/status_resistance@2379177
  - text: It generally affects modifiers placed by enemies rather than allies.
    marks:
    - corpus:liquipedia_dota2/status_resistance@2379177#Definition
  - text: Resistance changes apply only to subsequently applied debuffs; existing
      debuffs and their current instances are not updated.
    marks:
    - corpus:liquipedia_dota2/status_resistance@2379177#Definition
  - text: Auras and permanent modifiers have no duration to reduce, and aura linger
      duration is unaffected.
    marks:
    - corpus:liquipedia_dota2/status_resistance@2379177#Definition
  - text: For modifiers with damage over time, the tick interval adapts to a reduced
      duration so total damage over time stays the same.
    marks:
    - corpus:liquipedia_dota2/status_resistance@2379177#Definition
  - text: Status resistance does not affect movement-speed slow duration, which Slow
      Resistance sources manipulate.
    marks:
    - corpus:liquipedia_dota2/status_resistance@2379177#Definition
  - text: Status resistance sources stack multiplicatively, preventing different stacked
      sources from reaching 100% resistance.
    marks:
    - corpus:liquipedia_dota2/status_resistance@2379177#Stacking
  - text: Bonuses from Sange-based items do not stack with each other; the higher
      value takes priority.
    marks:
    - corpus:liquipedia_dota2/status_resistance@2379177#Equations
  - text: The status resistance multiplier equals (1 − base status resistance) × (1
      − MAX(Sange-%based)) × the product of (1 − each status resistance modifier).
    marks:
    - corpus:liquipedia_dota2/status_resistance@2379177#Equations
  - text: Total debuff duration equals original duration × status resistance multiplier
      × the product of (1 − each debuff-duration modifier).
    marks:
    - corpus:liquipedia_dota2/status_resistance@2379177#Equations
  - text: With base resistance 0, Bulldoze resistance 0.5, and Sange and Yasha resistance
      0.16, Spirit Breaker has 58% resistance and a 0.42 debuff-duration multiplier.
    marks:
    - corpus:liquipedia_dota2/status_resistance@2379177#Examples
  - text: Status resistance affects incoming debuff durations, whereas debuff-duration
      manipulation affects outgoing debuff durations.
    marks:
    - corpus:liquipedia_dota2/status_resistance@2379177#Debuff_Duration_Manipulation
---

# Status Resistance

Status Resistance is a hero attribute that reduces the duration of most status debuffs. Every unit has a base status resistance of 0 by default. [corpus:liquipedia_dota2/status_resistance@2379177]

## Definition

Status resistance generally affects only modifiers placed by enemies, not allies. Technical exceptions exist, and not every modifier is affected. When status resistance changes, the new debuff duration applies only to subsequently applied debuffs; existing debuffs and their current instances are not updated.

| Component | Behavior | Example |
|---|---|---|
| Base Status Resistance | Every unit currently has a base 0- status resistance. | — |
| Auras | Do not have a duration to reduce. The aura linger duration is not affected. | Natural Order |
| Effect Delay | Not reduced if the purpose of a temporary modifier is to delay another ability effect/component. | Reincarnation |
| Permanent Modifiers | Do not have a duration to reduce. | Brain Drain |
| Damage Over Time | Damage over time is generally not reduced. Total damage dealt over time stays the same. Modifiers with damage over time have the damage tick interval adapted to the reduced duration. | Shackles |
| Attack Speed Slow Duration | Reduces attack speed slowing sources' duration. | Dispose |
| Movement Speed Slow Duration | Slow Resistance sources manipulate movement speed slow duration and are not affected by status resistance sources. | Grow |
| %Bonus/Reductions | Status Resistance bonus or reduction sources from abilities, items, talents. Percentage-based values stack independently of each other. | Bulldoze [corpus:liquipedia_dota2/status_resistance@2379177#Definition] |

### Equations

Status resistance bonuses from Sange-based items do not stack with each other; the higher status resistance value takes priority.

\[
\text{Total Status Resistance}=1-\text{Status Resistance Multiplier}
\]

\[
\text{Status Resistance Multiplier}
=(1-\text{Base Status Resistance})
\times(1-\operatorname{MAX}(\text{Sange-%based}))
\times\prod_{i=1}^{n}(1-\text{Status Resistance Modifiers }i)
\]

\[
\text{Total Debuff Duration}
=\text{Original Duration}
\times\text{Status Resistance Multiplier}
\times\prod_{i=1}^{n}(1-\text{Debuff Duration Modifiers }i)
\]
[corpus:liquipedia_dota2/status_resistance@2379177#Equations]

## Stacking

All status resistance sources stack multiplicatively. Consequently, a unit's status resistance changes less when its existing resistance is higher and more when it is lower. This prevents a unit from reaching 100% status resistance by stacking different sources.

Only certain status-resistance-granting sources have stacking restrictions, described as being separated into 3 groups. Sange-based item bonuses do not stack with each other, and the higher value takes priority. Sources from different groups stack independently but remain multiplicative with each other.

| Group | Category | Rule or sources |
|---|---|---|
| Group 1 | Sange-based | Sange-based items; Sange and Yasha (16%) |
| Group 2 | Stack-based | Stack-based bonuses/reductions stack additively with themselves and multiplicatively with other sources; Corrosive Weaponry (Pre 7.36) |
| Group 3 | Misc | Sources outside the first 2 groups fully stack with each other, with multiple instances of themselves, and with other item bonuses; %Bonuses/Reductions from Abilities; Talents; Spell Steal |
| Group 4 | Outgoing Debuff Duration Amp | Timeless Relic [corpus:liquipedia_dota2/status_resistance@2379177#Stacking] |

### Examples

#### Example 1a: Status Resistance Bonus and Multiplier

Spirit Breaker has Sange and Yasha equipped and level 2 Bulldoze active.

| Input | Value |
|---|---:|
| Base unit status resistance | 0 |
| Bulldoze bonus status resistance | 0.5 |
| Sange and Yasha bonus status resistance | 0.16 |

\[
\begin{aligned}
\text{Total Status Resistance}
&=1-(1-0)*(1-0.5)*(1-0.16)\\
&=0.58
\end{aligned}
\]

Spirit Breaker has 58% status resistance, and all debuff duration applied to him is multiplied by 0.42.

#### Example 1b: Debuff Duration and Multiplier

For a 3-second debuff on the Spirit Breaker from Example 1a:

\[
\begin{aligned}
\text{Total Debuff Duration}
&=3*0.42\\
&=1.26
\end{aligned}
\]

The debuff affects Spirit Breaker for 1.26s instead of 3s.

#### Example 2: Actual or Total Debuff Duration

Spirit Breaker from the previous example now has both Sange and Yasha and is affected by a 0.1-status resistance reduction. The enemy Rubick has Timeless Relic equipped.

| Input | Value |
|---|---:|
| Base unit status resistance | 0 |
| Sange and Yasha bonus status resistance | 16/100 |
| Status resistance reduction | -0.1 |
| Original debuff duration | 3-second |

\[
\begin{aligned}
\text{Total Status Resistance}
&=1-(1-0)*(1-0.16)*(1--0.1)\\
&=0.076
\end{aligned}
\]

Spirit Breaker has 7.6% status resistance, and all debuff duration applied to him is multiplied by 0.924 before other debuff duration amplification is applied. [corpus:liquipedia_dota2/status_resistance@2379177#Examples]

## Modifying Status Resistance

Several abilities and items have abilities that grant or reduce status resistance. [corpus:liquipedia_dota2/status_resistance@2379177#Modifying_Status_Resistance]

### Increasing Sources

| Source | Requirement |
|---|---|
| Aeon Disk – Combo Breaker | — |
| Fire – Permanent Phase | — |
| Night Stalker – Hunter in the Night | Requires talent. |
| Roshan – Spell Block | — |
| Slardar – Seaborn Sentinel | Requires Aghanim's Scepter. |
| Spirit Breaker – Bulldoze | — |
| Tiny – Insurmountable | — |
| Unrelenting Eye – Relentless | — |
| Ursa – Earthshock | Requires Aghanim's Shard. |
| Ursa – Enrage | — [corpus:liquipedia_dota2/status_resistance@2379177#Increasing_Sources] |

#### Items

These items grant bonus status resistance to the hero who has them equipped. Values exclude portions from actives or auras.

| Item | Value | Item Cost | Cost/Value Point |
|---|---:|---:|---:|
| Sange and Yasha | 16% | 4200 | 262.5 |
| Titanic Enchantment | 0.06% | N/A | N/A [corpus:liquipedia_dota2/status_resistance@2379177#Items] |

#### Talents

Status Resistance is a passive ability that affects self, with a status resistance bonus that varies. It increases the hero's status resistance and stacks multiplicatively with other status resistance sources. Its modifier is hidden.

| Existing values |
|---|
| 10%/15%/20%/25% |

Heroes can have talents that grant bonus status resistance under the following talent-table categories:

| Bonus | Level 10 Left | Level 10 Right | Level 15 Left | Level 15 Right | Level 20 Left | Level 20 Right | Level 25 Left | Level 25 Right |
|---|---|---|---|---|---|---|---|---|
| Status Resistance |  |  |  |  |  |  |  |  [corpus:liquipedia_dota2/status_resistance@2379177#Talents] |

### Reducing Sources

| Source |
|---|
| Bane – Ichor of Nyctasha [corpus:liquipedia_dota2/status_resistance@2379177#Reducing_Sources] |

### Debuff Duration Manipulation

Status resistance affects incoming debuff durations, whereas debuff duration manipulation affects outgoing debuff durations. Any ability whose duration would be reduced by status resistance has its duration increased by debuff duration increases.

| Debuff Duration Amplification Source |
|---|
| Bristleback – Prickly |
| Lion – To Hell and Back |
| Rubick – Curiosity [corpus:liquipedia_dota2/status_resistance@2379177#Debuff_Duration_Manipulation] |

## Unaffected Abilities

| Unaffected ability or effect |
|---|
| Abaddon – Curse of Avernus' initial debuff |
| Alchemist – Acid Spray |
| Ancient Apparition – Cold Feet's initial debuff |
| Ancient Apparition – Ice Vortex |
| Anti-Mage – Mana Void's kill time window modifier |
| Batrider – Flamebreak's damage debuff |
| Brewmaster – Cinder Brew's additional duration upon ignition |
| Disruptor – Thunder Strike's main debuff |
| Disruptor – Kinetic Field's slowing barrier |
| Disruptor – Static Storm |
| Dark Willow – Cursed Crown's initial debuff |
| Doom – Infernal Blade's damage debuff |
| Dragon Knight – Elder Dragon Form's poison debuff |
| Earth Spirit – Geomagnetic Grip's pull |
| Earth Spirit – Magnetize |
| Elder Titan – Natural Order |
| Enigma – Malefice's main debuff |
| Enigma – Black Hole |
| Faceless Void – Chronosphere |
| Fire – Permanent Immolation |
| Huskar – Burning Spear |
| Invoker – Cold Snap's main debuff |
| Invoker – Chaos Meteor |
| Jakiro – Dual Breath's damage debuff |
| Jakiro – Macropyre |
| Keeper of the Light – Will-O-Wisp |
| Kunkka – Torrent's knockup |
| Lich – Sinister Gaze |
| Lina – Laguna Blade's damage delay |
| Lion – Finger of Death's damage delay |
| Magnus – Skewer's drag debuff |
| Mars – Spear of Mars' drag debuff |
| Mars – Arena of Blood's slowing barrier |
| Medusa – Stone Gaze's slow and facing timer |
| Naga Siren – Song of the Siren |
| Necrophos – Ghost Shroud |
| Necrophos – Heartstopper Aura |
| Necrophos – Reaper's Scythe |
| Night Stalker – Crippling Fear |
| Oracle – Purifying Flames |
| Pangolier – Rolling Thunder's knockback/timeout modifiers |
| Phoenix – Supernova's damage debuff |
| Pudge – Meat Hook |
| Pugna – Nether Ward |
| Pugna – Life Drain |
| Razor – Static Link |
| Riki – Smoke Screen |
| Sand King – Sand Storm's talent-granted debuff |
| Sand King – Caustic Finale's initial debuff |
| Shadow Demon – Shadow Poison |
| Shadow Fiend – Presence of the Dark Lord |
| Silencer – Last Word's initial debuff |
| Snapfire – Lil' Shredder's second and following stacks |
| Sniper – Shrapnel |
| Sniper – Assassinate's vision modifier |
| Spirit Breaker – Charge of Darkness' vision modifier |
| Spirit Breaker – Nether Strike's vision modifier |
| Timbersaw – Chakram's slow while stationary |
| Timbersaw – Second Chakram's slow while stationary |
| Tiny – Avalanche |
| Tiny – Toss |
| Treant Protector – Nature's Grasp |
| Tusk – Snowball's vision modifier |
| Tusk – Walrus PUNCH!'s knockup |
| Tusk – Walrus Kick's knockback |
| Underlord – Firestorm |
| Underlord – Pit of Malice's interval timer |
| Underlord – Atrophy Aura |
| Undying – Flesh Golem's attack debuff |
| Venomancer – Poison Nova |
| Vhoul Assassin – Envenomed Weapon |
| Viper – Nethertoxin |
| Warlock – Shadow Word |
| Warlock Golem – Permanent Immolation |
| Weaver – The Swarm |
| Windranger – Windrun |
| Winter Wyvern – Winter's Curse's taunt |
| Witch Doctor – Maledict |
| Assault Cuirass – Assault Aura |
| Dagon – Energy Burst's damage delay |
| Dragon Scale – Afterburn |
| Eul's Scepter of Divinity – Cyclone |
| Fallen Sky – Fallen Sky's damage debuff |
| Force Staff – Force |
| Hurricane Pike – Hurricane Thrust |
| Meteor Hammer – Meteor Hammer's damage debuff |
| Radiance – Burn |
| Spirit Vessel – Soul Release |
| Urn of Shadows – Soul Release [corpus:liquipedia_dota2/status_resistance@2379177#Unaffected_Abilities] |

## Duration Reduced

| Ability or effect whose duration is reduced |
|---|
| Abaddon – Curse of Avernus' curse debuff |
| Alchemist – Unstable Concoction |
| Ancient Apparition – Cold Feet's stun |
| Ancient Apparition – Chilling Touch |
| Ancient Apparition – Ice Blast |
| Ancient Thunderhide – Slam |
| Anti-Mage – Mana Void's stun and cooldown debuffs |
| Arc Warden – Spark Wraith |
| Axe – Berserker's Call |
| Axe – Counter Helix Shard Debuff Duration |
| Bane – Nightmare's main and invulnerability debuffs |
| Bane – Enfeeble |
| Bane – Fiend's Grip |
| Batrider – Sticky Napalm |
| Batrider – Flamebreak's knockback |
| Batrider – Flaming Lasso |
| Beastmaster – Wild Axes |
| Beastmaster – Primal Roar's primary and secondary target debuffs |
| Bloodseeker – Bloodrage |
| Bloodseeker – Blood Rite |
| Bloodseeker – Rupture |
| Bounty Hunter – Shuriken Toss |
| Bounty Hunter – Shadow Walk |
| Bounty Hunter – Track |
| Brewmaster – Thunder Clap |
| Brewmaster – Cinder Brew's initial duration |
| Bristleback – Viscous Nasal Goo |
| Bristleback – Quill Spray |
| Broodmother – Spawn Spiderlings |
| Centaur Conqueror – War Stomp |
| Centaur Warrunner – Hoof Stomp |
| Centaur Warrunner – Stampede's trample slow |
| Chaos Knight – Chaos Bolt |
| Chaos Knight – Reality Rift |
| Chen – Penitence |
| Clockwerk – Battery Assault's mini-stuns |
| Clockwerk – Power Cogs' knockback |
| Clockwerk – Hookshot |
| Crystal Maiden – Crystal Nova |
| Crystal Maiden – Frostbite |
| Crystal Maiden – Freezing Field |
| Dark Seer – Vacuum |
| Dark Seer – Ion Shell |
| Dark Seer – Wall of Replica |
| Dark Willow – Bramble Maze |
| Dark Willow – Cursed Crown's stun |
| Dark Willow – Terrorize |
| Dazzle – Bad Juju |
| Death Prophet – Silence |
| Death Prophet – Exorcism's Aghanim's Scepter slow |
| Disruptor – Thunder Strike's slow |
| Doom – Infernal Blade's stun |
| Doom – Doom |
| Dragon Knight – Breathe Fire |
| Dragon Knight – Dragon Tail |
| Dragon Knight – Elder Dragon Form's frost debuff |
| Drow Ranger – Frost Arrows |
| Drow Ranger – Gust's knockback and silence |
| Drow Ranger – Multishot's Frost Arrows |
| Earth – Hurl Boulder |
| Earth Spirit – Boulder Smash's knockback and slow |
| Earth Spirit – Rolling Boulder |
| Earth Spirit – Geomagnetic Grip's silence |
| Earth Spirit – Enchant Remnant |
| Earthshaker – Fissure |
| Earthshaker – Aftershock |
| Elder Titan – Echo Stomp |
| Elder Titan – Earth Splitter |
| Ember Spirit – Searing Chains |
| Enchantress – Enchant |
| Enigma – Malefice's stun |
| Faceless Void – Time Dilation |
| Faceless Void – Time Lock |
| Familiar – Stone Form |
| Forged Spirit – Melting Strike |
| Ghost – Frost Attack |
| Grimstroke – Stroke of Fate |
| Grimstroke – Phantom's Embrace's latch and silence durations |
| Grimstroke – Ink Swell's stun |
| Grimstroke – Soulbind |
| Gyrocopter – Homing Missile |
| Gyrocopter – Call Down |
| Hellbear Smasher – Thunder Clap |
| Huskar – Inner Fire |
| Huskar – Life Break's slow and taunt |
| Invoker – Cold Snap's stun |
| Invoker – Tornado |
| Invoker – Deafening Blast |
| Io – Tether's slow |
| Jakiro – Ice Path |
| Keeper of the Light – Blinding Light's knockback and blind |
| Keeper of the Light – Chakra Magic's mana leak debuff |
| Kunkka – Torrent's slow |
| Kunkka – X Marks the Spot |
| Kunkka – Ghostship |
| Legion Commander – Duel |
| Leshrac – Split Earth |
| Leshrac – Lightning Storm's slow |
| Lich – Frost Blast |
| Lich – Frost Shield |
| Lich – Chain Frost |
| Lifestealer – Open Wounds |
| Lina – Light Strike Array |
| Lion – Earth Spike |
| Lion – Hex |
| Lion – Mana Drain |
| Lone Druid – Savage Roar |
| Luna – Lucent Beam |
| Luna – Eclipse's talent stun |
| Lycan – Howl |
| Magnus – Shockwave's pull and slow |
| Magnus – Skewer's slow |
| Magnus – Reverse Polarity |
| Mars – Spear of Mars impale stun and secondary knockback |
| Mars – God's Rebuke's knockback and slow |
| Mars – Arena of Blood's knockback |
| Medusa – Mystic Snake's slow and petrify |
| Medusa – Stone Gaze's petrify |
| Meepo – Earthbind |
| Mirana – Sacred Arrow |
| Monkey King – Boundless Strike |
| Monkey King – Jingu Mastery |
| Monkey King – Primal Spring |
| Morphling – Adaptive Strike (Strength) |
| Mud Golem – Hurl Boulder |
| Naga Siren – Ensnare |
| Naga Siren – Rip Tide |
| Nature's Prophet – Wrath of Nature's Aghanim's Scepter treants debuff |
| Necronomicon Archer – Purge |
| Night Stalker – Void |
| Nyx Assassin – Impale |
| Nyx Assassin – Spiked Carapace |
| Nyx Assassin – Vendetta |
| Ogre Frostmage – Ice Armor's slow |
| Ogre Magi – Fireblast |
| Ogre Magi – Unrefined Fireblast |
| Oracle – Fortune's End |
| Oracle – Fate's Edict |
| Outworld Destroyer – Astral Imprisonment |
| Outworld Destroyer – Essence Flux |
| Pangolier – Lucky Shot |
| Pangolier – Rolling Thunder's stun |
| Phantom Assassin – Stifling Dagger |
| Phantom Lancer – Spirit Lance |
| Phoenix – Supernova's stun |
| Puck – Waning Rift |
| Puck – Dream Coil's leash and stun debuffs |
| Pudge – Dismember |
| Pugna – Decrepify |
| Queen of Pain – Scream of Pain's talent fear |
| Queen of Pain – Sonic Wave's knockback |
| Razor – Plasma Field's slow |
| Razor – Eye of the Storm's armor reduction |
| Roshan – Bash |
| Roshan – Slam |
| Rubick – Telekinesis' lift and stun debuffs |
| Rubick – Fade Bolt |
| Sand King – Burrowstrike |
| Sand King – Caustic Finale's slow |
| Sand King – Epicenter |
| Satyr Banisher – Purge |
| Shadow Demon – Disruption |
| Shadow Demon – Demonic Purge |
| Shadow Fiend – Shadowraze |
| Shadow Fiend – Requiem of Souls' slow and fear |
| Shadow Shaman – Hex |
| Shadow Shaman – Shackles |
| Shard Golem – Hurl Boulder |
| Silencer – Glaives of Wisdom |
| Silencer – Last Word's silence |
| Silencer – Global Silence |
| Skywrath Mage – Concussive Shot |
| Skywrath Mage – Ancient Seal |
| Slardar – Slithereen Crush |
| Slardar – Bash of the Deep |
| Slardar – Corrosive Haze |
| Slark – Pounce |
| Slark – Essence Shift |
| Snapfire – Scatterblast |
| Snapfire – Firesnap Cookie's stun |
| Snapfire – Lil' Shredder's first stack |
| Snapfire – Mortimer Kisses |
| Sniper – Headshot |
| Sniper – Assassinate's stun |
| Spectre – Spectral Dagger |
| Spectre – Desolate |
| Spiderling – Spawn Spiderite |
| Spirit Bear – Entangling Claws |
| Spirit Breaker – Charge of Darkness' stun |
| Spirit Breaker – Greater Bash |
| Storm – Cyclone |
| Storm Spirit – Electric Vortex |
| Storm Spirit – Overload |
| Sven – Storm Hammer |
| Techies – Blast Off! |
| Templar Assassin – Meld's armor reduction and talent stun |
| Terrorblade – Reflection |
| Terrorblade – Metamorphosis' Aghanim's Scepter fear |
| Tidehunter – Gush |
| Tidehunter – Anchor Smash |
| Tidehunter – Ravage |
| Timbersaw – Whirling Death |
| Timbersaw – Chakram's slow while passing |
| Timbersaw – Second Chakram's slow while passing |
| Tinker – Laser |
| Tinker – Heat-Seeking Missile's talent stun |
| Treant Protector – Leech Seed |
| Treant Protector – Overgrowth |
| Troll Warlord – Berserker's Rage root |
| Troll Warlord – Whirling Axes (Melee) |
| Troll Warlord – Whirling Axes (Ranged) |
| Troll Warlord – Battle Trance cast on enemy |
| Tusk – Snowball's stun |
| Tusk – Tag Team |
| Tusk – Walrus PUNCH!'s slow |
| Tusk – Walrus Kick's slow |
| Underlord – Pit of Malice's root |
| Undying Zombie – Deathlust |
| Ursa – Earthshock |
| Ursa – Fury Swipes |
| Vengeful Spirit – Magic Missile |
| Vengeful Spirit – Wave of Terror |
| Vengeful Spirit – Nether Swap's Aghanim's Scepter fear |
| Visage – Grave Chill |
| Void Spirit – Aether Remnant |
| Void Spirit – Dissimilate's talent stun |
| Void Spirit – Astral Step |
| Warlock – Fatal Bonds |
| Warlock – Upheaval |
| Warlock – Chaotic Offering's stun |
| Windranger – Shackleshot |
| Winter Wyvern – Splinter Blast |
| Winter Wyvern – Winter's Curse on primary target |
| Witch Doctor – Paralyzing Cask |
| Wraith King – Wraithfire Blast's stun |
| Wraith King – Reincarnation's slow |
| Zeus – Lightning Bolt |
| Abyssal Blade – Overwhelm |
| Abyssal Blade – Bash |
| Orb of Blight – Lesser Corruption |
| Bloodthorn – Soul Rend |
| Desolator – Corruption |
| Diffusal Blade – Inhibit |
| Dust of Appearance – Reveal |
| Echo Sabre – Echo Strike |
| Ethereal Blade – Ether Blast |
| Eye of Skadi – Cold Attack |
| Fallen Sky – Fallen Sky's stun |
| Grove Bow – Magic Amp |
| Heaven's Halberd – Disarm |
| Medallion of Courage – Valor |
| Meteor Hammer – Meteor Hammer's stun |
| Mind Breaker – Silence Strike |
| Nullifier – Nullify's main and slow debuffs |
| Orchid Malevolence – Soul Burn |
| Rod of Atos – Cripple |
| Scythe of Vyse – Hex |
| Shiva's Guard – Arctic Blast |
| Silver Edge – Shadow Walk's break debuff |
| Skull Basher – Bash |
| Stygian Desolator – Greater Corruption |
| Veil of Discord – Magic Weakness [corpus:liquipedia_dota2/status_resistance@2379177#Duration_Reduced] |

## Dynamic Tick Intervals

Several abilities that operate at intervals adapt those intervals to changed durations, including changes caused by status resistance or debuff duration amplification.

| Ability with dynamic tick intervals |
|---|
| Ancient Apparition – Ice Blast |
| Bane – Fiend's Grip |
| Batrider – Flaming Lasso |
| Brewmaster – Cinder Brew |
| Crystal Maiden – Frostbite |
| Dark Willow – Bramble Maze |
| Doom – Doom |
| Ember Spirit – Searing Chains |
| Necronomicon Archer – Purge |
| Pudge – Dismember |
| Satyr Banisher – Purge |
| Shadow Demon – Demonic Purge |
| Shadow Shaman – Shackles |
| Spirit Bear – Entangling Claws |
| Treant Protector – Overgrowth |
| Diffusal Blade – Inhibit [corpus:liquipedia_dota2/status_resistance@2379177#Dynamic_Tick_Intervals] |

## Other Interactions

| Ability or item | Interaction |
|---|---|
| Bane – Nightmare | Its duration is reduced normally when cast on an enemy. When transferred to another enemy via an attack command, the invulnerability modifier always uses the base duration and is then reduced by the new target's status resistance. The Nightmare modifier copies the previous target's reduced duration and is then further reduced by the new target's status resistance. |
| Beastmaster – Primal Roar | Reduces the duration of all debuffs it can place on primary and secondary targets. On secondary targets, knockback speed adapts to the reduced duration so that knockback distance remains the same. |
| Kunkka – X Marks the Spot | Reduces duration normally. When the target has more than 75% status resistance, it is no longer returned automatically when the effect expires. |
| Lifestealer – Open Wounds | Reduces duration. The slow tick rate does not adapt to the reduced duration. |
| Medallion of Courage – Valor | Reduces debuff duration on the target. The debuff on the caster does not adapt. |
| Sand King – Caustic Finale | When applied by attacks, it reduces only the slow duration after the explosion and does not affect the initial debuff. When applied with Burrowstrike, it reduces the initial debuff duration as well as the slow duration. |
| Silencer – Glaives of Wisdom | The self-buff duration is reduced along with the enemy debuff duration. |
| Slark – Essence Shift | The self-buff duration is reduced along with the enemy debuff duration. |
| Solar Crest – Shine | Reduces debuff duration on the target. The penalties on the caster do not adapt. |
| Spectre – Spectral Dagger | Reduces the trail-creating debuff duration. When directly targeted, it may reduce the slow debuff duration. When not directly targeted, it does not affect the slow debuff. |
| Templar Assassin – Psionic Trap | When activated through the sub-spell on the caster or through Psionic Projection, it reduces only the slow value. When activated through the sub-spell on the trap itself, it reduces the slow value and duration and increases damage per tick. [corpus:liquipedia_dota2/status_resistance@2379177#Other_Interactions] |

## Recent Changes

| Version | Date | Description |
|---|---|---|
| 7.34 | 2023-08-08 | Status Resistance no longer affects the impact of movement speed slow sources. |
| 7.29 | 2021-04-09 | Tiny now has a talent that grants 15% status resistance. |
| 7.29 | 2021-04-09 | Ursa now has a talent that grants Enrage 10% status resistance. |
| 7.29 | 2021-04-09 | Troll Warlord with Aghanim's Shard upgrade has a new Rampage ability that grants 25% status resistance to the team while is in melee form. |
| 7.28 | 2020-12-17 | Created Ceremonial Robe. |
| 7.28 | 2020-12-17 | Removed Trident. |
| 7.28 | 2020-12-17 | Enfeeble no longer provides status resistance reduction. |
| 7.28 | 2020-12-17 | Arcane Supremacy no longer provides debuff duration amplification. |
| 7.28 | 2020-12-17 | Fire now has 30% status resistance. |
| 7.28 | 2020-12-17 | Satanic no longer grants status resistance. |
| 7.28 | 2020-12-17 | Status resistance bonuses from Sange-based items, such as Sange and Yasha, Kaya and Sange, and Heaven's Halberd, no longer stack with each other. |
| 7.28 | 2020-12-17 | Reduced Heaven's Halberd status resistance bonus from 20% to 16%. |
| 7.28 | 2020-12-17 | Increased Sange and Yasha status resistance bonus from 20% to 25%. |
| 7.28 | 2020-12-17 | Increased Kaya and Sange status resistance bonus from 20% to 25%. [corpus:liquipedia_dota2/status_resistance@2379177#Recent_Changes] |