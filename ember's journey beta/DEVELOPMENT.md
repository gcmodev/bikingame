# Ember's Journey - Development Guide

## Quick Start

### Running the Game

**Option 1: Double-click the batch file**
```
run_game.bat
```

**Option 2: Manual command**
```powershell
# Install dependencies
pip install -r requirements.txt

# Run the game
python main.py
```

## Project Status

### ✅ Completed Core Systems

1. **Player System** (`game/player.py`)
   - Movement (left/right)
   - Jumping with gravity
   - Attack mechanics
   - Health/damage system
   - Animation states

2. **Enemy AI** (`game/enemy.py`)
   - Patrol behavior
   - Player detection and chase
   - Attack when in range
   - Health system
   - Death animation

3. **World System** (`game/world.py`)
   - Level loading from JSON
   - Tile-based collision
   - Platform support
   - Level transitions
   - Interactive objects

4. **Camera** (`game/camera.py`)
   - Smooth player following
   - Deadzone for comfortable movement
   - Level boundary clamping

5. **Dialogue System** (`game/dialogue.py`)
   - Text box rendering
   - Typewriter effect
   - Multi-line support
   - NPC conversations

6. **UI System** (`game/ui.py`)
   - Health display (hearts)
   - Soul Ember counter
   - Memory Fragment counter
   - Notification system
   - Menu system

## Code Architecture

### Main Game Loop (`main.py`)

The `Game` class manages:
- Window and rendering
- Game state (menu, playing, paused)
- Entity management (player, enemies, NPCs)
- Collectibles
- Level loading

### Player Controls

Current keyboard mappings:
- `A` / `Left Arrow`: Move left
- `D` / `Right Arrow`: Move right
- `W` / `Space`: Jump
- `J` / `Z`: Attack
- `S` / `Down`: Interact
- `ESC`: Pause

### Adding New Features

#### Adding a New Enemy Type

1. Edit `game/enemy.py`
2. Add new variant in `setup_stats()`:
```python
elif self.variant == "new_enemy":
    self.health = 5
    self.damage = 2
    self.move_speed = 60
```

#### Adding a New Level

1. Create JSON file in `data/levels/`
2. Define tiles, spawns, and transitions
3. Load with `game.load_level("level_name")`

Example level structure:
```json
{
  "name": "New Level",
  "width": 640,
  "height": 240,
  "tiles": [...],
  "spawns": [...],
  "interactive_objects": [...],
  "transitions": [...]
}
```

#### Adding New Dialogue

Edit `game/dialogue.py` in the `load_dialogue()` method:
```python
"new_npc": {
    "name": "NPC Name",
    "conversations": {
        "greeting": ["Hello!", "How are you?"]
    }
}
```

## Testing Checklist

- [ ] Player can move left and right
- [ ] Player can jump
- [ ] Player can attack
- [ ] Enemies patrol and chase
- [ ] Enemies attack when close
- [ ] Player takes damage
- [ ] Collectibles can be picked up
- [ ] Dialogue boxes appear
- [ ] Camera follows player
- [ ] Pause menu works
- [ ] Health display updates
- [ ] Counters update

## Performance Tips

- Game runs at 60 FPS target
- Base resolution: 320x180 (scaled to 1280x720)
- Placeholder graphics are minimal for fast development
- All assets will be replaced later

## Next Development Steps

### Phase 1: Core Completion
- [ ] Fix any bugs in existing systems
- [ ] Add save/load functionality
- [ ] Implement respawn at benches

### Phase 2: Asset Integration
- [ ] Replace placeholder player with sprites
- [ ] Replace placeholder enemies with sprites
- [ ] Add tile graphics
- [ ] Add background layers

### Phase 3: Content Creation
- [ ] Design 5-7 interconnected levels
- [ ] Create all NPCs and dialogue
- [ ] Place collectibles strategically
- [ ] Add environmental storytelling elements

### Phase 4: Polish
- [ ] Add particle effects
- [ ] Implement sound effects
- [ ] Add background music
- [ ] Create opening cutscene
- [ ] Create ending cutscene

### Phase 5: Testing
- [ ] Playtest full 10-minute experience
- [ ] Balance difficulty
- [ ] Fix collision issues
- [ ] Optimize performance

## File Organization

```
ember's journey beta/
├── main.py              # Entry point - run this!
├── run_game.bat         # Quick launcher
├── requirements.txt     # Python dependencies
├── README.md           # Project overview
│
├── game/               # All game logic
│   ├── player.py       # Player character
│   ├── enemy.py        # Enemy AI
│   ├── npc.py          # Non-player characters
│   ├── dialogue.py     # Dialogue system
│   ├── world.py        # Level management
│   ├── camera.py       # Camera system
│   └── ui.py           # User interface
│
├── assets/             # Game assets (add later)
│   ├── sprites/
│   ├── tilesets/
│   ├── backgrounds/
│   ├── sounds/
│   └── music/
│
└── data/               # Game data
    └── levels/         # Level JSON files
```

## Common Issues & Solutions

### Game Won't Start
- Make sure Python 3.8+ is installed
- Run: `pip install pygame`
- Check for syntax errors in console

### Player Falls Through Floor
- Check collision tiles in level JSON
- Ensure `collision: true` is set
- Verify tile coordinates

### Enemies Don't Spawn
- Check spawn points in level JSON
- Verify enemy variant name is correct
- Check console for errors

### Dialogue Doesn't Show
- Ensure NPC has dialogue_id set
- Check dialogue data in dialogue.py
- Verify player is within interaction range

## Debugging Tips

Add print statements to debug:
```python
# In main.py update()
print(f"Player pos: {self.player.rect.x}, {self.player.rect.y}")
print(f"Enemies: {len(self.enemies)}")
print(f"Health: {self.health}")
```

## Contributing

When adding features:
1. Test thoroughly
2. Comment your code
3. Update this guide
4. Keep performance in mind
5. Follow existing code style

## Resources

- [Pygame Documentation](https://www.pygame.org/docs/)
- [Python Documentation](https://docs.python.org/3/)
- Game Design Document (see main document)

---

**Happy Developing! 🎮⚔️**
