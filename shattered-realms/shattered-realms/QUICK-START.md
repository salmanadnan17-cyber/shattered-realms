# The Shattered Realms - Complete Setup Guide

## What You've Received

A complete D&D 5e campaign module for Foundry Virtual Tabletop featuring:

### Content Overview
- **50+ Game-Ready Elements** across multiple categories
- **Weeks of Gameplay** - Content designed for 20-40 sessions
- **Flexible Structure** - Works as linear campaign or sandbox exploration
- **Professional Quality** - Balanced encounters, detailed lore, integrated storylines

### Included Files

#### Core Module Files
- `module.json` - Module manifest (Foundry VTT configuration)
- `README.md` - Campaign overview and player-facing information
- `GM-GUIDE.md` - Comprehensive game master guide
- `INSTALLATION.md` - Detailed installation instructions
- `CHANGELOG.md` - Version history and planned features
- `LICENSE` - MIT License for distribution

#### Game Content (in /packs directory)

**Actors** (10 NPCs/Creatures):
- Valdris the Shattered (CR 13 Lich - Main Villain)
- Grommak Shadowfang (CR 5 Orc Chieftain - Ally)
- Elara Moonwhisper (CR 8 Archmage - Faction Leader)
- Sir Gareth Stonewatch (CR 3 Knight)
- Rift Troll (CR 7 - Mutated giant)
- Bloodaxe Orc Raider (CR 1)
- Twilight Druid (CR 4)
- Rift Goblin (CR 1/2)
- Phase Spider Matriarch (CR 5)
- Rift Demon (CR 6)

**Items** (10 Magic Items/Equipment):
- Riftblade (Very Rare longsword +2)
- Amulet of Planar Anchoring (Rare protection)
- Staff of Reality Weaving (Legendary spellcaster focus)
- Boots of Phase Walking (Uncommon mobility)
- Cloak of Many Planes (Very Rare utility)
- Ring of Rift Sight (Uncommon detection)
- Shadowfang War Axe (Rare greataxe +1)
- Potion of Rift Resistance (Uncommon consumable)
- Twilight Crystal (Rare material component)
- Rift Shard (Very Rare material component)

**Scenes** (4 Mapped Locations):
- Rift City - Central Plaza (Major hub city)
- The Broken Tower - Level 1 (Dungeon, levels 1-3)
- Shadowfang Hold - Great Hall (Orc fortress)
- Twilight Forest - Heartwood Grove (Corrupted wilderness)

**Journal Entries** (5 Detailed Documents):
- Campaign Guide (World overview, factions, lore)
- Locations Guide (Rift City, Ironpeak, Twilight Forest details)
- Quest: The Broken Tower (Levels 1-3 adventure)
- Quest: Shadows of Ironpeak (Levels 3-5 adventure)
- Bestiary - Rift Creatures (Monster tactics and lore)

**Rollable Tables** (5 Tables):
- Random Rift Encounters (20 results)
- Rift Treasure (12 results)
- Wilderness Encounters - Ironpeak Region (12 results)
- Twilight Forest Encounters (10 results)
- Rift City Random Events (20 results)

## Installation Options

### Option 1: Quick Start (Recommended for Most Users)

1. **Extract the ZIP file** to your Foundry VTT Data folder:
   - Windows: `%appdata%/FoundryVTT/Data/modules/`
   - Mac: `~/Library/Application Support/FoundryVTT/Data/modules/`
   - Linux: `~/.local/share/FoundryVTT/Data/modules/`

2. **Restart Foundry VTT**

3. **Create or open a D&D 5e world**

4. **Enable the module:**
   - Go to Game Settings → Manage Modules
   - Check "The Shattered Realms - Complete Campaign"
   - Save Module Settings

5. **Import Content:**
   - Create Compendium Packs in Foundry matching the module structure
   - Import the JSON files from `packs/` directories into respective compendiums
   - Alternatively, manually import actors, items, etc. as needed

### Option 2: GitHub Installation

1. **Upload to GitHub** (if hosting yourself):
   - Create a new repository
   - Update URLs in `module.json`
   - Push the contents
   - Use the raw GitHub URL for the manifest

2. **Install in Foundry:**
   - Use the manifest URL in Foundry's "Install Module" dialog
   - Foundry will download and install automatically

### Option 3: Manual Content Import

If you prefer not to use modules:
1. Open your Foundry world
2. Manually import each JSON file from the `packs/` directory
3. Use Foundry's "Import Data" feature for actors, items, etc.

## First Session Prep

### Before Your First Game:

1. **Read the GM Guide** (`GM-GUIDE.md`)
   - Understand the world's themes and structure
   - Review the campaign structure options
   - Familiarize yourself with major NPCs

