---
title: Mechanics
kind: concept
patch: 7.41d
card:
  entity: mechanics
  sentences:
  - text: Mechanics are Dota 2’s inner workings for calculating where elements originate
      and how they interact, including damage, which has two categories and three
      overall types.
    marks:
    - corpus:liquipedia_dota2/mechanics@2378401
    - corpus:liquipedia_dota2/mechanics@2378401#Attack_Mechanics
  - text: All heroes have at least three basic abilities and one ultimate ability.
    marks:
    - corpus:liquipedia_dota2/mechanics@2378401#Unit_Mechanics
  - text: Most melee heroes have a default attack range of 150, while ranged heroes
      can have a default range of up to 675.
    marks:
    - corpus:liquipedia_dota2/mechanics@2378401#Attack_Mechanics
  - text: Attack modifiers add effects to basic attacks, with some stacking together
      and others not stacking.
    marks:
    - corpus:liquipedia_dota2/mechanics@2378401#Attack_modifiers
  - text: Three lanes lead into each team’s base, with jungle areas between them.
    marks:
    - corpus:liquipedia_dota2/mechanics@2378401#World_Mechanics
  - text: A stun prevents movement and all actions, whereas a root prevents movement
      but permits some actions.
    marks:
    - corpus:liquipedia_dota2/mechanics@2378401#Status_effects
  - text: Death dispel is the strongest and rarest dispel type and removes nearly
      all status effects.
    marks:
    - corpus:liquipedia_dota2/mechanics@2378401#Dispelling
  - text: Denying a low-health friendly hero, creep, or building prevents enemies
      from receiving its gold and experience.
    marks:
    - corpus:liquipedia_dota2/mechanics@2378401#Gameplay
  - text: Versions update game mechanics with new heroes, items, and balance adjustments
      and are shipped with patches.
    marks:
    - corpus:liquipedia_dota2/mechanics@2378401#System
  - text: Official cheats are available for testing in private lobbies but cannot
      be used in matchmaking.
    marks:
    - corpus:liquipedia_dota2/mechanics@2378401#Settings
  - text: Matchmaking automatically pairs players, usually through internal skill
      calculations, and offers casual and ranked play.
    marks:
    - corpus:liquipedia_dota2/mechanics@2378401#Matchmaking
  - text: Cosmetic items change heroes and interface elements without affecting game
      mechanics.
    marks:
    - corpus:liquipedia_dota2/mechanics@2378401#Cosmetic_items
---

# Mechanics

Mechanics are the inner workings of Dota 2. Mechanics topics explain how elements are calculated, where they originate, and their complex interactions with other mechanics. [corpus:liquipedia_dota2/mechanics@2378401]

## Unit Mechanics

