# Ember's Journey

A Hollow Knight-inspired 2D side-scrolling adventure game built with Python and Pygame.

## Project Structure

```
ember's journey beta/
├── main.py                 # Main game entry point
├── requirements.txt        # Python dependencies
├── game/                   # Game code modules
│   ├── __init__.py
│   ├── player.py          # Player character logic
│   ├── enemy.py           # Enemy AI and behavior
│   ├── npc.py             # NPC characters
│   ├── dialogue.py        # Dialogue system
│   ├── world.py           # Level loading and tiles
│   ├── camera.py          # Camera system
│   └── ui.py              # UI and HUD
├── assets/                # Game assets (to be added)
│   ├── sprites/
│   │   ├── player/
│   │   ├── enemies/
│   │   ├── npcs/
│   │   └── props/
│   ├── tilesets/
│   ├── backgrounds/
│   ├── sounds/
│   └── music/
└── data/                  # Game data
    └── levels/            # Level JSON files
```

## Setup

1. Install Python 3.8 or higher
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Game

```bash
python main.py
```

## Controls

- **A/D or Arrow Keys**: Move left/right
- **W or Space**: Jump
- **J or Z**: Attack
- **S or Down Arrow**: Interact with NPCs, benches, etc.
- **ESC**: Pause menu

## Current Features

✅ Player movement and physics
✅ Jumping and gravity
✅ Simple combat system
✅ Enemy AI (patrol, chase, attack)
✅ NPC dialogue system
✅ Camera following player
✅ Level loading and collision
✅ Health system
✅ Collectibles (Soul Embers, Memory Fragments)
✅ UI and HUD

## Next Steps

- [ ] Add sprite assets (replace placeholder graphics)
- [ ] Create level JSON files
- [ ] Add sound effects and music
- [ ] Implement save system
- [ ] Add cutscenes
- [ ] Create more enemy variants
- [ ] Design full 10-minute demo levels

## Game Design

This is a 10-minute demo inspired by Hollow Knight, featuring:
- Dark medieval fantasy atmosphere
- Exploration and simple combat
- Environmental storytelling
- Memory fragments to collect
- Mysterious NPCs
- Ends with "TO BE CONTINUED..."

## Development Notes

The game is built using:
- **Python 3.x**
- **Pygame** for rendering and input
- Base resolution: 320x180 (scaled to 1280x720)
- Target: 60 FPS

All placeholder graphics will be replaced with proper pixel art sprites once assets are created.
