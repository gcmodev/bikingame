"""
Menu System - Main menu, pause menu, and other menus
"""

import pygame
import os

class Menu:
    """Main menu and pause menu system"""
    
    def __init__(self):
        """Initialize menu"""
        # Try to load pixel font, fallback to pygame default
        self.pixel_font = None
        self.load_fonts()
        
        # Menu state
        self.active = False
        self.menu_type = "MAIN"  # MAIN, PAUSE, SETTINGS
        self.selected_index = 0
        
        # Colors
        self.bg_color = (26, 28, 46)  # Dark blue
        self.text_color = (255, 255, 255)
        self.selected_color = (6, 182, 212)  # Cyan
        self.shadow_color = (0, 0, 0)
        self.box_color = (20, 20, 30, 200)
        self.border_color = (100, 150, 200)
        
        # Menu options
        self.main_menu_options = ["Start Game", "Settings", "Quit"]
        self.pause_menu_options = ["Resume", "Restart", "Main Menu", "Quit"]
        
        # Animation
        self.title_pulse = 0
        self.selector_offset = 0
        
    def load_fonts(self):
        """Load pixel fonts"""
        font_path = "assets/fonts/pixel.ttf"
        
        if os.path.exists(font_path):
            try:
                self.title_font = pygame.font.Font(font_path, 18)  # Much smaller!
                self.menu_font = pygame.font.Font(font_path, 10)
                self.small_font = pygame.font.Font(font_path, 8)
            except:
                self.use_default_fonts()
        else:
            self.use_default_fonts()
    
    def use_default_fonts(self):
        """Use pygame's default fonts as fallback"""
        # Pygame's default font - using smaller sizes for cleaner look
        self.title_font = pygame.font.Font(None, 36)
        self.menu_font = pygame.font.Font(None, 20)
        self.small_font = pygame.font.Font(None, 14)
    
    def show(self, menu_type="MAIN"):
        """Show menu"""
        self.active = True
        self.menu_type = menu_type
        self.selected_index = 0
    
    def hide(self):
        """Hide menu"""
        self.active = False
    
    def navigate_up(self):
        """Move selection up"""
        options = self.get_current_options()
        self.selected_index = (self.selected_index - 1) % len(options)
    
    def navigate_down(self):
        """Move selection down"""
        options = self.get_current_options()
        self.selected_index = (self.selected_index + 1) % len(options)
    
    def get_current_options(self):
        """Get current menu options"""
        if self.menu_type == "MAIN":
            return self.main_menu_options
        elif self.menu_type == "PAUSE":
            return self.pause_menu_options
        return []
    
    def get_selected_option(self):
        """Get currently selected option"""
        options = self.get_current_options()
        if 0 <= self.selected_index < len(options):
            return options[self.selected_index]
        return None
    
    def update(self, dt):
        """Update menu animations"""
        if not self.active:
            return
        
        # Minimal animation - just a subtle pulse
        self.title_pulse += dt * 2
    
    def draw(self, surface):
        """Draw menu"""
        if not self.active:
            return
        
        width = surface.get_width()
        height = surface.get_height()
        
        if self.menu_type == "MAIN":
            self.draw_main_menu(surface, width, height)
        elif self.menu_type == "PAUSE":
            self.draw_pause_menu(surface, width, height)
    
    def draw_main_menu(self, surface, width, height):
        """Draw main menu"""
        # Full background
        surface.fill(self.bg_color)
        
        # Draw title - simpler, cleaner
        title_text = "EMBER'S JOURNEY"
        title_surface = self.title_font.render(title_text, True, self.selected_color)
        title_rect = title_surface.get_rect(center=(width // 2, 40))
        
        # Shadow for depth
        shadow_surface = self.title_font.render(title_text, True, self.shadow_color)
        shadow_rect = shadow_surface.get_rect(center=(width // 2 + 2, 42))
        surface.blit(shadow_surface, shadow_rect)
        surface.blit(title_surface, title_rect)
        
        # Subtitle - moved further down
        subtitle_text = "A Dark Medieval Adventure"
        subtitle_surface = self.small_font.render(subtitle_text, True, (180, 180, 180))
        subtitle_rect = subtitle_surface.get_rect(center=(width // 2, 65))
        surface.blit(subtitle_surface, subtitle_rect)
        
        # Draw menu options - start much lower
        self.draw_menu_options(surface, width, height, 95)
        
        # Draw controls hint at bottom
        hint_text = "W/S: Navigate  |  SPACE: Select  |  F11: Fullscreen"
        hint_surface = self.small_font.render(hint_text, True, (120, 120, 120))
        hint_rect = hint_surface.get_rect(center=(width // 2, height - 15))
        surface.blit(hint_surface, hint_rect)
    
    def draw_pause_menu(self, surface, width, height):
        """Draw pause menu overlay"""
        # Semi-transparent overlay
        overlay = pygame.Surface((width, height))
        overlay.set_alpha(200)
        overlay.fill((0, 0, 0))
        surface.blit(overlay, (0, 0))
        
        # Menu box - centered and properly sized
        box_width = 140
        box_height = 120
        box_x = (width - box_width) // 2
        box_y = (height - box_height) // 2
        
        # Draw box background
        pygame.draw.rect(surface, self.box_color, (box_x, box_y, box_width, box_height))
        pygame.draw.rect(surface, self.border_color, (box_x, box_y, box_width, box_height), 2)
        
        # Title
        title_text = "PAUSED"
        title_surface = self.menu_font.render(title_text, True, self.selected_color)
        title_rect = title_surface.get_rect(center=(width // 2, box_y + 18))
        surface.blit(title_surface, title_rect)
        
        # Draw menu options - start below title
        self.draw_menu_options(surface, width, height, box_y + 40)
    
    def draw_menu_options(self, surface, width, height, start_y):
        """Draw menu options with selection"""
        options = self.get_current_options()
        
        for i, option in enumerate(options):
            is_selected = (i == self.selected_index)
            
            # Color based on selection
            color = self.selected_color if is_selected else self.text_color
            
            # Render text - clean and simple
            text_surface = self.menu_font.render(option, True, color)
            text_rect = text_surface.get_rect(center=(width // 2, start_y + i * 25))
            
            # Draw text only (no shadow for cleaner look)
            surface.blit(text_surface, text_rect)
            
            # Draw simple selector
            if is_selected:
                # Simple bracket style selector
                left_bracket = ">"
                right_bracket = "<"
                
                left_surface = self.menu_font.render(left_bracket, True, self.selected_color)
                right_surface = self.menu_font.render(right_bracket, True, self.selected_color)
                
                surface.blit(left_surface, (text_rect.left - 15, text_rect.top))
                surface.blit(right_surface, (text_rect.right + 5, text_rect.top))
    
    def draw_loading_screen(self, surface, progress=0):
        """Draw loading screen"""
        width = surface.get_width()
        height = surface.get_height()
        
        surface.fill(self.bg_color)
        
        # Title
        title_text = "EMBER'S JOURNEY"
        title_surface = self.title_font.render(title_text, True, self.selected_color)
        title_rect = title_surface.get_rect(center=(width // 2, height // 2 - 30))
        surface.blit(title_surface, title_rect)
        
        # Loading bar
        bar_width = 200
        bar_height = 20
        bar_x = (width - bar_width) // 2
        bar_y = height // 2 + 20
        
        # Background
        pygame.draw.rect(surface, (50, 50, 50), (bar_x, bar_y, bar_width, bar_height))
        
        # Progress
        progress_width = int(bar_width * progress)
        pygame.draw.rect(surface, self.selected_color, (bar_x, bar_y, progress_width, bar_height))
        
        # Border
        pygame.draw.rect(surface, self.border_color, (bar_x, bar_y, bar_width, bar_height), 2)
        
        # Loading text
        loading_text = f"Loading... {int(progress * 100)}%"
        loading_surface = self.small_font.render(loading_text, True, self.text_color)
        loading_rect = loading_surface.get_rect(center=(width // 2, bar_y + 40))
        surface.blit(loading_surface, loading_rect)
