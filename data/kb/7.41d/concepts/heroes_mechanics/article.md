---
title: Heroes/Mechanics
kind: concept
patch: 7.41d
card:
  entity: heroes_mechanics
  sentences:
  - text: Heroes are Dota 2’s player-controlled main characters; each has strength,
      agility, and intelligence, uses a primary attribute or benefits from all three
      as Universal, gains experience toward level 30, allocates attribute and ability
      points, and spends gold on items.
    marks:
    - corpus:liquipedia_dota2/heroes_mechanics@2359189
  - text: Every locked-in hero spawns once at the beginning of a match after the picking
      phase.
    marks:
    - corpus:liquipedia_dota2/heroes_mechanics@2359189#Spawning
  - text: Hero clones are the only heroes that spawn later.
    marks:
    - corpus:liquipedia_dota2/heroes_mechanics@2359189#Clones
  - text: Hero kills grant gold scaling with the victim’s level and killing streak
      and experience scaling with the victim’s level.
    marks:
    - corpus:liquipedia_dota2/heroes_mechanics@2359189#Killing_and_Dying
  - text: A killing streak begins after 3 hero kills without dying and is capped at
      the value for 10 kills.
    marks:
    - corpus:liquipedia_dota2/heroes_mechanics@2359189#Killing_and_Dying
  - text: First Blood grants an additional 135 only to the hero that deals the killing
      blow.
    marks:
    - corpus:liquipedia_dota2/heroes_mechanics@2359189#Killing_and_Dying
  - text: A multi-kill starts when a second hero is killed within 18 seconds of the
      first and extends when each subsequent kill occurs within 18 seconds of the
      previous kill.
    marks:
    - corpus:liquipedia_dota2/heroes_mechanics@2359189#Killing_and_Dying
  - text: On death, a player loses gold based on NetWorth/40, but only unreliable
      gold can be lost.
    marks:
    - corpus:liquipedia_dota2/heroes_mechanics@2359189#Killing_and_Dying
  - text: Only deaths to enemies grant a bounty and end a killing streak; deaths to
      neutral creeps or denial by an ally or oneself do neither.
    marks:
    - corpus:liquipedia_dota2/heroes_mechanics@2359189#Killing_and_Dying
  - text: Default hero respawn time starts at 12s and reaches 100s at level 25.
    marks:
    - corpus:liquipedia_dota2/heroes_mechanics@2359189#Respawn_Time
  - text: While dead, a player can buy the hero back to respawn instantly at the fountain.
    marks:
    - corpus:liquipedia_dota2/heroes_mechanics@2359189#Buyback
  - text: Buyback costs 200 + NetWorth / 13, rounded down.
    marks:
    - corpus:liquipedia_dota2/heroes_mechanics@2359189#Details
---

# Heroes and Mechanics

## Main

Heroes are Dota 2’s essential main characters and are controlled by players. Every hero possesses strength, agility, and intelligence; one may be the hero’s primary attribute. Heroes without a primary attribute are Universal and benefit from all three attributes. Heroes gain experience to level up to level 30, receiving additional attribute points and ability points that can level abilities or grant more attributes. They can spend gold to purchase items. [corpus:liquipedia_dota2/heroes_mechanics@2359189]

## Complexity

