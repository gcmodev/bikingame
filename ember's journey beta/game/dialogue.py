"""
Dialogue System - Text boxes and conversation management
"""

import pygame
import json

class DialogueSystem:
    """Manages dialogue boxes and conversations"""
    
    def __init__(self):
        """Initialize dialogue system"""
        self.active = False
        self.current_dialogue = None
        self.dialogue_index = 0
        self.dialogue_data = self.load_dialogue()
        
        # Visual
        self.box_rect = pygame.Rect(20, 120, 280, 50)  # Position on 320x180 screen
        self.text_color = (255, 255, 255)
        self.box_color = (20, 20, 30)
        self.border_color = (100, 150, 200)
        
        # Text rendering
        self.font = None  # Will use pygame default
        self.line_spacing = 12
        self.char_delay = 0.03  # Typewriter effect
        self.char_timer = 0
        self.chars_shown = 0
        self.full_text = ""
        self.wrapped_lines = []
        
        # Input
        self.can_advance = False
        self.advance_delay = 0.3
        self.advance_timer = 0
    
    def load_dialogue(self):
        """Load dialogue data from JSON (or hardcoded for now)"""
        # TODO: Load from data/dialogue.json when available
        # For now, return hardcoded dialogue
        return {
            "scribe": {
                "name": "The Scribe",
                "conversations": {
                    "first_meeting": [
                        "Another one awakes... Do you seek the truth, little knight?",
                        "The archives hold secrets. But beware the Hollow Ones...",
                        "They were once like you. Now... only echoes remain."
                    ],
                    "after_fragments": [
                        "So you've found them... the fragments of what was lost.",
                        "The path ahead is long. Perhaps... you'll be the one to restore the bells.",
                        "Good luck, little knight. May your light never fade."
                    ],
                    "repeat": [
                        "The silence grows deeper each day...",
                        "I wonder if the bells will ever ring again..."
                    ]
                }
            }
        }
    
    def start_dialogue(self, npc_id, conversation="first_meeting"):
        """Start a dialogue sequence"""
        if npc_id in self.dialogue_data:
            npc_data = self.dialogue_data[npc_id]
            
            if conversation in npc_data["conversations"]:
                self.current_dialogue = {
                    "npc_name": npc_data["name"],
                    "lines": npc_data["conversations"][conversation]
                }
                self.dialogue_index = 0
                self.active = True
                self.chars_shown = 0
                self.char_timer = 0
                self.can_advance = False
                self.advance_timer = 0
                self.prepare_current_line()
    
    def prepare_current_line(self):
        """Prepare the current dialogue line for display"""
        if self.current_dialogue and self.dialogue_index < len(self.current_dialogue["lines"]):
            self.full_text = self.current_dialogue["lines"][self.dialogue_index]
            self.wrapped_lines = self.wrap_text(self.full_text, self.box_rect.width - 20)
            self.chars_shown = 0
            self.char_timer = 0
    
    def wrap_text(self, text, max_width):
        """Wrap text to fit within max width"""
        # Simple word wrapping
        if not self.font:
            self.font = pygame.font.Font(None, 16)
        
        words = text.split(' ')
        lines = []
        current_line = []
        
        for word in words:
            test_line = ' '.join(current_line + [word])
            test_width = self.font.size(test_line)[0]
            
            if test_width <= max_width:
                current_line.append(word)
            else:
                if current_line:
                    lines.append(' '.join(current_line))
                current_line = [word]
        
        if current_line:
            lines.append(' '.join(current_line))
        
        return lines
    
    def advance(self):
        """Move to next dialogue line or close"""
        if not self.can_advance:
            # Show all text immediately
            self.chars_shown = len(self.full_text)
            self.can_advance = True
            return
        
        self.dialogue_index += 1
        
        if self.dialogue_index >= len(self.current_dialogue["lines"]):
            # End of dialogue
            self.close()
        else:
            # Next line
            self.prepare_current_line()
            self.can_advance = False
            self.advance_timer = 0
    
    def close(self):
        """Close dialogue"""
        self.active = False
        self.current_dialogue = None
        self.dialogue_index = 0
    
    def update(self, dt=0.016):
        """Update dialogue state"""
        if not self.active:
            return
        
        # Typewriter effect
        if self.chars_shown < len(self.full_text):
            self.char_timer += dt
            
            if self.char_timer >= self.char_delay:
                self.char_timer = 0
                self.chars_shown += 1
        else:
            # All text shown, can advance
            if not self.can_advance:
                self.advance_timer += dt
                
                if self.advance_timer >= self.advance_delay:
                    self.can_advance = True
    
    def is_active(self):
        """Check if dialogue is currently showing"""
        return self.active
    
    def draw(self, surface):
        """Draw dialogue box"""
        if not self.active or not self.current_dialogue:
            return
        
        if not self.font:
            self.font = pygame.font.Font(None, 16)
        
        # Draw box background
        pygame.draw.rect(surface, self.box_color, self.box_rect)
        pygame.draw.rect(surface, self.border_color, self.box_rect, 2)
        
        # Draw NPC name
        name_font = pygame.font.Font(None, 14)
        name_text = name_font.render(self.current_dialogue["npc_name"], True, self.border_color)
        surface.blit(name_text, (self.box_rect.x + 10, self.box_rect.y + 5))
        
        # Draw dialogue text with typewriter effect
        visible_text = self.full_text[:self.chars_shown]
        visible_lines = self.wrap_text(visible_text, self.box_rect.width - 20)
        
        y_offset = self.box_rect.y + 20
        for line in visible_lines[:3]:  # Max 3 lines
            line_surface = self.font.render(line, True, self.text_color)
            surface.blit(line_surface, (self.box_rect.x + 10, y_offset))
            y_offset += self.line_spacing
        
        # Draw continue indicator
        if self.can_advance:
            indicator_text = "[Press S] ▼"
            indicator_font = pygame.font.Font(None, 12)
            indicator_surface = indicator_font.render(indicator_text, True, self.text_color)
            indicator_x = self.box_rect.right - indicator_surface.get_width() - 10
            indicator_y = self.box_rect.bottom - 15
            surface.blit(indicator_surface, (indicator_x, indicator_y))
