---
title: Damage Types
kind: concept
patch: 7.41d
card:
  entity: damage_types
  sentences:
  - text: Damage types are the three main classifications—Physical, Magical, and Pure—of
      damage that reduces a unit’s current health.
    marks:
    - corpus:liquipedia_dota2/damage_types@2346392
  - text: Damage sources are attacks, abilities, and items.
    marks:
    - corpus:liquipedia_dota2/damage_types@2346392#Damage_Sources
  - text: A unit’s total Attack Damage is the sum of its Main Attack Damage and Bonus
      Attack Damage.
    marks:
    - corpus:liquipedia_dota2/damage_types@2346392#Damage_Sources
  - text: Spell damage includes all abilities, including item abilities and attack
      modifiers, that deal magical, physical, or pure damage.
    marks:
    - corpus:liquipedia_dota2/damage_types@2346392#Damage_Sources
  - text: Armor reduces physical damage by a percentage, while damage block applies
      a flat reduction.
    marks:
    - corpus:liquipedia_dota2/damage_types@2346392#Physical
  - text: Ethereal units are unaffected by physical damage.
    marks:
    - corpus:liquipedia_dota2/damage_types@2346392#Physical
  - text: Magic resistance reduces magical damage, while ethereal status amplifies
      it.
    marks:
    - corpus:liquipedia_dota2/damage_types@2346392#Magical
  - text: Pure damage ignores Armor, Magic Resistance, and Damage Block.
    marks:
    - corpus:liquipedia_dota2/damage_types@2346392#Pure
  - text: Against abilities that do not pierce it, debuff immunity grants 100% resistance
      to pure and reflected damage, causing 0 damage.
    marks:
    - corpus:liquipedia_dota2/damage_types@2346392#Debuff_Immunity
  - text: Damage flags can modify behavior through HP Removal, No-reflection, No-Spell-Lifesteal,
      and No-Spell-Amplification.
    marks:
    - corpus:liquipedia_dota2/damage_types@2346392#Flags
  - text: HP Removal ignores and does not trigger on-damage effects.
    marks:
    - corpus:liquipedia_dota2/damage_types@2346392#HP_Removal
  - text: Instant Kill kills units without using damage and ignores almost all damage
      manipulation.
    marks:
    - corpus:liquipedia_dota2/damage_types@2346392#Instant_Kill
---

# Damage Types

## Overview

Damage is any means by which a unit’s current health can be reduced. The three main damage classifications are Physical, Magical, and Pure. [corpus:liquipedia_dota2/damage_types@2346392]

## Definition

