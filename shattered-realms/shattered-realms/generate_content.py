#!/usr/bin/env python3
"""
Generate comprehensive Foundry VTT compendium data for The Shattered Realms
"""
import json
import os
import uuid

def generate_id():
    return str(uuid.uuid4()).replace('-', '')[:16]

# ACTORS - NPCs and Monsters
actors = [
    {
        "_id": generate_id(),
        "name": "Valdris the Shattered",
        "type": "npc",
        "img": "icons/magic/death/skull-horned-worn-fire-blue.webp",
        "system": {
            "abilities": {
                "str": {"value": 11},
                "dex": {"value": 16},
                "con": {"value": 16},
                "int": {"value": 20},
                "wis": {"value": 14},
                "cha": {"value": 16}
            },
            "attributes": {
                "ac": {"value": 17},
                "hp": {"value": 135, "max": 135},
                "movement": {"walk": 30, "fly": 30}
            },
            "details": {
                "cr": 13,
                "type": {"value": "undead"},
                "alignment": "Neutral Evil",
                "biography": {"value": "<p>Once a brilliant archmage, Valdris was consumed by his obsession with controlling the Shattered Rifts. He transformed himself into a lich, believing undeath would give him the centuries needed to master planar magic. Now he seeks to tear open all the rifts simultaneously, merging the planes into one chaotic realm under his control.</p>"}
            }
        }
    },
    {
        "_id": generate_id(),
        "name": "Grommak Shadowfang",
        "type": "npc",
        "img": "icons/creatures/abilities/mouth-teeth-long-red.webp",
        "system": {
            "abilities": {
                "str": {"value": 18},
                "dex": {"value": 12},
                "con": {"value": 16},
                "int": {"value": 12},
                "wis": {"value": 14},
                "cha": {"value": 14}
            },
            "attributes": {
                "ac": {"value": 16},
                "hp": {"value": 93, "max": 93},
                "movement": {"walk": 30}
            },
            "details": {
                "cr": 5,
                "type": {"value": "humanoid"},
                "alignment": "Lawful Neutral",
                "biography": {"value": "<p>Chieftain of the Shadowfang Clan, Grommak is a visionary orc leader who believes his people's future lies in civilization, not endless war. He has forbidden raiding and instead focuses on building, trading, and proving that orcs can be more than monsters. This makes him beloved by his progressive followers and reviled by traditionalist orcs.</p>"}
            }
        }
    },
    {
        "_id": generate_id(),
        "name": "Rift Troll",
        "type": "npc",
        "img": "icons/creatures/mammals/bull-horned-glowing-orange.webp",
        "system": {
            "abilities": {
                "str": {"value": 20},
                "dex": {"value": 8},
                "con": {"value": 20},
                "int": {"value": 5},
                "wis": {"value": 9},
                "cha": {"value": 5}
            },
            "attributes": {
                "ac": {"value": 15},
                "hp": {"value": 115, "max": 115},
                "movement": {"walk": 30}
            },
            "details": {
                "cr": 7,
                "type": {"value": "giant"},
                "alignment": "Chaotic Evil",
                "biography": {"value": "<p>Trolls that have been exposed to rift energy develop strange mutations. Some can blink short distances, others regenerate even faster than normal, and a few can temporarily phase through solid matter. All are more aggressive and cunning than typical trolls.</p>"}
            }
        }
    },
    {
        "_id": generate_id(),
        "name": "Bloodaxe Orc Raider",
        "type": "npc",
        "img": "icons/weapons/axes/axe-double-engraved.webp",
        "system": {
            "abilities": {
                "str": {"value": 16},
                "dex": {"value": 12},
                "con": {"value": 16},
                "int": {"value": 7},
                "wis": {"value": 11},
                "cha": {"value": 10}
            },
            "attributes": {
                "ac": {"value": 13},
                "hp": {"value": 30, "max": 30},
                "movement": {"walk": 30}
            },
            "details": {
                "cr": 1,
                "type": {"value": "humanoid"},
                "alignment": "Chaotic Evil",
                "biography": {"value": "<p>The Bloodaxe Tribe rejects civilization and clings to the old orc ways of raiding and pillaging. They view the Shadowfang Clan as traitors and regularly attack them to 'remind them of their true nature.' They also raid human and dwarf settlements.</p>"}
            }
        }
    },
    {
        "_id": generate_id(),
        "name": "Twilight Druid",
        "type": "npc",
        "img": "icons/magic/nature/root-vine-entangled-hand.webp",
        "system": {
            "abilities": {
                "str": {"value": 10},
                "dex": {"value": 14},
                "con": {"value": 12},
                "int": {"value": 12},
                "wis": {"value": 18},
                "cha": {"value": 11}
            },
            "attributes": {
                "ac": {"value": 14},
                "hp": {"value": 45, "max": 45},
                "movement": {"walk": 30}
            },
            "details": {
                "cr": 4,
                "type": {"value": "humanoid"},
                "alignment": "Chaotic Neutral",
                "biography": {"value": "<p>These elven druids have been corrupted by the twilight energy seeping from the rifts in their forest. They now view the rifts as the ultimate expression of nature's chaos and work to expand them. Their magic is twisted, creating aberrant plants and warping the natural order.</p>"}
            }
        }
    },
    {
        "_id": generate_id(),
        "name": "Rift Goblin",
        "type": "npc",
        "img": "icons/creatures/eyes/lizard-single-slit-pink.webp",
        "system": {
            "abilities": {
                "str": {"value": 8},
                "dex": {"value": 16},
                "con": {"value": 10},
                "int": {"value": 10},
                "wis": {"value": 8},
                "cha": {"value": 8}
            },
            "attributes": {
                "ac": {"value": 14},
                "hp": {"value": 12, "max": 12},
                "movement": {"walk": 30}
            },
            "details": {
                "cr": "1/2",
                "type": {"value": "humanoid"},
                "alignment": "Chaotic Evil",
                "biography": {"value": "<p>Goblins that live near rifts develop strange abilities. These particular goblins can briefly become incorporeal, allowing them to dodge attacks or slip through barriers. They use this ability to steal and ambush travelers near rift zones.</p>"}
            }
        }
    },
    {
        "_id": generate_id(),
        "name": "Phase Spider Matriarch",
        "type": "npc",
        "img": "icons/creatures/invertebrates/spider-large-giant-web.webp",
        "system": {
            "abilities": {
                "str": {"value": 18},
                "dex": {"value": 17},
                "con": {"value": 16},
                "int": {"value": 6},
                "wis": {"value": 12},
                "cha": {"value": 6}
            },
            "attributes": {
                "ac": {"value": 14},
                "hp": {"value": 68, "max": 68},
                "movement": {"walk": 40, "climb": 40}
            },
            "details": {
                "cr": 5,
                "type": {"value": "monstrosity"},
                "alignment": "Unaligned",
                "biography": {"value": "<p>An unusually large phase spider that has made its lair near a rift. It can shift between the Material and Ethereal planes, and has learned to drag prey into the Ethereal plane where its webbing is even stronger.</p>"}
            }
        }
    },
    {
        "_id": generate_id(),
        "name": "Rift Demon",
        "type": "npc",
        "img": "icons/magic/unholy/strike-beam-blood-red-purple.webp",
        "system": {
            "abilities": {
                "str": {"value": 18},
                "dex": {"value": 15},
                "con": {"value": 16},
                "int": {"value": 11},
                "wis": {"value": 12},
                "cha": {"value": 14}
            },
            "attributes": {
                "ac": {"value": 16},
                "hp": {"value": 85, "max": 85},
                "movement": {"walk": 40, "fly": 40}
            },
            "details": {
                "cr": 6,
                "type": {"value": "fiend"},
                "alignment": "Chaotic Evil",
                "biography": {"value": "<p>Demons occasionally slip through the rifts from the Abyss. This particular demon has learned to use the rifts to teleport short distances and is hunting for a way to permanently open a rift to allow more demons through.</p>"}
            }
        }
    },
    {
        "_id": generate_id(),
        "name": "Sir Gareth Stonewatch",
        "type": "npc",
        "img": "icons/equipment/chest/breastplate-layered-steel.webp",
        "system": {
            "abilities": {
                "str": {"value": 16},
                "dex": {"value": 11},
                "con": {"value": 14},
                "int": {"value": 11},
                "wis": {"value": 12},
                "cha": {"value": 14}
            },
            "attributes": {
                "ac": {"value": 18},
                "hp": {"value": 58, "max": 58},
                "movement": {"walk": 30}
            },
            "details": {
                "cr": 3,
                "type": {"value": "humanoid"},
                "alignment": "Lawful Good",
                "biography": {"value": "<p>A knight of the Order of the Adamant Shield, Sir Gareth has dedicated his life to protecting common folk from rift-spawned monsters. He is brave, honorable, and sometimes recklessly charges into danger to save innocents.</p>"}
            }
        }
    },
    {
        "_id": generate_id(),
        "name": "Elara Moonwhisper",
        "type": "npc",
        "img": "icons/magic/light/beam-rays-blue-large.webp",
        "system": {
            "abilities": {
                "str": {"value": 8},
                "dex": {"value": 14},
                "con": {"value": 12},
                "int": {"value": 18},
                "wis": {"value": 15},
                "cha": {"value": 13}
            },
            "attributes": {
                "ac": {"value": 15},
                "hp": {"value": 60, "max": 60},
                "movement": {"walk": 30}
            },
            "details": {
                "cr": 8,
                "type": {"value": "humanoid"},
                "alignment": "Neutral Good",
                "biography": {"value": "<p>Archmage and leader of the Circle of Binding, Elara is one of the most powerful wizards in the realm. She believes the rifts are a blight that must be sealed permanently, and dedicates all her resources to finding a way to do so. She can be zealous in pursuit of this goal.</p>"}
            }
        }
    }
]

