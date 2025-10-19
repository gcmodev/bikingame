"""
Camera System - Follows player and keeps them in view
"""

import pygame

class Camera:
    """Camera that follows the player"""
    
    def __init__(self, width, height):
        """Initialize camera"""
        self.width = width
        self.height = height
        
        # Camera position (top-left corner of view)
        self.x = 0
        self.y = 0
        
        # Level bounds
        self.level_width = width
        self.level_height = height
        
        # Follow settings
        self.follow_speed = 5  # Higher = tighter follow
        self.deadzone_width = 60  # Don't move camera if player is in this zone
        self.deadzone_height = 40
        
        # Target position
        self.target_x = 0
        self.target_y = 0
    
    def set_bounds(self, level_width, level_height):
        """Set the level boundaries"""
        self.level_width = level_width
        self.level_height = level_height
    
    def update(self, player):
        """Update camera to follow player"""
        # Calculate center of screen
        center_x = self.x + self.width // 2
        center_y = self.y + self.height // 2
        
        # Calculate player center
        player_center_x = player.rect.centerx
        player_center_y = player.rect.centery
        
        # Check if player is outside deadzone
        dx = player_center_x - center_x
        dy = player_center_y - center_y
        
        # Horizontal movement
        if abs(dx) > self.deadzone_width // 2:
            if dx > 0:
                self.target_x = player_center_x - self.width // 2
            else:
                self.target_x = player_center_x - self.width // 2
        
        # Vertical movement
        if abs(dy) > self.deadzone_height // 2:
            if dy > 0:
                self.target_y = player_center_y - self.height // 2
            else:
                self.target_y = player_center_y - self.height // 2
        
        # Smooth camera movement
        self.x += (self.target_x - self.x) * self.follow_speed * 0.1
        self.y += (self.target_y - self.y) * self.follow_speed * 0.1
        
        # Clamp camera to level bounds
        self.x = max(0, min(self.x, self.level_width - self.width))
        self.y = max(0, min(self.y, self.level_height - self.height))
    
    def get_offset(self):
        """Get camera offset for rendering"""
        return int(self.x), int(self.y)
    
    def apply(self, rect):
        """Apply camera offset to a rect"""
        return pygame.Rect(rect.x - int(self.x), rect.y - int(self.y), rect.width, rect.height)
