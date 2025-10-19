# Menu System Visual Reference

## Main Menu Layout (320x180 resolution)

```
┌────────────────────────────────────────────────────────────┐
│                                                            │
│                                                            │
│              ███ EMBER'S JOURNEY ███                       │
│            A Dark Medieval Adventure                       │
│                                                            │
│                                                            │
│                    ▶ Start Game                            │
│                      Settings                              │
│                      Quit                                  │
│                                                            │
│                                                            │
│  W/S or ↑/↓: Navigate  |  SPACE/ENTER: Select  |  ESC: Back│
└────────────────────────────────────────────────────────────┘
```

## Pause Menu Layout

```
┌────────────────────────────────────────────────────────────┐
│                                                            │
│                [Semi-transparent dark overlay]             │
│                                                            │
│           ┌──────────────────────────────┐                 │
│           │                              │                 │
│           │         PAUSED               │                 │
│           │                              │                 │
│           │      ▶ Resume                │                 │
│           │        Restart               │                 │
│           │        Main Menu             │                 │
│           │        Quit                  │                 │
│           │                              │                 │
│           └──────────────────────────────┘                 │
│                                                            │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

## Color Reference

```
┌─────────────────┬──────────────┬───────────────────────────┐
│ Element         │ Color Code   │ Usage                     │
├─────────────────┼──────────────┼───────────────────────────┤
│ Background      │ #1a1c2e      │ Main menu background      │
│ Title           │ #06b6d4      │ Game title (cyan)         │
│ Selected Option │ #06b6d4      │ Highlighted menu item     │
│ Normal Text     │ #ffffff      │ Unselected menu items     │
│ Shadow          │ #000000      │ Text shadow for depth     │
│ Box Background  │ #14141e      │ Pause menu box            │
│ Box Border      │ #6496c8      │ Pause menu border         │
│ Subtitle        │ #ffffff      │ Menu subtitle text        │
│ Hint Text       │ #969696      │ Control hints at bottom   │
└─────────────────┴──────────────┴───────────────────────────┘
```

## Animation States

### Title Pulse
```
Normal → Slightly Larger → Normal → Repeat
 100%  →      105%       →  100%  → Loop
```

### Selector Arrow
```
Position A → Position B → Position A → Repeat
   ▶       →    ▶        →     ▶     → Loop
  (0px)    →   (3px)     →    (0px)  → Loop
```

## Menu State Machine

```
┌─────────────┐
│  MAIN MENU  │
│  (Start)    │
└──────┬──────┘
       │ Select "Start Game"
       ↓
┌─────────────┐
│   PLAYING   │◄─────────────┐
└──────┬──────┘              │
       │ Press ESC           │
       ↓                     │
┌─────────────┐              │
│ PAUSE MENU  │              │
└──────┬──────┘              │
       │                     │
       ├─ Resume ────────────┘
       │
       ├─ Restart ───────────┐
       │                     │
       ├─ Main Menu ─────┐   │
       │                 ↓   ↓
       └─ Quit        ┌─────────────┐
                      │   PLAYING   │
                      │  (Reloaded) │
                      └─────────────┘
```

## Font Hierarchy

```
Title Font:    48px → "EMBER'S JOURNEY"
               ▼
Menu Font:     24px → "Start Game", "Resume", etc.
               ▼
Small Font:    16px → "A Dark Medieval Adventure"
               ▼
Tiny Font:     12px → Control hints (future)
```

## Interactive Elements

### Selection Indicator
```
Not Selected:    Settings
Selected:      ▶ Settings  (Cyan color + Arrow)
```

### Button States
```
Idle:     Normal white text
Hover:    Cyan text with arrow
Pressed:  Momentary, then action
```

## Spacing & Layout

```
Main Menu:
┌─ Top: 60px from top
│  Title: "EMBER'S JOURNEY"
│
├─ +35px
│  Subtitle: "A Dark Medieval Adventure"
│
├─ +30px (Total: 90px from title)
│  Menu Options Start
│  - Each option: 30px apart
│
└─ Bottom: 20px from bottom
   Control hints
```

```
Pause Menu Box:
┌─ Width: 200px
│  Height: 150px
│  Centered on screen
│
├─ Title: 25px from box top
├─ Options start: 60px from box top
│  - Each option: 20px apart
│
└─ Padding: 10px all sides
```

## Keyboard Navigation Flow

```
Main Menu Options (3 total):
┌──────────────┐
│  Start Game  │ ← W/↑ from here wraps to bottom
├──────────────┤
│  Settings    │
├──────────────┤
│  Quit        │ ← S/↓ from here wraps to top
└──────────────┘

Pause Menu Options (4 total):
┌──────────────┐
│  Resume      │ ← W/↑ wraps to bottom
├──────────────┤
│  Restart     │
├──────────────┤
│  Main Menu   │
├──────────────┤
│  Quit        │ ← S/↓ wraps to top
└──────────────┘
```

## ASCII Art Concept (High Resolution)

```
  ███████╗███╗   ███╗██████╗ ███████╗██████╗ 
  ██╔════╝████╗ ████║██╔══██╗██╔════╝██╔══██╗
  █████╗  ██╔████╔██║██████╔╝█████╗  ██████╔╝
  ██╔══╝  ██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
  ███████╗██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
  ╚══════╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝

               J O U R N E Y
```

---

This reference helps visualize the menu system structure!