# ITEMS - Magic Items and Equipment
items = [
    {
        "_id": generate_id(),
        "name": "Riftblade",
        "type": "weapon",
        "img": "icons/weapons/swords/sword-guard-purple.webp",
        "system": {
            "description": {
                "value": "<p><strong>Weapon (longsword), very rare (requires attunement)</strong></p><p>This blade was forged from metal harvested from a collapsed rift. It shimmers with otherworldly energy and can cut through the fabric of reality itself.</p><p><strong>Properties:</strong></p><ul><li>+2 to attack and damage rolls</li><li>Deals an additional 1d6 force damage on hit</li><li>Once per day, you can use an action to slash open a small rift that allows you to teleport up to 60 feet to an unoccupied space you can see</li><li>You have advantage on saving throws against spells and effects that involve planar travel or dimensional shifting</li></ul>",
                "chat": "",
                "unidentified": "A sword that seems to shimmer and blur slightly, as if not quite fully present in this reality."
            },
            "quantity": 1,
            "weight": 3,
            "rarity": "veryRare",
            "identified": True,
            "activation": {"type": "action", "cost": 1},
            "damage": {
                "parts": [["1d8 + 2", "slashing"], ["1d6", "force"]]
            },
            "weaponType": "martialM",
            "properties": {"ver": True}
        }
    },
    {
        "_id": generate_id(),
        "name": "Amulet of Planar Anchoring",
        "type": "equipment",
        "img": "icons/equipment/neck/amulet-jeweled-gold-blue.webp",
        "system": {
            "description": {
                "value": "<p><strong>Wondrous item, rare (requires attunement)</strong></p><p>This amulet contains a fragment of stabilized reality, anchoring you to the Material Plane.</p><p><strong>Properties:</strong></p><ul><li>You cannot be unwillingly teleported, banished, or sent to another plane</li><li>You have advantage on saving throws against effects from rifts</li><li>You can sense the direction and approximate distance to the nearest rift within 1 mile</li><li>Once per long rest, you can cast <em>dispel magic</em> on a rift-related magical effect</li></ul>",
                "chat": "",
                "unidentified": "An amulet that feels unusually solid and real when held."
            },
            "quantity": 1,
            "weight": 0.5,
            "rarity": "rare",
            "identified": True,
            "armor": {"type": "trinket"}
        }
    },
    {
        "_id": generate_id(),
        "name": "Staff of Reality Weaving",
        "type": "weapon",
        "img": "icons/weapons/staves/staff-ornate-purple.webp",
        "system": {
            "description": {
                "value": "<p><strong>Staff, legendary (requires attunement by a spellcaster)</strong></p><p>This staff was created by studying the nature of rifts. It allows its wielder to subtly manipulate reality.</p><p><strong>Properties:</strong></p><ul><li>+2 to spell attack rolls and spell save DC</li><li>Grants the ability to cast <em>teleport</em> once per day without using a spell slot</li><li>You can spend 1 minute to create a temporary minor rift that acts as a portal to any location on the Material Plane you have visited before (lasts 10 minutes)</li><li>Creatures have disadvantage on saving throws against your spells that involve force damage or dimensional effects</li></ul><p><strong>Curse:</strong> Each time you use the staff's rift-creating power, roll a d20. On a 1, the rift becomes unstable and summons 1d4 hostile creatures from a random plane.</p>",
                "chat": "",
                "unidentified": "A staff carved with strange symbols that seem to shift when not directly observed."
            },
            "quantity": 1,
            "weight": 4,
            "rarity": "legendary",
            "identified": True,
            "weaponType": "simpleM",
            "damage": {
                "parts": [["1d6", "bludgeoning"]]
            }
        }
    },
    {
        "_id": generate_id(),
        "name": "Boots of Phase Walking",
        "type": "equipment",
        "img": "icons/equipment/feet/boots-armored-steel.webp",
        "system": {
            "description": {
                "value": "<p><strong>Wondrous item, uncommon (requires attunement)</strong></p><p>These boots shimmer with ethereal energy, allowing brief shifts between planes.</p><p><strong>Properties:</strong></p><ul><li>As a bonus action, you can partially phase into the Ethereal Plane until the start of your next turn. While phased, you can move through other creatures and objects as if they were difficult terrain. You take 1d10 force damage if you end your turn inside an object.</li><li>You can use this ability 3 times per long rest</li><li>You have advantage on Dexterity saving throws to avoid traps</li></ul>",
                "chat": "",
                "unidentified": "Boots that seem slightly transparent."
            },
            "quantity": 1,
            "weight": 2,
            "rarity": "uncommon",
            "identified": True,
            "armor": {"type": "clothing"}
        }
    },
    {
        "_id": generate_id(),
        "name": "Cloak of Many Planes",
        "type": "equipment",
        "img": "icons/equipment/back/cloak-collared-blue.webp",
        "system": {
            "description": {
                "value": "<p><strong>Wondrous item, very rare (requires attunement)</strong></p><p>This cloak has been woven from threads taken from different planes of existence.</p><p><strong>Properties:</strong></p><ul><li>You gain resistance to one damage type of your choice (fire, cold, lightning, acid, or thunder). You can change this resistance after a long rest.</li><li>Once per day, you can cast <em>plane shift</em> to transport yourself and up to 8 willing creatures to a location on a different plane that you have visited before</li><li>You can understand (but not speak) all languages</li></ul>",
                "chat": "",
                "unidentified": "A cloak that shifts colors and patterns constantly."
            },
            "quantity": 1,
            "weight": 1,
            "rarity": "veryRare",
            "identified": True,
            "armor": {"type": "clothing"}
        }
    },
    {
        "_id": generate_id(),
        "name": "Ring of Rift Sight",
        "type": "equipment",
        "img": "icons/equipment/finger/ring-band-simple-rounded-copper.webp",
        "system": {
            "description": {
                "value": "<p><strong>Ring, uncommon (requires attunement)</strong></p><p>This ring allows you to perceive rifts and planar instabilities.</p><p><strong>Properties:</strong></p><ul><li>You can see invisible creatures and objects within 60 feet</li><li>You can see into the Ethereal Plane to a distance of 60 feet</li><li>You can automatically detect rifts within 120 feet and can sense their approximate size and stability</li><li>You have disadvantage on saving throws against gaze attacks and similar vision-based effects</li></ul>",
                "chat": "",
                "unidentified": "A ring with a strange crystalline setting."
            },
            "quantity": 1,
            "weight": 0,
            "rarity": "uncommon",
            "identified": True,
            "armor": {"type": "trinket"}
        }
    },
    {
        "_id": generate_id(),
        "name": "Shadowfang War Axe",
        "type": "weapon",
        "img": "icons/weapons/axes/axe-broad-black.webp",
        "system": {
            "description": {
                "value": "<p><strong>Weapon (greataxe), rare</strong></p><p>This axe was forged by the Shadowfang Clan as a symbol of their new way. It combines orcish warrior tradition with dwarven craftsmanship.</p><p><strong>Properties:</strong></p><ul><li>+1 to attack and damage rolls</li><li>When you score a critical hit, the target must succeed on a DC 15 Wisdom saving throw or be frightened of you until the end of your next turn</li><li>You have advantage on Charisma (Intimidation) checks while wielding this weapon</li></ul>",
                "chat": "",
                "unidentified": "A well-crafted axe with orcish and dwarven symbols."
            },
            "quantity": 1,
            "weight": 7,
            "rarity": "rare",
            "identified": True,
            "weaponType": "martialM",
            "damage": {
                "parts": [["1d12 + 1", "slashing"]]
            },
            "properties": {"hvy": True, "two": True}
        }
    },
    {
        "_id": generate_id(),
        "name": "Potion of Rift Resistance",
        "type": "consumable",
        "img": "icons/consumables/potions/potion-flask-corked-blue.webp",
        "system": {
            "description": {
                "value": "<p><strong>Potion, uncommon</strong></p><p>This swirling, iridescent potion protects against the corrupting influence of rifts.</p><p>When you drink this potion, for the next hour you have advantage on all saving throws against effects caused by rifts, and you take half damage from any damage caused by rift energy or rift-spawned creatures.</p>",
                "chat": "",
                "unidentified": "A potion with strange colors swirling inside."
            },
            "quantity": 1,
            "weight": 0.5,
            "rarity": "uncommon",
            "identified": True,
            "consumableType": "potion",
            "uses": {
                "value": 1,
                "max": 1,
                "per": "charges"
            },
            "activation": {"type": "action", "cost": 1}
        }
    },
    {
        "_id": generate_id(),
        "name": "Twilight Crystal",
        "type": "loot",
        "img": "icons/commodities/gems/gem-rough-teal.webp",
        "system": {
            "description": {
                "value": "<p><strong>Wondrous item, rare</strong></p><p>A crystal harvested from the Twilight Forest, infused with rift energy. Valued by wizards and alchemists.</p><p>A twilight crystal can be used as a material component for spells that manipulate time, space, or reality. When used this way, the spell's save DC increases by 1.</p><p>Alternatively, a wizard can spend 1 hour to absorb the crystal's energy, gaining the ability to cast one additional spell of 3rd level or lower without using a spell slot. The crystal is consumed in this process.</p><p><strong>Market Value:</strong> 500-800 gold pieces.</p>",
                "chat": "",
                "unidentified": "A strange glowing crystal."
            },
            "quantity": 1,
            "weight": 0.1,
            "rarity": "rare",
            "identified": True
        }
    },
    {
        "_id": generate_id(),
        "name": "Rift Shard",
        "type": "loot",
        "img": "icons/commodities/materials/glass-faceted-black.webp",
        "system": {
            "description": {
                "value": "<p><strong>Material component, very rare</strong></p><p>A fragment of solidified rift energy. Extremely dangerous to handle but incredibly valuable.</p><p>A rift shard can be used as a focus for planar magic. Any spell you cast that involves summoning, banishment, teleportation, or planar travel has its range increased by 50%.</p><p>A rift shard can also be consumed to power a ritual that creates a temporary rift. This requires 1 hour and a successful DC 18 Arcana check. On success, a rift opens that remains stable for 10 minutes. On failure, the shard explodes, dealing 10d6 force damage to all creatures within 20 feet.</p><p><strong>Market Value:</strong> 2,000-5,000 gold pieces (if you can find a buyer).</p>",
                "chat": "",
                "unidentified": "A shard of something that hurts to look at directly."
            },
            "quantity": 1,
            "weight": 0.5,
            "rarity": "veryRare",
            "identified": True
        }
    }
]

