---
title: Silence
kind: concept
patch: 7.41d
card:
  entity: silence
  sentences:
  - text: Silence is a status effect that prevents affected units from using active
      hero abilities for its duration and interrupts channeling spells already in
      use.
    marks:
    - corpus:liquipedia_dota2/silence@2405718
  - text: It fully prevents active-ability orders except item casts.
    marks:
    - corpus:liquipedia_dota2/silence@2405718#Definition
  - text: Silence disables the functionality of abilities currently set to Autocast.
    marks:
    - corpus:liquipedia_dota2/silence@2405718#Definition
  - text: Toggled abilities remain in their current On or Off state, although mana
      exhaustion can toggle a mana-draining ability off normally.
    marks:
    - corpus:liquipedia_dota2/silence@2405718#Mechanics
  - text: Silence also disables active attack modifiers.
    marks:
    - corpus:liquipedia_dota2/silence@2405718#Mechanics
  - text: Effects from abilities cast before silence continue operating.
    marks:
    - corpus:liquipedia_dota2/silence@2405718#Mechanics
  - text: Passive abilities remain functional even when they have a cooldown or mana
      cost.
    marks:
    - corpus:liquipedia_dota2/silence@2405718#Mechanics
  - text: Abilities with the DOTA_ABILITY_BEHAVIOR_IGNORE_SILENCE flag remain castable,
      and silence cannot prevent their channeling or cast-point start.
    marks:
    - corpus:liquipedia_dota2/silence@2405718#Abilities_Castable_When_Silenced
  - text: All sources of fear and hex also apply silence.
    marks:
    - corpus:liquipedia_dota2/silence@2405718#Silence
  - text: Mute is the counterpart that disables active items rather than active abilities.
    marks:
    - corpus:liquipedia_dota2/silence@2405718#Mute
  - text: Mute cancels channeled items but does not affect passives or ongoing item
      effects.
    marks:
    - corpus:liquipedia_dota2/silence@2405718#Mute
  - text: Version 6.84, dated 2015-04-30, changed Silence so it no longer disables
      invisibility.
    marks:
    - corpus:liquipedia_dota2/silence@2405718#Version_History
---

# Silence

Silence is a status effect that prevents affected units from using active hero abilities for its duration and interrupts any channeling spells already in use. It can aid ganks against heroes with blink or invisibility spells because silences tend to last longer than other disables, allowing more time to kill the target. Even brief teamfight silences can prevent enemies from combining their spells. [corpus:liquipedia_dota2/silence@2405718]

## Definition

| Ability and item disable | Disabled aspect or definition | Example |
|---|---|---|
| Silence | Fully prevents active-ability orders except item casts. Autocast abilities currently set to Autocast have their functionality disabled. Toggled abilities remain in their current On / Off state for the duration, but their functionality is not disabled. | Global Silence |
| Break | Fully disables passive abilities, but does not disable item passives or Talents, with some exceptions. On-death passives such as Reincarnation and direct-synergy passives such as Caustic Finale with Burrowstrike are generally not disabled. | Viper Strike |
| Mute | Fully prevents item-cast orders except ability casts. | Doom |

