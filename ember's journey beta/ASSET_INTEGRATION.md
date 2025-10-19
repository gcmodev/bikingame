# 📋 Asset Integration Checklist

Use this checklist when you're ready to replace placeholders with real sprites!

## 🎨 Phase 1: Player Sprites

### Create/Collect Sprites
- [ ] `idle.png` - 2 frames (64x32 total)
- [ ] `walk.png` - 4 frames (128x32 total)  
- [ ] `jump.png` - 1 frame (32x32)
- [ ] `attack.png` - 3 frames (96x32 total)
- [ ] `hurt.png` - 1 frame (32x32)

### Place Sprites
- [ ] Copy all to `assets/sprites/player/`

### Update Code
Edit `game/player.py`:
```python
# Add at top
import os

# In __init__:
self.load_sprites()

# Add method:
def load_sprites(self):
    self.sprites = {}
    sprite_path = "assets/sprites/player/"
    
    # Load each sprite sheet
    self.sprites['idle'] = pygame.image.load(
        os.path.join(sprite_path, 'idle.png')
    ).convert_alpha()
    # ... repeat for other sprites
```

### Update Draw Method
Replace the placeholder drawing with sprite blitting:
```python
def draw(self, surface, camera_x, camera_y):
    screen_x = self.rect.x - camera_x
    screen_y = self.rect.y - camera_y
    
    # Get current sprite frame
    sprite_sheet = self.sprites[self.animation_state]
    frame_width = 32
    frame_rect = pygame.Rect(
        self.animation_frame * frame_width, 0,
        frame_width, 32
    )
    frame = sprite_sheet.subsurface(frame_rect)
    
    # Flip if facing left
    if not self.facing_right:
        frame = pygame.transform.flip(frame, True, False)
    
    surface.blit(frame, (screen_x, screen_y))
```

## 👹 Phase 2: Enemy Sprites

### Create/Collect Sprites
- [ ] `hollow_soldier_idle.png` - 2 frames
- [ ] `hollow_soldier_walk.png` - 3 frames
- [ ] `hollow_soldier_attack.png` - 2 frames
- [ ] `hollow_soldier_death.png` - 3 frames

### Place Sprites
- [ ] Copy to `assets/sprites/enemies/`

### Update Code
Similar to player - edit `game/enemy.py`

## 💬 Phase 3: NPC Sprites

### Create/Collect Sprites
- [ ] `scribe_idle.png` - 2 frames (96x48 total)

### Place Sprites
- [ ] Copy to `assets/sprites/npcs/`

### Update Code
Edit `game/npc.py`

## 🌍 Phase 4: Environment

### Tilesets
- [ ] Create `dungeon_tileset.png` (16x16 tiles in grid)
- [ ] Place in `assets/tilesets/`
- [ ] Update `game/world.py` to load and use tiles

### Backgrounds
- [ ] Create background images for each area
- [ ] Place in `assets/backgrounds/`
- [ ] Update `game/world.py` to draw backgrounds

### Props
- [ ] `memory_fragment.png`
- [ ] `soul_ember.png`
- [ ] `bench.png`
- [ ] Place in `assets/sprites/props/`

## 🎵 Phase 5: Audio

### Music
- [ ] `awakening.ogg`
- [ ] `archives.ogg`
- [ ] `whispers.ogg`
- [ ] `revelation.ogg`
- [ ] Place in `assets/music/`

### Sound Effects
- [ ] Player sounds (footstep, jump, attack, hurt)
- [ ] Enemy sounds (walk, attack, death)
- [ ] Environment sounds (bench, door, whispers)
- [ ] UI sounds (menu, text)
- [ ] Place in `assets/sounds/`

### Update Code
Add to `main.py` in `__init__`:
```python
# Load music
pygame.mixer.music.load('assets/music/awakening.ogg')
pygame.mixer.music.play(-1)  # Loop

# Load sounds
self.sounds = {
    'jump': pygame.mixer.Sound('assets/sounds/jump.wav'),
    'attack': pygame.mixer.Sound('assets/sounds/sword_swing.wav'),
    # ... etc
}
```

Play sounds when actions occur:
```python
# In player.jump():
self.sounds['jump'].play()
```

## 🎬 Phase 6: Cutscenes

### Create Cutscene Images
- [ ] Memory fragment flash images (3 images)
- [ ] Opening cutscene frames
- [ ] Ending cutscene frames
- [ ] Place in `assets/backgrounds/cutscenes/`

### Update Code
Create `game/cutscene.py` to handle cutscene playback

## ✅ Testing Each Phase

After each phase:
- [ ] Run the game
- [ ] Check that new assets load correctly
- [ ] Verify animations play smoothly
- [ ] Check for missing files errors
- [ ] Test performance (should still be 60 FPS)

## 🐛 Common Issues

### Sprites Don't Appear
- Check file path is correct
- Verify file exists in the folder
- Make sure image format is PNG
- Check console for errors

### Sprites Look Wrong
- Verify sprite sheet layout (horizontal strip)
- Check frame sizes match code
- Ensure transparency is preserved (use .convert_alpha())

### Sounds Don't Play
- Check file format (WAV for sounds, OGG for music)
- Verify pygame.mixer is initialized
- Check volume settings
- Test with a simple sound first

### Performance Issues
- Optimize sprite sizes
- Use .convert_alpha() only once when loading
- Don't load assets every frame
- Cache loaded images

## 📝 Code Template for Loading Sprites

```python
class SpriteLoader:
    """Helper class for loading sprite sheets"""
    
    @staticmethod
    def load_sprite_sheet(path, frame_width, frame_height, num_frames):
        """Load a horizontal sprite sheet"""
        sheet = pygame.image.load(path).convert_alpha()
        frames = []
        
        for i in range(num_frames):
            frame_rect = pygame.Rect(
                i * frame_width, 0,
                frame_width, frame_height
            )
            frame = sheet.subsurface(frame_rect)
            frames.append(frame)
        
        return frames
```

Use it like:
```python
self.idle_frames = SpriteLoader.load_sprite_sheet(
    'assets/sprites/player/idle.png',
    32, 32, 2  # width, height, num_frames
)
```

## 🎯 Priority Order

If you want to add assets gradually:

1. **Start with player** - Most visible
2. **Add enemies** - Second most important
3. **Add tiles/backgrounds** - Environment feel
4. **Add NPCs** - Dialogue immersion
5. **Add props** - Polish
6. **Add sounds** - Atmosphere
7. **Add music** - Final touch

## 📚 Resources

- **Sprite Loading**: See pygame documentation for `pygame.image.load()`
- **Animation**: See existing animation code in `player.py`
- **Sound**: See pygame.mixer documentation

---

**Take it one step at a time! The code is ready for your assets!** 🎨✨
