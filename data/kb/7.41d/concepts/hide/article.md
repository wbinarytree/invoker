---
title: Hide
kind: concept
patch: 7.41d
card:
  entity: hide
  sentences:
  - text: Hiding, also called banishing, temporarily removes a unit from the game,
      preventing it from moving, attacking, or casting abilities or items; most sources
      also grant invulnerability.
    marks:
    - corpus:liquipedia_dota2/hide@2396533
    - corpus:liquipedia_dota2/hide@2396533#Mechanics
  - text: Hidden units continue to gain experience and gold.
    marks:
    - corpus:liquipedia_dota2/hide@2396533#Mechanics
  - text: Abilities generally cannot affect hidden units, although exceptions include
      Shadow Poison.
    marks:
    - corpus:liquipedia_dota2/hide@2396533#Mechanics
  - text: Meat Hook passes through a hidden unit and may hit a unit behind it.
    marks:
    - corpus:liquipedia_dota2/hide@2396533#Mechanics
  - text: Solar Guardian and Fowl Play hide units without granting invulnerability.
    marks:
    - corpus:liquipedia_dota2/hide@2396533#Sources
  - text: Dispel abilities cannot target hidden units but fully affect them.
    marks:
    - corpus:liquipedia_dota2/hide@2396533#Piercing_Hidden
  - text: Hide itself does not stop forced movement.
    marks:
    - corpus:liquipedia_dota2/hide@2396533#Piercing_Hidden
  - text: Spell Block triggers on a hidden unit only when the spell can negatively
      affect it or bounce off it.
    marks:
    - corpus:liquipedia_dota2/hide@2396533#Piercing_Hidden
  - text: Bounce spells cannot select a hidden unit as a new target but still bounce
      off a target that becomes hidden afterward.
    marks:
    - corpus:liquipedia_dota2/hide@2396533#Piercing_Hidden
  - text: Disseminate's duration pauses when its unit is hidden by its own Disruption.
    marks:
    - corpus:liquipedia_dota2/hide@2396533#Effect_Pause
  - text: A debuff-immune unit under Enchant Remnant can attack and use items and
      abilities while hidden.
    marks:
    - corpus:liquipedia_dota2/hide@2396533#Debuff_Immunity
  - text: Hidden units still block Neutral Creep spawns but do not count toward triggering
      certain neutral-creep abilities.
    marks:
    - corpus:liquipedia_dota2/hide@2396533#Map_Interactions
---

# Hide

Hiding, also called banishing, causes a unit to disappear temporarily from the game. [corpus:liquipedia_dota2/hide@2396533]

## Mechanics

A hidden unit cannot move, attack, or cast abilities or items. Most hide sources also make the unit invulnerable. Hidden units continue to gain experience and gold.