[corpus:liquipedia_dota2/silence@2405718#Definition]

## Mechanics

When a unit is silenced, a grid-like effect overlays its ability icons in the HUD. Left-clicking an active ability or pressing its hotkey displays **Silenced** in red on the screen.

Silence disables every active ability, including toggle abilities and active attack modifiers. It immediately cancels an ability being channeled. If an ability is Toggled/On, silence only prevents the player from toggling it off; if it drains mana and the unit runs out of mana while silenced, it is Toggled Off normally.

Silence does not stop effects from abilities already cast. Silencing Razor after Static Link or Eye of the Storm has been cast does not stop the link from draining or the storm from striking.

Silence does not disable passive abilities. It prevents the active part of Vampiric Spirit from being used but does not prevent skeleton charges from being gained or lifesteal from proccing. Passive abilities remain unaffected even when they have a cooldown or mana cost. [corpus:liquipedia_dota2/silence@2405718#Mechanics]

### Abilities Castable When Silenced

Abilities with the `DOTA_ABILITY_BEHAVIOR_IGNORE_SILENCE` flag remain castable while silenced. Silence also cannot prevent their channeling or the start of their cast point.

| Category | Unit or source | Ability | Requirement marker |
|---|---|---|---|
| Ability | Ancient Apparition | Release | — |
| Ability | Buildings | Glyph of Fortification | — |
| Ability | Fiend's Gate | Warp | — |
| Ability | Roshan | Roar of Retribution | — |
| Ability | Runes | Activate | — |
| Ability | Scan | Scan | — |
| Ability | Undying | Tombstone (Enterance) | 2b |
| Ability | Twin Gate | Warp | — |
| Ability | Watcher | Lantern of Sight | — |
| Attack Modifier | Bounty Hunter | Jinada | — |
| Attack Modifier | Omniknight | Hammer of Purity | — |
| Attack Modifier | Kunkka | Tidebringer | — |
| Attack Modifier | Treant Protector | Leech Seed | — |
| Attack Modifier | Weaver | Geminate Attack | — |
| Toggle | Brewmaster | Drunken Brawler | — |
| Toggle | Kez | Switch Discipline | — |
| Toggle | Largo | Amphibian Rhapsody | — |
| Toggle | Muerta | Gunslinger | — |
| Toggle | Phantom Lancer | Phantom Rush | — |
| Toggle | Troll Warlord | Battle Stance | — |
| Conditional | Lone Druid | Savage Roar | — |
| Conditional | Spirit Bear | Savage Roar | — |

| Marker | Requirement |
|---|---|
| 1 | Requires a talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. |
| 3 | Requires the selected corresponding facet. |

[corpus:liquipedia_dota2/silence@2405718#Abilities_Castable_When_Silenced]

### Silence Sources

All sources of fear and hex also apply silence.

| Source type | Unit or item | Ability | Condition marker |
|---|---|---|---|
| Ability | Arc Warden | Flux | 2a |
| Ability | Bloodseeker | Blood Rite | — |
| Ability | Clockwerk | Hookshot | 4 |
| Ability | Dawnbreaker | Solar Guardian | 4 |
| Ability | Death Prophet | Silence | — |
| Ability | Disruptor | Static Storm | — |
| Ability | Doom | Doom | — |
| Ability | Drow Ranger | Gust | — |
| Ability | Earth Spirit | Geomagnetic Grip | — |
| Ability | Enigma | Black Hole | — |
| Ability | Grimstroke | Phantom's Embrace | — |
| Ability | Kez | Talon Toss | — |
| Ability | Legion Commander | Duel | 6 |
| Ability | Lone Druid | Savage Roar | — |
| Ability | Marci | Unleash | 2a |
| Ability | Muerta | Dead Shot | — |
| Ability | Muerta | The Calling | — |
| Ability | Night Stalker | Crippling Fear | — |
| Ability | Outworld Destroyer | Astral Imprisonment | 2b, 7 |
| Ability | Psionic Trap | Trap | 2b |
| Ability | Puck | Waning Rift | — |
| Ability | Queen of Pain | Blink | 2b |
| Ability | Riki | Smoke Screen | — |
| Ability | Shadow Fiend | Requiem of Souls | — |
| Ability | Silencer | Last Word | — |
| Ability | Silencer | Global Silence | — |
| Ability | Skywrath Mage | Ancient Seal | — |
| Ability | Snapfire | Gobble Up | — |
| Ability | Spirit Bear | Savage Roar | — |
| Ability | Templar Assassin | Psionic Projection | 2b |
| Ability | Templar Assassin | Psionic Trap | 2b |
| Ability | Void Spirit | Aether Remnant | — |
| Ability | Void Spirit | Dissimilate | — |
| Ability | Void Spirit | Resonant Pulse | 2a |
| Ability | Hoodwink | Decoy (Illusion) | 5 |
| Item | Bloodthorn | Soul Rend | — |
| Item | Mask of Madness | Berserk | — |
| Item | Mind Breaker | Silence Strike | — |
| Item | Orchid Malevolence | Soul Burn | — |
| Item | Wind Waker | Cyclone | 8 |

| Marker | Condition |
|---|---|
| 1 | Requires a talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. |
| 3 | Requires the selected corresponding facet. |
| 4 | Silences caster when moving. |
| 5 | Only silences the illusion. |
| 6 | Both the Dueled target and caster are silenced. |
| 7 | Only silences allies. |
| 8 | Silences when cast on yourself. |

[corpus:liquipedia_dota2/silence@2405718#Silence]

## Mute

Mute is the counterpart to silence: it disables a unit's active items in the same fashion that silence disables active abilities. It does not affect passives or stop ongoing item effects, but it cancels channeled items. It does not prevent disassembling and prevents the unit from toggling items On / Off.

Non-sharable items are always muted when picked up by a unit other than their owner. All sources of fear and hex also apply mute.

| Source | Ability | Condition marker |
|---|---|---|
| Dawnbreaker | Solar Guardian | 4 |
| Disruptor | Static Storm | 2a |
| Doom | Doom | 1 |
| Legion Commander | Duel | 5 |
| Outworld Destroyer | Astral Imprisonment | 2b, 6 |
| Phoenix | Supernova | — |
| Snapfire | Gobble Up | — |
| Tusk | Snowball | 7 |
| Void Spirit | Dissimilate | — |
| Wind Waker | Cyclone | 8 |

| Marker | Condition |
|---|---|
| 1 | Requires a Talent. |
| 2a | Requires Aghanim's Scepter. |
| 2b | Requires Aghanim's Shard. |
| 3 | Requires selecting the corresponding facet. |
| 4 | Mutes caster after succes channeling. |
| 5 | Both the Dueled target and caster are muted. |
| 6 | Only mutes allies. |
| 7 | Mutes Tusk while inside the Snowball. Allies inside are not muted, but they can't act. |
| 8 | Mutes when cast on yourself. |

[corpus:liquipedia_dota2/silence@2405718#Mute]

## Version History

| Version | Date | Description |
|---|---|---|
| 7.33 | 2023-04-20 | The following items now use the Mute mechanic:<br>• Blink Dagger<br>• Overwhelming Blink<br>• Swift Blink<br>• Arcane Blink |
| 7.07 | 2017-10-31 | Added a HUD indication over the inventory to show the mute state. |
| 6.84 | 2015-04-30 | Item silencing is now called Mute.<br>Silence no longer disables invisibility. |

[corpus:liquipedia_dota2/silence@2405718#Version_History]

## Patch History

| Patch | Description |
|---|---|
| 25 Mar 2021 | Added a generic Mute modifier. |
| 08 Aug 2019 | Added new overhead visual effects for Mute debuffs. |
| 13 Sep 2018 | Increased music volume during silence effects from 0.4 to 0.6. |
| 23 Dec 2015 | Fixed Infernal Blade and Tidebringer not being disabled by silence. |
| 16 Dec 2015, Update 3 | Fixed a bug where items could not be targeted while muted. |
| 30 Apr 2014 | Fixed Silence interrupting channeling items. |
| 15 Aug 2012 | Fixed the Silenced state getting stuck in the HUD. |

[corpus:liquipedia_dota2/silence@2405718#Patch_History]