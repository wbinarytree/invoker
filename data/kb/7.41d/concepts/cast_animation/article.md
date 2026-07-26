---
title: Cast Animation
kind: concept
patch: 7.41d
card:
  entity: cast_animation
  sentences:
  - text: A cast animation is each unit ability’s unique visual sequence, beginning
      when a required target is selected or its hotkey is pressed and encompassing
      the cast point and any cast backswing that mechanically delay actions.
    marks:
    - corpus:liquipedia_dota2/cast_animation@2383517
    - corpus:liquipedia_dota2/cast_animation@2383517#Definition
  - text: The cast point is the period the caster must complete before the ability
      applies its effects, and the animation begins immediately to indicate it.
    marks:
    - corpus:liquipedia_dota2/cast_animation@2383517#Definition
  - text: Interrupting before the cast point cancels the effects without starting
      cooldown or consuming mana; disables, the caster’s own action, Stop (S), and
      Halt (H) can cause this.
    marks:
    - corpus:liquipedia_dota2/cast_animation@2383517#Definition
  - text: A No Target ability with an instant cast point applies its effects immediately
      when its hotkey is pressed.
    marks:
    - corpus:liquipedia_dota2/cast_animation@2383517#Cast_Point
  - text: Targetable abilities apply their effects when the target is selected and
      interrupt channeling even with an instant cast point.
    marks:
    - corpus:liquipedia_dota2/cast_animation@2383517#Cast_Point
  - text: Most items and every toggleable ability have neither a cast point nor a
      backswing.
    marks:
    - corpus:liquipedia_dota2/cast_animation@2383517#Instant_Cast
  - text: A 0 cast point can retain its backswing, whereas the Immediate Flag removes
      both and activates on the same server tick when possible.
    marks:
    - corpus:liquipedia_dota2/cast_animation@2383517#Instant_Cast
  - text: Force takes 0.067 seconds after Shadow Walk because its non-instant cast
      time equals one server tick and another tick separates the commands.
    marks:
    - corpus:liquipedia_dota2/cast_animation@2383517#Instant_Cast
  - text: Cast backswing follows the cast point, prevents attacks and other abilities
      while the caster stands still, and does not affect the completed ability.
    marks:
    - corpus:liquipedia_dota2/cast_animation@2383517#Cast_Backswing
  - text: Stop (S), a Move order, or another ability cancels backswing, but a ⇧ Shift-queue
      waits until backswing ends.
    marks:
    - corpus:liquipedia_dota2/cast_animation@2383517#Cast_Backswing
  - text: Doom casting Chain Lightning uses its 0.3-second cast point and a 0.87-second
      backswing to fill the slot’s 1.17-second total cast animation.
    marks:
    - corpus:liquipedia_dota2/cast_animation@2383517#Cast_Backswing
  - text: Channeling begins after the cast point; interruption before then prevents
      channeling, cooldown, and mana consumption.
    marks:
    - corpus:liquipedia_dota2/cast_animation@2383517#Channeling
---

# Cast Animation

## Overview

Every unit has a unique cast animation for each ability. It begins when a required target is chosen or, for an ability without a target, when its hotkey is pressed. Animation length varies by ability; animations are created for the ability usually occupying the slot to which the animation is bound. Although visual, cast animations mechanically affect gameplay. [corpus:liquipedia_dota2/cast_animation@2383517]

## Definition

