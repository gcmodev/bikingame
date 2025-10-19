"""
World System - Level loading, tile management, and collision
"""

import pygame
import json
import os

class World:
    """Manages level data, tiles, and collision"""
    
    def __init__(self):
        """Initialize world"""
        self.current_level = None
        self.level_width = 320
        self.level_height = 180
        
        # Tile data
        self.tiles = []  # All tiles in the level
        self.collision_tiles = []  # Tiles that have collision
        self.background_tiles = []  # Decorative background
        
        # Spawn points
        self.spawns = []
        
        # Interactive objects
        self.interactive_objects = []
        
        # Level transitions
        self.transitions = []
        
        # Colors for placeholder tiles
        self.tile_colors = {
            'floor': (74, 85, 104),  # Dark gray
            'wall': (45, 55, 72),    # Darker gray
            'platform': (100, 116, 139),  # Medium gray
            'background': (26, 28, 46)  # Very dark blue
        }
    
    def load_level(self, level_name):
        """Load a level from data or create procedurally"""
        self.current_level = level_name
        
        # Try to load from JSON file
        level_path = f"data/levels/{level_name}.json"
        
        if os.path.exists(level_path):
            self.load_from_file(level_path)
        else:
            # Create a basic level procedurally for testing
            self.create_test_level(level_name)
    
    def load_from_file(self, filepath):
        """Load level from JSON file"""
        try:
            with open(filepath, 'r') as f:
                data = json.load(f)
            
            self.level_width = data.get('width', 320)
            self.level_height = data.get('height', 180)
            self.tiles = data.get('tiles', [])
            self.collision_tiles = [t for t in self.tiles if t.get('collision', False)]
            self.spawns = data.get('spawns', [])
            self.interactive_objects = data.get('interactive_objects', [])
            self.transitions = data.get('transitions', [])
            
        except Exception as e:
            print(f"Error loading level: {e}")
            self.create_test_level(self.current_level)
    
    def create_test_level(self, level_name):
        """Create a simple test level"""
        self.tiles.clear()
        self.collision_tiles.clear()
        self.spawns.clear()
        self.interactive_objects.clear()
        self.transitions.clear()
        
        if level_name == "tutorial_chamber":
            # Set level size
            self.level_width = 480
            self.level_height = 180
            
            # Create floor
            for i in range(0, 480, 16):
                tile = {
                    'x': i,
                    'y': 164,
                    'width': 16,
                    'height': 16,
                    'type': 'floor',
                    'collision': True
                }
                self.tiles.append(tile)
                self.collision_tiles.append(tile)
            
            # Create some walls
            for i in range(0, 180, 16):
                # Left wall
                tile_left = {
                    'x': 0,
                    'y': i,
                    'width': 16,
                    'height': 16,
                    'type': 'wall',
                    'collision': True
                }
                self.tiles.append(tile_left)
                self.collision_tiles.append(tile_left)
            
            # Create some platforms
            platforms = [
                {'x': 120, 'y': 120, 'width': 48},
                {'x': 220, 'y': 100, 'width': 48},
                {'x': 320, 'y': 120, 'width': 64}
            ]
            
            for plat in platforms:
                tile = {
                    'x': plat['x'],
                    'y': plat['y'],
                    'width': plat['width'],
                    'height': 16,
                    'type': 'platform',
                    'collision': True
                }
                self.tiles.append(tile)
                self.collision_tiles.append(tile)
            
            # Add some enemies
            self.spawns.append({'type': 'enemy', 'x': 200, 'y': 140, 'variant': 'hollow_soldier'})
            self.spawns.append({'type': 'enemy', 'x': 350, 'y': 140, 'variant': 'hollow_soldier'})
            
            # Add NPC
            self.spawns.append({'type': 'npc', 'x': 280, 'y': 130, 'npc_id': 'scribe'})
            
            # Add collectibles
            self.spawns.append({'type': 'collectible', 'x': 150, 'y': 100, 'item_type': 'soul_ember'})
            self.spawns.append({'type': 'collectible', 'x': 250, 'y': 80, 'item_type': 'soul_ember'})
            self.spawns.append({'type': 'collectible', 'x': 400, 'y': 100, 'item_type': 'memory_fragment'})
            
            # Add bench
            self.interactive_objects.append({'type': 'bench', 'x': 100, 'y': 148})
        
        elif level_name == "archives":
            # Larger level
            self.level_width = 640
            self.level_height = 240
            
            # Create floor
            for i in range(0, 640, 16):
                tile = {
                    'x': i,
                    'y': 224,
                    'width': 16,
                    'height': 16,
                    'type': 'floor',
                    'collision': True
                }
                self.tiles.append(tile)
                self.collision_tiles.append(tile)
            
            # Multi-level platforms
            levels = [
                {'y': 180, 'platforms': [{'x': 80, 'w': 64}, {'x': 200, 'w': 96}, {'x': 400, 'w': 80}]},
                {'y': 130, 'platforms': [{'x': 150, 'w': 48}, {'x': 320, 'w': 64}, {'x': 500, 'w': 48}]}
            ]
            
            for level in levels:
                for plat in level['platforms']:
                    tile = {
                        'x': plat['x'],
                        'y': level['y'],
                        'width': plat['w'],
                        'height': 16,
                        'type': 'platform',
                        'collision': True
                    }
                    self.tiles.append(tile)
                    self.collision_tiles.append(tile)
            
            # Add more enemies
            for i in range(3):
                self.spawns.append({
                    'type': 'enemy',
                    'x': 100 + i * 200,
                    'y': 200,
                    'variant': 'hollow_soldier'
                })
    
    def get_collision_tiles(self):
        """Get all tiles with collision"""
        return self.collision_tiles
    
    def get_spawns(self):
        """Get all entity spawn points"""
        return self.spawns
    
    def get_interactive_objects(self):
        """Get all interactive objects"""
        return self.interactive_objects
    
    def get_transitions(self):
        """Get all level transitions"""
        return self.transitions
    
    def draw(self, surface, camera_x, camera_y):
        """Draw the level"""
        # Draw background color
        surface.fill(self.tile_colors['background'])
        
        # Draw all tiles
        for tile in self.tiles:
            screen_x = tile['x'] - camera_x
            screen_y = tile['y'] - camera_y
            
            # Only draw if on screen
            if -16 <= screen_x <= 320 and -16 <= screen_y <= 180:
                tile_type = tile.get('type', 'floor')
                color = self.tile_colors.get(tile_type, (100, 100, 100))
                
                pygame.draw.rect(surface, color, 
                               (screen_x, screen_y, tile['width'], tile['height']))
                
                # Draw border for visibility
                border_color = tuple(max(0, c - 20) for c in color)
                pygame.draw.rect(surface, border_color,
                               (screen_x, screen_y, tile['width'], tile['height']), 1)
        
        # Draw interactive objects
        for obj in self.interactive_objects:
            screen_x = obj['x'] - camera_x
            screen_y = obj['y'] - camera_y
            
            if obj['type'] == 'bench':
                # Draw simple bench placeholder
                pygame.draw.rect(surface, (249, 115, 22), (screen_x, screen_y, 32, 16))
                pygame.draw.circle(surface, (255, 150, 50), (int(screen_x + 16), int(screen_y + 8)), 6, 2)