# TABLES - Rollable tables for encounters and events
tables = [
    {
        "_id": generate_id(),
        "name": "Random Rift Encounters",
        "img": "icons/magic/symbols/runes-star-pentagon-blue.webp",
        "description": "Roll when characters approach or investigate a rift",
        "formula": "1d20",
        "results": [
            {"range": [1, 3], "text": "Rift Goblins (1d6+2) are scavenging near the rift", "img": "icons/creatures/eyes/lizard-single-slit-pink.webp"},
            {"range": [4, 6], "text": "A Rift Demon is attempting to stabilize the rift to allow more demons through", "img": "icons/magic/unholy/strike-beam-blood-red-purple.webp"},
            {"range": [7, 9], "text": "Phase Spider Matriarch with 1d4+1 young phase spiders hunting near the rift", "img": "icons/creatures/invertebrates/spider-large-giant-web.webp"},
            {"range": [10, 12], "text": "The rift suddenly pulses, all within 30 feet must make DC 15 Charisma save or be teleported 1d100 feet in a random direction", "img": "icons/magic/symbols/runes-triangle-blue.webp"},
            {"range": [13, 15], "text": "A group of Rift Walkers are studying the rift and offer information or assistance", "img": "icons/environment/people/group-men-grey.webp"},
            {"range": [16, 17], "text": "Twilight Druids are performing a ritual to expand the rift", "img": "icons/magic/nature/root-vine-entangled-hand.webp"},
            {"range": [18, 19], "text": "A Rift Troll bursts from the rift, disoriented and aggressive", "img": "icons/creatures/mammals/bull-horned-glowing-orange.webp"},
            {"range": [20, 20], "text": "The rift briefly connects to a beneficial plane - roll on the Beneficial Rift Effects table", "img": "icons/magic/light/orbs-group-purple.webp"}
        ]
    },
    {
        "_id": generate_id(),
        "name": "Rift Treasure",
        "img": "icons/containers/chest/chest-reinforced-steel-red.webp",
        "description": "Treasures found in rift zones or on rift-related enemies",
        "formula": "1d12",
        "results": [
            {"range": [1, 3], "text": "1d4 x 100 gold pieces and a random common magic item", "img": "icons/commodities/currency/coins-assorted-mix-gold.webp"},
            {"range": [4, 6], "text": "1d3 Twilight Crystals (500 gp each)", "img": "icons/commodities/gems/gem-rough-teal.webp"},
            {"range": [7, 8], "text": "1 Rift Shard and 2d6 x 100 gold pieces", "img": "icons/commodities/materials/glass-faceted-black.webp"},
            {"range": [9, 10], "text": "Potion of Rift Resistance and 1d6 x 50 gold pieces", "img": "icons/consumables/potions/potion-flask-corked-blue.webp"},
            {"range": [11, 11], "text": "Random uncommon magic item with a rift theme", "img": "icons/equipment/finger/ring-band-simple-rounded-copper.webp"},
            {"range": [12, 12], "text": "Random rare magic item with planar properties", "img": "icons/equipment/neck/amulet-jeweled-gold-blue.webp"}
        ]
    },
    {
        "_id": generate_id(),
        "name": "Wilderness Encounters - Ironpeak Region",
        "img": "icons/environment/wilderness/terrain-mountain-rocky.webp",
        "description": "Random encounters in the Ironpeak Mountains",
        "formula": "1d12",
        "results": [
            {"range": [1, 2], "text": "Bloodaxe Orc Raiders (2d4) attacking a dwarf caravan", "img": "icons/weapons/axes/axe-double-engraved.webp"},
            {"range": [3, 4], "text": "Shadowfang Orc patrol (1d6+2) - potentially friendly if approached peacefully", "img": "icons/environment/people/group-men-grey.webp"},
            {"range": [5, 6], "text": "Cave entrance leading to Deep Roads (possibly infested)", "img": "icons/environment/wilderness/cave-entrance-mountain.webp"},
            {"range": [7, 8], "text": "Evidence of recent giant activity (tracks, destroyed trees, etc.)", "img": "icons/skills/wounds/bone-broken-marrow-yellow.webp"},
            {"range": [9, 10], "text": "Abandoned dwarven outpost with potential treasure or danger", "img": "icons/environment/settlement/house-stone.webp"},
            {"range": [11, 11], "text": "Small rift opening - roll on Random Rift Encounters table", "img": "icons/magic/symbols/runes-star-pentagon-blue.webp"},
            {"range": [12, 12], "text": "Dwarf merchant caravan willing to trade or share information", "img": "icons/environment/people/commoner-cart.webp"}
        ]
    },
    {
        "_id": generate_id(),
        "name": "Twilight Forest Encounters",
        "img": "icons/environment/wilderness/tree-oak.webp",
        "description": "Encounters in the corrupted Twilight Forest",
        "formula": "1d10",
        "results": [
            {"range": [1, 2], "text": "Twilight Druids (1d4) performing a corruption ritual", "img": "icons/magic/nature/root-vine-entangled-hand.webp"},
            {"range": [3, 4], "text": "Corrupted treants attacking anything that moves", "img": "icons/magic/nature/tree-animated-strike.webp"},
            {"range": [5, 6], "text": "Illusion or time distortion - make DC 14 Wisdom save or become confused for 1d4 rounds", "img": "icons/magic/perception/eye-ringed-glow-yellow.webp"},
            {"range": [7, 8], "text": "Refugees from Silverleaf fleeing deeper corruption", "img": "icons/environment/people/commoner-family.webp"},
            {"range": [9, 9], "text": "Portal to the Feywild appears briefly - opportunity or danger", "img": "icons/magic/symbols/runes-star-purple.webp"},
            {"range": [10, 10], "text": "Ancient elven shrine with protective magic still functioning", "img": "icons/environment/settlement/temple.webp"}
        ]
    },
    {
        "_id": generate_id(),
        "name": "Rift City Random Events",
        "img": "icons/environment/settlement/city-many-towers.webp",
        "description": "Daily events and encounters in Rift City",
        "formula": "1d20",
        "results": [
            {"range": [1, 4], "text": "Nothing unusual - normal city life", "img": "icons/environment/people/group-men-grey.webp"},
            {"range": [5, 8], "text": "Merchant offers to sell rift-related goods or information", "img": "icons/environment/people/commoner-merchant.webp"},
            {"range": [9, 11], "text": "Argument between Circle of Binding and Rift Walkers members - might escalate", "img": "icons/skills/social/diplomacy-handshake.webp"},
            {"range": [12, 14], "text": "Something unusual emerged from the Central Rift last night - rumors spread", "img": "icons/magic/symbols/runes-star-pentagon-blue.webp"},
            {"range": [15, 16], "text": "Job opportunity posted - escort needed for rift zone expedition", "img": "icons/sundries/documents/document-sealed-brown-red.webp"},
            {"range": [17, 18], "text": "Pickpocket or con artist targets the party", "img": "icons/skills/trades/woodcutting-sawing-logger-brown.webp"},
            {"range": [19, 19], "text": "Planar merchant from another plane selling exotic goods", "img": "icons/containers/boxes/crate-wooden-reinforced.webp"},
            {"range": [20, 20], "text": "Important NPC seeks party's help with urgent matter", "img": "icons/environment/people/cleric-orange.webp"}
        ]
    }
]

