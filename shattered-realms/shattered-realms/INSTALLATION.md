# Installation and Setup Guide

## For Module Developers / GitHub Publishing

This module is structured to work with Foundry VTT version 11+. 

### File Structure
```
shattered-realms/
├── module.json           # Module manifest
├── README.md             # Campaign overview and usage guide
├── LICENSE               # MIT License
├── INSTALLATION.md       # This file
├── packs/                # Compendium packs
│   ├── actors/           # NPCs and creatures
│   ├── items/            # Equipment and magic items
│   ├── journals/         # Lore, quests, and documentation
│   ├── scenes/           # Maps and locations
│   └── tables/           # Rollable tables
├── assets/               # Images and media
│   ├── maps/             # Map images
│   ├── tokens/           # Token artwork
│   └── ui/               # UI elements
└── lang/                 # Localization files
```

### Converting JSON to Foundry DB Format

The JSON files in the `packs/` directories are in a portable format. To use this module in Foundry VTT:

**Option 1: Import Directly (Recommended for Users)**
1. Copy this entire folder to your Foundry VTT `Data/modules/` directory
2. The JSON files can be imported into compendiums via Foundry's import features
3. Create compendium packs in Foundry and import the JSON files

**Option 2: Use fvtt CLI Tool (For Developers)**
```bash
# Install the Foundry Package CLI tool
npm install -g @foundryvtt/foundryvtt-cli

# Pack the JSON files into LevelDB format
fvtt package pack shattered-realms
```

**Option 3: Manual Import in Foundry**
1. Start Foundry VTT and create/open a world using the dnd5e system
2. Enable this module
3. Create new Compendium Packs matching the structure in module.json
4. Use the "Import Data" feature to import each JSON file into its respective compendium

### GitHub Setup

To host this module on GitHub:

1. **Create a new repository:**
   ```bash
   git init
   git add .
   git commit -m "Initial commit: The Shattered Realms campaign module"
   ```

2. **Update module.json URLs:**
   Replace the following in `module.json`:
   - `"url"`: Your repository URL
   - `"manifest"`: `https://raw.githubusercontent.com/YOURUSERNAME/shattered-realms/main/module.json`
   - `"download"`: `https://github.com/YOURUSERNAME/shattered-realms/archive/refs/heads/main.zip`

3. **Push to GitHub:**
   ```bash
   git remote add origin https://github.com/YOURUSERNAME/shattered-realms.git
   git branch -M main
   git push -u origin main
   ```

4. **Create a Release:**
   - Go to your repository on GitHub
   - Click "Releases" → "Create a new release"
   - Tag version: `v1.0.0`
   - Upload the ZIP file
   - Publish release

### For Players

If you just want to use this module:

1. Download the latest release ZIP
2. Extract to your Foundry VTT `Data/modules/` folder
3. Restart Foundry VTT
4. In your D&D 5e world, enable "The Shattered Realms" module
5. Import content from the compendium packs

## Troubleshooting

**Q: The compendiums show up but are empty**
A: The JSON files need to be imported. Create the compendiums in Foundry, then import the JSON files from the `packs/` directory.

**Q: I get an error about missing assets**
A: Some references in the JSON point to default Foundry icons. If you want custom art, replace the `img` paths in the JSON files with your own assets in the `assets/` folder.

**Q: The module doesn't show up in Foundry**
A: Make sure the folder is named exactly `shattered-realms` (matching the `id` in module.json) and is in your `Data/modules/` directory.

## Support

For issues, questions, or contributions, visit the GitHub repository.
