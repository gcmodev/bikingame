"""
Ember's Journey - Main Game File
A Hollow Knight-inspired 2D Adventure
"""

import pygame
import sys
from game.player import Player
from game.enemy import Enemy
from game.npc import NPC
from game.world import World
from game.camera import Camera
from game.ui import UI
from game.dialogue import DialogueSystem
from game.menu import Menu

# Game Constants
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720
BASE_WIDTH = 320
BASE_HEIGHT = 180
SCALE = 4  # 320x180 scaled to 1280x720
FPS = 60

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

class Game:
    """Main game class managing all game states and systems"""
    
    def __init__(self):
        """Initialize the game"""
        pygame.init()
        pygame.mixer.init()
        
        # Display setup
        self.fullscreen = False
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Ember's Journey")
        
        # Create a surface for base resolution (will be scaled up)
        self.game_surface = pygame.Surface((BASE_WIDTH, BASE_HEIGHT))
        
        # Clock for FPS
        self.clock = pygame.time.Clock()
        
        # Game state
        self.running = True
        self.paused = False
        self.current_state = "MENU"  # MENU, PLAYING, CUTSCENE, ENDING
        
        # Initialize game systems
        self.menu = Menu()
        self.menu.show("MAIN")  # Show main menu on start
        self.world = World()
        self.camera = Camera(BASE_WIDTH, BASE_HEIGHT)
        self.player = Player(50, 100)
        self.ui = UI()
        self.dialogue_system = DialogueSystem()
        
        # Game entities
        self.enemies = []
        self.npcs = []
        self.collectibles = []
        
        # Player stats
        self.health = 3
        self.max_health = 3
        self.soul_embers = 0
        self.memory_fragments = 0
        
        # Initialize first level
        self.load_level("tutorial_chamber")
        
    def load_level(self, level_name):
        """Load a level and spawn entities"""
        self.world.load_level(level_name)
        self.camera.set_bounds(
            self.world.level_width,
            self.world.level_height
        )
        
        # Clear existing entities
        self.enemies.clear()
        self.npcs.clear()
        self.collectibles.clear()
        
        # Spawn entities based on level data
        for spawn in self.world.get_spawns():
            if spawn['type'] == 'enemy':
                enemy = Enemy(spawn['x'], spawn['y'], spawn.get('variant', 'hollow_soldier'))
                self.enemies.append(enemy)
            elif spawn['type'] == 'npc':
                npc = NPC(spawn['x'], spawn['y'], spawn.get('npc_id', 'scribe'))
                self.npcs.append(npc)
            elif spawn['type'] == 'collectible':
                self.collectibles.append(spawn)
    
    def handle_events(self):
        """Handle input events"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            
            if event.type == pygame.KEYDOWN:
                # F11 for fullscreen toggle (works anywhere)
                if event.key == pygame.K_F11:
                    self.toggle_fullscreen()
                    return
                
                # Handle menu navigation
                if self.current_state == "MENU" and self.menu.active:
                    self.handle_menu_input(event.key)
                    return
                
                # ESC for pause menu
                if event.key == pygame.K_ESCAPE:
                    if self.current_state == "PLAYING":
                        if not self.paused:
                            self.paused = True
                            self.menu.show("PAUSE")
                        else:
                            self.paused = False
                            self.menu.hide()
                    return
                
                # Handle pause menu input
                if self.paused and self.menu.active:
                    self.handle_menu_input(event.key)
                    return
                
                # Handle dialogue advancement
                if self.dialogue_system.is_active():
                    if event.key in [pygame.K_s, pygame.K_DOWN, pygame.K_SPACE]:
                        self.dialogue_system.advance()
                    return  # Don't process other inputs while dialogue is active
                
                # Player input
                if not self.paused and self.current_state == "PLAYING":
                    if event.key in [pygame.K_SPACE, pygame.K_w]:
                        self.player.jump()
                    elif event.key in [pygame.K_j, pygame.K_z]:
                        self.player.attack()
                    elif event.key in [pygame.K_s, pygame.K_DOWN]:
                        self.interact()
    
    def handle_menu_input(self, key):
        """Handle menu navigation"""
        if key in [pygame.K_UP, pygame.K_w]:
            self.menu.navigate_up()
        elif key in [pygame.K_DOWN, pygame.K_s]:
            self.menu.navigate_down()
        elif key in [pygame.K_RETURN, pygame.K_SPACE]:
            self.select_menu_option()
        elif key == pygame.K_ESCAPE:
            if self.menu.menu_type == "PAUSE":
                self.paused = False
                self.menu.hide()
    
    def select_menu_option(self):
        """Handle menu option selection"""
        option = self.menu.get_selected_option()
        
        if option == "Start Game":
            self.start_game()
        elif option == "Resume":
            self.paused = False
            self.menu.hide()
        elif option == "Restart":
            self.restart_game()
        elif option == "Main Menu":
            self.return_to_main_menu()
        elif option == "Quit":
            self.running = False
    
    def start_game(self):
        """Start a new game"""
        self.current_state = "PLAYING"
        self.menu.hide()
        # Reset game state
        self.health = self.max_health
        self.soul_embers = 0
        self.memory_fragments = 0
        self.load_level("tutorial_chamber")
    
    def restart_game(self):
        """Restart current level"""
        self.paused = False
        self.menu.hide()
        self.health = self.max_health
        self.player.rect.x = 50
        self.player.rect.y = 100
        self.load_level("tutorial_chamber")
    
    def return_to_main_menu(self):
        """Return to main menu"""
        self.current_state = "MENU"
        self.paused = False
        self.menu.show("MAIN")
    
    def interact(self):
        """Handle interaction with NPCs, benches, etc."""
        # Check for nearby NPCs
        for npc in self.npcs:
            if npc.is_near_player(self.player):
                self.dialogue_system.start_dialogue(npc.dialogue_id)
                return
        
        # Check for benches
        for obj in self.world.get_interactive_objects():
            if obj['type'] == 'bench':
                if abs(self.player.rect.centerx - obj['x']) < 30:
                    self.save_game()
                    self.health = self.max_health
                    return
    
    def save_game(self):
        """Save game progress"""
        # TODO: Implement save system
        print("Game saved!")
    
    def toggle_fullscreen(self):
        """Toggle between fullscreen and windowed mode"""
        self.fullscreen = not self.fullscreen
        
        if self.fullscreen:
            # Get desktop resolution
            display_info = pygame.display.Info()
            self.screen = pygame.display.set_mode((display_info.current_w, display_info.current_h), pygame.FULLSCREEN)
        else:
            self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    
    def update(self, dt):
        """Update game logic"""
        # Update menu if active
        if self.current_state == "MENU" or self.paused:
            self.menu.update(dt)
            return
        
        if self.current_state != "PLAYING":
            return
        
        # Update dialogue system first
        self.dialogue_system.update(dt)
        
        # Don't update gameplay if dialogue is active
        if self.dialogue_system.is_active():
            return
        
        # Get keyboard input
        keys = pygame.key.get_pressed()
        
        # Player update
        self.player.update(dt, keys, self.world.get_collision_tiles())
        
        # Update enemies
        for enemy in self.enemies[:]:
            enemy.update(dt, self.player, self.world.get_collision_tiles())
            
            # Check player attacks hitting enemies
            if self.player.is_attacking and enemy.check_hit(self.player.get_attack_rect()):
                if enemy.take_damage(1):  # Enemy died
                    self.enemies.remove(enemy)
                    self.soul_embers += 2  # Drop soul embers
            
            # Check enemy attacks hitting player
            if enemy.is_attacking and enemy.check_player_hit(self.player.rect):
                self.take_damage(1)
        
        # Update NPCs
        for npc in self.npcs:
            npc.update(dt)
        
        # Check collectible pickups
        for collectible in self.collectibles[:]:
            if self.player.rect.colliderect(
                pygame.Rect(collectible['x'], collectible['y'], 16, 16)
            ):
                self.collect_item(collectible)
                self.collectibles.remove(collectible)
        
        # Update camera to follow player
        self.camera.update(self.player)
        
        # Check for level transitions
        self.check_level_transitions()
    
    def take_damage(self, amount):
        """Player takes damage"""
        self.health -= amount
        self.player.hurt()
        
        if self.health <= 0:
            self.game_over()
    
    def collect_item(self, collectible):
        """Collect an item"""
        if collectible['item_type'] == 'soul_ember':
            self.soul_embers += 1
        elif collectible['item_type'] == 'memory_fragment':
            self.memory_fragments += 1
            # TODO: Show memory flash cutscene
            print(f"Memory Fragment collected! ({self.memory_fragments}/3)")
    
    def check_level_transitions(self):
        """Check if player has reached a level transition"""
        for transition in self.world.get_transitions():
            if self.player.rect.colliderect(
                pygame.Rect(transition['x'], transition['y'], transition['width'], transition['height'])
            ):
                self.load_level(transition['target_level'])
                self.player.rect.x = transition['spawn_x']
                self.player.rect.y = transition['spawn_y']
                break
    
    def game_over(self):
        """Handle player death"""
        # TODO: Implement respawn at last bench
        print("Game Over!")
        self.health = self.max_health
        self.player.rect.x = 50
        self.player.rect.y = 100
    
    def draw(self):
        """Render everything"""
        # Clear the base surface
        self.game_surface.fill(BLACK)
        
        # Draw menu if in menu state
        if self.current_state == "MENU":
            self.menu.draw(self.game_surface)
        else:
            # Get camera offset
            cam_x, cam_y = self.camera.get_offset()
            
            # Draw world (background, tiles, platforms)
            self.world.draw(self.game_surface, cam_x, cam_y)
            
            # Draw collectibles
            for collectible in self.collectibles:
                x = collectible['x'] - cam_x
                y = collectible['y'] - cam_y
                # Draw placeholder (will be replaced with sprites)
                color = (6, 182, 212) if collectible['item_type'] == 'memory_fragment' else (249, 115, 22)
                pygame.draw.circle(self.game_surface, color, (int(x), int(y)), 4)
            
            # Draw NPCs
            for npc in self.npcs:
                npc.draw(self.game_surface, cam_x, cam_y)
            
            # Draw enemies
            for enemy in self.enemies:
                enemy.draw(self.game_surface, cam_x, cam_y)
            
            # Draw player
            self.player.draw(self.game_surface, cam_x, cam_y)
            
            # Draw UI (HUD, dialogue, menus)
            self.ui.draw(self.game_surface, self.health, self.max_health, self.soul_embers, self.memory_fragments)
            
            # Draw dialogue if active
            if self.dialogue_system.is_active():
                self.dialogue_system.draw(self.game_surface)
            
            # Draw pause menu if paused
            if self.paused:
                self.menu.draw(self.game_surface)
        
        # Scale up the base surface to screen size
        screen_size = self.screen.get_size()
        
        if self.fullscreen:
            # Center the scaled game on fullscreen
            aspect_ratio = BASE_WIDTH / BASE_HEIGHT
            screen_aspect = screen_size[0] / screen_size[1]
            
            if screen_aspect > aspect_ratio:
                # Screen is wider - fit to height
                new_height = screen_size[1]
                new_width = int(new_height * aspect_ratio)
            else:
                # Screen is taller - fit to width
                new_width = screen_size[0]
                new_height = int(new_width / aspect_ratio)
            
            scaled_surface = pygame.transform.scale(self.game_surface, (new_width, new_height))
            x_offset = (screen_size[0] - new_width) // 2
            y_offset = (screen_size[1] - new_height) // 2
            
            self.screen.fill(BLACK)
            self.screen.blit(scaled_surface, (x_offset, y_offset))
        else:
            # Normal windowed mode
            scaled_surface = pygame.transform.scale(self.game_surface, screen_size)
            self.screen.blit(scaled_surface, (0, 0))
        
        # Update display
        pygame.display.flip()
    
    def run(self):
        """Main game loop"""
        while self.running:
            # Delta time in seconds
            dt = self.clock.tick(FPS) / 1000.0
            
            # Handle events
            self.handle_events()
            
            # Update game state
            self.update(dt)
            
            # Draw everything
            self.draw()
        
        # Cleanup
        pygame.quit()
        sys.exit()


def main():
    """Entry point"""
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