# JOURNALS - More lore and quest information
journals_additional = [
    {
        "_id": generate_id(),
        "name": "Quest: The Broken Tower",
        "pages": [
            {
                "_id": generate_id(),
                "name": "Quest Overview",
                "type": "text",
                "title": {"show": True, "level": 1},
                "text": {
                    "format": 1,
                    "content": """
                    <h1>The Broken Tower</h1>
                    <p><strong>Level Range:</strong> 1-3</p>
                    <p><strong>Location:</strong> 15 miles east of Rift City</p>
                    
                    <h2>Hook</h2>
                    <p>Strange lights and sounds have been reported from the ruins of Malachar's Tower, an abandoned wizard's spire that was damaged during the Cataclysm. The Circle of Binding offers 200 gold to investigate and ensure no dangerous rift activity is occurring there.</p>
                    
                    <h2>Background</h2>
                    <p>Malachar was one of the archmages whose war created the Shattered Rifts. His tower was partially destroyed in the final battle. Recently, a group of cultists discovered his hidden laboratory and are attempting to recreate his rift-opening experiments.</p>
                    
                    <h2>Key NPCs</h2>
                    <ul>
                        <li><strong>Elara Moonwhisper</strong> - Quest giver, will provide background information</li>
                        <li><strong>Kragnis the Vile</strong> - Cult leader, 4th level evil wizard attempting to open a permanent rift</li>
                        <li><strong>Ghost of Malachar</strong> - Haunts the tower, may help or hinder depending on how he's approached</li>
                    </ul>
                    
                    <h2>Tower Layout</h2>
                    <p><strong>Ground Floor:</strong> Collapsed entrance hall, rift goblins scavenging (2d4)</p>
                    <p><strong>Second Floor:</strong> Old library with valuable scrolls, phase spider nest</p>
                    <p><strong>Third Floor:</strong> Malachar's ghost appears, will test the party's intentions</p>
                    <p><strong>Fourth Floor (Ruined):</strong> Open to sky, unstable rift pulsing with energy</p>
                    <p><strong>Laboratory (Hidden):</strong> Cultists performing ritual, must be stopped before they succeed</p>
                    
                    <h2>Rewards</h2>
                    <ul>
                        <li>200 gold from Circle of Binding</li>
                        <li>Scrolls from the library (3 random 1st level spells, 1 2nd level spell)</li>
                        <li>Malachar's Staff (quarterstaff +1) if ghost is appeased</li>
                        <li>Small rift shard from the destroyed ritual</li>
                        <li>Reputation with Circle of Binding</li>
                    </ul>
                    """
                }
            }
        ]
    },
    {
        "_id": generate_id(),
        "name": "Quest: Shadows of Ironpeak",
        "pages": [
            {
                "_id": generate_id(),
                "name": "Quest Overview",
                "type": "text",
                "title": {"show": True, "level": 1},
                "text": {
                    "format": 1,
                    "content": """
                    <h1>Shadows of Ironpeak</h1>
                    <p><strong>Level Range:</strong> 3-5</p>
                    <p><strong>Location:</strong> Ironpeak Mountains</p>
                    
                    <h2>Hook</h2>
                    <p>Bloodaxe orc raiders have been attacking both dwarven and Shadowfang settlements, wearing armor marked with symbols of both groups. Someone is trying to start a war. King Thrain and Chieftain Grommak both seek neutral investigators to uncover the truth before conflict erupts.</p>
                    
                    <h2>The Truth</h2>
                    <p>A group of dwarven hardliners who refuse to accept peace with the Shadowfang Clan have allied with a Bloodaxe warlord. They're staging false-flag attacks to reignite the old hatreds and drive the orcs from the mountains.</p>
                    
                    <h2>Key Locations</h2>
                    <ul>
                        <li><strong>Khaz-Durum:</strong> Dwarven capital, meet with King Thrain</li>
                        <li><strong>Shadowfang Hold:</strong> Orc fortress, meet with Grommak</li>
                        <li><strong>Attacked Villages:</strong> Investigate attack sites for clues</li>
                        <li><strong>Hidden Camp:</strong> Find the conspirators' base in the Deep Roads</li>
                    </ul>
                    
                    <h2>Challenges</h2>
                    <ul>
                        <li>Navigating political tensions between dwarves and orcs</li>
                        <li>Investigating attack sites before evidence disappears</li>
                        <li>Infiltrating or assaulting the conspirators' camp</li>
                        <li>Preventing the final false-flag attack</li>
                        <li>Exposing the conspiracy without causing a civil war</li>
                    </ul>
                    
                    <h2>Rewards</h2>
                    <ul>
                        <li>800 gold (400 from dwarves, 400 from Shadowfang)</li>
                        <li>Shadowfang War Axe or masterwork dwarven armor</li>
                        <li>Honorary membership in either dwarven or orc clan</li>
                        <li>Allies for future adventures</li>
                    </ul>
                    """
                }
            }
        ]
    },
    {
        "_id": generate_id(),
        "name": "Bestiary - Rift Creatures",
        "pages": [
            {
                "_id": generate_id(),
                "name": "Rift-Spawned Monsters",
                "type": "text",
                "title": {"show": True, "level": 1},
                "text": {
                    "format": 1,
                    "content": """
                    <h1>Rift-Spawned Creatures</h1>
                    
                    <h2>Rift Goblins</h2>
                    <p>Small humanoids mutated by proximity to rifts. They can briefly become incorporeal, allowing them to dodge attacks or slip through barriers.</p>
                    <p><strong>Tactics:</strong> Use hit-and-run tactics, phasing through walls to escape or attack from unexpected angles.</p>
                    <p><strong>Loot:</strong> Small amounts of copper/silver, occasionally a Twilight Crystal</p>
                    
                    <h2>Rift Trolls</h2>
                    <p>Trolls exposed to rift energy develop strange mutations. Some can teleport short distances, others regenerate even faster than normal.</p>
                    <p><strong>Variants:</strong></p>
                    <ul>
                        <li><strong>Blinking Troll:</strong> Can teleport up to 30 feet as a bonus action</li>
                        <li><strong>Phase Troll:</strong> Can become ethereal for brief moments</li>
                        <li><strong>Regenerating Troll:</strong> Regenerates 15 hp per turn instead of 10</li>
                    </ul>
                    
                    <h2>Rift Demons</h2>
                    <p>Demons that have slipped through rifts from the Abyss. They seek to widen the rifts to allow more of their kind through.</p>
                    <p><strong>Abilities:</strong> Rift teleportation, resistance to mundane weapons, corrupting presence</p>
                    <p><strong>Weakness:</strong> Rift-forged weapons deal extra damage to them</p>
                    
                    <h2>Twilight Beasts</h2>
                    <p>Animals and magical beasts corrupted by the twilight energy in the forest. They are more aggressive and often have reality-warping abilities.</p>
                    <p><strong>Common Types:</strong> Twilight wolves (pack hunters that can become briefly invisible), corrupted owlbears, phase spiders</p>
                    """
                }
            }
        ]
    }
]

