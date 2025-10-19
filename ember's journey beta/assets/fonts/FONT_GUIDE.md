# Pixel Font Guide

## Using Pixel Fonts in Ember's Journey

The game is configured to use pixel fonts for an authentic retro look!

## Recommended Fonts

### Free Pixel Fonts (Download these):

1. **Press Start 2P** (Minecraft/Arcade style)
   - Download: https://fonts.google.com/specimen/Press+Start+2P
   - Best for: Title screens, menus
   - Style: Classic arcade/NES look

2. **VT323** (Terminal style)
   - Download: https://fonts.google.com/specimen/VT323
   - Best for: Dialogue, UI text
   - Style: Retro computer terminal

3. **Pixelify Sans**
   - Download: https://fonts.google.com/specimen/Pixelify+Sans
   - Best for: Body text, readable pixel font
   - Style: Modern pixel art

4. **Determination Mono** (Undertale-style)
   - Search online for free download
   - Best for: Dialogue boxes
   - Style: Similar to Undertale

5. **m5x7** or **m3x6** (Minimal pixel)
   - Download from: https://managore.itch.io/m5x7
   - Best for: Very small text
   - Style: Ultra compact

## Installation

1. Download your chosen font (TTF or OTF file)
2. Rename it to `pixel.ttf`
3. Place it in this folder: `assets/fonts/pixel.ttf`
4. Restart the game!

## Quick Setup (Recommended)

**For Minecraft-like look:**
1. Go to: https://fonts.google.com/specimen/Press+Start+2P
2. Click "Download family"
3. Extract the ZIP file
4. Find `PressStart2P-Regular.ttf`
5. Copy it to `assets/fonts/` and rename to `pixel.ttf`

## File Structure

```
assets/fonts/
├── pixel.ttf          ← Main menu font (place here!)
└── FONT_GUIDE.md      ← This file
```

## Current Behavior

- **With font file**: Uses your custom pixel font
- **Without font file**: Falls back to Pygame's default font (still pixelated!)

The game will work either way, but custom fonts look better!

## Font Sizes Used

The game uses these sizes:
- **Title**: 32pt (48px on screen)
- **Menu**: 16pt (24px on screen)  
- **Small**: 12pt (16px on screen)

## Testing Your Font

After adding the font:
1. Launch the game
2. Check the main menu title "EMBER'S JOURNEY"
3. Navigate the menu options
4. The text should look crisp and pixelated!

## Troubleshooting

**Font looks blurry?**
- Make sure it's a proper pixel/bitmap font
- Try a different font from the list above

**Font not loading?**
- Check the file is named exactly `pixel.ttf`
- Make sure it's in `assets/fonts/` folder
- Check console for error messages

**Font too big/small?**
- This is normal - sizes are optimized for 320x180 base resolution
- The game scales everything up automatically

## License Note

Make sure any font you use allows commercial/game use if you plan to distribute your game!

Most fonts on Google Fonts are free for all uses.
