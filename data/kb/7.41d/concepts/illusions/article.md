---
title: Illusions
kind: concept
patch: 7.41d
card:
  entity: illusions
  sentences:
  - text: Illusions are imperfect copies of heroes created by abilities or items;
      they copy a hero’s level, attributes, attack and defense values, abilities,
      and items, cannot cast active abilities or use active items, and deal 40% damage
      to buildings.
    marks:
    - corpus:liquipedia_dota2/illusions@2376496
    - corpus:liquipedia_dota2/illusions@2376496#Stats
  - text: An illusion’s stats, level, ability levels, and items are fixed at creation
      and do not adapt to the original hero.
    marks:
    - corpus:liquipedia_dota2/illusions@2376496#Stats
  - text: Every illusion is invulnerable for 0.1 seconds after spawning.
    marks:
    - corpus:liquipedia_dota2/illusions@2376496
  - text: Allies identify illusions by an additional model and portrait texture, a
      creep health bar, and a duration indicator.
    marks:
    - corpus:liquipedia_dota2/illusions@2376496#Visual_Appearance
  - text: A camouflaged illusion appears identical to the copied hero for enemies,
      while allies still see it as an illusion.
    marks:
    - corpus:liquipedia_dota2/illusions@2376496#Visual_Appearance
  - text: All illusions have fixed base day/night vision of 800/400.
    marks:
    - corpus:liquipedia_dota2/illusions@2376496#Stats
  - text: An illusion’s gold and experience bounty each equal two times its level.
    marks:
    - corpus:liquipedia_dota2/illusions@2376496#Bounty
  - text: Spirit Lance, Doppelganger, Juxtapose, and Wall of Replica illusions instead
      grant fixed gold and experience bounties of 5 and 5.
    marks:
    - corpus:liquipedia_dota2/illusions@2376496#Bounty
  - text: Strong illusions behave like regular illusions but resist abilities that
      would instantly destroy ordinary illusions.
    marks:
    - corpus:liquipedia_dota2/illusions@2376496#Strong_Illusions
  - text: Dagon, Poison Touch, Glimpse, Lion’s Hex, Meat Hook, Scythe of Vyse, Shadow
      Shaman’s Hex, and Mystic Flare instantly destroy non-strong illusions.
    marks:
    - corpus:liquipedia_dota2/illusions@2376496#Instant_Kill
  - text: Illusions deal 75% less damage to buildings under Backdoor Protection and
      60% less damage to unprotected buildings.
    marks:
    - corpus:liquipedia_dota2/illusions@2376496#Other_Interactions
  - text: Certain abilities make nearby owned illusions perform nonfunctional fake
      casts alongside the real hero to preserve camouflage.
    marks:
    - corpus:liquipedia_dota2/illusions@2376496#Casting_Fake_Abilities
---

# Illusions

## Overview

Illusions are imperfect, weaker copies of heroes created by abilities or items. They look like heroes and are mostly treated as heroes, but usually deal reduced outgoing damage and take increased incoming damage. They cannot cast abilities or use active item abilities; some passive abilities are also disabled. They cannot drop or pick up items or runes. They yield a small amount of gold and experience based on the copied hero’s level, but do not soak up gold or experience. They cannot level up, gold from their last hits goes to their owners, and their deaths do not interfere with kill streaks or counters.

An illusion may be created from its owner, an allied hero, or an enemy hero. It copies the hero’s appearance, level, attributes, attack values, defensive values such as base armor and base magic resistance, and abilities at their current levels. It also copies all owned items and their stats, although some item and ability effects are disabled.

All illusions deal 60% less damage against buildings. This stacks multiplicatively with their outgoing-damage reductions and with the reduction hero damage suffers against the structure armor type. Because illusions are based on heroes, their damage scales together with the heroes and can remain significant for pushing, especially later in a match.

Every illusion is invulnerable for 0.1 seconds upon spawning, regardless of its creation source. Illusions use the same allied-only spawn sound and the same death sound when killed or expired. [corpus:liquipedia_dota2/illusions@2376496]

