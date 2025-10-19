# 🚀 QUICK START GUIDE

## Get Playing in 3 Steps!

### Step 1: Install Python
If you don't have Python installed:
1. Go to https://www.python.org/downloads/
2. Download Python 3.8 or higher
3. **Important**: Check "Add Python to PATH" during installation!

### Step 2: Install Pygame
Open PowerShell in this folder and run:
```powershell
pip install pygame
```

Or just double-click: `run_game.bat`

### Step 3: Run the Game!
```powershell
python main.py
```

## Controls

| Action | Keys |
|--------|------|
| Move | A/D or Arrow Keys |
| Jump | W or Space |
| Attack | J or Z |
| Talk/Interact | S or Down Arrow |
| Pause | ESC |

## What to Expect

You'll see a **playable prototype** with:
- ✅ A player character (gray rectangle for now)
- ✅ Enemies that patrol and attack (red rectangles)
- ✅ An NPC you can talk to (blue rectangle)
- ✅ Collectibles to pick up (colored circles)
- ✅ A working health system (3 hearts)
- ✅ Smooth camera following
- ✅ Combat system

**Everything works!** Graphics are placeholders that will be replaced with your sprites.

## Try This:

1. **Move around** - Use A/D to walk
2. **Jump on platforms** - Press Space to jump
3. **Fight an enemy** - Press J near the red rectangles
4. **Talk to the NPC** - Walk to the blue rectangle and press S
5. **Collect items** - Walk over the colored circles
6. **Check your stats** - See hearts and counters in top corners

## Troubleshooting

**"pygame not found"**
```powershell
pip install pygame
```

**"Python not recognized"**
- Install Python from python.org
- Make sure "Add to PATH" was checked

**Game won't start**
- Check console for error messages
- Make sure you're in the correct folder
- Try: `python --version` to verify Python is installed

## Next Steps

Once you've tested the game:
1. Read `PROJECT_SUMMARY.md` for complete overview
2. Check `DEVELOPMENT.md` for detailed guides
3. See `assets/ASSET_GUIDE.md` for adding graphics
4. Create your own levels in `data/levels/`

## File Structure

```
📁 ember's journey beta/
  📄 main.py              ← Run this!
  📄 run_game.bat         ← Or double-click this!
  📁 game/                ← All game code
  📁 assets/              ← Put your sprites here (later)
  📁 data/                ← Level files
  📄 README.md            ← Project info
  📄 DEVELOPMENT.md       ← Dev guide
  📄 PROJECT_SUMMARY.md   ← What's included
```

---

## 🎮 Ready to Play!

The game is **fully functional** and ready for your creative touch!

**Questions?** Check the other documentation files or the code comments.

Let's bring Ember to life! ⚔️✨
