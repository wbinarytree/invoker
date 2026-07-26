---
title: Invisibility
kind: concept
patch: 7.41d
card:
  entity: invisibility
  sentences:
  - text: Invisibility is a status effect that prevents enemies from seeing a unit
      within their vision range, enabling scouting, spying, and ambushes; enemies
      can counter it with True Sight.
    marks:
    - corpus:liquipedia_dota2/invisibility@2383943
  - text: An invisible unit is unselectable and attack immune to the enemy team.
    marks:
    - corpus:liquipedia_dota2/invisibility@2383943#Mechanics
  - text: Becoming invisible triggers a one-time disjoint rather than periodic disjoints
      during the effect.
    marks:
    - corpus:liquipedia_dota2/invisibility@2383943#Mechanics
  - text: True Sight prevents this disjoint unless the unit has True Sight Immunity.
    marks:
    - corpus:liquipedia_dota2/invisibility@2383943#Mechanics
  - text: With few exceptions, invisibility ends when a unit reaches an attack point
      or an ability or item’s cast point.
    marks:
    - corpus:liquipedia_dota2/invisibility@2383943#Mechanics
  - text: Multiple invisibility sources apply independently, and the unit remains
      invisible while at least one is active.
    marks:
    - corpus:liquipedia_dota2/invisibility@2383943#Mechanics
  - text: Invisible units and their minimap icons are not rendered for the enemy team.
    marks:
    - corpus:liquipedia_dota2/invisibility@2383943#Appearance
  - text: During fade delay, invisibility has no effect, and attacking or casting
      an ability or item resets the delay.
    marks:
    - corpus:liquipedia_dota2/invisibility@2383943#Fade_Delay
  - text: Fade time has a fixed duration and is not reset or broken by actions performed
      during it.
    marks:
    - corpus:liquipedia_dota2/invisibility@2383943#Fade_Time
  - text: While invisible or fading, a unit never automatically attacks nearby enemies,
      regardless of auto-attack settings.
    marks:
    - corpus:liquipedia_dota2/invisibility@2383943#Attack_Behavior
  - text: True Sight nullifies invisibility for its observer, making the affected
      unit selectable and targetable normally.
    marks:
    - corpus:liquipedia_dota2/invisibility@2383943#True_Sight
  - text: Most area spells affect invisible units, but single-target spells cannot
      target them without True Sight.
    marks:
    - corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units
---

# Invisibility

Invisibility is a status effect that prevents enemies from seeing a unit even within their vision range, allowing the unit to scout, spy on, and ambush enemies by sneaking through their lines. Enemies can counter it by acquiring True Sight. [corpus:liquipedia_dota2/invisibility@2383943]

## Mechanics