## Visual Appearance

Allied illusions are always distinguishable through an additional texture layer on their model and unit portrait and through a creep health bar. They also display a duration indicator to the left of the health bar.

Whether enemies can distinguish an illusion depends on its source. Some enemy-visible illusions retain the additional texture and creep health bar but lack the duration indicator; others are camouflaged. A camouflaged illusion looks identical to its copied hero to enemies: it lacks the illusion texture and uses the regular hero health bar, including the hero icon, player name, mana bar, and extra icons such as Battle Pass badges. Allies still see it normally as an illusion.

There are 7 different illusion textures. The appearance and ability entries are:

| Appearance or ability entry |
|---|
| Default |
| Fiend's Grip²ᵃ |
| Phantasm |
| Chaos Bolt²ᵇ |
| Decoy²ᵃ |
| Illusionist's Cape |
| Manta Style |
| Illusion Rune |
| Mirror Image |
| Disruption |
| Shadow Step |
| Haunt |
| Blink Fragment (Old) |
| Wall of Replica |
| Vengeance Aura²ᵃ ⁴ |
| Reflection |
| Conjure Image |
| Doppelganger |
| Spirit Lance |
| Doppelganger |
| Juxtapose |
| Dark Portrait²ᵃ |
| Normal Punch²ᵃ |
| Camouflaged |
| - |

The displayed camouflage indicators are:

| Indicator |
|---|
| Yes |
| No |
| No |
| Yes |
| Yes |
| No |
| No |

