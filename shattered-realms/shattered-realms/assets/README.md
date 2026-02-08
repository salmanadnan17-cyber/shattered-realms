# Assets Directory

This directory contains visual and audio assets for The Shattered Realms module.

## Directory Structure

### /maps
Place map images here. Reference them in scene JSON files.
- Recommended format: JPG or WebP for file size
- Recommended resolution: 2000-4000 pixels
- Use descriptive names: `rift-city-plaza.jpg`, `broken-tower-level-1.webp`, etc.

### /tokens
Place token artwork here for actors.
- Recommended format: PNG with transparency or WebP
- Recommended size: 400x400 pixels minimum
- Naming convention: `actor-name-token.png`

### /ui
UI elements and module artwork.
- Place the module cover image here
- Any custom UI elements for scenes or journals

## Default Icons

Currently, this module uses Foundry VTT's default icon set. The paths in the JSON files reference icons that come with Foundry (in the `icons/` directory).

To use custom art:
1. Add your images to these directories
2. Update the `img` properties in the JSON files to point to your custom assets
3. Use relative paths like: `modules/shattered-realms/assets/maps/your-map.jpg`

## License Note

If you add custom artwork, ensure you have the rights to distribute it with this module.

## Recommended Resources

Free/CC art sources:
- 2-Minute Tabletop (maps)
- Forgotten Adventures (tokens and maps)
- Game-icons.net (icons)
- OpenGameArt.org
