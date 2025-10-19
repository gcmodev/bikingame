"""
UI System - HUD, menus, and on-screen displays
"""

import pygame

class UI:
    """User interface and HUD"""
    
    def __init__(self):
        """Initialize UI"""
        self.font_small = None
        self.font_medium = None
        self.font_large = None
        
        # Colors
        self.text_color = (255, 255, 255)
        self.shadow_color = (0, 0, 0)
        self.health_color = (239, 68, 68)  # Red
        self.ember_color = (249, 115, 22)  # Orange
        self.fragment_color = (6, 182, 212)  # Cyan
        
        # Health display
        self.heart_size = 12
        self.heart_spacing = 14
        
        # Notification system
        self.notifications = []
    
    def draw(self, surface, health, max_health, soul_embers, memory_fragments):
        """Draw the HUD"""
        if not self.font_small:
            self.font_small = pygame.font.Font(None, 14)
            self.font_medium = pygame.font.Font(None, 18)
            self.font_large = pygame.font.Font(None, 24)
        
        # Draw health (hearts in top-left)
        self.draw_health(surface, health, max_health)
        
        # Draw soul embers count (top-right)
        self.draw_counter(surface, "Soul Embers", soul_embers, self.ember_color, 200, 5)
        
        # Draw memory fragments (top-right, below embers)
        self.draw_counter(surface, "Fragments", memory_fragments, self.fragment_color, 200, 20)
        
        # Draw notifications
        self.draw_notifications(surface)
    
    def draw_health(self, surface, health, max_health):
        """Draw health hearts"""
        x = 5
        y = 5
        
        for i in range(max_health):
            # Draw heart (simplified as rectangle for now)
            if i < health:
                # Full heart
                self.draw_heart(surface, x + i * self.heart_spacing, y, True)
            else:
                # Empty heart
                self.draw_heart(surface, x + i * self.heart_spacing, y, False)
    
    def draw_heart(self, surface, x, y, filled):
        """Draw a heart shape (simplified)"""
        size = self.heart_size
        
        if filled:
            # Filled heart (simple diamond shape for now)
            points = [
                (x + size//2, y),
                (x + size, y + size//2),
                (x + size//2, y + size),
                (x, y + size//2)
            ]
            pygame.draw.polygon(surface, self.health_color, points)
        else:
            # Empty heart outline
            points = [
                (x + size//2, y),
                (x + size, y + size//2),
                (x + size//2, y + size),
                (x, y + size//2)
            ]
            pygame.draw.polygon(surface, (100, 100, 100), points, 2)
    
    def draw_counter(self, surface, label, value, color, x, y):
        """Draw a labeled counter"""
        # Draw shadow
        shadow_text = self.font_small.render(f"{label}: {value}", True, self.shadow_color)
        surface.blit(shadow_text, (x + 1, y + 1))
        
        # Draw text
        text = self.font_small.render(f"{label}: {value}", True, color)
        surface.blit(text, (x, y))
    
    def draw_notifications(self, surface):
        """Draw notification messages"""
        y_offset = 40
        
        for notification in self.notifications[:]:
            # Draw centered notification
            text = self.font_medium.render(notification['text'], True, notification['color'])
            text_rect = text.get_rect(center=(160, y_offset))
            
            # Draw background
            bg_rect = text_rect.inflate(10, 5)
            pygame.draw.rect(surface, (0, 0, 0, 180), bg_rect)
            pygame.draw.rect(surface, notification['color'], bg_rect, 2)
            
            # Draw text
            surface.blit(text, text_rect)
            
            # Update timer
            notification['timer'] -= 1/60  # Assuming 60 FPS
            if notification['timer'] <= 0:
                self.notifications.remove(notification)
            
            y_offset += 20
    
    def show_notification(self, text, color=(255, 255, 255), duration=2.0):
        """Show a notification message"""
        self.notifications.append({
            'text': text,
            'color': color,
            'timer': duration
        })
    
    def draw_interact_prompt(self, surface, text="Press S to Interact"):
        """Draw interaction prompt"""
        # Draw at bottom center
        prompt_text = self.font_small.render(text, True, self.text_color)
        rect = prompt_text.get_rect(center=(160, 165))
        
        # Draw background
        bg_rect = rect.inflate(10, 5)
        pygame.draw.rect(surface, (0, 0, 0, 180), bg_rect)
        pygame.draw.rect(surface, self.text_color, bg_rect, 1)
        
        surface.blit(prompt_text, rect)
    
    def draw_menu(self, surface, title, options, selected_index):
        """Draw a menu"""
        # Draw semi-transparent background
        overlay = pygame.Surface((160, 120))
        overlay.set_alpha(200)
        overlay.fill((20, 20, 30))
        surface.blit(overlay, (80, 30))
        
        # Draw border
        pygame.draw.rect(surface, (100, 150, 200), (80, 30, 160, 120), 2)
        
        # Draw title
        title_text = self.font_large.render(title, True, self.text_color)
        title_rect = title_text.get_rect(center=(160, 50))
        surface.blit(title_text, title_rect)
        
        # Draw options
        y_start = 75
        for i, option in enumerate(options):
            color = (255, 255, 100) if i == selected_index else self.text_color
            option_text = self.font_medium.render(option, True, color)
            
            if i == selected_index:
                # Draw selector
                pygame.draw.polygon(surface, color, [
                    (95, y_start + i * 20 + 5),
                    (95, y_start + i * 20 + 12),
                    (100, y_start + i * 20 + 8)
                ])
            
            surface.blit(option_text, (110, y_start + i * 20))
