# Asset Organization Guide

## Directory Structure

This guide explains where to place your game assets once they are created.

### Sprites

#### Player Sprites (`assets/sprites/player/`)
- `idle.png` - Idle animation spritesheet (2 frames, 32x32 each)
- `walk.png` - Walking animation (4 frames, 32x32 each)
- `jump.png` - Jump frame (1 frame, 32x32)
- `attack.png` - Attack animation (3 frames, 32x32 each)
- `hurt.png` - Hurt frame (1 frame, 32x32)
- `death.png` - Death animation (3 frames, 32x32 each)

#### Enemy Sprites (`assets/sprites/enemies/`)
- `hollow_soldier_idle.png` - 2 frames, 32x32 each
- `hollow_soldier_walk.png` - 3 frames, 32x32 each
- `hollow_soldier_attack.png` - 2 frames, 32x32 each
- `hollow_soldier_death.png` - 3 frames, 32x32 each

#### NPC Sprites (`assets/sprites/npcs/`)
- `scribe_idle.png` - 2 frames, 48x48 each
- (Add more NPCs as needed)

#### Props (`assets/sprites/props/`)
- `memory_fragment.png` - Animated crystal (3 frames, 16x16 each)
- `soul_ember.png` - Floating ember (2 frames, 8x8 each)
- `bench.png` - Save point bench (32x16)
- `lore_tablet.png` - Stone tablet (16x24)
- `locked_door.png` - Door with lock (48x64)
- `sealed_gate.png` - Massive gate (128x96)

### Tilesets

#### Tiles (`assets/tilesets/`)
- `dungeon_tileset.png` - 16x16 tiles arranged in a grid
  - Stone floor
  - Stone walls
  - Platforms
  - Decorative elements
  - Moss/cracks

### Backgrounds

#### Backgrounds (`assets/backgrounds/`)
- `tutorial_bg.png` - Dark chamber background
- `archives_bg.png` - Library background
- `passage_bg.png` - Narrow corridor background
- `grand_chamber_bg.png` - Final room background

### Audio

#### Music (`assets/music/`)
- `awakening.ogg` - Tutorial/early areas (2 min loop)
- `archives.ogg` - Main exploration music (2 min loop)
- `whispers.ogg` - Tense passage music (2 min loop)
- `revelation.ogg` - Final chamber (30 sec)

#### Sounds (`assets/sounds/`)

**Player Sounds:**
- `footstep.wav`
- `jump.wav`
- `sword_swing.wav`
- `sword_hit.wav`
- `player_hurt.wav`
- `collect_ember.wav`
- `collect_fragment.wav`

**Enemy Sounds:**
- `hollow_walk.wav`
- `hollow_attack.wav`
- `hollow_death.wav`

**Environment Sounds:**
- `bench_sit.wav`
- `door_unlock.wav`
- `tablet_activate.wav`
- `whispers_ambient.wav` (looping)

**UI Sounds:**
- `menu_select.wav`
- `pause.wav`
- `text_scroll.wav`

## Sprite Sheet Format

All sprite sheets should be horizontal strips with frames arranged left to right.

Example for a 4-frame animation:
```
[Frame 1][Frame 2][Frame 3][Frame 4]
```

Each frame should be the same size (e.g., 32x32 pixels).

## Naming Conventions

- Use lowercase
- Use underscores for spaces
- Be descriptive
- Include animation name
- Example: `hollow_soldier_walk.png`

## File Formats

- **Sprites**: PNG with transparency
- **Tilesets**: PNG with transparency
- **Backgrounds**: PNG (can be opaque)
- **Music**: OGG or MP3
- **Sounds**: WAV for short sounds

## Color Palette Reference

Based on the design document:

- **Backgrounds**: #1a1c2e, #2d3748, #4a5568
- **Player**: #e5e7eb, #f3f4f6
- **Memory Fragments**: #06b6d4 (cyan)
- **Soul Embers**: #f97316 (orange)
- **Save Benches**: #f97316 (orange glow)
- **Moth Guide**: #86efac (pale green)
- **Enemies**: #991b1b (dark red)

## Integration Notes

Once you add assets:

1. Update the code to load sprites instead of drawing placeholders
2. Implement proper animation system
3. Add audio playback
4. Test all assets in-game

The code is already structured to easily swap placeholders with real assets!