# SCENES - Map locations
scenes = [
    {
        "_id": generate_id(),
        "name": "Rift City - Central Plaza",
        "img": "icons/environment/settlement/city-many-towers.webp",
        "width": 4000,
        "height": 3000,
        "padding": 0.25,
        "initial": {
            "x": 2000,
            "y": 1500,
            "scale": 0.5
        },
        "backgroundColor": "#999999",
        "gridType": 1,
        "grid": 100,
        "gridDistance": 5,
        "gridUnits": "ft",
        "shiftX": 0,
        "shiftY": 0,
        "description": "The heart of Rift City, built around the stabilized Central Rift. Markets, guildhalls, and the headquarters of major factions surround the pulsing planar gateway.",
        "notes": [],
        "tokens": [],
        "walls": []
    },
    {
        "_id": generate_id(),
        "name": "The Broken Tower - Level 1",
        "img": "icons/environment/settlement/tower-ruins.webp",
        "width": 2800,
        "height": 2800,
        "padding": 0,
        "initial": {
            "x": 1400,
            "y": 1400,
            "scale": 1
        },
        "backgroundColor": "#666666",
        "gridType": 1,
        "grid": 70,
        "gridDistance": 5,
        "gridUnits": "ft",
        "shiftX": 0,
        "shiftY": 0,
        "description": "Ground floor of Malachar's ruined tower. Collapsed entrance, scavenging rift goblins, and remnants of magical defenses.",
        "notes": [],
        "tokens": [],
        "walls": []
    },
    {
        "_id": generate_id(),
        "name": "Shadowfang Hold - Great Hall",
        "img": "icons/environment/settlement/house-stone.webp",
        "width": 3000,
        "height": 2400,
        "padding": 0.1,
        "initial": {
            "x": 1500,
            "y": 1200,
            "scale": 0.75
        },
        "backgroundColor": "#8B7355",
        "gridType": 1,
        "grid": 75,
        "gridDistance": 5,
        "gridUnits": "ft",
        "shiftX": 0,
        "shiftY": 0,
        "description": "The great hall of the Shadowfang Clan, where Chieftain Grommak holds court. Rebuilt from ancient dwarven ruins with a unique blend of orcish and dwarven architecture.",
        "notes": [],
        "tokens": [],
        "walls": []
    },
    {
        "_id": generate_id(),
        "name": "Twilight Forest - Heartwood Grove",
        "img": "icons/environment/wilderness/tree-oak.webp",
        "width": 4500,
        "height": 3500,
        "padding": 0.2,
        "initial": {
            "x": 2250,
            "y": 1750,
            "scale": 0.5
        },
        "backgroundColor": "#4A3F5C",
        "gridType": 1,
        "grid": 90,
        "gridDistance": 5,
        "gridUnits": "ft",
        "shiftX": 0,
        "shiftY": 0,
        "description": "The corrupted heart of the Twilight Forest. Ancient trees twisted by rift energy surround a massive, pulsing rift. The Twilight Druids perform their dark rituals here.",
        "notes": [],
        "tokens": [],
        "walls": []
    }
]

# Write all files
print("Writing actors...")
with open("/home/claude/shattered-realms/packs/actors/actors.json", "w") as f:
    json.dump(actors, f, indent=2)

print("Writing items...")
with open("/home/claude/shattered-realms/packs/items/items.json", "w") as f:
    json.dump(items, f, indent=2)

print("Writing tables...")
with open("/home/claude/shattered-realms/packs/tables/tables.json", "w") as f:
    json.dump(tables, f, indent=2)

print("Writing additional journals...")
with open("/home/claude/shattered-realms/packs/journals/quests-and-lore.json", "w") as f:
    json.dump(journals_additional, f, indent=2)

print("Writing scenes...")
with open("/home/claude/shattered-realms/packs/scenes/scenes.json", "w") as f:
    json.dump(scenes, f, indent=2)

print("Content generation complete!")
print(f"Generated:")
print(f"  - {len(actors)} actors")
print(f"  - {len(items)} items")
print(f"  - {len(tables)} rollable tables")
print(f"  - {len(journals_additional)} journal entries")
print(f"  - {len(scenes)} scenes")