Unit mechanics are properties used by units generally, including heroes, creeps, and summons. Heroes possess unique mechanics that other units do not. [corpus:liquipedia_dota2/mechanics@2378401#Unit_Mechanics]

| Mechanic | Introduction |
|---|---|
| Abilities; Cooldown | Skills used by units on the battlefield. All heroes have at least three basic abilities and one ultimate ability. Hero abilities are acquired upon leveling up with experience. Most abilities must be activated; others are passive or augment basic attacks. Active abilities have a cooldown period between uses. [corpus:liquipedia_dota2/mechanics@2378401#Unit_Mechanics] |
| Attributes; Strength; Agility; Intelligence | Baseline stats that increase with each level. Strength increases health and health regeneration, Agility increases armor and attack speed, and Intelligence increases mana and mana regeneration. Every hero is associated with one of three attributes as its Primary Attribute; raising it also raises physical attack damage. Items and abilities can also increase attributes. [corpus:liquipedia_dota2/mechanics@2378401#Unit_Mechanics] |
| Talents | Bonuses that increase a hero’s stats and properties. Players can pick one of two talents at levels 10, 15, 20, and 25. The unchosen talents can be acquired at level 27, 28, 29 and 30 respectively. [corpus:liquipedia_dota2/mechanics@2378401#Unit_Mechanics] |
| Experience (XP) | Points needed for heroes to level up. Experience is gained from killing creeps, enemy heroes, certain talents and the Wisdom Rune. A hero’s maximum level is 30, after which experience no longer serves any purpose. [corpus:liquipedia_dota2/mechanics@2378401#Unit_Mechanics] |
| Spawning | Heroes spawn at the fountain in their base. Dead heroes respawn after a set amount of time determined by the hero’s level. [corpus:liquipedia_dota2/mechanics@2378401#Unit_Mechanics] |
| Health; Health Regeneration; Restoration Manipulation | Health is the amount of hit points a hero has. Health and health regeneration can be increased by strength, items, talents and abilities. [corpus:liquipedia_dota2/mechanics@2378401#Unit_Mechanics] |
| Mana; Mana Regeneration | Mana is the resource required to use most abilities. Mana and mana regeneration can be increased by intelligence, items, talents and abilities. [corpus:liquipedia_dota2/mechanics@2378401#Unit_Mechanics] |
| Armor; Armor Manipulation; Effective HP | Armor reduces incoming physical damage by a scaling amount per attack. It comes in three types and can be increased or decreased by agility, items, talents and abilities. [corpus:liquipedia_dota2/mechanics@2378401#Unit_Mechanics] |
| Damage Block | Reduces incoming damage by a fixed amount per attack and is granted by some items and abilities. [corpus:liquipedia_dota2/mechanics@2378401#Unit_Mechanics] |
| Magic Resistance; Effective HP | Reduces incoming magical damage by a percentage. All heroes start with 25% Magic Resistance, which can be further increased by items, talents and abilities. [corpus:liquipedia_dota2/mechanics@2378401#Unit_Mechanics] |
| Evasion; True Strike; Accuracy | Evasion grants a percentage chance to avoid a physical attack completely. True strike allows a hero to ignore evasion. [corpus:liquipedia_dota2/mechanics@2378401#Unit_Mechanics] |
| Status Resistance | A hero attribute that reduces the duration of most status debuffs. By default, every unit has a base status resistance of zero. [corpus:liquipedia_dota2/mechanics@2378401#Unit_Mechanics] |
| Movement Speed | The rate at which a unit moves. Items and abilities can increase or decrease movement speed. [corpus:liquipedia_dota2/mechanics@2378401#Unit_Mechanics] |
| Slow Resistance | A hero attribute that reduces the slow values of slows. By default, every unit has a base slow resistance of zero. [corpus:liquipedia_dota2/mechanics@2378401#Unit_Mechanics] |
| Turn Rate | The rate at which a unit’s model turns, measured with time. Most actions require the model to face the direction of the action about to be taken. [corpus:liquipedia_dota2/mechanics@2378401#Unit_Mechanics] |
| Collision Size; Phased | A unit’s internal size, which is impassable and can block other units. Most heroes have the same collision size regardless of their graphical model. [corpus:liquipedia_dota2/mechanics@2378401#Unit_Mechanics] |
| Aura | Passive buffs and debuffs that surround a hero or unit in a circular radius. Auras come from abilities and items and cannot be dispelled. [corpus:liquipedia_dota2/mechanics@2378401#Unit_Mechanics] |
| Illusions | Copies of heroes generated by abilities, items, or runes. Illusions come in different types and possess lesser properties of the original hero. [corpus:liquipedia_dota2/mechanics@2378401#Unit_Mechanics] |

## Attack Mechanics

| Mechanic | Introduction |
|---|---|
| Damage Categories; Attack Damage; Spell Damage | Damage has two different categories. Attack damage is usually dealt by basic attacks, some abilities and certain items. Spell damage is usually dealt by abilities, most items and certain attack modifiers. Both categories may use any of the three different damage types. [corpus:liquipedia_dota2/mechanics@2378401#Attack_Mechanics] |
| Damage Types; Physical Damage; Magical Damage; Pure Damage; HP Removal | There are three overall damage types. Physical damage is dealt by basic attacks and some abilities. Magical damage is dealt by abilities and items. Pure damage is the rarest and penetrates armor and magic resistance. HP Removal ignores all forms of damage manipulation and is not technically a damage type itself. [corpus:liquipedia_dota2/mechanics@2378401#Attack_Mechanics] |
| Attack Damage; Total Attack Damage; Instant Attack | Damage dealt by basic attacks. It is usually physical, rarely magical or pure, and is divided into four Attack Classes that interact differently with different Unit Types. [corpus:liquipedia_dota2/mechanics@2378401#Attack_Mechanics] |
| Spell Damage; Spell Amplification; Spell Lifesteal | Damage dealt by any source other than basic attacks. Spell damage can have magical, physical, or pure damage types. [corpus:liquipedia_dota2/mechanics@2378401#Attack_Mechanics] |
| Damage Manipulation; Damage Amplification; Damage Reduction; Damage Negation; Damage Barrier | Calculations affecting the final value of a damage instance. Items and abilities can amplify, reduce, or negate final damage. [corpus:liquipedia_dota2/mechanics@2378401#Attack_Mechanics] |
| Damage over Time | Periodic damage dealt over intervals, usually in small amounts. [corpus:liquipedia_dota2/mechanics@2378401#Attack_Mechanics] |
| Attack Speed | The time required to perform an attack. Items and abilities can increase or decrease attack speed. [corpus:liquipedia_dota2/mechanics@2378401#Attack_Mechanics] |
| Attack Animation; Attack Point; Attack Backswing | The model animation played when a unit attacks. Damage is dealt at the attack point, followed by the attack backswing. Attack animations play faster or slower according to the unit’s attack speed. [corpus:liquipedia_dota2/mechanics@2378401#Attack_Mechanics] |
| Cast Animation; Cast Point; Cast Backswing | The model animation played when a unit uses an ability. The ability is used at the cast point, followed by the cast backswing. Each ability has its own unique cast animation. [corpus:liquipedia_dota2/mechanics@2378401#Attack_Mechanics] |
| Channeling | The model animation for certain abilities that require a unit to stand still to affect the ability over time. [corpus:liquipedia_dota2/mechanics@2378401#Attack_Mechanics] |
| Projectile Speed | The speed at which a ranged basic attack’s projectile travels. Abilities have unique projectile speeds for their projectiles. [corpus:liquipedia_dota2/mechanics@2378401#Attack_Mechanics] |
| Attack Range | The distance from which a unit can perform basic attacks. Most Melee heroes have a default range of 150, while Ranged heroes can have a default range of up to 675. [corpus:liquipedia_dota2/mechanics@2378401#Attack_Mechanics] |

### Attack Modifiers

Attack modifiers add effects to basic attacks. Some stack with one another in several ways, while others do not stack at all. [corpus:liquipedia_dota2/mechanics@2378401#Attack_modifiers]

| Mechanic | Introduction |
|---|---|
| Critical Strike | Increases damage from basic attacks by a percentage multiplier. [corpus:liquipedia_dota2/mechanics@2378401#Attack_modifiers] |
| Cleave & Splash | Cause damage from basic attacks to spill beyond one target into a larger area. [corpus:liquipedia_dota2/mechanics@2378401#Attack_modifiers] |
| Bash | Gives basic attacks a chance to stun. [corpus:liquipedia_dota2/mechanics@2378401#Attack_modifiers] |
| Lifesteal | Causes attacks to regenerate a portion of their damage as health. [corpus:liquipedia_dota2/mechanics@2378401#Attack_modifiers] |
| Mana Break | Causes attacks to burn the target’s mana and deal damage based on the burned amount. [corpus:liquipedia_dota2/mechanics@2378401#Attack_modifiers] |
| Autocast | Modifiers innate to abilities that can be toggled On / Off. [corpus:liquipedia_dota2/mechanics@2378401#Attack_modifiers] |

## World Mechanics

| Mechanic | Introduction |
|---|---|
| Game Map; Lanes; Jungle | The battlefield where Dota 2 matches take place. Three Lanes are present and lead into each team’s base. Between them are wooded areas known as the Jungle. [corpus:liquipedia_dota2/mechanics@2378401#World_Mechanics] |
| Buildings; Ancient; Towers; Barracks; Outposts | Structures that aid each opposing side’s defense. The Ancient is the main building and must be destroyed for a side to win. Glyph of Fortification can make buildings temporarily invulnerable. [corpus:liquipedia_dota2/mechanics@2378401#World_Mechanics] |
| Shops | Stores scattered across the map that sell items to heroes. [corpus:liquipedia_dota2/mechanics@2378401#World_Mechanics] |
| Gold; Buyback | Currency used to buy items that increase a hero’s capabilities. Heroes gain a small amount of gold every second and can earn more by killing creeps, enemy heroes, and buildings. Dead heroes can spend gold on Buyback to respawn instantly. [corpus:liquipedia_dota2/mechanics@2378401#World_Mechanics] |
| Items; Recipes; Item Sharing; Disassembling | Objects purchasable on the game map. Items increase a hero’s properties and grant special abilities and effects. Smaller items combine into larger items with recipes. Some items can be disassembled. Neutral items can be found by killing neutral creeps. [corpus:liquipedia_dota2/mechanics@2378401#World_Mechanics] |
| Courier | A special unit owned by each player that holds and delivers items to players. [corpus:liquipedia_dota2/mechanics@2378401#World_Mechanics] |
| Creeps; Lane Creeps; Neutral Creeps | Units that spawn automatically and are killed for gold and experience. Lane creeps attack and push toward the opposing base. Neutral creeps reside in the jungle. [corpus:liquipedia_dota2/mechanics@2378401#World_Mechanics] |
| Summons | Units created by heroes to aid them in combat. [corpus:liquipedia_dota2/mechanics@2378401#World_Mechanics] |
| Wards | Units that provide vision or another utility. [corpus:liquipedia_dota2/mechanics@2378401#World_Mechanics] |
| Runes | Special boosters that spawn on the map. They give extra gold and experience to heroes who pick them up, along with various power-up effects. [corpus:liquipedia_dota2/mechanics@2378401#World_Mechanics] |
| Vision; Ground Vision; Flying Vision; Shared Vision; Expose; True Sight | A unit’s ability to see the map in real time rather than have it covered by fog of war. Most units have a vision radius around them. Some units can become invisible and can only be detected by True Sight. [corpus:liquipedia_dota2/mechanics@2378401#World_Mechanics] |
| Time of Day | The night-and-day cycle. Some heroes have abilities that function differently at night, when vision is also limited. [corpus:liquipedia_dota2/mechanics@2378401#World_Mechanics] |
| Trees | Impassible vegetation on the game map. Trees can be cut down and regrow over time; some items and abilities interact with them. [corpus:liquipedia_dota2/mechanics@2378401#World_Mechanics] |
| Pseudo-random Distribution | The chance that an ability or item effect occurs, increasing every time it does not occur. [corpus:liquipedia_dota2/mechanics@2378401#World_Mechanics] |
| True Random Distribution | The chance that an ability or item effect occurs, calculated independently of previous instances. [corpus:liquipedia_dota2/mechanics@2378401#World_Mechanics] |

## Status Effects

Status effects are conditions caused by abilities and items that can afflict units. [corpus:liquipedia_dota2/mechanics@2378401#Status_effects]

| Mechanic | Effect |
|---|---|
| Stun; Shackle | The unit cannot move or perform any actions. Shackle is the same as stun but requires the attacking hero to channel the effect. [corpus:liquipedia_dota2/mechanics@2378401#Status_effects] |
| Root | The unit cannot move but can perform some actions. [corpus:liquipedia_dota2/mechanics@2378401#Status_effects] |
| Leash | The unit cannot move outside a limited range but can perform some actions. It is similar to root. [corpus:liquipedia_dota2/mechanics@2378401#Status_effects] |
| Hex | The unit becomes a critter and cannot perform any actions except moving at a slow pace. [corpus:liquipedia_dota2/mechanics@2378401#Status_effects] |
| Cyclone | The unit is swept into the air, where it is invulnerable but cannot move or perform any actions. [corpus:liquipedia_dota2/mechanics@2378401#Status_effects] |
| Hide/Banish | The unit is temporarily removed from the game map and cannot be damaged or affected by any other mechanics. [corpus:liquipedia_dota2/mechanics@2378401#Status_effects] |
| Blind | The unit has a chance to miss basic attacks. [corpus:liquipedia_dota2/mechanics@2378401#Status_effects] |
| Silence | The unit cannot use unit abilities but can still use item abilities. [corpus:liquipedia_dota2/mechanics@2378401#Status_effects] |
| Mute | The unit cannot use item abilities. [corpus:liquipedia_dota2/mechanics@2378401#Status_effects] |
| Break | The unit’s passive abilities are disabled. [corpus:liquipedia_dota2/mechanics@2378401#Status_effects] |
| Disarm | The unit cannot attack but can still use abilities. [corpus:liquipedia_dota2/mechanics@2378401#Status_effects] |
| Slow | The unit’s movement speed is reduced. Most slows end after a set time, while others gradually decrease over time. [corpus:liquipedia_dota2/mechanics@2378401#Status_effects] |
| Trap | The unit’s movement is restricted by pathing blockers, but it can still act. Units try to path around them when possible. [corpus:liquipedia_dota2/mechanics@2378401#Status_effects] |
| Barrier | The unit’s movement and several sources of forced movement are restricted by barriers, but it can still act. Units do not try to path around them; manual guidance is required. [corpus:liquipedia_dota2/mechanics@2378401#Status_effects] |
| Taunt | The unit is forced to attack a specified target, ignoring player input. [corpus:liquipedia_dota2/mechanics@2378401#Status_effects] |
| Fear | The unit is forced to run toward its team’s fountain, ignoring player input. [corpus:liquipedia_dota2/mechanics@2378401#Status_effects] |
| Hypnosis | The unit is forced to move toward a hypnotizing source, ignoring player input. [corpus:liquipedia_dota2/mechanics@2378401#Status_effects] |
| Forced Movement | The unit is forced to move in a specified direction, ignoring player input. [corpus:liquipedia_dota2/mechanics@2378401#Status_effects] |
| Teleport/Blink | The unit moves to a location instantaneously. [corpus:liquipedia_dota2/mechanics@2378401#Status_effects] |
| Invisibility | The unit cannot be seen by normal vision but can be detected by True Sight. [corpus:liquipedia_dota2/mechanics@2378401#Status_effects] |
| Phased | The unit can move through other units, ignoring collision size. [corpus:liquipedia_dota2/mechanics@2378401#Status_effects] |
| Invulnerability | The unit is immune to most damage sources, and most spells cannot target it. [corpus:liquipedia_dota2/mechanics@2378401#Status_effects] |
| Hidden | Comes with invulnerability and provides even greater protection from spells. [corpus:liquipedia_dota2/mechanics@2378401#Status_effects] |
| Debuff Immunity | The unit becomes immune to pure and reflected damage. For the effect’s duration, most negative effects applied by enemy spells have no effect. [corpus:liquipedia_dota2/mechanics@2378401#Status_effects] |
| Spell Immunity | The unit cannot be targeted or affected by most spells. [corpus:liquipedia_dota2/mechanics@2378401#Status_effects] |
| Spell Block | Protects the unit from most single-target abilities, ranging from basic small abilities to the strongest single-target ultimates. [corpus:liquipedia_dota2/mechanics@2378401#Status_effects] |
| Attack Immunity | The unit cannot be attacked, and already-launched attack projectiles cannot harm or affect it. The unit remains affected by physical spell damage. [corpus:liquipedia_dota2/mechanics@2378401#Status_effects] |
| Ethereal | The unit assumes a ghostly form, becoming immune to physical damage but usually taking more magical damage. Ethereal units are disarmed and attack immune. [corpus:liquipedia_dota2/mechanics@2378401#Status_effects] |

### Dispelling

Dispel methods remove buffs, debuffs, and status effects and are important to understanding Dota 2’s internal interactions. [corpus:liquipedia_dota2/mechanics@2378401#Dispelling]

| Mechanic | Introduction |
|---|---|
| Basic Dispel | A simple dispel granted by abilities and items. [corpus:liquipedia_dota2/mechanics@2378401#Dispelling] |
| Strong Dispel | A greater dispel that removes more status effects and is granted by a handful of abilities. [corpus:liquipedia_dota2/mechanics@2378401#Dispelling] |
| Death Dispel | The strongest and rarest dispel type. It removes nearly all status effects. [corpus:liquipedia_dota2/mechanics@2378401#Dispelling] |
| Spell Immunity | Dispels some abilities. [corpus:liquipedia_dota2/mechanics@2378401#Dispelling] |

## Gameplay

| Mechanic | Introduction |
|---|---|
| Game Modes | Map conditions with different rulesets for hero picking and other variables. [corpus:liquipedia_dota2/mechanics@2378401#Gameplay] |
| Custom Games; Modding | Community-created game modes with their own rules and assets. Custom games are made through modding. [corpus:liquipedia_dota2/mechanics@2378401#Gameplay] |
| Head-up Display (HUD) | The in-game graphical interface showing a hero’s portrait, abilities, items, stats, and more. [corpus:liquipedia_dota2/mechanics@2378401#Gameplay] |
| Minimap; Scan | The minimap is a small graphical representation of the game map where heroes and other information can be seen. Scanning reveals the presence of enemies on it. [corpus:liquipedia_dota2/mechanics@2378401#Gameplay] |
| Disjoint | Dodging a projectile with an ability or item. Not all projectiles can be disjointed. [corpus:liquipedia_dota2/mechanics@2378401#Gameplay] |
| Denying | Killing a low-health friendly hero, creep or building. Denying prevents enemy heroes from gaining gold and experience from the denied unit or building. [corpus:liquipedia_dota2/mechanics@2378401#Gameplay] |
| Creep Control Techniques | Methods of manipulating creeps for positioning or to spawn more creeps to kill later. [corpus:liquipedia_dota2/mechanics@2378401#Gameplay] |
| Roles | Play styles that heroes fulfill to serve a specific function for their team. [corpus:liquipedia_dota2/mechanics@2378401#Gameplay] |
| Ganking | Ambushing and attacking isolated enemy heroes to secure an early-game advantage. [corpus:liquipedia_dota2/mechanics@2378401#Gameplay] |
| Pushing | Focusing on destroying buildings and pressuring the lanes. [corpus:liquipedia_dota2/mechanics@2378401#Gameplay] |
| Harassment | Attacking opponents to intimidate them from farming effectively, especially during the early game. [corpus:liquipedia_dota2/mechanics@2378401#Gameplay] |
| Farming | Accumulating gold by killing as many creeps as possible. [corpus:liquipedia_dota2/mechanics@2378401#Gameplay] |
| Jungling | Farming in the jungle by killing neutral creeps instead of farming in the lanes. [corpus:liquipedia_dota2/mechanics@2378401#Gameplay] |
| Initiating | Starting a teamfight, usually by first disabling opponents with powerful abilities. [corpus:liquipedia_dota2/mechanics@2378401#Gameplay] |

## System

System mechanics are major functions not directly part of the game, involving features related to player input, Steam, and others. [corpus:liquipedia_dota2/mechanics@2378401#System]

| Mechanic | Introduction |
|---|---|
| Patches | Game-client updates that include changes to elements outside mechanics, such as cosmetic items or the graphical interface. [corpus:liquipedia_dota2/mechanics@2378401#System] |
| Versions | Game-mechanics updates, including new heroes, items, and balance adjustments. Versions are shipped with patches. [corpus:liquipedia_dota2/mechanics@2378401#System] |
| Trophies & Profile Levels | In-game achievements awarded for accomplishing various feats. [corpus:liquipedia_dota2/mechanics@2378401#System] |
| Events | Time-limited promotions with exclusive cosmetic items, trophies, and more. They usually occur around big tournaments and holidays. [corpus:liquipedia_dota2/mechanics@2378401#System] |
| Spectating; Replay | A function allowing players to watch live games and replays of past games. [corpus:liquipedia_dota2/mechanics@2378401#System] |

### Settings

Game settings let users change display, graphics, audio, and control settings. [corpus:liquipedia_dota2/mechanics@2378401#Settings]

| Mechanic | Introduction |
|---|---|
| Controls; Hotkeys; Chat Wheel | Settings for hotkeys, mouse-cursor interactions, and the in-game chat wheel. [corpus:liquipedia_dota2/mechanics@2378401#Settings] |
| Launch Options | Command lines that can be entered in Steam’s settings to change the Dota 2 client. [corpus:liquipedia_dota2/mechanics@2378401#Settings] |
| Console Commands | Commands usable through the in-game console. [corpus:liquipedia_dota2/mechanics@2378401#Settings] |
| Cheats | Official cheats usable in private lobbies for testing. Cheats cannot be used in matchmaking. [corpus:liquipedia_dota2/mechanics@2378401#Settings] |

### Matchmaking

Matchmaking is an automated system that finds and matches players together, usually through internal calculations of player skill. Casual and ranked matchmaking are both available. [corpus:liquipedia_dota2/mechanics@2378401#Matchmaking]

| Mechanic | Introduction |
|---|---|
| Matchmaking Rating | The value determining a player’s skill level, also called MMR. Winning increases the rating, while losing decreases it. [corpus:liquipedia_dota2/mechanics@2378401#Matchmaking] |
| Leaderboards | Regional ladder rankings for the top players with the highest matchmaking rating. [corpus:liquipedia_dota2/mechanics@2378401#Matchmaking] |
| Bots | AI-controlled heroes that players can choose to match with. [corpus:liquipedia_dota2/mechanics@2378401#Matchmaking] |
| Priority | An internal flag determining whom players are matched with. Players with a history of bad conduct enter low priority and can only match with others in low priority. [corpus:liquipedia_dota2/mechanics@2378401#Matchmaking] |
| Ban; Report; Commend; Player Behavior Summary | Punishments are given to players who violate rules or community norms. Communication bans are based on feedback from other players. Total game bans are given to players who use third-party programs to cheat. [corpus:liquipedia_dota2/mechanics@2378401#Matchmaking] |

### Cosmetic Items

Cosmetic items alter the appearance of heroes and various interface elements. They are purely cosmetic and do not affect game mechanics. [corpus:liquipedia_dota2/mechanics@2378401#Cosmetic_items]

| Mechanic | Introduction |
|---|---|
| Item Drop System; Drop List | Cosmetic items drop randomly after matches. Rare items drop less often. [corpus:liquipedia_dota2/mechanics@2378401#Cosmetic_items] |
| Rarity | An item property scaling from Common to Arcana. Rarer items are generally harder to obtain and contain more customizations. [corpus:liquipedia_dota2/mechanics@2378401#Cosmetic_items] |
| Quality | An item property associated with the circumstances of the item’s origin. [corpus:liquipedia_dota2/mechanics@2378401#Cosmetic_items] |
| Armory | The in-game interface where all cosmetic items are stored. [corpus:liquipedia_dota2/mechanics@2378401#Cosmetic_items] |
| Treasures | Boxes that can be opened to obtain random cosmetic items. [corpus:liquipedia_dota2/mechanics@2378401#Cosmetic_items] |
| Gems | Modifiers socketable into some items to grant a counter or custom effects. [corpus:liquipedia_dota2/mechanics@2378401#Cosmetic_items] |
| Music | Soundtracks that play according to game events. Numerous custom music packs exist. [corpus:liquipedia_dota2/mechanics@2378401#Cosmetic_items] |
| Steam Market | A community marketplace where cosmetic items can be bought and sold. [corpus:liquipedia_dota2/mechanics@2378401#Cosmetic_items] |
| Trading | Trading cosmetic items with a Steam friend, subject to certain restrictions. [corpus:liquipedia_dota2/mechanics@2378401#Cosmetic_items] |
| Gifting | Sending cosmetic items to a friend as a gift, subject to certain restrictions. [corpus:liquipedia_dota2/mechanics@2378401#Cosmetic_items] |