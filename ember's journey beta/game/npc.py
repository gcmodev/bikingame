"""
NPC System - Friendly characters that provide dialogue
"""

import pygame

class NPC:
    """Non-player character class"""
    
    def __init__(self, x, y, npc_id="scribe"):
        """Initialize NPC"""
        self.rect = pygame.Rect(x, y, 24, 32)  # Slightly larger than player
        self.npc_id = npc_id
        
        # Setup based on NPC type
        self.setup_npc()
        
        # Animation
        self.animation_frame = 0
        self.animation_timer = 0
        self.animation_speed = 0.2
        
        # Interaction
        self.interaction_range = 30
        self.can_interact = True
    
    def setup_npc(self):
        """Setup NPC properties based on ID"""
        if self.npc_id == "scribe":
            self.name = "The Scribe"
            self.dialogue_id = "scribe"
            self.color = (59, 130, 246)  # Blue
        # Add more NPCs here
    
    def is_near_player(self, player):
        """Check if player is close enough to interact"""
        distance = abs(self.rect.centerx - player.rect.centerx)
        return distance <= self.interaction_range and self.can_interact
    
    def update(self, dt):
        """Update NPC (mainly animation)"""
        self.animation_timer += dt
        
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.animation_frame = (self.animation_frame + 1) % 2  # Gentle idle animation
    
    def draw(self, surface, camera_x, camera_y):
        """Draw NPC"""
        screen_x = self.rect.x - camera_x
        screen_y = self.rect.y - camera_y
        
        # Draw placeholder (will be replaced with sprite)
        pygame.draw.rect(surface, self.color, (screen_x, screen_y, self.rect.width, self.rect.height))
        
        # Draw a subtle glow effect
        glow_color = tuple(min(255, c + 50) for c in self.color)
        pygame.draw.rect(surface, glow_color, (screen_x, screen_y, self.rect.width, self.rect.height), 2)