²ᵃ Requires Aghanim's Scepter. ²ᵇ Requires Aghanim's Shard. ⁴ The Vengeance Illusion always uses the hero health bar for both enemies and allies, but is otherwise distinguishable. [corpus:liquipedia_dota2/illusions@2376496#Visual_Appearance]

## Illusion-Creating Abilities

Collision size affects illusion-creating sources. Two heroes or units cannot occupy the same coordinates without phased movement and are pushed 58-distance apart upon losing phased movement, regardless of their collision sizes. Phantom Lancer and Chaos Knight have collision sizes of 18 and 27 respectively.

| Caster collision size | Target collision size or condition | Pushed distance |
|---|---|---:|
| (18) | (27) | 58 |
| (27) | (18) | 58 |
| Both caster and target have the same collision size | Both caster and target have the same collision size | 58 |
| Target differs from the caster and is larger | `TargetCollision > CasterCollision [?]` | 87 |

When Chaos Knight casts Chaos Bolt on an enemy Marci and Siege Creep, the Siege Creep has 40 collision size. Because Chaos Knight and Marci have the same collision size, the Phantasm illusion spawns 58-distance away when Marci lacks phased movement. For the Siege Creep, it instead spawns 87-distance away. [corpus:liquipedia_dota2/illusions@2376496#Illusion_Creating_Abilities]

### Sources

| Illusion-creating source |
|---|
| Anti-Mage – Counterspell²ᵇ |
| Anti-Mage – Counterspell Ally²ᵇ |
| Bane – Fiend's Grip²ᵃ |
| Dark Seer – Normal Punch |
| Dark Seer – Wall of Replica |
| Hoodwink – Decoy |
| Manta Style – Mirror Image |
| Naga Siren – Mirror Image |
| Phantom Lancer – Spirit Lance |
| Phantom Lancer – Doppelganger |
| Phantom Lancer – Juxtapose |
| Ringmaster – Funhouse Mirror |
| Shadow Demon – Disruption |
| Spectre – Shadow Step |
| Spectre – Haunt |
| Terrorblade – Reflection |
| Terrorblade – Conjure Image |
| Runes – Illusion |

¹ Requires talent. ²ᵃ Requires Aghanim's Scepter. ²ᵇ Requires Aghanim's Shard. [corpus:liquipedia_dota2/illusions@2376496#Sources]

### Strong Illusions

Strong illusions behave like regular illusions but cannot be instantly killed by the abilities listed under instant-kill interactions.

| Strong-illusion source |
|---|
| Grimstroke – Dark Portrait |
| Morphling – Morph (Alt-Cast)²ᵃ |
| Vengeful Spirit – Vengeance Aura²ᵃ |

²ᵃ Requires Aghanim's Scepter. [corpus:liquipedia_dota2/illusions@2376496#Strong_Illusions]

## Stats

**Illusions** is a passive ability affecting self. An illusion’s stats, level, ability levels, and items are set when it is created and do not adapt to the original hero.

| Property | Value |
|---|---:|
| Against Reinforced | 0.4 |
| Bonus Attack Damage Negation | 100% |
| Bonus Armor Negation | 100% |
| Bonus Magic Resistance Negation | 100% |

Illusions copy these traits from the original hero:

| Copied trait |
|---|
| All attributes, Attribute Gain per Level, and the hero's Primary Attribute |
| Health, Mana and their regeneration values |
| Base Attack Damage, Attack Range, Attack Speed, Attack Animation, and Projectile Speed |
| Base Armor |
| Damage Block |
| Base Magic Resistance, Status Resistance, and Slow Resistance |
| Spell Damage Amplification |
| Turn Rate |
| Unit Size |
| Evasion |
| Talents, items, and passive abilities providing the bonuses above |

All illusions have fixed base day/night vision of 800/400; vision bonuses otherwise work normally. Only Total Attack Damage manipulation sources fully affect an illusion’s main attack damage. Illusions deal 40% damage to buildings after all total attack damage manipulation sources, and this innate value stacks multiplicatively with Attack Classes. Against Roshan, they deal 99.6% total damage because of Strength of the Immortal. Abilities cast by illusions deal full spell damage.

The incoming- and outgoing-damage multipliers supplied by the creating ability are handled by the Damage Manipulation modifier.

| Hidden modifier |
|---|
| `modifier_property_bonusdamageoutgoing_percentage` |
| `modifier_property_damageoutgoing_percentage_illusion_amplify` |

[corpus:liquipedia_dota2/illusions@2376496#Stats]

### Magic Resistance Bonuses

Magic-resistance sources vary in whether they work with illusions. Magic-resistance-increasing abilities do not affect illusions except Fate's Edict and magic-resistance-increasing talents. The HUD nevertheless always displays magic resistance as though the illusion were fully affected.

| Magic-resistance source affecting illusions |
|---|
| Elder Titan – Natural Order |
| Astral Spirit – Natural Order |
| Ethereal Blade – Ether Blast |
| Ghost Scepter – Ghost Form |
| Leshrac – Nihilism¹ |
| Necrophos – Ghost Shroud |
| Pugna – Decrepify |

| Magic-resistance source not affecting illusions |
|---|
| Ancient Apparition – Ice Vortex |
| Grove Bow – Magic Amp |
| Keeper of the Light – Solar Bind |
| Nyx Assassin – Vendetta² |
| Skywrath Mage – Ancient Seal |
| Viper – Poison Attack |

¹ Requires Aghanim's Scepter. ² Requires Aghanim's Shard. [corpus:liquipedia_dota2/illusions@2376496#Magic_Resistance_Bonuses]

### Bounty

An illusion’s gold and experience bounty equals two times its level:

`2 * IllusionLVL`

Gold is granted to the player who kills the illusion, while experience is shared within the default experience area. Experience is granted only when a player kills the illusion. Expiration or death to lane creeps, towers, fountains, or neutral creeps grants no experience.

| Level | Gold |
|---:|---:|
| 1 | 2 |
| 2 | 4 |
| 3 | 6 |
| 4 | 8 |
| 5 | 10 |
| 6 | 12 |
| 7 | 14 |
| 8 | 16 |
| 9 | 18 |
| 10 | 20 |
| 11 | 22 |
| 12 | 24 |
| 13 | 26 |
| 14 | 28 |
| 15 | 30 |
| 16 | 32 |
| 17 | 34 |
| 18 | 36 |
| 19 | 38 |
| 20 | 40 |
| 21 | 42 |
| 22 | 44 |
| 23 | 46 |
| 24 | 48 |
| 25 | 50 |
| 26 | 52 |
| 27 | 54 |
| 28 | 56 |
| 29 | 58 |
| 30 | 60 |

The following illusions grant a fixed 5 and 5 regardless of level:

| Fixed-bounty illusion |
|---|
| Spirit Lance |
| Doppelganger |
| Juxtapose, created by Phantom Lancer or his illusions |
| Wall of Replica |

[corpus:liquipedia_dota2/illusions@2376496#Bounty]

### Copying Buffs and Debuffs

Illusions usually do not copy the original hero’s buffs and debuffs. Exceptions include the toggled On/Off states of items and certain abilities.

| Buff copied upon creation |
|---|
| Alchemist – Chemical Rage |
| Armlet of Mordiggian – Unholy Strength² |
| Dragon Knight – Elder Dragon Form |
| Lone Druid – True Form |
| Lycan – Shapeshift |
| Lycan – Wolf Bite¹ |
| Moon Shard – Consume³ |
| Morphling – Attribute Shift |
| Terrorblade – Metamorphosis⁴ |
| Troll Warlord – Berserker's Rage |
| Undying – Flesh Golem |

¹ Wolf Bite requires Aghanim's Scepter. ² Unholy Strength’s buff and effects appear copied, but only the strength is actually copied. ³ Consume’s buff is copied, but not its attack-speed bonus; only its bonus night vision is copied. ⁴ Metamorphosis’s modifier is copied upon creation, but its aura overrides the modifier, causing the form to revert after the illusion is no longer affected by the aura. [corpus:liquipedia_dota2/illusions@2376496#Copying_Buffs_and_Debuffs]

## Attack Modifiers

Attack modifiers apply effects to basic attacks, including healing, damage, and disables. Individual modifiers have their own rules: they may work fully, partially, with reduced values, or not at all for illusions.

| Attack modifier copied and fully functional |
|---|
| Abaddon – Curse of Avernus |
| Brewmaster – Drunken Brawler |
| Chaos Knight – Chaos Strike |
| Crystalys – Critical Strike |
| Daedalus – Critical Strike |
| Dragon Knight – Elder Dragon Form³ |
| Drow Ranger – Marksmanship Split Shot¹ ² |
| Juggernaut – Blade Dance |
| Legion Commander – Moment of Courage |
| Luna – Moon Glaives |
| Lycan – Shapeshift |
| Lycan – Wolf Bite¹ |
| Mask of Madness – Lifesteal |
| Medusa – Split Shot² |
| Monkey King Bar – Pierce⁴ |
| Morbid Mask – Lifesteal |
| Phantom Assassin – Coup de Grace |
| Phantom Lancer – Juxtapose |
| Revenant's Brooch – Phantom Critical |
| Satanic – Lifesteal |
| Sniper – Take Aim |
| Spectre – Desolate |
| Templar Assassin – Psi Blades |
| Troll Warlord – Fervor |
| Venomancer – Poison Sting |
| Vladmir's Offering – Vladmir's Aura |
| Wraith King – Mortal Strike |
| Wraith King – Vampiric Spirit |

¹ Requires Aghanim's Scepter. ² The damage reductions of Marksmanship and Split Shot are the only reductions that affect illusions. ³ All 3 Elder Dragon Form modifiers—Corrosive Breath, Splash Attack, and Frost Breath—work for illusions. ⁴ Only the accuracy works for illusions. [corpus:liquipedia_dota2/illusions@2376496#Attack_Modifiers]

### Mana Break

Mana Break abilities and talents are copied from the original hero, but illusions with Mana Break burn less mana than real heroes.

| Mana Break source |
|---|
| Anti-Mage – Mana Break |
| Diffusal Blade – Manabreak |
| Disperser – Manabreak |

[corpus:liquipedia_dota2/illusions@2376496#Mana_Break]

### Not Copied

| Attack modifier not copied or functional |
|---|
| Abyssal Blade – Bash |
| Battle Fury – Cleave¹ |
| Battle Fury – Quell |
| Bounty Hunter – Jinada |
| Desolator – Corruption¹ |
| Echo Sabre – Echo Strike |
| Eye of Skadi – Cold Attack¹ |
| Faceless Void – Time Lock |
| Gleipnir – Chain Lightning |
| Javelin – Pierce |
| Kunkka – Tidebringer¹ ² |
| Lifestealer – Feast |
| Maelstrom – Chain Lightning |
| Magnus – Empower |
| Meepo – Ransack |
| Monkey King Bar – Pierce |
| Mjollnir – Chain Lightning |
| Monkey King – Jingu Mastery |
| Orb of Blight – Lesser Corruption |
| Orb of Corrosion – Corrosion |
| Orb of Frost – Frost |
| Orb of Venom – Poison Attack |
| Quelling Blade – Quell |
| Riki – Cloak and Dagger Backstab |
| Sand King – Caustic Finale |
| Skull Basher – Bash |
| Slardar – Bash of the Deep |
| Slark – Essence Shift |
| Sniper – Headshot |
| Spirit Breaker – Greater Bash |
| Sven – Great Cleave |
| Tiny – Grow |
| Troll Warlord – Berserker's Rage Root |
| Troll Warlord – Fervor |
| Ursa – Fury Swipes |
| Winter Wyvern – Arctic Burn |
| Weaver – Geminate Attack |

¹ These modifiers’ particle effects and sounds occur, but their effects are not applied. ² Tidebringer is always on Autocast for illusions and procs whenever off cooldown, but none of its effects are applied. [corpus:liquipedia_dota2/illusions@2376496#Not_Copied]

## Active Abilities

Illusions cannot use active abilities or items, but may inherit an ongoing ability cast by the original hero before their creation. A few abilities behave differently when their caster is an illusion.

| Ability | Illusion interaction |
|---|---|
| Abaddon – Borrowed Time | Even when allowed to cast abilities, the illusion does not auto-activate Borrowed Time below 400 health. |
| Batrider – Firefly | The fire trail disappears immediately when the casting illusion dies rather than remaining for its remaining duration. |
| Chen – Holy Persuasion | All persuaded units die instantly when the illusion dies. |
| Doom – Infernal Blade | Illusions cannot use it; attempting to cast it makes the illusion perform a regular attack. |
| Earth Spirit – Enchant Remnant | Illusions cannot cast it. |
| Elder Titan – Astral Spirit | If the illusion dies while Astral Spirit is out, the spirit also dies and does not return. |
| Enchantress – Nature's Attendants | The ability ends immediately when the illusion dies rather than continuing to heal nearby allies. |
| Leshrac – Diabolic Edict | The ability ends immediately when the illusion dies rather than continuing to damage nearby enemies. |
| Leshrac – Lightning Storm | It immediately stops bouncing when the illusion dies. |
| Medusa – Mana Shield | It can be toggled but does not work for illusions. |
| Mirana – Moonlight Shadow | Because the ability does not affect illusions, its casting illusion does not turn invisible. |
| Nyx Assassin – Burrow | Illusions cannot cast it. |
| Ogre Magi – Unrefined Fireblast | Illusions cannot cast it. |
| Phantom Assassin – Stifling Dagger | Only attack modifiers functional for the illusion can proc; a dagger cast by an illusion can never bash. |
| Phoenix – Supernova | If the illusion dies or expires during Supernova, Supernova continues to damage enemies and stun them at the end. |
| Rubick – Fade Bolt | It immediately stops bouncing when the illusion dies. |
| Sand King – Epicenter | It ends immediately when the illusion dies rather than continuing to release pulses. |
| Spirit Breaker – Charge of Darkness | Despite Greater Bash not working for illusions, Charge of Darkness still applies the bash radius. |
| Spirit Breaker – Nether Strike | Despite Greater Bash not working for illusions, Nether Strike still applies the bash radius. |
| Timbersaw – Chakram | Illusions cannot cast the blue Chakram. |
| Treant Protector – Eyes In The Forest | Illusions cannot cast it. |
| Tusk – Walrus Kick | Illusions cannot cast it. |
| Visage – Soul Assumption | Illusions do not display the charge meter above them. |
| Zeus – Arc Lightning | It immediately stops bouncing when the illusion dies. |

[corpus:liquipedia_dota2/illusions@2376496#Active_Abilities]

### Casting Fake Abilities

Under certain conditions, abilities cause all illusions owned by the illusion creator and within a certain range of the target to fake-cast while the real hero casts. This helps camouflage the real hero, but the illusions still do not use active abilities.

The illusions play the entire cast animation and fake-cast at the same time as the real ability. Idle illusions turn toward the target before casting. If the cast is canceled with `S`, they complete the cast animation but do not release the fake ability. Moving or attacking illusions continue their orders without turning, although the cast animation overrides their movement or attack animation. They complete the animation and release the fake ability when the real ability is released. Fake abilities interact with nothing.

| Ability fake-cast by illusions |
|---|
| Chaos Knight – Chaos Bolt |
| Naga Siren – Ensnare |
| Naga Siren – Rip Tide |
| Phantom Lancer – Spirit Lance |

[corpus:liquipedia_dota2/illusions@2376496#Casting_Fake_Abilities]

## Passive Abilities

### Fully Functional

| Category | Functional passive |
|---|---|
| Ability | Axe – Counter Helix |
| Ability | Disruptor – Electromagnetic Repulsion |
| Ability | Enchantress – Untouchable |
| Ability | Kez – Kazurai Katana |
| Ability | Medusa – Split Shot |
| Ability | Muerta – Supernatural¹ |
| Ability | Naga Siren – Rip Tide |
| Ability | Naga Siren – Eelskin |
| Ability | Night Stalker – Hunter in the Night |
| Ability | Ogre Magi – Multicast |
| Ability | Phantom Assassin – Immaterial |
| Ability | Phantom Lancer – Phantom Rush |
| Ability | Shadow Fiend – Necromastery |
| Ability | Tidehunter – Kraken Shell |
| Ability | Treant Protector – Nature's Guise |
| Ability | Troll Warlord – Fervor |
| Ability | Visage – Gravekeeper's Cloak |
| Ability | Bristleback – Warpath² |
| Item | Abyssal Blade – Damage Block |
| Item | Aether Lens – Aethereal Focus |
| Item | Crimson Guard – Damage Block |
| Item | Octarine Core – Cooldown Reduction |
| Item | Vanguard – Damage Block |

¹ Supernatural does not apply to illusions created by Reflection. ² Warpath procs when illusions cast abilities. Because Warpath also applies a stack to every owned illusion by default, an illusion gains two stacks per cast. [corpus:liquipedia_dota2/illusions@2376496#Passive_Abilities]

### Partially Functional

| Passive | Functional portion |
|---|---|
| Bloodseeker – Thirst¹ | Health restoration and the maximum movement-speed limit work; the movement-speed bonus, hero detection, and vision do not. |
| Bristleback – Bristleback² | Only damage block/reduction works. |
| Dragon Knight – Dragon Blood³ | Only the health-regeneration bonus works. |
| Timbersaw – Reactive Armor³ | Only the health-regeneration bonus works. |
| Viper – Corrosive Skin⁴ | Only the damage per second and slow bonus work. |

[corpus:liquipedia_dota2/illusions@2376496#Passive_Abilities]

### Not Functional

| Passive ability not functional for illusions |
|---|
| Abaddon – Borrowed Time¹ |
| Alchemist – Greevil's Greed |
| Anti-Mage – Counterspell¹ |
| Centaur Warrunner – Retaliate |
| Drow Ranger – Marksmanship |
| Faceless Void – Distortion Field |
| Gyrocopter – Side Gunner |
| Infused Raindrops – Magical Damage Block |
| Linken's Sphere – Spellblock |
| Meepo – Divided We Stand |
| Pangolier – Lucky Shot |
| Pudge – Flesh Heap |
| Razor – Storm Surge |
| Shadow Fiend – Requiem of Souls¹ |
| Slark – Shadow Dance¹ |
| Spectre – Dispersion |
| Wraith King – Reincarnation |
| Wraith King – Vampiric Spirit (Death Delay) |
| Zeus – Static Field |
| Zeus – Lightning Hands |

¹ The passive components of these active abilities do not work for illusions. [corpus:liquipedia_dota2/illusions@2376496#Passive_Abilities]

### Auras

| Aura bestowed by illusions |
|---|
| Assault Cuirass – Assault Aura |
| Beastmaster – Inner Beast |
| Buckler – Buckler Aura |
| Centaur Warrunner – Retaliate Aura |
| Crystal Maiden – Arcane Aura |
| Elder Titan – Natural Order¹ |
| Guardian Greaves – Guardian Aura |
| Headdress – Regeneration Aura |
| Luna – Lunar Blessing |
| Lycan – Feral Impulse |
| Mekansm – Mekansm Aura |
| Necrophos – Heartstopper Aura |
| Pipe of Insight – Insight Aura |
| Radiance – Burn² ³ |
| Ring of Basilius – Basilius Aura |
| Shadow Fiend – Presence of the Dark Lord |
| Shiva's Guard – Freezing Aura |
| Underlord – Atrophy Aura⁴ |
| Undying – Plague Aura |
| Vengeful Spirit – Vengeance Aura |
| Vladmir's Offering – Vladmir's Aura |

¹ Despite lacking an Astral Spirit, an illusion’s Natural Order always bestows both its armor-reduction and magic-resistance-reduction auras. ² Illusions copy these auras’ toggled On/Off states. ³ Burn is weaker on illusions, dealing 35 damage per second instead of 60. ⁴ Illusions bestow Atrophy Aura. When an enemy dies in an illusion’s aura range, Underlord receives the damage bonus if he owns the illusion; otherwise, the illusion receives it.

| Aura not bestowed by illusions |
|---|
| Drow Ranger – Marksmanship Agility Aura |
| Gem of True Sight – True Sight |
| Lycan – Shapeshift Speed and Crit Aura |
| Terrorblade – Metamorphosis Aura |
| Wraith King – Wraith Delay Aura¹ |

¹ Requires Aghanim's Scepter. [corpus:liquipedia_dota2/illusions@2376496#Aura]

## Ability Interactions

Most abilities treat illusions as regular heroes, but some apply different effects, interact differently, or do not affect illusions. [corpus:liquipedia_dota2/illusions@2376496#Ability_Interactions]

### Instant Kill

The following abilities instantly destroy an illusion unless it is a strong illusion:

| Instant-killing ability |
|---|
| Dagon – Energy Burst |
| Dazzle – Poison Touch⁵ |
| Disruptor – Glimpse |
| Lion – Hex |
| Pudge – Meat Hook |
| Scythe of Vyse – Hex |
| Shadow Shaman – Hex |
| Skywrath Mage – Mystic Flare |

¹ Instantly kills the target upon landing if it is not a hero or clone. ² Requires a talent. ³ Requires Aghanim's Scepter. ⁴ Requires Aghanim's Shard. ⁵ Poison Touch only hexes when cast from Nothl Projection. [corpus:liquipedia_dota2/illusions@2376496#Instant_Kill]

### Creep Duration

The following abilities use their non-hero or creep duration against illusions rather than their hero duration:

| Treats illusions as non-hero units |
|---|
| Abaddon – Borrowed Time Aura¹ |
| Ancient Apparition – Ice Blast |
| Bloodseeker – Thirst |
| Chen – Hand of God |
| Dark Seer – Wall of Replica |
| Earth Spirit – Rolling Boulder |
| Enchantress – Enchant |
| Guardian Greaves – Guardian Aura |
| Invoker – E.M.P. |
| Io – Spirits |
| Kunkka – Ghostship |
| Mirana – Moonlight Shadow |
| Nature's Prophet – Wrath of Nature |
| Pudge – Flesh Heap |
| Riki – Tricks of the Trade |
| Skywrath Mage – Concussive Shot |
| Skywrath Mage – Mystic Flare |
| Slark – Essence Shift |
| Slark – Pounce |
| Smoke of Deceit – Disguise |
| Spectre – Haunt |
| Spectre – Dispersion² |
| Spectre – Shadow Step¹ |
| Undying – Decay |
| Urn of Shadows – Soul Release |
| Visage – Soul Assumption |
| Witch Doctor – Paralyzing Cask |

¹ Requires Aghanim's Scepter. ² Requires Aghanim's Shard. [corpus:liquipedia_dota2/illusions@2376496#Creep_Duration]

#### Ward Units

When attacked by an illusion, these ward units require the creep amount of attacks to destroy rather than the hero amount:

| Ward unit treating illusions as non-hero units |
|---|
| Phoenix – Supernova |
| Pugna – Nether Ward |
| Undying – Tombstone |

[corpus:liquipedia_dota2/illusions@2376496#Ward_Units]

### No Effect

These abilities do not affect illusions, cannot target them, or do not work against them:

| No effect on illusions |
|---|
| Alchemist – Greevil's Greed¹ |
| Alchemist – Aghanim's Scepter Synth² |
| Broodmother – Spin Web² |
| Necrophos – Heartstopper Aura |
| Observer and Sentry Wards – Share Wards² |
| Rubick – Spell Steal |
| Shadow Fiend – Necromastery¹ |
| Tango – Devour² |
| Templar Assassin – Psi Blades |
| Underlord – Atrophy Aura¹ |
| Viper – Nethertoxin |

¹ These abilities ignore illusion deaths, so killing an illusion does not apply their effects. ² These abilities either lack a target or do not place their buffs or debuffs on illusions. [corpus:liquipedia_dota2/illusions@2376496#No_Effect]

### Other Interactions

| Ability or mechanic | Interaction with illusions |
|---|---|
| Bounty Hunter – Track | Illusions provide no bounty when they die while tracked. |
| Bristleback – Warpath | Warpath places its buff or grants a stack to the caster and every illusion controlled by the caster. |
| Buildings – Backdoor Protection | Illusions deal 75% less damage to protected buildings instead of 25% like other units. They deal 60% less damage to unprotected buildings. |
| Elder Titan – Astral Spirit | It damages illusions but does not count them toward its damage and speed buff. |
| Legion Commander – Overwhelming Odds | It deals additional damage based on current health to illusions, which are treated as creeps. |
| Legion Commander – Duel | Defeating an illusion in a Duel grants no victory damage. |
| Medusa – Mystic Snake | It does not drain mana from illusions. |
| Roshan – Strength of the Immortal | It grants 0.4 damage resistance against attacks from illusions. |
| Silencer – Glaives of Wisdom | It does not steal intelligence from illusions when they are attacked or die. |
| Storm – Dispel Magic | It damages illusions in addition to dispelling them. |
| Tusk – Snowball | Allied illusions cannot enter Snowball; only Tusk’s own illusions can. Added illusions do not increase its damage. |

[corpus:liquipedia_dota2/illusions@2376496#Other_Interactions]

## Recent Changes

| Version | Date | Change |
|---|---|---|
| 7.40 | 2025-12-15 | All illusions now have fixed base day/night vision range of 800/400. |
| 7.34 | 2023-08-08 | The Spirit Bear is no longer restricted from having illusions. |
| 7.30c | 2021-09-11 | The Vengeance Illusion now uses a hero health bar instead of the regular unit health bar. |

[corpus:liquipedia_dota2/illusions@2376496#Recent_Changes]