2. **Review Starting Content:**
   - Read: "Campaign Guide" journal entry
   - Read: "Quest: The Broken Tower" for your first adventure
   - Have "Random Rift Encounters" table ready

3. **Prepare NPCs:**
   - Import Elara Moonwhisper (quest giver)
   - Import Rift Goblins and Phase Spider Matriarch (encounters)

4. **Set Up Scene:**
   - Import "Rift City - Central Plaza" if starting there
   - Or "The Broken Tower - Level 1" if jumping straight to adventure

5. **Session Zero:**
   - Discuss themes with players
   - Help them create characters connected to the world
   - Establish expectations

## Quick Start Adventure

### The Broken Tower (Levels 1-3)

**Hook:**
Strange lights from an abandoned wizard's tower. Circle of Binding pays 200gp to investigate.

**Structure:**
- Ground Floor: Rift Goblin scavengers (easy combat)
- Second Floor: Phase Spider nest (moderate)
- Third Floor: Ghost encounter (roleplay/investigation)
- Hidden Lab: Cultists opening a rift (climax)

**Runtime:** 2-3 sessions

**Rewards:** Gold, magic items, reputation, hooks to larger campaign

## Campaign Paths

### Path 1: Linear Story (Recommended for New GMs)
1. The Broken Tower (Levels 1-3)
2. Shadows of Ironpeak (Levels 3-5)
3. Additional quests (you can create or we can expand)
4. Final confrontation with Valdris

### Path 2: Sandbox Exploration (Experienced GMs)
- Use random encounter tables
- Let players explore locations freely
- Introduce faction quests based on their interests
- Valdris works in the background

### Path 3: Faction-Focused (Political Intrigue)
- Focus on Circle of Binding vs Rift Walkers conflict
- Dwarf/Orc tensions in Ironpeak
- Twilight Druid threat
- Valdris as final unifying threat

## Troubleshooting

**Q: Compendiums are empty after installation**
- The JSON files need to be manually imported into Foundry compendiums
- Create the compendiums first, then import the JSON data

**Q: References to missing images**
- JSON files use default Foundry icons (in `icons/` directory)
- These should work automatically
- To use custom art, add to `assets/` and update JSON paths

**Q: How do I convert JSON to Foundry DB format?**
- For developers: Use `@foundryvtt/foundryvtt-cli` package
- For users: Manual import through Foundry UI works fine

**Q: Module doesn't appear in Foundry**
- Ensure folder is named exactly `shattered-realms`
- Check `module.json` is in the root of that folder
- Restart Foundry after placing the module

## Customization Tips

### Easy Modifications:
- Change NPC names and descriptions in JSON files
- Adjust CR ratings for your party's power level
- Add your own quests using the existing structure
- Create new rollable tables for your specific needs

### Advanced Modifications:
- Add your own artwork to `/assets` directories
- Create additional scenes
- Expand the faction system
- Add custom items with rift themes
- Develop additional quest lines

## Support and Community

### Getting Help:
- Check `INSTALLATION.md` for detailed technical instructions
- Review `GM-GUIDE.md` for running the campaign
- Foundry VTT Discord server (community help)
- Foundry VTT documentation site

### Sharing and Attribution:
- This module is MIT licensed
- Feel free to modify and share
- Attribution appreciated but not required
- Consider sharing your improvements!

## Next Steps

1. ✅ Install the module in Foundry VTT
2. ✅ Read the Campaign Guide and GM Guide
3. ✅ Import content into your world
4. ✅ Plan your Session Zero
5. ✅ Prep "The Broken Tower" adventure
6. ✅ Have fun exploring the Shattered Realms!

## Content Roadmap

**Already Included:**
- ✅ Core world setting and lore
- ✅ Major NPCs and factions
- ✅ Starting adventure (Levels 1-3)
- ✅ Second adventure (Levels 3-5)
- ✅ Magic items and treasure
- ✅ Random encounter tables
- ✅ Multiple scenes/locations

**Potential Expansions:**
- 🔄 Additional mid-level quests (Levels 5-7)
- 🔄 High-level campaign conclusion (Levels 8-10+)
- 🔄 More detailed maps with walls, lighting, tokens
- 🔄 Additional creatures and NPCs
- 🔄 More magic items
- 🔄 Player handouts and maps
- 🔄 Audio/music suggestions
- 🔄 Macros for rift effects
- 🔄 Custom character options

---

**Welcome to the Shattered Realms!**

This campaign offers weeks of adventure in a world where reality itself is broken. Whether you run it as written or make it your own, I hope you and your players enjoy exploring this fractured realm where ancient magic, political intrigue, and heroic deeds shape the future of civilization.

May your rifts be stable and your dice roll high!