Invisible units appear transparent to allies and enemies with True Sight. To the enemy team, an invisible unit is unselectable and attack immune. It is also flagged as invisible, producing additional ability interactions. [corpus:liquipedia_dota2/invisibility@2383943#Mechanics]

Applying invisibility triggers a one-time disjoint when the unit becomes invisible; it does not trigger periodically throughout the duration. Applying another invisibility over an existing one also disjoints. The disjoint does not trigger when an enemy has True Sight over the unit unless the unit has True Sight Immunity. Losing True Sight does not trigger a disjoint, even when True Sight had been preventing an invisibility. [corpus:liquipedia_dota2/invisibility@2383943#Mechanics]

How invisibility is lost depends on its source. With very few exceptions, it ends upon reaching the attack point of an attack or the cast point of an ability or item. Extended effects such as Eclipse and Epicenter therefore do not cancel invisibility with each beam or pulse, and channeling abilities do not cancel it after channeling has begun. [corpus:liquipedia_dota2/invisibility@2383943#Mechanics]

Multiple invisibility sources can be applied independently, and the unit remains invisible while at least one source is active. Some sources also make the unit phased. [corpus:liquipedia_dota2/invisibility@2383943#Mechanics]

### Appearance

Invisible units and their minimap icons are not rendered for the enemy team. [corpus:liquipedia_dota2/invisibility@2383943#Appearance]

To allies and enemies with True Sight over the unit, it appears transparent but remains visible. It can be selected and attacked normally and is not treated as invisible by abilities. Its minimap marker becomes a ring with a pointer rather than a full circle with a pointer. [corpus:liquipedia_dota2/invisibility@2383943#Appearance]

Shared vision exposes the unit’s silhouette while leaving its model invisible. The unit becomes selectable but still cannot be targeted by abilities or attacks. Invisible units cast no shadows for either enemies or allies. [corpus:liquipedia_dota2/invisibility@2383943#Appearance]

### Fade Delay

Fade delay is an initial delay before invisibility. During it, none of invisibility’s effects apply: the unit is fully visible, is not considered invisible, and can act normally. Attacking or casting an ability or item resets the delay. Once it elapses, the unit proceeds either to fade time or directly to invisibility. [corpus:liquipedia_dota2/invisibility@2383943#Fade_Delay]

Fade delay is usually used by abilities that continuously reapply invisibility over a duration, ensuring downtime after invisibility is broken. [corpus:liquipedia_dota2/invisibility@2383943#Fade_Delay]

| Ability with fade delay | Citation |
|---|---|
| Glimmer Cape – Glimmer | [corpus:liquipedia_dota2/invisibility@2383943#Fade_Delay] |
| Lycan Wolf – Invisibility | [corpus:liquipedia_dota2/invisibility@2383943#Fade_Delay] |
| Mirana – Moonlight Shadow | [corpus:liquipedia_dota2/invisibility@2383943#Fade_Delay] |
| Oracle – False Promise2a | [corpus:liquipedia_dota2/invisibility@2383943#Fade_Delay] |
| Sand King – Sand Storm | [corpus:liquipedia_dota2/invisibility@2383943#Fade_Delay] |
| Riki – Cloak and Dagger | [corpus:liquipedia_dota2/invisibility@2383943#Fade_Delay] |

1 Requires talent.  
2a Requires Aghanim’s Scepter.  
2b Requires Aghanim’s Shard. [corpus:liquipedia_dota2/invisibility@2383943#Fade_Delay]

### Fade Time

Fade time is a transition between visible and invisible states. The unit’s model gradually becomes transparent, but it is not yet considered invisible. [corpus:liquipedia_dota2/invisibility@2383943#Fade_Time]

Fade time always has a fixed duration and cannot be altered. Unlike fade delay, actions performed during fade time do not reset it or break the coming invisibility. When it expires, the unit becomes truly invisible, after which orders may break invisibility depending on the source. Fade time is usually used by abilities that apply invisibility once per cast. [corpus:liquipedia_dota2/invisibility@2383943#Fade_Time]

| Ability with fade time | Citation |
|---|---|
| Bounty Hunter – Shadow Walk | [corpus:liquipedia_dota2/invisibility@2383943#Fade_Time] |
| Bounty Hunter – Friendly Shadow | [corpus:liquipedia_dota2/invisibility@2383943#Fade_Time] |
| Clinkz – Skeleton Walk | [corpus:liquipedia_dota2/invisibility@2383943#Fade_Time] |
| Storm – Wind Walk | [corpus:liquipedia_dota2/invisibility@2383943#Fade_Time] |
| Shadow Amulet – Fade | [corpus:liquipedia_dota2/invisibility@2383943#Fade_Time] |
| Shadow Blade – Shadow Walk | [corpus:liquipedia_dota2/invisibility@2383943#Fade_Time] |
| Silver Edge – Shadow Walk | [corpus:liquipedia_dota2/invisibility@2383943#Fade_Time] |
| Weaver – Shukuchi | [corpus:liquipedia_dota2/invisibility@2383943#Fade_Time] |
| Windranger – Windrun2a | [corpus:liquipedia_dota2/invisibility@2383943#Fade_Time] |
| Runes – Invisibility | [corpus:liquipedia_dota2/invisibility@2383943#Fade_Time] |

### Attack Behavior

While invisible or fading, a unit never automatically attacks nearby enemies regardless of its auto-attack settings, including when revealed by True Sight and being attacked. Attack orders issued before invisibility become move orders; direct attack orders issued after the unit is already invisible are executed normally. [corpus:liquipedia_dota2/invisibility@2383943#Attack_Behavior]

This restriction does not apply during fade delay. Attacks proceed normally and reset the delay when executed. Attack orders given before fade delay are still carried out and may cancel the following invisibility depending on their timing. [corpus:liquipedia_dota2/invisibility@2383943#Attack_Behavior]

## Sources of Invisibility

| Source | Cast Time | Fade Duration | Phased Movement | Cast Interrupts Channeling | Using Abilities Breaks Invisibility | Attacking Breaks Invisibility | Instant Attack Breaks Invisibility | Dispellable by Basic Dispel | True Sight Immunity | Citation |
|---|---:|---|---|---|---|---|---|---|---|---|
| Friendly Shadow | 0 Instant Cast | 0.5 | Yes | No | Yes | Yes | Yes | No | No | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Shadow Walk | 0 Instant Cast | 1 \| 0.75 \| 0.5 \| 0.25 | Yes | No | Yes; No if: Friendly Shadow, Track [?] | Yes | Yes | No | No | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Skeleton Walk | 0 Instant Cast | 0.6 | Yes | No | Yes; No if: Strafe, Death Pact, Burning Army [?] | Yes | NoYes | No | No | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Decoy | 0 Instant Cast | 0 Instant Cast | No | Yes | Yes | Yes | NoYes | No | No | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Ghost Walk | 0 Instant Cast | 0 Instant Cast | Yes | No | Yes; No if: Quas, Wex, Exort, Invoke [?] | Yes | NoYes | No | No | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Raven’s Veil | 0.3 | 0.0 | No | Yes | Yes; No if: Switch Discipline [?] | Yes | NoYes | No | No | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Invisibility | 0 Passive | 2 Delay | No | No | Yes | Yes | ? | No | No | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Moonlight Shadow | 0.5 | 2.5 \| 2 \| 1.5 Delay | No | Yes | Yes | Yes | NoYes | No | No | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Burrow | 1.5 | 0.0 | Yes | Yes | No | No; Self- Disarmed | No | No | No | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Vendetta | 0 Instant Cast | 0.0 | Yes | No | Yes; No if: Spiked Carapace [?] | Yes; No if attacking: Rune | Yes | No | No | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Blur | 0.3 | 0.0 | No | Yes | No | Yes only if attacking: Roshan | Yes only if attacking: Roshan | No | Only for Blur | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Blur | 0 Instant Cast | 0.0 | No | Yes | No | Yes only if attacking: Roshan | Yes only if attacking: Roshan | No | Only for Blur | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Juxtapose | 0 Instant Cast | 0 Instant Cast | Yes | Yes | Yes | Yes | NoYes | No | No | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Cloak and Dagger | 0 Passive | 4 \| 3 \| 2; 2.75 \| 1.75 \| 0.75; Delay | No | No | No | Yes | NoYes | No | No | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Invisibility | 0 Instant Cast | 2 | No | Yes | Yes | Yes | NoYes | No | No | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Stored Rune (Invisibility} | 0.0 | 2 | No | Yes | Yes | Yes | NoYes | No | No | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Sand Storm | 0.0 | 0.7 Delay | No | Yes | Yes | Yes | NoYes | No | No | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Shadow Dance | 0 Instant Cast | 0.0 | No | Yes | No | No | No | No; Disabled While Invulnerable | Yes | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Depth Shroud | 0.1 | 0.0 | No | Yes | No | No | No | No; Disabled While Invulnerable | Yes | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Wind Walk | 0 Instant Cast | 0.6 | Yes | No | Yes | Yes | ? | No | No | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Meld | 0.0 | 0.0 | Yes | Yes | Yes; No if: Psionic Projection [?] | Yes | Yes | No | No | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Nature’s Guise [?] | 0 Instant Cast | 0.0 | Yes | Yes | No | Yes | Yes | No | No | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Silent as the Grave | 0 Instant Cast | 0.0 | Yes | No | Yes | Yes | Yes | No | No | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Shukuchi | 0 Instant Cast | 0.25 | Yes | No | Yes | Yes | NoYes | No | No | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Windrun | 0 Instant Cast | 0.2 | Yes | No | Yes | No | No | Yes | No | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Glimmer | 0 Instant Cast | 0.5 Delay | No | No | Yes | Yes | NoYes | Yes | No | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Fade | 0 Instant Cast | 1.5 | No | No | Yes | Yes | NoYes | Yes | No | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Shadow Walk | 0 Instant Cast | 0.3 | Yes | No | Yes | Yes | Yes; No if: Reciprocity, Echo Slash, Lunar Orbit | No | No | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Shadow Walk | 0 Instant Cast | 0.3 | Yes | No | Yes | Yes | Yes; No if: Reciprocity, Echo Slash, Lunar Orbit | No | No | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Disguise | 0.0 | 0.0 | No | Yes | No | Yes | NoYes | No | Yes | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |

The following abilities never break invisibility from any source:

| Ability | Citation |
|---|---|
| Bottle – Store Rune | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Invoker – Quas | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Invoker – Wex | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Invoker – Exort | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Invoker – Invoke | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Kez – Switch Discipline | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Largo – Amphibian Rhapsody | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Radiance – Burn | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |
| Runes – Activate | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_Invisibility] |

### Permanent Invisibility

| Property | Value | Citation |
|---|---|---|
| Invisibility | Ability | [corpus:liquipedia_dota2/invisibility@2383943#Permanent_Invisibility] |
| Type | Passive | [corpus:liquipedia_dota2/invisibility@2383943#Permanent_Invisibility] |
| Affects | Self | [corpus:liquipedia_dota2/invisibility@2383943#Permanent_Invisibility] |
| Effect | This unit is permanently invisible. | [corpus:liquipedia_dota2/invisibility@2383943#Permanent_Invisibility] |
| Fade Time | 0 | [corpus:liquipedia_dota2/invisibility@2383943#Permanent_Invisibility] |

A permanently invisible unit becomes invisible once summoned or created. Its ability and modifier are not displayed in-game. [corpus:liquipedia_dota2/invisibility@2383943#Details]

| Permanently invisible unit | Ability | Citation |
|---|---|---|
| Observer Ward | Planted Ward | [corpus:liquipedia_dota2/invisibility@2383943#Details] |
| Sentry Ward | Planted Ward | [corpus:liquipedia_dota2/invisibility@2383943#Details] |
| Techies | Proximity Mines4 | [corpus:liquipedia_dota2/invisibility@2383943#Details] |
| Templar Assassin | Trap | [corpus:liquipedia_dota2/invisibility@2383943#Details] |
| Treant’s Eyes | Eyes In The Forest | [corpus:liquipedia_dota2/invisibility@2383943#Details] |

4 Immune to True Sight. [corpus:liquipedia_dota2/invisibility@2383943#Details]

## Instant Attacks

Spell damage-based attacks do not break invisibility from any source, including Disguise and Blur. [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack]

| Spell damage-based attack | Citation |
|---|---|
| Luna – Moon Glaives | [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack] |
| Storm Spirit – Overload1 | [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack] |

Except for the abilities above, other instant attacks always break the following invisibility sources:

| Invisibility source | Citation |
|---|---|
| Bounty Hunter – Shadow Walk | [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack] |
| Bounty Hunter – Friendly Shadow | [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack] |
| Nyx Assassin – Vendetta | [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack] |
| Templar Assassin – Meld | [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack] |
| Treant Protector – Nature’s Guise | [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack] |
| Visage – Silent as the Grave | [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack] |
| Shadow Blade – Shadow Walk 4 | [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack] |
| Silver Edge – Shadow Walk 4 | [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack] |

4 Reciprocity, Echo Slash and Lunar Orbit do not break invisibility from this source. [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack]

Triggering an instant attack from the following sources does not break most invisibility sources. Casting the ability itself nevertheless removes invisibility from every source except Depth Shroud, Shadow Dance and Disguise. [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack]

| Instant-attack source | Citation |
|---|---|
| Clinkz – Burning Barrage | [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack] |
| Defiant Shell – Reciprocity | [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack] |
| Ember Spirit – Sleight of Fist | [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack] |
| Faceless Void – Time Lock | [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack] |
| Faceless Void – Time Walk2a | [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack] |
| Hoodwink – Acorn Shot (Ground-Targeted) | [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack] |
| Kez – Echo Slash | [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack] |
| Kez – Falcon Rush | [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack] |
| Kez – Talon Toss | [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack] |
| Lifestealer – Infest 2a | [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack] |
| Luna – Lunar Orbit | [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack] |
| Marci – Bodyguard | [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack] |
| Puck – Dream Coil 2a | [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack] |
| Riki – Tricks of the Trade | [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack] |
| Sand King – Stinger | [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack] |
| Sand King – Epicenter2a | [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack] |
| Sand King – Epicenter2a 2b | [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack] |
| Weaver – Geminate Attack | [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack] |
| Weaver – Shikuchi2b | [corpus:liquipedia_dota2/invisibility@2383943#Instant_Attack] |

## True Sight

An invisible Riki can be revealed by a Tower’s True Sight. True Sight is a negative status effect that nullifies invisibility for its observer. A unit affected by True Sight is no longer considered invisible to that observer until the effect is removed: it can be selected and targeted normally and is no longer treated as invisible by abilities. [corpus:liquipedia_dota2/invisibility@2383943#True_Sight]

True Sight differs from exposure. True Sight directly counters invisibility; exposure only reveals the unit’s silhouette and makes it selectable. An exposed unit remains untargetable, attack immune and treated as invisible by abilities. [corpus:liquipedia_dota2/invisibility@2383943#True_Sight]

### Sources of True Sight

See also: Exposure. [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight]

| Category | Source | Citation |
|---|---|---|
| Aura-based: Buildings | Ancient – True Sight | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Aura-based: Buildings | Fountain – True Sight | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Aura-based: Buildings | Towers – True Sight | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Aura-based: Hero Abilities | Clockwerk – Rocket Flare1 | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Aura-based: Hero Abilities | Hoodwink – Decoy 1 | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Aura-based: Hero Abilities | Hoodwink – Sharpshooter 1 | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Aura-based: Hero Abilities | Demonic Warrior (Book of the Dead) – True Sight | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Aura-based: Hero Abilities | Ringmaster – Spotlight | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Aura-based: Hero Abilities | Slardar – Slithereen Crush2b | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Aura-based: Hero Abilities | Void Spirit – Aether Remnant2b | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Aura-based: Hero Abilities | Zeus – Lightning Bolt | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Aura-based: Hero Abilities | Zeus – Lightning Bolt | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Aura-based: Hero Abilities | Zeus – Thundergod’s Wrath | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Aura-based: Items | Dust of Appearance – Reveal | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Aura-based: Items | Gem of True Sight – Reveal | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Aura-based: Items | Gem of True Sight – True Sight | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Aura-based: Items | Sentry Ward – True Sight | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Aura-based: Items | Ringmaster – Crystal Ball | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Other sources | Anti-Mage – Mana Void3 | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Other sources | Bloodseeker – Thirst | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Other sources | Bounty Hunter – Track | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Other sources | Drow Ranger – Gust | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Other sources | Earth Spirit – Enchant Remnant | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Other sources | Faceless Void – Time Zone | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Other sources | Legion Commander – Duel | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Other sources | Lion – Mana Drain | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Other sources | Mars – Spear of Mars | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Other sources | Nyx Assassin – Nyxth Sense | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Other sources | Primal Beast – Pulverize | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Other sources | Pudge – Dismember | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Other sources | Pugna – Life Drain | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Other sources | Shadow Shaman – Shackles | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Other sources | Slardar – Corrosive Haze | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Other sources | Sniper – Assassinate | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Other sources | Tidehunter – Dead in the Water | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Root | Ancient Prowler Shaman – Petrify | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Root | Crystal Maiden – Freezing Field2a | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Root | Crystal Maiden – Frostbite | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Root | Crystal Maiden – Crystal Clone | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Root | Dark Willow – Bramble Maze | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Root | Ember Spirit – Searing Chains4 | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Root | Hill Troll – Ensnare | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Root | Lone Druid – Entangle | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Root | Spirit Bear – Entangling Claws | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Root | Medusa – Gorgon’s Grasp | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Root | Meepo – Earthbind | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Root | Naga Siren – Ensnare | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Root | Nature’s Prophet – Wrath of Nature2a 4 | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Root | Oracle – Fortune’s End | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Root | Treant Protector – Nature’s Guise2b | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Root | Treant Protector – Nature’s Guise4 | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Root | Troll Warlord – Berserker’s Rage | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Root | Underlord – Pit of Malice | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Root | Underlord – Fiend’s Gate2a | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Root | Gleipnir – Eternal Chains | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Root | Rod of Atos – Cripple | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Taunt | Winter Wyvern – Winter’s Curse | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Hypnotise | Lich – Sinister Gaze | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Hypnotise | Ringmaster – Wheel of Wonder | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |
| Hypnotise | Void Spirit – Aether Remnant | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight] |

1 Requires a talent.  
2a Requires Aghanim’s Scepter.  
2b Requires Aghanim’s Shard.  
3 Requires selecting the corresponding facet.  
4 Cannot apply the effect if the unit is already invisible unless it is affected by True Sight. [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight]

### Sources Affecting Wards

| Category | Source | Citation |
|---|---|---|
| Buildings | Ancient – True Sight | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight_affecting_Wards] |
| Buildings | Fountain – True Sight | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight_affecting_Wards] |
| Buildings | Towers – True Sight | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight_affecting_Wards] |
| Items | Gem of True Sight – Reveal | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight_affecting_Wards] |
| Items | Gem of True Sight – True Sight | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight_affecting_Wards] |
| Items | Sentry Ward – True Sight | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight_affecting_Wards] |
| Other Abilities | Clockwerk – Rocket Flare 1 | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight_affecting_Wards] |
| Other Abilities | Faceless Void – Chronosphere | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight_affecting_Wards] |
| Other Abilities | Zeus – Lightning Bolt | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight_affecting_Wards] |
| Other Abilities | Zeus – Lightning Bolt | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight_affecting_Wards] |
| Other Abilities | Zeus – Thundergod’s Wrath | [corpus:liquipedia_dota2/invisibility@2383943#Sources_of_True_Sight_affecting_Wards] |

### True Sight Immunity

True Sight immunity prevents True Sight from revealing affected units. [corpus:liquipedia_dota2/invisibility@2383943#True_Sight_Immunity]

| Category | Source | Citation |
|---|---|---|
| Disguise-based Sources | Smoke of Deceit – Disguise | [corpus:liquipedia_dota2/invisibility@2383943#True_Sight_Immunity] |
| Other Sources | Slark – Depth Shroud | [corpus:liquipedia_dota2/invisibility@2383943#True_Sight_Immunity] |
| Other Sources | Slark – Shadow Dance | [corpus:liquipedia_dota2/invisibility@2383943#True_Sight_Immunity] |
| Other Sources | Phantom Assassin – Blur | [corpus:liquipedia_dota2/invisibility@2383943#True_Sight_Immunity] |
| Other Sources | Techies – Proximity Mines | [corpus:liquipedia_dota2/invisibility@2383943#True_Sight_Immunity] |

Invisibility from Blur cannot be revealed by True Sight. [corpus:liquipedia_dota2/invisibility@2383943#True_Sight_Immunity]

### Piercing True Sight Immunity

See also: Vision#Exposing True Sight Immune Units. [corpus:liquipedia_dota2/invisibility@2383943#Piercing_True_Sight_Immunity]

| Source | Citation |
|---|---|
| Spectre – Haunt | [corpus:liquipedia_dota2/invisibility@2383943#Piercing_True_Sight_Immunity] |
| Terrorblade – Reflection | [corpus:liquipedia_dota2/invisibility@2383943#Piercing_True_Sight_Immunity] |
| Warlock – Eldritch Summoning | [corpus:liquipedia_dota2/invisibility@2383943#Piercing_True_Sight_Immunity] |
| Lich – Sinister Gaze 2a | [corpus:liquipedia_dota2/invisibility@2383943#Piercing_True_Sight_Immunity] |
| Lion – Sinister Gaze 1 | [corpus:liquipedia_dota2/invisibility@2383943#Piercing_True_Sight_Immunity] |
| Zeus – Lightning Bolt | [corpus:liquipedia_dota2/invisibility@2383943#Piercing_True_Sight_Immunity] |
| Zeus – Thundergod’s Wrath | [corpus:liquipedia_dota2/invisibility@2383943#Piercing_True_Sight_Immunity] |

## Interactions with Other Spells

See also: Disjointing with invisibility and Disjointable projectiles. [corpus:liquipedia_dota2/invisibility@2383943#Invisibility_interactions_with_other_spells]

### Targeting Invisible Units

Most area spells affect invisible units, with some exceptions. Single-target spells cannot target invisible units without True Sight. Shared vision makes the model visible but does not allow single-target spells to target it. [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units]

Spells that choose specific or random targets on cast interact inconsistently with invisibility. These include bouncing spells such as Arc Lightning and multi-target spells such as Poison Touch and Heat-Seeking Missile. The following do not target invisible units: [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units]

| Spell | Citation |
|---|---|
| Abaddon – Aphotic Shield | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Batrider – Flaming Lasso1 | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Bristleback – Viscous Nasal Goo1 | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Clinkz – Searing Arrows2 | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Clockwerk – Battery Assault | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Dark Willow – Bedlam | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Dazzle – Poison Touch | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Death Prophet – Exorcism | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Drow Ranger – Marksmanship1 | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Ember Spirit – Searing Chains | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Ember Spirit – Sleight of Fist | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Grimstroke – Soulbind | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Gyrocopter – Rocket Barrage | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Gyrocopter – Homing Missile3 | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Gyrocopter – Flak Cannon | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Gyrocopter – Side Gunner1 | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Harpy Stormcrafter – Chain Lightning | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Juggernaut – Omnislash | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Leshrac – Lightning Storm4 | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Lich – Chain Frost | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Lion – Mana Drain2 | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Luna – Moon Glaives | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Luna – Eclipse | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Maelstrom – Chain Lightning | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Medusa – Split Shot | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Medusa – Mystic Snake | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Mirana – Starstorm | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Mjollnir – Chain Lightning | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Morphling – Adaptive Strike2 | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Nature’s Prophet – Wrath of Nature | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Ogre Magi – Multicast Ignite | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Phantom Assassin – Stifling Dagger1 | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Phantom Lancer – Spirit Lance2 | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Razor – Eye of the Storm | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Riki – Tricks of the Trade | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Rubick – Fade Bolt | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Shadow Shaman – Ether Shock | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Shadow Shaman – Mass Serpent Ward1 | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Skywrath Mage – Arcane Bolt1 2 | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Skywrath Mage – Concussive Shot5 | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Skywrath Mage – Ancient Seal1 | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Skywrath Mage – Mystic Flare6 | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Sniper – Assassinate1 | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Spirit Breaker – Charge of Darkness3 | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Storm Spirit – Electric Vortex1 | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Terrorblade – Reflection | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Tinker – Laser1 | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Tinker – Heat-Seeking Missile | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Tiny – Toss7 | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Treant Protector – Overgrowth | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Undying – Soul Rip | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Undying – Tombstone | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Visage – Soul Assumption2 | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Warlock – Fatal Bonds | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Weaver – The Swarm | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Witch Doctor – Paralyzing Cask | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Witch Doctor – Death Ward1 | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Zeus – Arc Lightning | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |

1 Requires Aghanim’s Scepter. When upgraded, these spells can target secondary units but ignore invisible ones.  
2 Requires a talent. When upgraded, these spells can target secondary units but ignore invisible ones.  
3 These spells choose a new target if their current target dies. They do not choose invisible targets.  
4 Soulbind does not bind the target to invisible allies, but an existing link remains if a bound unit turns invisible.  
5 Lightning Storm also includes the single strikes from Aghanim’s Scepter-upgraded Pulse Nova.  
6 Concussive Shot does not seek invisible units; its area effect hits nearby invisible units.  
7 The secondary Mystic Flare is not created on invisible enemies; its area damage affects invisible units.  
8 Toss does not select nearby invisible enemy units to toss; its area damage hits invisible enemies. [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units]

The following spells have mixed interactions:

| Spell | Interaction | Citation |
|---|---|---|
| Mjollnir – Static Charge | Always hits the triggering unit even when invisible, but does not hit other nearby invisible enemies. | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Queen of Pain – Shadow Strike | With the area talent, Shadow Strike targets invisible enemies within the area, but its projectiles are instantly disjointed. | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |
| Zeus – Thundergod’s Wrath | Targets invisible enemies, but its damage and lightning require vision. Only vision and True Sight are applied around invisible enemies. | [corpus:liquipedia_dota2/invisibility@2383943#Targeting_invisible_units] |

### Turning Invisible After Cast

For most spells, invisibility does not interrupt an effect that has already begun; it continues normally. Exceptions exist. [corpus:liquipedia_dota2/invisibility@2383943#Turning_invisible_after_cast]

Every invisibility source disjoints projectiles. Even a split-second loss of vision from invisibility is enough to disjoint a projectile, including when vision is regained before impact. This does not occur when the observer has True Sight over the unit. [corpus:liquipedia_dota2/invisibility@2383943#Turning_invisible_after_cast]

| Spell | Interaction after invisibility | Citation |
|---|---|---|
| Axe – Berserker’s Call | When the caster turns invisible, taunted enemies can receive one order before the effect expires. After completing that order, they freeze in place until the effect expires. | [corpus:liquipedia_dota2/invisibility@2383943#Turning_invisible_after_cast] |
| Ember Spirit – Sleight of Fist | An already marked unit that turns invisible before being slashed is completely skipped if it remains invisible on its turn. | [corpus:liquipedia_dota2/invisibility@2383943#Turning_invisible_after_cast] |
| Grimstroke – Phantom’s Embrace | The phantom instantly dies when its target turns invisible. | [corpus:liquipedia_dota2/invisibility@2383943#Turning_invisible_after_cast] |
| Huskar – Life Break | When the caster turns invisible, taunted enemies can receive one order before the effect expires. After completing that order, they freeze in place until the effect expires. | [corpus:liquipedia_dota2/invisibility@2383943#Turning_invisible_after_cast] |
| Medusa – Mystic Snake | If the current target is invisible on impact, the snake does not affect it and does not count the jump. | [corpus:liquipedia_dota2/invisibility@2383943#Turning_invisible_after_cast] |
| Undying – Tombstone | Zombies instantly die when their target turns invisible. | [corpus:liquipedia_dota2/invisibility@2383943#Turning_invisible_after_cast] |
| Weaver – The Swarm | A beetle instantly dies when its target turns invisible. | [corpus:liquipedia_dota2/invisibility@2383943#Turning_invisible_after_cast] |

## Version History

| Version | Date | Description | Citation |
|---|---|---|---|
| 7.07 | 2017-10-31 | Broodmother no longer gains invisibility in her Spin Web. | [corpus:liquipedia_dota2/invisibility@2383943#Version_History] |

## Patch History

| Date | Description | Citation |
|---|---|---|
| 14 Mar 2018 | Fixed invisibility being unable to disjoint attack projectiles. | [corpus:liquipedia_dota2/invisibility@2383943#Patch_History] |
| 02 Jul 2015 | Sleight of Fist, Omnislash and Thundergod’s Wrath now damage invisible units that have been revealed. | [corpus:liquipedia_dota2/invisibility@2383943#Patch_History] |
| 18 Jun 2015 | Fixed various bugs with True Sight. | [corpus:liquipedia_dota2/invisibility@2383943#Patch_History] |
| 14 Jun 2013 | Fixed True Sight being unable to be applied to sleeping and/or invulnerable units. | [corpus:liquipedia_dota2/invisibility@2383943#Patch_History] |
| 01 Jul 2011 | Fixed projectile dodging to occur when invisibility fade time finishes. Fixed projectile dodging from invisibility to occur only when the unit successfully becomes invisible, so it does not dodge when the enemy team has True Sight over it. Made becoming invisible inherently perform a projectile dodge. Fixed Standard auto-attack allowing attacks while fading out, which unintentionally broke invisibility. True Sight sources are now disabled by Hex sources and Doom. | [corpus:liquipedia_dota2/invisibility@2383943#Patch_History] |
| 05 May 2011 | Abilities that provide invisibility can now dodge incoming ability projectiles. | [corpus:liquipedia_dota2/invisibility@2383943#Patch_History] |