Hero complexity is a difficulty rating assigned by Valve using unknown criteria. High-complexity heroes are generally less reliably useful than low-complexity heroes, especially when played improperly. Heroes at maximum complexity have unique mechanisms, hard-to-understand abilities, or multi-unit control. [corpus:liquipedia_dota2/heroes_mechanics@2359189#Complexity]

## Spawning

All heroes spawn once at the beginning of a match after the picking phase, provided the player locked in their pick. Radiant heroes spawn facing 45° northeast, while Dire heroes face 45° southwest. [corpus:liquipedia_dota2/heroes_mechanics@2359189#Spawning]

### Clones

Hero clones are the only heroes that spawn later and can currently be created by 4 heroes. Like heroes, clones do not disappear when dying or expiring. Meepo Clones respawn like regular heroes; Arc Warden and Monkey King clones respawn whenever Tempest Double or Wukong’s Command is cast again. [corpus:liquipedia_dota2/heroes_mechanics@2359189#Clones]

Hero clones are treated almost entirely like regular heroes, with special spell interactions for fairness. Meepo’s permanent clones die together with the main hero, while Arc Warden’s clone more closely resembles a summon or illusion. Monkey King’s clones act as spell effects and cannot be interacted with; they stand at fixed locations and automatically attack nearby enemy heroes until the spell expires. [corpus:liquipedia_dota2/heroes_mechanics@2359189#Clones]

| Hero and ability | Clone behavior |
|---|---|
| Arc Warden — Tempest Double | Creates a temporary self that can independently use abilities and items. It becomes weaker as its distance from the caster increases and expires like a regular summon. |
| Dazzle — Nothl Projection | Creates a temporary invulnerable clone that can use abilities and items. Dazzle is fully disabled and vulnerable while it exists. The clone cannot move too far from Dazzle and dies if Dazzle is killed. |
| Meepo — Divided We Stand | Creates permanent clones that can use copied abilities and items, although they copy only boots. The main hero and all clones always die and respawn together, regardless of which one is killed. |
| Monkey King — Wukong’s Command | Creates a temporary army of stationary, uncontrollable, invulnerable clones that attack only heroes within their attack range. |
| Monkey King — Wukong’s Command | Passively spawns a Wukong’s Command Soldier that can use Jingu Mastery, based on a charge-replenishment timer. |

[corpus:liquipedia_dota2/heroes_mechanics@2359189#Clones]

### Illusions

Illusions are hero-type units, but they do not respawn. They despawn completely after dying like other units and summons, and each recast of an illusion-creating spell produces entirely new illusions. Illusions are hero-based summons that copy a hero while acting like summons. [corpus:liquipedia_dota2/heroes_mechanics@2359189#Illusions]

## Killing and Dying

Killing a hero grants much larger bonuses than killing almost any other unit. Heroes grant scaling gold based on their level and current killing streak and scaling experience based on their level. Heroes acquire killing streaks by killing heroes; these streaks increase their bounty and therefore their value to enemies. A killing streak begins after 3 hero kills without a death, is capped at 10 kills, and has the same worth beyond 10 kills as at 10. A hero’s current streak is globally announced whenever that hero makes a kill. [corpus:liquipedia_dota2/heroes_mechanics@2359189#Killing_and_Dying]

The match’s first hero kill, **First Blood!**, grants an additional 135 to the killing hero. The hero receives this gold only if it dealt the killing blow. Otherwise, it receives only assist gold and experience—or nothing—depending on the time since it last damaged the target and, if too much time has passed, its distance from the target. [corpus:liquipedia_dota2/heroes_mechanics@2359189#Killing_and_Dying]

Hero-kill experience depends on the victim’s level: higher levels grant a higher possible currentXP bounty. Although heroes can reach level 30, the experience bounty is capped at level 25. [corpus:liquipedia_dota2/heroes_mechanics@2359189#Killing_and_Dying]

Killing multiple heroes in quick succession produces a multi-kill. Multi-kills have no gameplay effect and are aesthetic only. The killer need not remain alive between kills: a multi-kill can continue after the killer dies. It begins when a second hero is killed within 18 seconds of the first and extends whenever another hero is killed within 18 seconds of the previous kill. A multi-kill has no limit but is soft-capped at 5, repeating the same line for 5 or more kills. Announcer responses are customizable. [corpus:liquipedia_dota2/heroes_mechanics@2359189#Killing_and_Dying]

| Kills | Audio | Announcement | Announcement with killing streak |
|---:|---|---|---|
| 1 | N/A | N/A | N/A |
| 2 | Link▶️ | Player got a double kill! | ... with a double kill! |
| 3 | Link▶️ | Player has a TRIPLE kill! | ... with a TRIPLE kill! |
| 4 | Link▶️ | Player earned an ULTRA KILL! | ... with an ULTRA KILL! |
| 5+ | Link▶️ | RAMPAGE!!! | ...RAMPAGE!!! |

[corpus:liquipedia_dota2/heroes_mechanics@2359189#Killing_and_Dying]

When a hero dies, it remains dead for a duration based on its level, and its player loses gold based on \(\tfrac{\text{NetWorth}}{40}\). This loss cannot be directly reduced or avoided. Only unreliable gold is lost; reliable gold is retained, so a hero with little unreliable gold and substantial reliable gold loses less than one with substantial unreliable gold and little reliable gold. Death also removes any ongoing killing streak but does not remove experience. [corpus:liquipedia_dota2/heroes_mechanics@2359189#Killing_and_Dying]

Death grants gold and experience to nearby enemies and the killer, but rewards are granted and streaks are lost only when the hero dies to an enemy. Dying to neutral creeps or being denied by an ally or oneself neither grants enemies a bounty nor ends the current killing streak. Hero-kill sounds for Ultra Kill and Rampage were added in 6.60. [corpus:liquipedia_dota2/heroes_mechanics@2359189#Killing_and_Dying]

## Respawning

After its initial spawn, a hero is not created again but instead respawns. A dead hero returns after a level-based duration, with maximum respawn time reached at level 25. Only Heroes, Couriers, and Roshan can respawn. [corpus:liquipedia_dota2/heroes_mechanics@2359189#Respawning]

On respawning, a hero is instantly moved to its fountain area. Radiant heroes face 45° northeast and Dire heroes face 45° southwest. Health and mana are replenished, but cooldowns are unaffected and buffs and debuffs are not cleared. [corpus:liquipedia_dota2/heroes_mechanics@2359189#Respawning]

A respawned hero becomes invulnerable and untargetable until issued a command, preventing spawn-camping. Rejuvenation Aura provides this invulnerability. Commands that end it include regular orders such as moving, attacking, and casting abilities, as well as shop interactions such as buying and selling items. [corpus:liquipedia_dota2/heroes_mechanics@2359189#Respawning]

### Respawn Time

Total respawn time is defined as:

```text
Base Respawn Time [?]
Set Respawn Time [?]
+ Buyback Respawn Time Increase
± Other Flat Bonus Respawn Time
```

[corpus:liquipedia_dota2/heroes_mechanics@2359189#Respawn_Time]

Hero respawn time starts at 12s and increases through level 25, where it reaches 100s. [corpus:liquipedia_dota2/heroes_mechanics@2359189#Respawn_Time]

| LVL | Default Respawn Time |
|---:|---:|
| 1 | 12s |
| 2 | 15s |
| 3 | 18s |
| 4 | 21s |
| 5 | 24s |
| 6 | 26s |
| 7 | 28s |
| 8 | 30s |
| 9 | 32s |
| 10 | 34s |
| 11 | 36s |
| 12 | 44s |
| 13 | 46s |
| 14 | 48s |
| 15 | 50s |
| 16 | 52s |
| 17 | 54s |
| 18 | 65s |
| 19 | 70s |
| 20 | 75s |
| 21 | 80s |
| 22 | 85s |
| 23 | 90s |
| 24 | 95s |
| 25+ | 100s |

[corpus:liquipedia_dota2/heroes_mechanics@2359189#Respawn_Time]

| Respawn-time source | Values and behavior |
|---|---|
| Gold — Buyback | Next Respawn Time Increase: 25. Neutral Set Respawn Time: 26. The buyback penalty is added to respawn time unless affected by the aforementioned Reincarnation sources. Dying to neutral creeps sets respawn time to a minimum of 26s. |
| Courier — Passive Bonus | Base Respawn Time: 45. Respawn Time Increase per Level: 5. Couriers level with their owners and respawn at their faction’s fountain after their respawn time. |
| Undying — Ceaseless Dirge | Cooldown: 480. When Undying dies, he automatically respawns in the fountain. The ability begins the game on cooldown. |
| Vengeful Spirit — Vengeance Illusion | Duration: Respawn Time. On death, Vengeful Spirit creates a strong illusion that deals and takes full damage and can cast all her abilities. If it is alive when she respawns, she takes its place. It disappears when she respawns or when it reaches the normal death duration. Buyback’s time-increase penalty does not increase its duration. |

[corpus:liquipedia_dota2/heroes_mechanics@2359189#Respawn_Time]

### Buyback

Buyback is an ability affecting Self. While dead, a player can spend money to buy the hero back, causing it to respawn instantly at the fountain. [corpus:liquipedia_dota2/heroes_mechanics@2359189#Buyback]

| Buyback value | Amount |
|---|---:|
| Base Gold Cost | 200 |
| Networth Gold Divisor | 13 |
| Next Respawn Time Increase | 25 |
| Neutral Set Respawn Time | 26 |
| Cooldown | 480 |

[corpus:liquipedia_dota2/heroes_mechanics@2359189#Buyback]

#### Details

The buyback button appears on the hero portrait while the hero is dead. Buyback cannot be used while the dead hero remains stunned, including by Toss, Walrus PUNCH!, Walrus Kick, or Winter’s Curse, or while the hero is reincarnating. [corpus:liquipedia_dota2/heroes_mechanics@2359189#Details]

Buyback takes reliable gold first and then unreliable gold. Its base cost is 200 plus a fraction of the hero’s net worth, rounded down:

\[
200 + \text{NetWorth} / 13
\]

The respawn-time increase applies to the next respawn and does not count deaths with Reincarnation. [corpus:liquipedia_dota2/heroes_mechanics@2359189#Details]

#### Displays

Buyback status appears in 3 locations: on the HP bar while dead, in the gold tooltip at any time, and below the hero icon while dead. [corpus:liquipedia_dota2/heroes_mechanics@2359189#Displays]

The **BUYBACK** button is accessible only while dead and appears on the right side of the death bar. The death bar replaces the HP bar while dead and displays respawn time. The button has 3 statuses: [corpus:liquipedia_dota2/heroes_mechanics@2359189#Displays]

| Status | Display |
|---|---|
| Ready | The button is grey and heightened, reads **BUYBACK** in white, and displays the current buyback gold cost. |
| Insufficient gold | The button is red and pushed back. **BUYBACK** turns red, and the current gold cost remains displayed. |
| On cooldown | The button resembles the insufficient-gold state, but a timer showing the remaining cooldown replaces the gold cost. |

[corpus:liquipedia_dota2/heroes_mechanics@2359189#Displays]

Alt+Right Click on a hero’s portrait prints that hero’s respawn time if the hero is dead. Allies can also see buyback status below the hero icon on the top bar while the hero is dead. A golden border around the flag means buyback is ready and usable; no golden border means the player either lacks enough gold or is on cooldown. [corpus:liquipedia_dota2/heroes_mechanics@2359189#Displays]

Hovering over the gold opens a tooltip displaying the currently required buyback gold, cooldown status, and either the amount still needed or the player’s surplus gold. [corpus:liquipedia_dota2/heroes_mechanics@2359189#Displays]

When a hero buys back, a string sound audible to everyone plays, and a gold-stack icon appears below the hero’s top-bar icon for several seconds, visible to everyone. The hero also gives a buyback response audible to everyone, unlike regular-respawn responses, which only the player can hear. Consequently, every buyback has a revealing cue regardless of player settings. [corpus:liquipedia_dota2/heroes_mechanics@2359189#Displays]

## Leveling

Every hero begins at level 1 and can level up 29 times to level 30. Each level grants attribute points whose values differ by hero. Ability points are gained through level 25 and can be spent to level an ability or talent. Some abilities require particular hero levels before they can be learned or upgraded further. [corpus:liquipedia_dota2/heroes_mechanics@2359189#Leveling]

Most basic abilities have 4 levels and can be leveled at levels 1, 3, 5, and 7. Talents can be upgraded at levels 10, 15, 20, and 25. Ultimates usually have 3 levels and can usually be upgraded at levels 6, 12, and 18. Meepo requires different levels for his ultimate, while Invoker has a unique ability scheme. [corpus:liquipedia_dota2/heroes_mechanics@2359189#Leveling]

Heroes gain experience by killing enemy units or by being near an enemy unit when an ally kills it. The required experience range is 1500 if the hero did not make the kill or the killed unit was not a hero. Killing another hero always grants experience regardless of distance. [corpus:liquipedia_dota2/heroes_mechanics@2359189#Leveling]

When multiple heroes are in range of a killed enemy unit, its experience is split evenly among them. Every Meepo clone is included, while Arc Warden’s Tempest Double and Monkey King’s Wukong’s Command clones are excluded. A maximum-level hero still takes its experience share despite having no use for it, causing that experience to be wasted. Dead heroes cannot gain experience or receive a share, except Vengeful Spirit after acquiring Aghanim’s Scepter. [corpus:liquipedia_dota2/heroes_mechanics@2359189#Leveling]

Leveling up produces an angled yellow light beam that shines from the sky onto the hero and is visible to everyone. It also plays a sound effect audible only to the player. [corpus:liquipedia_dota2/heroes_mechanics@2359189#Leveling]

## Ability Interactions

The hero unit type creates distinct ability interactions. Some abilities cannot affect heroes, while others have altered effects or values against them. [corpus:liquipedia_dota2/heroes_mechanics@2359189#Ability_Interactions]

### Cannot Target or Affect Heroes

| Source | Ability |
|---|---|
| Battle Fury | Quell |
| Doom | Devour |
| Enigma | Demonic Conversion |
| Hand of Midas | Transmute |
| Helm of the Dominator | Dominate |
| Quelling Blade | Quell |

[corpus:liquipedia_dota2/heroes_mechanics@2359189#Ability_Interactions]

### Can Target or Affect Only Heroes

| Source | Ability |
|---|---|
| Abaddon | Borrowed Time |
| Alchemist | Unstable Concoction |
| Alchemist | Aghanim’s Scepter Synth |
| Ancient Apparition | Chilling Touch |
| Bloodseeker | Thirst |
| Bottle | Regenerate |
| Chaos Knight | Phantasm |
| Clarity | Replenish |
| Crimson Guard | Guard |
| Dark Seer | Wall of Replica |
| Dazzle | Shallow Grave |
| Disruptor | Glimpse |
| Earth Spirit | Enchant Remnant |
| Enchanted Mango | Eat Mango |
| Forged Spirit | Melting Strike |
| Glimmer Cape | Glimmer |
| Healing Salve | Salve |
| Io | Relocate |
| Kunkka | X Marks the Spot |
| Legion Commander | Duel |
| Linken’s Sphere | Transfer Spellblock |
| Lotus Orb | Echo Shell |
| Luna | Lunar Blessing |
| Magnus | Skewer |
| Mirana | Moonlight Shadow |
| Monkey King | Jingu Mastery |
| Monkey King | Wukong’s Command |
| Moon Shard | Consume |
| Morphling | Morph |
| Necrophos | Reaper’s Scythe |
| Nyx Assassin | Mind Flare |
| Oracle | False Promise |
| Outworld Destroyer | Sanity’s Eclipse |
| Puck | Dream Coil |
| Razor | Static Link |
| Riki | Tricks of the Trade |
| Rubick | Spell Steal |
| Shadow Amulet | Fade |
| Shadow Demon | Disruption |
| Slark | Pounce |
| Slark | Shadow Dance |
| Spectre | Haunt |
| Sven | God’s Strength |
| Tango | Devour |
| Terrorblade | Reflection |
| Terrorblade | Sunder |
| Tinker | Heat-Seeking Missile |
| Troll Warlord | Battle Trance |
| Urn of Shadows | Soul Release |
| Weaver | Time Lapse |
| Witch Doctor | Maledict |
| Witch Doctor | Death Ward |
| Wraith King | Wraith Delay Aura |
| Zeus | Thundergod’s Wrath |

[corpus:liquipedia_dota2/heroes_mechanics@2359189#Ability_Interactions]

### Different Interactions with Heroes

| Source and ability | Hero-specific interaction |
|---|---|
| Ancient Apparition — Ice Blast | Can place Frostbite only on heroes but can damage other units on impact. |
| Axe — Culling Blade | Does not go on cooldown when it kills a hero. |
| Batrider — Sticky Napalm | Deals full damage against heroes. |
| Batrider — Flaming Lasso | When upgraded, selects only heroes as secondary targets. |
| Boots of Travel 2 — Upgrade: Town Portal Scroll | Cannot target heroes at level 1 but can at level 2. |
| Bounty Hunter — Track | Can be cast only on heroes; its speed bonus can affect other units. |
| Brewmaster — Thunder Clap | Lasts less time on heroes. |
| Bristleback — Viscous Nasal Goo | Lasts less time on heroes. |
| Centaur Conqueror — War Stomp | Lasts less time on heroes. |
| Centaur Warrunner — Retaliate | Can damage any unit, but the talent’s aura affects only allied heroes. |
| Chen — Hand of God | Besides Chen’s own creeps, heals only allied heroes. |
| Crystal Maiden — Frostbite | Lasts less time on heroes. |
| Diffusal Blade — Inhibit | Does not root heroes. |
| Drow Ranger — Frost Arrows | Lasts less time on heroes. |
| Drow Ranger — Marksmanship | Reacts only to nearby heroes; splinter arrows work against other units. |
| Elder Titan — Astral Spirit | Grants more attack damage and movement speed from heroes hit. |
| Ember Spirit — Sleight of Fist | Grants a fixed attack-damage bonus when striking heroes, while reducing attack damage by a percentage when striking creeps. |
| Enchantress — Enchant | Slows heroes instead of converting them, but still converts illusions. |
| Faceless Void — Time Lock | Lasts less time on heroes. |
| Guardian Greaves — Guardian Aura | Its boost below the health threshold affects only heroes. |
| Gyrocopter — Homing Missile | Can be damaged only by heroes and buildings. |
| Invoker — E.M.P. | Restores mana to Invoker only for heroes hit. |
| Io — Spirits | Explodes upon colliding with heroes instead of passing through them. |
| Kunkka — Ghostship | Rum and the Aghanim’s Scepter dragging effect can affect only heroes; damage and stun can affect other units. |
| Legion Commander — Overwhelming Odds | Grants more movement speed from enemy heroes hit. Heroes hit increase its area damage more than other units. |
| Lifestealer — Infest | Can target allied heroes but not enemy heroes. It can target other units regardless of alliance. |
| Magnus — Shockwave | When upgraded, deals full damage to heroes while returning. |
| Mirana — Sacred Arrow | Does not instantly kill heroes. |
| Nature’s Prophet — Wrath of Nature | When upgraded, heroes that die while debuffed spawn Greater Treants instead of regular Treants. |
| Necrophos — Death Pulse | Grants more stacks for killing heroes. |
| Ogre Magi — Bloodlust | Autocast targets only heroes. |
| Phantom Assassin — Blur | Reacts only to nearby heroes. |
| Phoenix — Supernova | When upgraded, can be cast only on heroes. Only heroes can damage the sun. |
| Pudge — Dismember | Lasts less time on heroes. |
| Pugna — Nether Ward | Mana Degen Aura affects only heroes. Heroes require fewer attacks to destroy the ward. |
| Pugna — Life Drain | Restores mana only when the unit damaged by Life Drain is a hero. |
| Ring of Basilius — Basilius Aura | Can be toggled to affect only heroes. |
| Roshan — Slam | Lasts less time on heroes. |
| Rubick — Fade Bolt | Reduces more attack damage on heroes hit. |
| Sand King — Burrowstrike | When upgraded, places Caustic Finale only on heroes. |
| Shadow Fiend — Necromastery | Gains more souls from heroes killed. |
| Shadow Fiend — Requiem of Souls | When upgraded, heals only from heroes hit. |
| Skywrath Mage — Arcane Bolt | With Aghanim’s Scepter, secondary targeting prioritizes heroes. |
| Skywrath Mage — Concussive Shot | The projectile can target only heroes. With Aghanim’s Scepter, secondary targeting can target creeps but prioritizes heroes. |
| Skywrath Mage — Ancient Seal | Reduces only heroes’ magic resistance. With Aghanim’s Scepter, secondary targeting prioritizes heroes. |
| Skywrath Mage — Mystic Flare | Damages only heroes. With Aghanim’s Scepter, secondary targeting can target creeps—while still damaging only heroes—but prioritizes heroes. |
| Smoke of Deceit — Disguise | Breaks only from hero proximity but can disguise non-hero units. |
| Spectre — Spectral Dagger | Can directly target only heroes. |
| Spiderling — Poison Sting | Lasts less time on heroes. |
| Spirit Bear — Entangling Claws | Lasts less time on heroes. |
| Storm — Cyclone | Lasts less time on heroes. |
| Tinker — Laser | Lasts less time on heroes. When upgraded, jumps only to heroes. |
| Treant Protector — Living Armor | When ground-targeted, considers only heroes and buildings. |
| Tusk — Snowball | Only added heroes increase Snowball’s damage. |
| Underlord — Atrophy Aura | Dying heroes grant more attack damage than other units. |
| Undying — Tombstone | Heroes require fewer attacks to destroy the Tombstone and kill a Zombie. |
| Vhoul Assassin — Envenomed Weapon | Lasts less time on heroes. |
| Visage — Soul Assumption | Counts only damage dealt to heroes. With the double-strike talent, secondary targeting prioritizes heroes. |
| Weaver — The Swarm | Heroes require fewer attacks to destroy a Beetle. |
| Zeus — Lightning Bolt | Searches only for heroes when ground-targeted. |

[corpus:liquipedia_dota2/heroes_mechanics@2359189#Ability_Interactions]