While hidden, a unit cannot be affected by abilities except for certain exceptions, including Shadow Poison. Meat Hook passes through a hidden unit and may hit a unit behind it. [corpus:liquipedia_dota2/hide@2396533#Mechanics]

## Sources

### With invulnerability

| Hero or source | Ability |
|---|---|
| Brewmaster | Primal Split |
| Chaos Knight | Phantasm |
| Earth Spirit | Enchant Remnant |
| Fallen Sky | Fallen Sky |
| Lifestealer | Infest |
| Manta Style | Mirror Image |
| Monkey King | Wukong's Command (Clone) |
| Meepo | Dig |
| Meepo | MegaMeepo |
| Meepo | MegaMeepo Fling |
| Naga Siren | Mirror Image |
| Necrophos | Death Seeker |
| Outworld Destroyer | Astral Imprisonment<sup>4</sup> |
| Phantom Lancer | Doppelganger |
| Phoenix | Supernova |
| Puck | Phase Shift |
| Riki | Tricks of the Trade |
| Ringmaster | Funhouse Mirror |
| Runes | Illusion |
| Shadow Demon | Disruption |
| Snapfire | Gobble Up |
| Snapfire | Spit Out |
| Sven | Storm Hammer (Alt-Cast)<sup>2a</sup> |
| Terrorblade | Reflection (Illusion) |
| Undying | Tombstone (Enterance)<sup>2b</sup> |
| Tusk | Snowball |
| Void Spirit | Dissimilate |
| Witch Doctor | Voodoo Switcheroo |

### Without invulnerability

| Hero | Ability |
|---|---|
| Dawnbreaker | Solar Guardian |
| Shadow Shaman | Fowl Play<sup>2b</sup> |

| Marker | Requirement or exception |
|---|---|
| 1 | Requires a Talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. |
| 4 | After the Aghanim's Shard upgrade, Astral Imprisonment no longer hides allies. |

[corpus:liquipedia_dota2/hide@2396533#Sources]

## Piercing Hidden

Dispel abilities cannot target hidden units but fully affect them. Forced movement is not stopped by hide itself, although it may stop because of a stun or another reason.

Spell Block triggers on a hidden unit only if the spell can negatively affect that unit or can bounce off it. Bounce spells do not treat a hidden unit as a valid new target, but a spell still bounces off a unit that becomes hidden after being targeted.

### Enemy interactions

| Interaction | Hero | Ability |
|---|---|---|
| Affects a hidden enemy only under a specific source<sup>4</sup> | Outworld Destroyer | Sanity's Eclipse<sup>5</sup> |
| Affects a hidden enemy only under a specific source<sup>4</sup> | Shadow Demon | Disseminate<sup>6</sup> |
| Affects a hidden enemy only under a specific source<sup>4</sup> | Shadow Demon | Shadow Poison<sup>6</sup> |
| Affects a hidden enemy only under a specific source<sup>4</sup> | Shadow Demon | Shadow Poison Release<sup>6</sup> |
| Affects a hidden enemy only under a specific source<sup>4</sup> | Shadow Demon | Demonic Purge<sup>6</sup> |
| No Target | Spectre | Haunt |
| Link; must be connected before the unit becomes hidden | Death Prophet | Spirit Siphon |
| Link; must be connected before the unit becomes hidden | Razor | Static Link |

| Marker | Interaction rule |
|---|---|
| 4 | Unlike other abilities, these can damage hidden units, but only when the enemy is affected by specific hide sources. |
| 5 | Sanity's Eclipse affects only a unit under Astral Imprisonment. |
| 6 | These abilities and their effects, regardless of their source, fully affect the affected hero under Shadow Demon's most recent Disruption cast. |

### Ally interactions

| Interaction | Hero or item | Ability |
|---|---|---|
| Affects hidden allies | Centaur Warrunner | Stampede |
| Affects hidden allies | Clockwerk | Overclocking (Self-slow) |
| Affects hidden allies | Chen | Hand of God |
| Affects hidden allies | Mirana | Moonlight Shadow |
| Link; must be connected before the unit becomes hidden | Io | Tether |
| Teleport | Chen | Divine Favor (Self-Cast) |
| Teleport | Io | Relocate |
| Teleport | Keeper of the Light | Recall<sup>3</sup> |
| Teleport | Lone Druid | Summon Spirit Bear |
| Teleport | Meepo | Poof (Alt-Cast)<sup>4</sup> |
| Teleport | Sand King | Burrowstrike |
| Item | Arcane Boots | Replenish |
| Item | Crimson Guard | Guard |
| Item | Guardian Greaves | Mend |
| Item | Mekansm | Restore |

| Marker | Requirement or interaction rule |
|---|---|
| 3 | Requires selecting the corresponding facet. |
| 4 | Meepo can teleport to another Meepo even if that Meepo is hidden. |

[corpus:liquipedia_dota2/hide@2396533#Piercing_Hidden]

### Path Block

| Result | Hero or item | Ability |
|---|---|---|
| Allows | Disruptor | Kinetic Field |
| Allows | Disruptor | Kinetic Fence |
| Allows | Mars | Arena of Blood |
| Blocks | Clockwerk | Power Cogs |
| Blocks | Drow Ranger | Glacier |
| Blocks | Earthshaker | Fissure |
| Blocks | Hoodwink | Acorn Shot |
| Blocks | Iron Branch | Plant Tree |
| Blocks | Nature's Prophet | Sprout |
| Blocks | Tusk | Ice Shards |

[corpus:liquipedia_dota2/hide@2396533#Path_Block]

## Effect Pause

Shadow Demon's Disseminate duration is paused when the unit is hidden by its own Disruption. [corpus:liquipedia_dota2/hide@2396533#Effect_Pause]

## Castable While Hidden

| Hero | Hide source or ability | Permitted action |
|---|---|---|
| Earth Spirit | Rolling Boulder | Can self-cast while hidden by Enchant Remnant. |
| Lifestealer | Consume | Can cast while hidden by Infest. |
| Phoenix | Sun Ray | Can cast while hidden by Supernova. |
| Tusk | Snowball | Can grab allies. |
| Tusk | Snowball | Can use Ice Shards. |
| Tusk | Snowball | Can use Launch Snowball. |
| Tusk | Snowball | Can use Tag Team. |
| Puck | Phase Shift | Can use any ability during the 1 tick buff linger while hidden. |

[corpus:liquipedia_dota2/hide@2396533#Castable_while_Hidden]

### Debuff Immunity

| Hero | Ability | Interaction |
|---|---|---|
| Earth Spirit | Enchant Remnant | A debuff-immune unit under this effect can attack and use items and abilities while hidden. |
| Elder Titan | Astral Spirit | If Astral Spirit returns while Elder Titan is hidden, Debuff Immunity lets him move, attack, and use abilities and items while remaining hidden and invisible to everyone. |

[corpus:liquipedia_dota2/hide@2396533#Debuff_Immunity]

### Stun

Most hide sources apply only a stun.

| Hero or source | Ability |
|---|---|
| Brewmaster | Primal Split |
| Chaos Knight | Phantasm |
| Earth Spirit | Enchant Remnant |
| Fallen Sky | Fallen Sky |
| Manta Style | Mirror Image |
| Meepo | Dig |
| Meepo | MegaMeepo |
| Meepo | MegaMeepo Fling |
| Naga Siren | Mirror Image |
| Necrophos | Death Seeker |
| Outworld Destroyer | Astral Imprisonment<sup>4</sup> |
| Phantom Lancer | Doppelganger |
| Puck | Phase Shift |
| Runes | Illusion |
| Ringmaster | Funhouse Mirror |
| Shadow Demon | Disruption |
| Snapfire | Spit Out |
| Sven | Storm Hammer (Alt-Cast)<sup>2a</sup> |

After the Aghanim's Shard upgrade, Astral Imprisonment no longer hides allies and applies Silence instead of Stun.

#### Castable while stunned

| Hero or source | Ability |
|---|---|
| Abaddon | Borrowed Time |
| Bane | Nightmare End |
| Buildings | Glyph of Fortification |
| Dazzle | Nothl Projection<sup>2b</sup> |
| Elder Titan | Return Astral Spirit |
| Elder Titan | Move Astral Spirit |
| Lone Druid | Savage Roar<sup>2b</sup> |
| Spirit Bear | Savage Roar<sup>2b</sup> |
| Morphling | Attribute Shift<sup>2b</sup> |
| Roshan | Roar of Retribution |
| Rubick | Telekinesis Land<sup>2b, 4</sup> |
| Scan | Scan |
| Templar Assassin | Refraction<sup>2b</sup> |
| Troll Warlord | Battle Trance<sup>1</sup> |
| Ursa | Enrage<sup>2a</sup> |
| Visage | Stone Form |
| Familiar | Stone Form |

| Marker | Requirement or condition |
|---|---|
| 1 | Requires Talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. |
| 4 | Ignores stun only during Duel. |
| 5 | Ignores stun only if Telekinesis is self-cast. |

[corpus:liquipedia_dota2/hide@2396533#Stun]

### Silence

Some hide sources use Silence, Mute, and other modifiers.

| Hero | Ability |
|---|---|
| Shadow Shaman | Fowl Play<sup>2b</sup> |
| Snapfire | Gobble Up |
| Undying | Tombstone (Enterance)<sup>2b</sup> |
| Void Spirit | Dissimilate |

These modifiers allow the unit to pick up runes, drop or take items, and use the following abilities.

| Category | Hero or source | Ability |
|---|---|---|
| Castable while Silenced | Ancient Apparition | Release |
| Castable while Silenced | Buildings | Glyph of Fortification |
| Castable while Silenced | Fiend's Gate | Warp |
| Castable while Silenced | Roshan | Roar of Retribution |
| Castable while Silenced | Runes | Activate |
| Castable while Silenced | Scan | Scan |
| Castable while Silenced | Undying | Tombstone (Enterance)<sup>2b</sup> |
| Castable while Silenced | Twin Gate | Warp |
| Castable while Silenced | Watcher | Lantern of Sight |
| Attack Modifier | Bounty Hunter | Jinada |
| Attack Modifier | Omniknight | Hammer of Purity |
| Attack Modifier | Kunkka | Tidebringer |
| Attack Modifier | Treant Protector | Leech Seed |
| Attack Modifier | Weaver | Geminate Attack |
| Toggle | Brewmaster | Drunken Brawler |
| Toggle | Kez | Switch Discipline |
| Toggle | Largo | Amphibian Rhapsody |
| Toggle | Muerta | Gunslinger |
| Toggle | Phantom Lancer | Phantom Rush |
| Toggle | Troll Warlord | Battle Stance |
| Castable while Silenced [CONDITIONAL] | Lone Druid | Savage Roar |
| Castable while Silenced [CONDITIONAL] | Spirit Bear | Savage Roar |

| Marker | Requirement |
|---|---|
| 1 | Requires a talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. |

[corpus:liquipedia_dota2/hide@2396533#Silence]

### Can't Act

Some hide sources use Cannot Act and other modifiers.

| Hero | Ability |
|---|---|
| Dawnbreaker | Solar Guardian |
| Lifestealer | Infest |
| Phoenix | Supernova (Ally)<sup>2a</sup> |
| Tusk | Snowball (Ally) |
| Witch Doctor | Voodoo Switcheroo |

#### Castable while unable to act

| Hero or source | Ability |
|---|---|
| Buildings | Glyph of Fortification |
| Lifestealer | Consume |
| Elder Titan | Move Astral Spirit |
| Elder Titan | Return Astral Spirit |
| Scan | Scan |

[corpus:liquipedia_dota2/hide@2396533#Can't_Act]

### Other Modifiers

The following abilities do not apply Stun, Silence, or Can't Act, instead using other modifiers.

| Hero | Ability |
|---|---|
| Earth Spirit | Rolling Boulder |
| Phoenix | Supernova (Self) |
| Terrorblade | Reflection (Illusion) |
| Tusk | Snowball (Self) |

[corpus:liquipedia_dota2/hide@2396533#Other_Modifiers]

## Shared Unit Control

Changing the Hero box has no effect while hidden. [corpus:liquipedia_dota2/hide@2396533#Shared_Unit_Control]

## Map Interactions

Scan and Crystal Ball ignore hidden units. Rejuvenation Aura and Tower Protection ignore invulnerable units.

Hidden heroes cannot Pluck Lotus or pause the process. They cannot Gather Experience or pause that process.

Hidden units still block Neutral Creep spawns but do not count toward triggering certain neutral-creep abilities. Hidden heroes are not considered when determining whether heroes are near Tormentor. [corpus:liquipedia_dota2/hide@2396533#Map_Interactions]

## History

| Date | Change |
|---|---|
| 22 Dec 2022 | Fixed Avatar being castable with ⇧ Shift-queue while Doomed after returning from being hidden, such as by Disruption. |
| 08 Nov 2017 | Created the new health-bar status BANISHED. |
| 08 Nov 2017 | Added a status-duration indicator for Astral Imprisonment. |
| 08 Nov 2017 | Added a status-duration indicator for Disruption. |
| 22 Jan 2016 | Fixed a selection issue with non-hero units when they became temporarily hidden, such as during Astral Imprisonment. |
| 05 Feb 2014 | Fixed kill-assist gold not being given to hidden heroes, such as during Phase Shift. |

[corpus:liquipedia_dota2/hide@2396533#Patch_History]