The listed damage types are Physical, Magical, and Pure. [corpus:liquipedia_dota2/damage_types@2346392#Definition]

## Damage Sources

Damage can come from attacks, abilities, and items. Damage sources are generally divided into Attack Damage and Spell Damage.

Attack damage is the damage dealt per attack and is displayed on the sword icon in the HUD. A unit’s total attack damage is the sum of its Main Attack Damage and Bonus Attack Damage. Most attack damage is physical, with some exceptions.

Spell damage (`Sp`) is usually dealt in a separate instance from attack damage, with some exceptions. It includes all abilities—including item abilities and attack modifiers—that deal magical, physical, or pure damage. [corpus:liquipedia_dota2/damage_types@2346392#Damage_Sources]

## Damage Classification

All damage is classified as Physical, Magical, or Pure. Physical damage is reduced by Armor or Damage Block; Magical damage is reduced by Magic Resistance and Magical Damage Barrier; Pure damage is generally not reduced by anything except damage reduction that affects all damage types, such as Enrage and Defense Matrix.

All three damage types interact with other damage-related mechanics. Some damage sources also have the HP Removal flag, causing them to ignore mechanics that would otherwise manipulate the damage.

| Mechanic | Physical Attacks | Physical Abilities | Magical Attacks | Magical Abilities | Pure Attacks | Pure Abilities |
|---|---|---|---|---|---|---|
| Armor | Reduced | Reduced | - | - | - | - |
| Damage Block | Reduced | Normal¹ | - | - | - | - |
| Magic Resistance | - | - | Reduced | Reduced | - | - |
| Magical Damage Barrier | - | - | 0 | 0 | - | - |
| Ethereal | 0 | 0 | Amplified | Amplified | - | - |
| Evasion | May Miss | - | May Miss | - | May Miss | - |
| Invulnerability | 0; no effect on all damage types |  |  |  |  |  |
| Damage Manipulation² | Amplifies, Reduces and Negates all damage types |  |  |  |  |  |
| Damage Negation² |  |  |  |  |  |  |

¹ Except Moon Glaives: although considered spell damage, its damage is blocked.

² These categories include only ability effects that directly manipulate damage by reducing it, such as Bristleback; amplifying it, such as Bloodrage; or completely negating it, such as Refraction. Abilities that amplify or reduce damage by increasing or reducing units’ magic resistance or armor are excluded. [corpus:liquipedia_dota2/damage_types@2346392#Damage_Classification]

### Debuff Immunity

Debuff immunity is a modifier that stops most debuff effects on a unit without dispelling the debuffs or preventing them from being placed. It also grants resistance against magical damage, immunity against pure and reflected damage, and protection against mana loss.

It inherently grants increased magic resistance in an amount determined by the source ability. It also grants 100% resistance against pure and reflected damage, causing them to deal 0 damage. A 0-damage instance is still registered and may trigger on-damage effects unless flagged as HP Removal.

These resistances apply only against abilities that do not pierce debuff immunity. Magical, pure, or reflected damage from an ability that pierces debuff immunity completely ignores the corresponding resistances. Magical damage is dealt as though the debuff-immunity magic-resistance bonus were absent.

Physical damage does not interact with debuff immunity, regardless of whether the ability pierces it. [corpus:liquipedia_dota2/damage_types@2346392#Debuff_Immunity]

## Physical Damage

Most attack damage from all units, including buildings, is physical unless stated otherwise; certain abilities also deal physical damage. Total physical damage received is affected by armor through percentage reductions and by damage block through flat reductions. Ethereal units are unaffected by physical damage.

Some abilities, including Guardian Angel and Cold Embrace, provide physical-damage immunity, although affected units can still be targeted by attacks and abilities.

Physical damage from abilities and theoretically from items is usually unaffected by defense class unless it directly manipulates attack damage, as with attack-damage-increasing abilities or Exorcism. Physical damage from these abilities, except Moon Glaives, is affected by armor but not by evasion or damage block.

| Abilities Dealing Physical Damage |
|---|
| Sven – Great Cleave² |
| Weaver – The Swarm⁴ |
| Tiny – Tree Grab |
| Razor – Eye of the Storm |
| Viper – Predator |
| Slardar – Slithereen Crush |
| Dragon Knight – Elder Dragon Form² |
| Alchemist – Unstable Concoction |
| Alchemist – Unstable Concoction Throw |
| Medusa – Gorgon's Grasp |
| Bristleback – Hairball |
| Bristleback – Quill Spray |
| Centaur Warrunner – Retaliate |
| Pangolier – Rolling Thunder |
| Phantom Assassin – Fan of Knives |
| Primal Beast – Onslaught |
| Primal Beast – Rock Throw |
| Kunkka – Tidebringer² |
| Death Prophet – Exorcism² |
| Death Prophet – Silence |
| Storm – Wind Walk |
| Battle Fury – Cleave² |
| Mage Slayer – Mage Slayer |
| Skeleton Archer – Searing Arrows |
| Cleave – Cleave² |
| Ancient Black Dragon – Splash Attack |
| Ancient Prowler Shaman – Desecrate |
| Ancient Prowler Shaman – Petrify |

¹ Damage is directly added to total attack damage.

² Damage from these abilities is also affected by defense class.

³ Half the damage dealt is physical and the other half magical.

⁴ Damage dealt is blocked by damage block. [corpus:liquipedia_dota2/damage_types@2346392#Physical]

## Magical Damage

Magical damage primarily comes from abilities. The majority of abilities deal magical damage unless stated otherwise. Magical damage is reduced by magic resistance and amplified against ethereal units.

| Abilities Dealing Magical Damage |
|---|
| Warlock Golem – Permanent Immolation |
| Earth – Hurl Boulder |
| Astral Spirit – Echo Stomp |
| Fallen Sky – Fallen Sky |
| Fae Grenade – Shadow Brand |
| Witchbane – Subjugate |
| Shadow Fiend – Requiem of Souls |
| Drow Ranger – Glacier |
| Sven – Storm Hammer |
| Pugna – Life Drain |
| Pugna – Nether Blast |
| Pugna – Nether Ward |
| Clockwerk – Battery Assault |
| Clockwerk – Hookshot |
| Clockwerk – Power Cogs |
| Clockwerk – Rocket Flare |
| Earthshaker – Aftershock |
| Earthshaker – Echo Slam |
| Earthshaker – Fissure |
| Ancient Apparition – Chilling Touch |
| Ancient Apparition – Cold Feet |
| Ancient Apparition – Ice Vortex |
| Weaver – Shukuchi |
| Lina – Dragon Slave |
| Lina – Laguna Blade |
| Lina – Light Strike Array |
| Lina – Slow Burn |
| Vengeful Spirit – Magic Missile |
| Vengeful Spirit – Nether Swap |
| Vengeful Spirit – Wave of Terror |
| Tidehunter – Dead in the Water |
| Tidehunter – Gush |
| Tidehunter – Ravage |
| Lion – Earth Spike |
| Lion – Finger of Death |
| Lion – Mana Drain |
| Morphling – Adaptive Strike |
| Doom – Infernal Blade |
| Doom – Scorched Earth |
| Bloodseeker – Blood Rite |
| Lich – Chain Frost |
| Lich – Frost Blast |
| Lich – Frost Shield |
| Lich – Ice Spire |
| Tiny – Avalanche |
| Tiny – Toss |
| Razor – Plasma Field |
| Viper – Nethertoxin |
| Viper – Nosedive |
| Viper – Poison Attack |
| Viper – Viper Strike |
| Leshrac – Lightning Storm |
| Leshrac – Pulse Nova |
| Leshrac – Split Earth |
| Windranger – Powershot |
| Mirana – Leap |
| Mirana – Starstorm |
| Nature's Prophet – Curse of the Oldgrowth |
| Nature's Prophet – Sprout |
| Nature's Prophet – Wrath of Nature |
| Venomancer – Noxious Plague |
| Venomancer – Snakebite |
| Venomancer – Venomous Gale |
| Storm Spirit – Ball Lightning |
| Storm Spirit – Static Remnant |
| Puck – Illusory Orb |
| Puck – Waning Rift |
| Beastmaster – Drums of Slom |
| Beastmaster – Primal Roar |
| Beastmaster – Wild Axes |
| Sand King – Burrowstrike |
| Sand King – Caustic Finale |
| Sand King – Epicenter |
| Sand King – Sand Storm |
| Night Stalker – Crippling Fear |
| Night Stalker – Void |
| Necrophos – Death Pulse |
| Necrophos – Death Seeker |
| Necrophos – Reaper's Scythe |
| Tinker – Heat-Seeking Missile |
| Broodmother – Silken Bola (7.29 - 7.35d) |
| Batrider – Flamebreak (Pre 6.74) |
| Silencer – Glaives of Wisdom (6.15-7.35d) |
| Bristleback – Quill Spray (Pre 6.33) |
| Abaddon – Curse of Avernus (7.20 - 7.35d) |
| Ringmaster – Escape Act |
| Ringmaster – Impalement Arts |
| Ringmaster – Tame the Beasts |
| Ringmaster – Wheel of Wonder |
| Abaddon – Borrowed Time |
| Abaddon – Curse of Avernus |
| Dragon Knight – Breathe Fire |
| Dragon Knight – Dragon Tail |
| Dragon Knight – Fireball |
| Luna – Eclipse |
| Luna – Lucent Beam |
| Pudge – Dismember |
| Pudge – Rot |
| Undying – Decay |
| Undying – Soul Rip |
| Lycan – Shapeshift |
| Earth Spirit – Boulder Smash |
| Earth Spirit – Enchant Remnant |
| Earth Spirit – Geomagnetic Grip |
| Earth Spirit – Magnetize |
| Earth Spirit – Rolling Boulder |
| Queen of Pain – Blink |
| Queen of Pain – Shadow Strike |
| Magnus – Horn Toss |
| Magnus – Reverse Polarity |
| Magnus – Shockwave |
| Magnus – Skewer |
| Visage – Gravekeeper's Cloak |
| Visage – Soul Assumption |
| Visage – Stone Form |
| Elder Titan – Astral Spirit |
| Anti-Mage – Mana Void |
| Marci – Dispose |
| Marci – Rebound |
| Marci – Unleash |
| Ember Spirit – Activate Fire Remnant |
| Ember Spirit – Fire Remnant |
| Ember Spirit – Flame Guard |
| Ember Spirit – Immolation |
| Ember Spirit – Searing Chains |
| Rubick – Fade Bolt |
| Rubick – Telekinesis Land |
| Mars – Arena of Blood |
| Void Spirit – Aether Remnant |
| Void Spirit – Dissimilate |
| Void Spirit – Resonant Pulse |
| Arc Warden – Flux |
| Arc Warden – Spark Wraith |
| Warlock – Chaotic Offering |
| Warlock – Shadow Word |
| Warlock – Upheaval |
| Medusa – Cold Blooded |
| Medusa – Mystic Snake |
| Shadow Demon – Demonic Purge |
| Shadow Demon – Shadow Poison |
| Winter Wyvern – Arctic Burn |
| Winter Wyvern – Splinter Blast |
| Meepo – MegaMeepo Fling |
| Meepo – Poof |
| Enigma – Malefice |
| Enigma – Midnight Pulse |
| Shadow Shaman – Ether Shock |
| Shadow Shaman – Shackles |
| Witch Doctor – Maledict |
| Witch Doctor – Paralyzing Cask |
| Faceless Void – Time Dilation |
| Faceless Void – Time Walk |
| Batrider – Firefly |
| Batrider – Flamebreak |
| Batrider – Flaming Lasso |
| Batrider – Sticky Napalm |
| Monkey King – Primal Spring |
| Silencer – Arcane Curse |
| Silencer – Glaives of Wisdom |
| Silencer – Last Word |
| Wraith King – Wraithfire Blast |
| Bounty Hunter – Shuriken Toss |
| Grimstroke – Ink Swell |
| Grimstroke – Phantom's Embrace |
| Grimstroke – Stroke of Fate |
| Skywrath Mage – Arcane Bolt |
| Skywrath Mage – Concussive Shot |
| Skywrath Mage – Mystic Flare |
| Muerta – Dead Shot |
| Muerta – The Calling |
| Brewmaster – Thunder Clap |
| Naga Siren – Rip Tide |
| Zeus – Arc Lightning |
| Zeus – Heavenly Jump |
| Zeus – Lightning Bolt |
| Zeus – Lightning Hands |
| Zeus – Nimbus |
| Zeus – Static Field |
| Zeus – Thundergod's Wrath |
| Gyrocopter – Call Down |
| Gyrocopter – Homing Missile |
| Gyrocopter – Rocket Barrage |
| Slark – Dark Pact |
| Nyx Assassin – Impale |
| Nyx Assassin – Mind Flare |
| Hoodwink – Bushwhack |
| Hoodwink – Hunter's Boomerang |
| Hoodwink – Sharpshooter |
| Snapfire – Firesnap Cookie |
| Snapfire – Mortimer Kisses |
| Snapfire – Scatterblast |
| Huskar – Burning Spear |
| Huskar – Inner Fire |
| Huskar – Life Break |
| Ogre Magi – Fire Shield |
| Ogre Magi – Fireblast |
| Ogre Magi – Ignite |
| Ogre Magi – Unrefined Fireblast |
| Sniper – Concussive Grenade |
| Sniper – Shrapnel |
| Invoker – Chaos Meteor |
| Invoker – Cold Snap |
| Invoker – Deafening Blast |
| Invoker – E.M.P. |
| Invoker – Exort |
| Invoker – Ice Wall |
| Invoker – Quas |
| Invoker – Tornado |
| Invoker – Wex |
| Spirit Breaker – Charge of Darkness |
| Spirit Breaker – Greater Bash |
| Spirit Breaker – Nether Strike |
| Broodmother – Spawn Spiderlings |
| Broodmother – Spinner's Snare |
| Oracle – Fortune's End |
| Oracle – Purifying Flames |
| Oracle – Rain of Destiny |
| Techies – Blast Off! |
| Techies – Minefield Sign |
| Techies – Proximity Mines |
| Techies – Reactive Tazer |
| Techies – Sticky Bomb |
| Centaur Warrunner – Double Edge |
| Centaur Warrunner – Hitch A Ride |
| Centaur Warrunner – Hoof Stomp |
| Centaur Warrunner – Stampede |
| Centaur Warrunner – Work Horse |
| Outworld Destroyer – Astral Imprisonment |
| Outworld Destroyer – Sanity's Eclipse |
| Chaos Knight – Chaos Bolt |
| Templar Assassin – Psionic Projection |
| Templar Assassin – Trap |
| Io – Spirits |
| Jakiro – Dual Breath |
| Jakiro – Ice Path |
| Jakiro – Liquid Fire |
| Jakiro – Liquid Frost |
| Crystal Maiden – Crystal Clone |
| Crystal Maiden – Crystal Nova |
| Crystal Maiden – Freezing Field |
| Crystal Maiden – Frostbite |
| Crystal Maiden – Stop Freezing Field |
| Phantom Lancer – Spirit Lance |
| Timbersaw – Flamethrower |
| Timbersaw – Reactive Armor |
| Juggernaut – Blade Fury |
| Phoenix – Dying Light |
| Phoenix – Icarus Dive |
| Phoenix – Launch Fire Spirit |
| Phoenix – Sun Ray |
| Dark Seer – Ion Shell |
| Dark Seer – Normal Punch |
| Dark Seer – Surge |
| Dark Seer – Vacuum |
| Dark Seer – Wall of Replica |
| Tinker – March of the Machines |
| Tinker – Warp Flare |
| Keeper of the Light – Blinding Light |
| Keeper of the Light – Illuminate |
| Keeper of the Light – Will-O-Wisp |
| Dark Willow – Bedlam |
| Dark Willow – Bramble Maze |
| Dark Willow – Cursed Crown |
| Dark Willow – Shadow Realm |
| Dark Willow – Terrorize |
| Treant Protector – Eyes In The Forest |
| Treant Protector – Leech Seed |
| Treant Protector – Nature's Grasp |
| Treant Protector – Overgrowth |
| Primal Beast – Pulverize |
| Primal Beast – Trample |
| Primal Beast – Uproar |
| Dawnbreaker – Celestial Hammer |
| Dawnbreaker – Solar Guardian |
| Kunkka – Ghostship |
| Kunkka – Tidal Wave |
| Troll Warlord – Whirling Axes (Melee) |
| Troll Warlord – Whirling Axes (Ranged) |
| Legion Commander – Overwhelming Odds |
| Disruptor – Static Storm |
| Disruptor – Thunder Strike |
| Tusk – Ice Shards |
| Tusk – Snowball |
| Tusk – Walrus Kick |
| Underlord – Fiend's Gate |
| Underlord – Firestorm |
| Underlord – Pit of Malice |
| Lone Druid – Entangle |
| Lycan Lane Wolf – Cripple |
| Warpine Raider – Seed Shot |
| Storm – Cyclone |
| Storm – Dispel Magic |
| Cloak of Flames – Immolate |
| Ethereal Blade – Ether Blast |
| Maelstrom – Chain Lightning |
| Eul's Scepter of Divinity – Cyclone |
| Khanda – Empower Spell |
| Blood Grenade – Throw Grenade |
| Parasma – Witch Blade |
| Dust of Appearance – Reveal |
| Bloodthorn – Soul Rend |
| Phylactery – Empower Spell |
| Radiance – Burn |
| Meteor Hammer – Meteor Hammer |
| Orchid Malevolence – Soul Burn |
| Urn of Shadows – Soul Release |
| Wind Waker – Cyclone |
| Mjollnir – Chain Lightning |
| Mjollnir – Static Charge |
| Witch Blade – Witch Blade |
| Shiva's Guard – Arctic Blast |
| Spirit Vessel – Soul Release |
| Stormcrafter – Bottled Lightning |
| Slime Vial – Spill |
| Tormentor – The Shining |
| Ancient Ice Shaman – Icefire Bomb |
| Kez – Shodo Sai |
| Mercy & Grace – Dead Shot |
| Boglet – Arm of the Deep |
| Croaker – Tendrils of the Deep |
| Ancient Croaker – Congregations of the Deep |
| Crippling Crossbow – Hobble |
| Orb of Corrosion – Corrosion (Pre 7.38) |
| Demonic Warrior (Underlord) – Last Will |
| Demonic Warrior (Book of the Dead) – Last Will |
| Largo – Croak of Genius |
| Largo – Frogstomp |
| Spirit Bear (Pre 7.40) – Entangling Claws |
| Spirit Bear (Pre 7.40) – Fetch |
| Essence Distiller – Soul Release |
| Hydra's Breath – Miasma |
| Fire – Permanent Immolation |
| Tempest Double – Flux |
| Tempest Double – Spark Wraith |
| Harpy Stormcrafter – Chain Lightning |
| Centaur Conqueror – War Stomp |
| Satyr Mindstealer – Mana Burn |
| Mud Golem – Hurl Boulder |
| Satyr Tormenter – Shockwave |
| Hellbear Smasher – Thunder Clap |
| Ancient Black Dragon – Fireball |
| Ancient Thunderhide – Slam |
| Shard Golem – Hurl Boulder |
| Roshan – On The Move |
| Roshan – Roar of Retribution |
| Roshan – Slam |
| Raptor – Dive Bomb |
| Spirit Bear – Entangling Claws |
| Spirit Bear – Fetch |
| Psionic Trap – Trap |
| Familiar – Gravekeeper's Cloak |
| Familiar – Stone Form |
| Lycan Wolf – Cripple [corpus:liquipedia_dota2/damage_types@2346392#Magical] |

## Pure Damage

Pure damage interacts with neither Armor nor Magic Resistance. It is not amplified by magical-damage-amplification abilities and fully ignores Armor and Damage Block. It does not affect invulnerable units.

Some sources, including Dispersion, can manipulate Pure Damage through the mechanic called damage reduction. Pure damage affects units with Spell Immunity because spell immunity does not block damage, but an ability dealing pure damage is not necessarily able to target spell-immune units. Laser, for example, deals pure damage but cannot be cast on units with spell immunity.

| Abilities Dealing Pure Damage |
|---|
| Warlock Golem – Flaming Fists |
| Axe – Counter Helix |
| Bloodseeker – Rupture |
| Spectre – Desolate |
| Leshrac – Diabolic Edict |
| Enchantress – Impetus |
| Bane – Brain Sap |
| Bane – Enfeeble |
| Bane – Fiend's Grip |
| Meepo – Ransack |
| Enigma – Black Hole |
| Nyx Assassin – Vendetta |
| Invoker – Sun Strike |
| Omniknight – Hammer of Purity |
| Omniknight – Purification |
| Outworld Destroyer – Arcane Orb |
| Templar Assassin – Psi Blades |
| Timbersaw – Timber Chain |
| Timbersaw – Whirling Death |
| Tinker – Laser |
| Kez – Raptor Dance |
| Roshan – Throw |

¹ Mist Coil deals pure damage to the caster but magical damage to the target.

² Requires a talent.

³ Requires Aghanim's Scepter.

⁴ Requires Aghanim's Shard. [corpus:liquipedia_dota2/damage_types@2346392#Pure]

## Damage Flags

Abilities of any damage type can have flags that change their behavior in certain situations. Examples are HP Removal, No-reflection, No-Spell-Lifesteal, and No-Spell-Amplification. [corpus:liquipedia_dota2/damage_types@2346392#Flags]

### HP Removal

HP Removal is driven by the `DOTA_DAMAGE_FLAG_HPLOSS` damage flag. Abilities with this flag ignore and do not trigger any on-damage effects, so they cannot interrupt Blink Dagger or cancel consumables such as Clarity. Their damage cannot be amplified or negated by most generic damage manipulation and damage negation. In some cases it also ignores invulnerability. Damage ignored in this way remains registered and may count for statistical purposes.

HP Removal does not generate spell lifesteal because it does not yield a damage instance. Its damage values remain subject to normal damage classification: for example, magical HP Removal damage can still be affected by magic resistance and magical damage barriers.

| Abilities Using the HP Removal Flag |
|---|
| Abaddon – Aphotic Shield¹ |
| Bloodseeker – Bloodrage² |
| Bloodseeker – Blood Mist² |
| Necrophos – Heartstopper Aura |
| Oracle – False Promise³ |
| Orb of Venom – Poison Attack |
| Orb of Corrosion – Corrosion |
| Spectre – Dispersion |
| Venomancer – Poison Sting |
| Vhoul Assassin – Envenomed Weapon |

¹ Applies only to the Aghanim's Shard component of the spell.

² Maximum health paid as a cost per second is HP Removal to the caster.

³ This ability delays damage; the delayed damage is Pure and has the HP Removal flag. [corpus:liquipedia_dota2/damage_types@2346392#HP_Removal]

#### Setting Health

A unit’s health can be altered directly by setting it to particular values instead of healing or damaging it. This is registered as neither healing nor damage and is ignored by anything that reacts to healing or damage. It can never be lethal or set health beyond the unit’s max health. When the relevant abilities are cast with less health than their health cost, the caster’s health falls to 1HP.

Setting Health is not HP Removal. HP Removal remains damage, is flagged to bypass several but not all on-damage effects, and can be lethal. [corpus:liquipedia_dota2/damage_types@2346392#Setting_Health]

#### On-Damage Effects

Besides all damage-manipulation sources and spell lifesteal, the following abilities do not react to HP Removal damage:

| Abilities Unaffected by HP Removal Damage |
|---|
| Aegis of the Immortal – Expire Restore |
| Bane – Nightmare |
| Batrider – Sticky Napalm |
| Blade Mail – Damage Return |
| Blink Dagger – Blink |
| Bloodthorn – Soul Rend |
| Bottle – Regenerate |
| Bristleback – Bristleback |
| Clarity – Replenish |
| Elder Titan – Echo Stomp |
| Healing Salve – Salve |
| Invoker – Cold Snap |
| Invoker – Ghost Walk |
| Lifestealer – Open Wounds |
| Mjollnir – Static Charge |
| Monkey King – Tree Dance |
| Monkey King – Mischief |
| Nyx Assassin – Spiked Carapace |
| Orchid Malevolence – Soul Burn |
| Runes – Regeneration |
| Spirit Bear – Return |
| Tidehunter – Kraken Shell |
| Urn of Shadows – Soul Release |
| Viper – Corrosive Skin |
| Visage – Soul Assumption |
| Visage – Gravekeeper's Cloak |
| Warlock – Fatal Bonds [corpus:liquipedia_dota2/damage_types@2346392#On-Damage_Effects] |

### No-reflection

No-reflection is driven by the `DOTA_DAMAGE_FLAG_REFLECTION` damage flag. On-damage events from certain abilities do not interact with damage from abilities carrying this flag. This prevents infinite damage loops between two opposing heroes with Blade Mails.

| Damage Sources with No-reflection Flag |
|---|
| Arcanist's Armor – Mega Shield¹ |
| Blade Mail – Damage Return¹ |
| Nyx Assassin – Spiked Carapace¹ |
| Spectre – Dispersion² ³ |
| Viper – Corrosive Skin² |
| Warlock – Fatal Bonds¹ |

¹ Triggers on-damage effects from all abilities except those in the following list.

² Does not trigger on-damage effects.

³ Flagged as HP Removal.

| Abilities That Do Not React to the No-reflection Flag |
|---|
| Arcanist's Armor – Mega Shield |
| Batrider – Sticky Napalm |
| Blade Mail – Damage Return |
| Bristleback – Bristleback |
| Nyx Assassin – Spiked Carapace |
| Spectre – Dispersion |
| Viper – Corrosive Skin |
| Warlock – Fatal Bonds [corpus:liquipedia_dota2/damage_types@2346392#No-reflection] |

### No-Spell-Lifesteal

No-Spell-Lifesteal is driven by the `DOTA_DAMAGE_FLAG_NO_SPELL_LIFESTEAL` damage flag. Abilities with this flag cannot provide spell lifesteal even though their damage is categorized as spell damage. All HP Removal damage also generates no spell lifesteal because HP Removal does not yield a damage instance.

| Abilities Not Affected by Spell Lifesteal |
|---|
| Arcanist's Armor – Mega Shield |
| Battle Fury – Cleave |
| Blade Mail – Damage Return |
| Chipped Vest – Chipper |
| Kunkka – Tidebringer |
| Luna – Moon Glaives |
| Magnus – Empower |
| Nyx Assassin – Spiked Carapace |
| Silencer – Glaives of Wisdom¹ |
| Storm Spirit – Overload² |
| Sven – Great Cleave |
| Templar Assassin – Psi Blades |
| Tiny – Tree Grab |
| Tiny – Tree Throw |
| Witch Doctor – Death Ward³ |
| Witch Doctor – Voodoo Switcheroo³ |

¹ The bouncing attacks’ damage cannot provide spell lifesteal. The `-based` damage can provide spell lifesteal, including that of the bounces.

² The bouncing attacks’ damage cannot provide spell lifesteal. Overload’s area damage can provide spell lifesteal, including that of the bounces.

³ The bouncing attacks’ damage counts as spell damage but cannot provide spell lifesteal. [corpus:liquipedia_dota2/damage_types@2346392#No-Spell-Lifesteal]

### No-Spell-Amplification

No-Spell-Amplification is driven by the `DOTA_DAMAGE_FLAG_NO_SPELL_AMPLIFICATION` damage flag. Abilities with this flag ignore Outgoing Spell Damage Manipulation. Only spell amplification is ignored; other spell-damage manipulation remains effective.

| Abilities Not Affected by Spell Damage Amplifications |
|---|
| Arcanist's Armor – Mega Shield |
| Battle Fury – Cleave |
| Blade Mail – Damage Return |
| Chipped Vest – Chipper |
| Kunkka – Tidebringer |
| Lion – Finger of Death |
| Luna – Moon Glaives |
| Magnus – Empower |
| Necrophos – Heartstopper Aura |
| Nyx Assassin – Spiked Carapace |
| Silencer – Glaives of Wisdom¹ |
| Storm Spirit – Overload² |
| Sven – Great Cleave |
| Templar Assassin – Psi Blades |
| Tiny – Tree Grab |
| Tiny – Tree Throw |
| Witch Doctor – Death Ward³ |
| Witch Doctor – Voodoo Switcheroo³ |

¹ The bouncing attacks’ damage is unaffected by spell-damage amplification. The `-based` damage is fully affected, including that of the bounces.

² The bouncing attacks’ damage is unaffected by spell-damage amplification. Overload’s area damage is fully affected, including that of the bounces.

³ The bouncing attacks’ damage counts as spell damage but is unaffected by spell-damage amplification. [corpus:liquipedia_dota2/damage_types@2346392#No-Spell-Amplification]

### No-lethality

No-lethality is driven by the `DOTA_DAMAGE_FLAG_NON_LETHAL` damage flag. Damage with this flag is not lethal. Most such damage is applied only to allies.

| Damage Sources with No-lethality Flag |
|---|
| Abaddon – Mist Coil¹ |
| Bloodseeker – Bloodrage |
| Bloodseeker – Blood Mist¹ |
| Centaur Warrunner – Double Edge¹ |
| Huskar – Life Break¹ |
| Oracle – Purifying Flames² |
| Pudge – Rot¹ |
| Slark – Dark Pact¹ |
| Techies – Blast Off!¹ |
| Vhoul Assassin – Envenomed Weapon |

¹ Damage to the caster has the No-lethality flag.

² Damage to allies has the No-lethality flag. [corpus:liquipedia_dota2/damage_types@2346392#No-lethality]

### No-manipulation

No-manipulation is driven by the `DOTA_DAMAGE_FLAG_NO_DAMAGE_MULTIPLIERS` damage flag. Damage with this flag ignores all outgoing and incoming Damage manipulation. Spell-damage amplification is a form of damage manipulation and is therefore also ignored. Some damage block and damage barriers remain effective.

| Damage Sources with No-manipulation Flag |
|---|
| Bloodseeker – Bloodrage¹ |
| Bloodseeker – Blood Mist¹ |
| Necrophos – Heartstopper Aura |
| Oracle – False Promise² |
| Techies – Blast Off!³ |
| Tinker – Laser⁴ |
| Ringmaster – Spotlight⁵ |
| Wraith King – Spectral Blade⁶ |

¹ Maximum health paid as a cost per second has the No-manipulation flag.

² This ability delays damage; the delayed damage has the No-manipulation flag.

³ Current health paid as a cost per second has the No-manipulation flag.

⁴ Damage based on max HP has the No-manipulation flag.

⁵ Damage to illusions has the No-manipulation flag.

⁶ Pure damage when the debuff ends has the No-manipulation flag. [corpus:liquipedia_dota2/damage_types@2346392#No-manipulation]

## Instant Kill

Instant Kill kills units without using damage. Like HP Removal, it ignores almost all damage manipulation and can be prevented by only a few abilities.

A prominent use is killing expiring summoned units and illusions when their set duration ends. Summons and illusions replaced on cast are also killed this way. Minimum health from damage manipulation does not prevent Instant Kill. Abilities that prevent or bypass Instant Kill generally use hard-coded special interactions.

| Instant Kill Source | Effect |
|---|---|
| Ancient Apparition – Ice Blast | Instantly kills debuffed enemy heroes who drop below the threshold. |
| Axe – Culling Blade | Instantly kills the target if its current health is below the threshold. |
| Brewmaster – Primal Split | Instantly kills the caster if all brewlings die. |
| Lone Druid – Summon Spirit Bear | Instantly kills the Spirit Bear when the ability levels up, replacing it with a higher-level bear. Instantly kills the Spirit Bear if the caster dies; acquiring Aghanim's Scepter removes this restriction. |
| Meepo – Divided We Stand | Instantly kills all other Meepoes when one Meepo dies. |
| Phoenix – Supernova | Instantly kills the caster and targeted ally if the Phoenix Sun is destroyed. [corpus:liquipedia_dota2/damage_types@2346392#Instant_Kill] |

### Illusions

The following abilities instantly destroy illusions when used on them unless they are strong illusions:

| Instant-Killing Illusion Abilities |
|---|
| Dagon – Energy Burst |
| Dazzle – Poison Touch⁵ |
| Disruptor – Glimpse |
| Lion – Hex |
| Pudge – Meat Hook |
| Scythe of Vyse – Hex |
| Shadow Shaman – Hex |
| Skywrath Mage – Mystic Flare |

¹ Instantly kills the target upon landing if it is not a hero or clone.

² Requires a talent.

³ Requires Aghanim's Scepter.

⁴ Requires Aghanim's Shard.

⁵ Only hexes when cast from Nothl Projection. [corpus:liquipedia_dota2/damage_types@2346392#Illusions]

### Creeps

| Instant-Killing Creep Abilities |
|---|
| Axe – Culling Blade⁵ |
| Chen – Holy Persuasion¹ |
| Clinkz – Death Pact |
| Dagon – Energy Burst |
| Doom – Devour |
| Enchantress – Enchant¹ |
| Hand of Midas – Transmute |
| Helm of the Dominator – Dominate¹ |
| Helm of the Overlord – Dominate¹ |
| Lifestealer – Consume |
| Mirana – Sacred Arrow |
| Night Stalker – Hunter in the Night²b |
| Pudge – Meat Hook |
| Snapfire – Spit Out⁶ |

¹ Instantly kills the oldest captured unit if the maximum number of units is exceeded.

² Requires a talent.

³ Requires Aghanim's Scepter.

⁴ Requires Aghanim's Shard.

⁵ Instantly kills the target if its current health is below the threshold.

⁶ Instantly kills the launched unit upon landing if it is not a hero or clone. [corpus:liquipedia_dota2/damage_types@2346392#Creeps]

### Forced Kill

The following abilities use Instant Kill to forcefully remove or kill their units when particular conditions are met:

| Forced Instant Kill Effect | Effect |
|---|---|
| Lone Druid – Summon Spirit Bear | Instantly kills the Spirit Bear upon Lone Druid’s death. Aghanim's Scepter removes this restriction. |
| Meepo – Divided We Stand | If any Meepo Clone dies, they all die. |
| Minor Imp – Eldritch Explosion | Instantly kills the Minor Imp when it reaches its target. |
| Undying – Tombstone | Instantly kills all Undying Zombies when the Tombstone is destroyed or expires. [corpus:liquipedia_dota2/damage_types@2346392#Forced_Kill] |

## Damage Manipulation

Damage manipulation alters damage values by either increasing or reducing them. [corpus:liquipedia_dota2/damage_types@2346392#Damage_Manipulation]

## Removed Damage Types

The following damage types were removed in version 6.82. [corpus:liquipedia_dota2/damage_types@2346392#Trivia]

### Composite

Composite damage, also called mixed damage, was reduced by both armor and magic resistance. It pierced spell immunity and did not affect ethereal units.

| Previous Composite-Damage Source |
|---|
| Acid Spray |
| Wild Axes |
| Diabolic Edict |
| Summon Spirit Bear's backlash damage |
| Land Mines |
| Suicide Squad, Attack! |

All were changed to physical damage except the Spirit Bear’s backlash damage, which was changed to pure damage. [corpus:liquipedia_dota2/damage_types@2346392#Composite]

### Universal

Universal damage pierced spell immunity and was affected by magic resistance.

| Previous Universal-Damage Source |
|---|
| Pulverize |
| Doom |
| Echo Slam's initial damage |
| Midnight Pulse |
| Laguna Blade |
| March of the Machines |
| Flaming Fists |

Doom, Midnight Pulse, Flaming Fists, and Laguna Blade were changed to pure damage, allowing them to continue piercing spell immunity. Pulverize, Echo Slam’s initial damage, and March of the Machines were changed to magical damage and therefore no longer pierced spell immunity. [corpus:liquipedia_dota2/damage_types@2346392#Universal]