Every ability has a specific period through which its caster must progress before successfully applying its effects, commonly called the **cast point** or **cast time**. The cast point is not directly determined by the visual animation, but the animation begins immediately and therefore indicates the cast point. [corpus:liquipedia_dota2/cast_animation@2383517#Definition]

If a disable or the unit’s own action interrupts the cast before the cast point, the cast is canceled: its effects are not applied, it does not enter cooldown, and it consumes no mana. A player can also cancel it with a **Stop (S)** or **Halt (H)** command. Interrupting during cast time also ends the visual animation. [corpus:liquipedia_dota2/cast_animation@2383517#Definition]

In almost every case, the animation continues beyond the cast point. During this remaining animation, most abilities leave the unit standing still and unable to act unless the animation is canceled. This period is the **cast backswing**. [corpus:liquipedia_dota2/cast_animation@2383517#Definition]

## Cast Point

A No Target ability with an instant cast point applies its effects immediately when its hotkey is pressed. Certain No Target abilities may be cast without interrupting channeling. [corpus:liquipedia_dota2/cast_animation@2383517#Cast_Point]

For a targetable ability, its effects are applied as soon as its target is selected. Any ability requiring a unit, ground, or area target interrupts channeling even when its cast point is instant. [corpus:liquipedia_dota2/cast_animation@2383517#Cast_Point]

### Instant Cast

Most items and every toggleable ability have neither a cast point nor a backswing. They have the highest cast-order priority and can be used between certain chain-disables, such as **Sacred Arrow into Nightmare**, or between a disable that uses invulnerability and a periodic area disable, such as **Black Hole**. They can also be cast after an Ancient has fallen, during the scoreboard phase. This applies to most toggled items, although abilities such as **Switch Attribute** are not considered toggles. [corpus:liquipedia_dota2/cast_animation@2383517#Instant_Cast]

| Type | Aspect or definition | Example |
|---|---|---|
| Zero Cast Point | The cast point is set to 0. Any cast backswing is still used. | Homing Missile |
| Immediate Flag | Has neither cast point nor cast backswing and activates immediately on the same server tick, if possible. | Borrowed Time |
| Toggleable Abilities | A toggleable ability has neither cast point nor cast backswing. | Pulse Nova |
| Ignore Channel Flag | Does not interrupt channeling when cast; it may or may not have a cast point or cast backswing. | — |

[corpus:liquipedia_dota2/cast_animation@2383517#Instant_Cast]

Instant cast time differs from 0 cast point. If Marci with **Black King Bar** is simultaneously affected by **Disruption** and **Chronosphere**, she can cast **Avatar**, but not **Force**, after Disruption ends while Chronosphere remains active. Avatar has an instant cast time; Force does not. [corpus:liquipedia_dota2/cast_animation@2383517#Instant_Cast]

If Marci instead has **Shadow Blade** and commands **Shadow Walk**, then **Force**, Force is cast after **0.067 seconds**. Because Force is not instant cast, its cast time equals one server tick; another server tick occurs between the two different consecutive commands. If she commands Force and then Shadow Walk, Shadow Walk is cast instantly once Force is cast. [corpus:liquipedia_dota2/cast_animation@2383517#Instant_Cast]

### Instant Cast Sources

| Category | Unit ability |
|---|---|
| Instant Cast Unit Abilities | Abaddon – Borrowed Time |
| Instant Cast Unit Abilities | Alchemist – Unstable Concoction |
| Instant Cast Unit Abilities | Anti-Mage – Counterspell |
| Instant Cast Unit Abilities | Batrider – Firefly |
| Instant Cast Unit Abilities | Bloodseeker – Bloodrage |
| Instant Cast Unit Abilities | Spin Web – Destroy Spin Web |
| Instant Cast Unit Abilities | Bristleback – Quill Spray |
| Instant Cast Unit Abilities | Clockwerk – Battery Assault |
| Instant Cast Unit Abilities | Clockwerk – Overclocking |
| Instant Cast Unit Abilities | Crystal Maiden – Crystal Clone |
| Instant Cast Unit Abilities | Dark Willow – Bedlam |
| Instant Cast Unit Abilities | Dark Willow – Shadow Realm |
| Instant Cast Unit Abilities | Enchantress – Sproink |
| Instant Cast Unit Abilities | Gyrocopter – Rocket Barrage |
| Instant Cast Unit Abilities | Gyrocopter – Flak Cannon |
| Instant Cast Unit Abilities | Hoodwink – Scurry |
| Instant Cast Unit Abilities | Invoker – Quas |
| Instant Cast Unit Abilities | Invoker – Wex |
| Instant Cast Unit Abilities | Invoker – Exort |
| Instant Cast Unit Abilities | Invoker – Invoke |
| Instant Cast Unit Abilities | Io – Spirits |
| Instant Cast Unit Abilities | Io – Overcharge |
| Instant Cast Unit Abilities | Kez – Falcon Rush |
| Instant Cast Unit Abilities | Kez – Shodo Sai |
| Instant Cast Unit Abilities | Leshrac – Nihilism |
| Instant Cast Unit Abilities | Lina – Flame Cloak |
| Instant Cast Unit Abilities | Meepo – MegaMeepo |
| Instant Cast Unit Abilities | Necrophos – Ghost Shroud |
| Instant Cast Unit Abilities | Night Stalker – Crippling Fear |
| Instant Cast Unit Abilities | Nyx Assassin – Spiked Carapace |
| Instant Cast Unit Abilities | Pangolier – Shield Crash |
| Instant Cast Unit Abilities | Phoenix – Fire Spirits |
| Instant Cast Unit Abilities | Primal Beast – Trample |
| Instant Cast Unit Abilities | Primal Beast – Uproar |
| Instant Cast Unit Abilities | Pudge – Flesh Heap |
| Instant Cast Unit Abilities | Razor – Plasma Field |
| Instant Cast Unit Abilities | Razor – Eye of the Storm |
| Instant Cast Unit Abilities | Shadow Fiend – Feast of Souls |
| Instant Cast Unit Abilities | Slardar – Guardian Sprint |
| Instant Cast Unit Abilities | Slark – Dark Pact |
| Instant Cast Unit Abilities | Slark – Shadow Dance |
| Instant Cast Unit Abilities | Sniper – Take Aim |
| Instant Cast Unit Abilities | Spirit Breaker – Bulldoze |
| Instant Cast Unit Abilities | Storm Spirit – Overload2a |
| Instant Cast Unit Abilities | Sven – Warcry |
| Instant Cast Unit Abilities | Tombstone – Grab Ally |
| Instant Cast Unit Abilities | Templar Assassin – Refraction |
| Instant Cast Unit Abilities | Psionic Trap – Trap |
| Instant Cast Unit Abilities | Timbersaw – Whirling Death |
| Instant Cast Unit Abilities | Timbersaw – Flamethrower |
| Instant Cast Unit Abilities | Troll Warlord – Whirling Axes (Melee) |
| Instant Cast Unit Abilities | Troll Warlord – Battle Trance |
| Instant Cast Unit Abilities | Tusk – Tag Team |
| Instant Cast Unit Abilities | Ursa – Earthshock |
| Instant Cast Unit Abilities | Ursa – Enrage |
| Instant Cast Unit Abilities | Visage – Stone Form |
| Instant Cast Unit Abilities | Visage – Summon Familiars |
| Instant Cast Unit Abilities | Windranger – Windrun |
| Instant Cast Unit Abilities | Winter Wyvern – Arctic Burn |
| Instant Cast Unit Abilities | Zeus – Heavenly Jump |
| Transform | Morphling – Morph Replicate |
| Transform | Terrorblade – Metamorphosis |
| Transform | Terrorblade – Terror Wave |
| Transform | Undying – Flesh Golem |
| Debuff Immunity | Juggernaut – Blade Fury |
| Debuff Immunity | Lifestealer – Rage |
| Invisibility | Bounty Hunter – Friendly Shadow |
| Invisibility | Bounty Hunter – Shadow Walk |
| Invisibility | Clinkz – Skeleton Walk |
| Invisibility | Invoker – Ghost Walk6 |
| Invisibility | Nyx Assassin – Vendetta6 |
| Invisibility | Treant Protector – Nature's Guise |
| Invisibility | Visage – Silent as the Grave6 |
| Invisibility | Weaver – Shukuchi6 |
| Sub-Ability | Astral Spirit – Return Astral Spirit |
| Sub-Ability | Bane – Nightmare End |
| Sub-Ability | Crystal Maiden – Stop Freezing Field |
| Sub-Ability | Earth – Primal Split Cancel |
| Sub-Ability | Elder Titan – Return Astral Spirit |
| Sub-Ability | Elder Titan – Move Astral Spirit |
| Sub-Ability | Fire – Primal Split Cancel |
| Sub-Ability | Hoodwink – End Sharpshooter |
| Sub-Ability | Io – Spirits In |
| Sub-Ability | Io – Spirits Out |
| Sub-Ability | Kez – Cancel |
| Sub-Ability | Lifestealer – Consume |
| Sub-Ability | Monkey King – Spring Early |
| Sub-Ability | Morphling – Morph Replicate |
| Sub-Ability | Pangolier – Stop Rolling |
| Sub-Ability | Phoenix – Stop Icarus Dive |
| Sub-Ability | Phoenix – Stop Sun Ray |
| Sub-Ability | Phoenix – Toggle Movement |
| Sub-Ability | Primal Beast – Begin Onslaught |
| Sub-Ability | Ringmaster – Crack |
| Sub-Ability | Rubick – Telekinesis Land |
| Sub-Ability | Storm – Primal Split Cancel |
| Sub-Ability | Techies – Detonate Tazer |
| Sub-Ability | Templar Assassin – Trap |
| Sub-Ability | Timbersaw – Return Chakram |
| Sub-Ability | Tusk – Launch Snowball |
| Toggle | Clockwerk – Jetpack |
| Toggle | Io – Spirits In2a |
| Toggle | Io – Spirits Out2a |
| Toggle | Night Stalker – Crippling Fear2a |
| Toggle | Leshrac – Pulse Nova |
| Toggle | Mars – Bulwark |
| Toggle | Medusa – Split Shot |
| Toggle | Morphling – Attribute Shift |
| Toggle | Pudge – Rot |
| Toggle | Winter Wyvern – Arctic Burn2a |
| Toggle | Witch Doctor – Voodoo Restoration |
| Toggle | Harpy Scout – Take Off |
| Toggle | Brewmaster – Drunken Brawler |
| Toggle | Kez – Switch Discipline |
| Toggle | Largo – Amphibian Rhapsody |
| Toggle | Muerta – Gunslinger |
| Toggle | Phantom Lancer – Phantom Rush |
| Toggle | Troll Warlord – Battle Stance |

**Requirements:** `1` requires a talent; `2a` requires Aghanim’s Scepter; `2b` requires Aghanim’s Shard. [corpus:liquipedia_dota2/cast_animation@2383517#Instant_Cast_Sources]

### Instant Cast Items

The following item abilities have an instant cast point and do not interrupt channeling. [corpus:liquipedia_dota2/cast_animation@2383517#Instant_Cast_Items]

| Category | Item ability |
|---|---|
| Instant Cast Item Abilities | Blade Mail – Damage Return |
| Instant Cast Item Abilities | Boots of Bearing – Endurance |
| Instant Cast Item Abilities | Mask of Madness – Berserk |
| Instant Cast Item Abilities | Phase Boots – Phase |
| Instant Cast Item Abilities | Shiva's Guard – Arctic Blast |
| Instant Cast Item Abilities | Veil of Discord – Magic Weakness |
| Invisibility | Glimmer Cape – Glimmer |
| Invisibility | Shadow Amulet – Fade |
| Invisibility | Shadow Blade – Shadow Walk |
| Invisibility | Silver Edge – Shadow Walk |
| Toggle | Armlet of Mordiggian – Unholy Strength |
| Toggle | Divine Rapier – Transmute |
| Toggle | Radiance – Burn |

[corpus:liquipedia_dota2/cast_animation@2383517#Instant_Cast_Items]

The following item abilities have an instant cast point and interrupt channeling. [corpus:liquipedia_dota2/cast_animation@2383517#Instant_Cast_Items]

| Item ability |
|---|
| Arcane Boots – Replenish |
| Black King Bar – Avatar |
| Block of Cheese – Scrumptious |
| Bloodstone – Bloodpact |
| Book of the Dead – Greater Demonic Summoning |
| Cheese – Fondue |
| Clarity – Replenish |
| Crimson Guard – Guard |
| Dust of Appearance – Reveal |
| Enchanted Mango – Eat Mango |
| Faerie Fire – Imbue |
| Ghost Scepter – Ghost Form |
| Great Healing Lotus – Eat Lotus |
| Greater Healing Lotus – Eat Lotus |
| Guardian Greaves – Mend |
| Healing Lotus – Eat Lotus |
| Healing Salve – Salve |
| Holy Locket – Energy Charge |
| Magic Stick – Energy Charge |
| Magic Wand – Energy Charge |
| Mekansm – Restore |
| Moon Shard – Consume |
| Pavise – Protect |
| Pipe of Insight – Barrier |
| Power Treads – Switch Attribute |
| Refresher Shard – Reset Cooldowns |
| Runes – Amplify Damage |
| Runes – Arcane |
| Runes – Bounty |
| Runes – Haste |
| Runes – Illusion |
| Runes – Invisibility |
| Runes – Regeneration |
| Runes – Shield |
| Runes – Water |
| Satanic – Unholy Rage |
| Solar Crest – Shine |
| Soul Ring – Sacrifice |

[corpus:liquipedia_dota2/cast_animation@2383517#Instant_Cast_Items]

Most items with active abilities have a **0 cast point** and no cast backswing. The exception category is **Item Abilities with Cast Point Greater than 0**. [corpus:liquipedia_dota2/cast_animation@2383517#Instant_Cast_Items]

### Conditional Instant Cast

Certain abilities can become instant cast conditionally; their respective notes contain further information. [corpus:liquipedia_dota2/cast_animation@2383517#Conditional_Instant_Cast]

| Conditional instant cast ability |
|---|
| Bane – Fiend's Grip |
| Earth Spirit – Boulder Smash |
| Ember Spirit – Fire Remnant |
| Juggernaut – Healing Ward |
| Lich – Frost Blast |
| Lich – Frost Shield |
| Lich – Ice Spire |
| Lich – Chain Frost |
| Pugna – Nether Blast |
| Pugna – Decrepify |
| Pugna – Nether Ward |
| Riki – Smoke Screen |
| Troll Warlord – Whirling Axes (Ranged) |
| Troll Warlord – Whirling Axes (Melee) |

[corpus:liquipedia_dota2/cast_animation@2383517#Conditional_Instant_Cast]

### Vector Targeting

For Vector Targeting abilities, the cast point begins upon pressing the hotkey and selecting the direction. [corpus:liquipedia_dota2/cast_animation@2383517#Vector_Targeting]

| Vector Targeting ability |
|---|
| Bane – Nightmare3 |
| Broodmother – Spinner's Snare |
| Clinkz – Burning Army |
| Dark Seer – Wall of Replica |
| Disruptor – Kinetic Fence3 |
| Grimstroke – Stroke of Fate |
| Gyrocopter – Call Down |
| Marci – Rebound |
| Muerta – Dead Shot |
| Pangolier – Swashbuckle |
| Puck – Illusory Orb3 |
| Tusk – Walrus Kick2a |
| Void – Astral Pull |
| Void Spirit – Aether Remnant |
| Wildwing Ripper – Hurricane |
| Windranger – Gale Force |

**Requirements:** `1` requires a talent; `2a` requires Aghanim’s Scepter; `2b` requires Aghanim’s Shard; `3` requires selecting the corresponding facet. [corpus:liquipedia_dota2/cast_animation@2383517#Vector_Targeting]

### Modifying Cast Point

There are currently no sources that modify cast point. [corpus:liquipedia_dota2/cast_animation@2383517#Modifying_Cast_Point]

## Cast Backswing

Cast backswing is the portion of the animation after the cast point. During it, the caster stands still and cannot attack or use other abilities until the remaining animation finishes. It has no effect on the ability already cast and is purely cosmetic. [corpus:liquipedia_dota2/cast_animation@2383517#Cast_Backswing]

A player can cancel the backswing with **Stop (S)**, a Move order, or another ability cast. A **⇧ Shift-queue** does not cancel it; the next queued command executes after the backswing ends. [corpus:liquipedia_dota2/cast_animation@2383517#Cast_Backswing]

Backswing can be bound to the unit or the ability slot, and abilities with equal total animation times need not have equal backswings. A **0.3-second** cast point within a **1-second** animation produces a **0.7-second** backswing, whereas a **0.6-second** cast point within an animation of the same length produces a **0.4-second** backswing. Even a short backswing is difficult but possible to cancel. This affects abilities acquired through **Death Pact, Devour, Spell Steal, Morph**, or **Ability Draft**. [corpus:liquipedia_dota2/cast_animation@2383517#Cast_Backswing]

Doom uses the same **1.17-second** cast animation for **Devoured Ability 1** and **Devoured Ability 2**, irrespective of the brevity of the Devoured unit’s animation. The acquired ability’s backswing is the difference between its original cast point and that slot’s total cast animation: [corpus:liquipedia_dota2/cast_animation@2383517#Cast_Backswing]

```text
1.17 - AbilityCastPoint
```

If Doom casts **Chain Lightning**, whose cast point is **0.3-second**, its backswing takes **0.87 seconds** to conform to the slot’s **1.17** total cast animation, even though Harpy Stormcrafter has a different backswing when casting it. Rubick similarly conforms **Stolen Spell 1** and **Stolen Spell 2** to a **1.07-second** total cast animation based on the ability slot. [corpus:liquipedia_dota2/cast_animation@2383517#Cast_Backswing]

### Modifying Cast Backswing

Acquired neutral abilities use their original cast point. Their backswing is: [corpus:liquipedia_dota2/cast_animation@2383517#Modifying_Cast_Backswing]

```text
SlotCastAnimationTime - OriginalCastPoint, 0 when OriginalCastPoint ≥ SlotCastAnimationTime.
```

Certain cosmetic items also modify ability backswings by using different animations; these are mostly listed in the respective ability notes. [corpus:liquipedia_dota2/cast_animation@2383517#Modifying_Cast_Backswing]

| Backswing-modifying ability | Slot Cast Animation Time |
|---|---:|
| Doom - Devoured Ability | 1.17 |
| Rubick - Stolen Spell | 1.37 |

[corpus:liquipedia_dota2/cast_animation@2383517#Modifying_Cast_Backswing]

### Instant Cast Backswing

Besides toggleable abilities and abilities with instant cast time, an ability can have an instant cast backswing under the following conditions. [corpus:liquipedia_dota2/cast_animation@2383517#Instant_Cast_Backswing]

| Type | Aspect or definition | Examples |
|---|---|---|
| Ignore Backswing Flag | Ignores the cast backswing and immediately stops the ability animation once the cast point is reached. | Magnetic Field |
| Channeling | Begins channel time after reaching the cast point. | Upheaval |
| Forced Orders | Another ability component, such as transformation or channeling, immediately interrupts the backswing. | Pierce the Veil; Burrow |
| Extended Cast Point | In rare cases, the animation is too long to have any backswing animation. | Teleportation |
| Set Cast Backswing | The ability has no cast-backswing value; this includes all item abilities. | Release Illuminate |

[corpus:liquipedia_dota2/cast_animation@2383517#Instant_Cast_Backswing]

### Channeling

Channeling abilities begin their channel time after reaching their cast point. If interrupted before that point, the ability does not begin channeling, enter cooldown, or consume mana. Channeled abilities might not have cast backswings because the channel must follow the cast point where the backswing would otherwise occur. [corpus:liquipedia_dota2/cast_animation@2383517#Channeling]

## Cast Speed Manipulation

| Change | Source | Property |
|---|---|---|
| Cast Speed Decrease | Faceless Void - Time Zone | Cast Animation Factor:; this is an old ability. |
| Cast Speed Decrease | Giant's Maul - Crushing Blow | Cast Speed Slow: **20%** |
| Cast Speed Increase | Yasha and Kaya | Bonus Cast Speed: **25%** |
| Cast Speed Increase | Faceless Void - Time Zone | Cast Animation Factor:; this is an old ability. |

[corpus:liquipedia_dota2/cast_animation@2383517#Cast_Speed_Manipulation]

## Talents

| Ability | Type | Affects | Cast Speed Bonus | Effect | Status Effects |
|---|---|---|---:|---|---|
| Cast Speed | Passive | Self | 30% | Reduces the hero’s cast point and backswing. | `?` Hidden modifier |

[corpus:liquipedia_dota2/cast_animation@2383517#Talents]

The following heroes have a talent that grants increased cast speed; the talent listing is structured by bonus, levels **10**, **15**, **20**, and **25**, and the **Left** and **Right** choices at each level. [corpus:liquipedia_dota2/cast_animation@2383517#Talents]

## Version History

| Version | Date | Description |
|---|---|---|
| 6.00 | 2026-07-25 | Updated all of the cast animations so they more fully match the hero models. |

[corpus:liquipedia_dota2/cast_animation@2383517#Version_History]