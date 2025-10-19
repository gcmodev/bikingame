"""
Player Character - Ember
Handles player movement, combat, and animation
"""

import pygame

class Player:
    """Player character class"""
    
    def __init__(self, x, y):
        """Initialize player"""
        self.rect = pygame.Rect(x, y, 16, 24)  # Player hitbox
        
        # Physics
        self.velocity_x = 0
        self.velocity_y = 0
        self.gravity = 800  # Pixels per second squared
        self.jump_force = -300  # Initial jump velocity
        self.move_speed = 100  # Pixels per second
        
        # State
        self.on_ground = False
        self.facing_right = True
        self.is_attacking = False
        self.is_hurt = False
        
        # Animation
        self.animation_state = "idle"  # idle, walk, jump, attack, hurt
        self.animation_frame = 0
        self.animation_timer = 0
        self.animation_speed = 0.1  # Seconds per frame
        
        # Attack
        self.attack_timer = 0
        self.attack_duration = 0.3  # Seconds
        self.attack_range = 20
        self.attack_width = 25
        self.attack_height = 20
        
        # Invulnerability after getting hit
        self.hurt_timer = 0
        self.hurt_duration = 0.5
        self.invulnerable = False
        
        # Placeholder visual (will be replaced with sprites)
        self.color = (229, 231, 235)  # Light gray
    
    def jump(self):
        """Make player jump"""
        if self.on_ground and not self.is_attacking:
            self.velocity_y = self.jump_force
            self.on_ground = False
            self.animation_state = "jump"
    
    def attack(self):
        """Initiate attack"""
        if not self.is_attacking and self.on_ground:
            self.is_attacking = True
            self.attack_timer = self.attack_duration
            self.animation_state = "attack"
            self.animation_frame = 0
    
    def hurt(self):
        """Player takes damage"""
        if not self.invulnerable:
            self.is_hurt = True
            self.hurt_timer = self.hurt_duration
            self.invulnerable = True
            self.animation_state = "hurt"
            
            # Knockback
            self.velocity_x = -50 if self.facing_right else 50
            self.velocity_y = -100
    
    def update(self, dt, keys, collision_tiles):
        """Update player state"""
        # Update timers
        if self.attack_timer > 0:
            self.attack_timer -= dt
            if self.attack_timer <= 0:
                self.is_attacking = False
        
        if self.hurt_timer > 0:
            self.hurt_timer -= dt
            if self.hurt_timer <= 0:
                self.is_hurt = False
                self.invulnerable = False
        
        # Horizontal movement (only if not attacking or hurt)
        if not self.is_attacking and not self.is_hurt:
            if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                self.velocity_x = -self.move_speed
                self.facing_right = False
                if self.on_ground:
                    self.animation_state = "walk"
            elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                self.velocity_x = self.move_speed
                self.facing_right = True
                if self.on_ground:
                    self.animation_state = "walk"
            else:
                self.velocity_x = 0
                if self.on_ground and not self.is_attacking:
                    self.animation_state = "idle"
        
        # Apply gravity
        self.velocity_y += self.gravity * dt
        
        # Cap fall speed
        if self.velocity_y > 500:
            self.velocity_y = 500
        
        # Apply horizontal movement
        self.rect.x += self.velocity_x * dt
        self.handle_collision(collision_tiles, 'horizontal')
        
        # Apply vertical movement
        self.rect.y += self.velocity_y * dt
        self.handle_collision(collision_tiles, 'vertical')
        
        # Update animation
        self.update_animation(dt)
    
    def handle_collision(self, tiles, direction):
        """Handle collision with tiles"""
        self.on_ground = False
        
        for tile in tiles:
            tile_rect = pygame.Rect(tile['x'], tile['y'], tile['width'], tile['height'])
            
            if self.rect.colliderect(tile_rect):
                if direction == 'horizontal':
                    if self.velocity_x > 0:  # Moving right
                        self.rect.right = tile_rect.left
                    elif self.velocity_x < 0:  # Moving left
                        self.rect.left = tile_rect.right
                    self.velocity_x = 0
                
                elif direction == 'vertical':
                    if self.velocity_y > 0:  # Falling
                        self.rect.bottom = tile_rect.top
                        self.velocity_y = 0
                        self.on_ground = True
                    elif self.velocity_y < 0:  # Jumping up
                        self.rect.top = tile_rect.bottom
                        self.velocity_y = 0
    
    def update_animation(self, dt):
        """Update animation frame"""
        self.animation_timer += dt
        
        # Animation frame counts
        frame_counts = {
            'idle': 2,
            'walk': 4,
            'jump': 1,
            'attack': 3,
            'hurt': 1
        }
        
        max_frames = frame_counts.get(self.animation_state, 1)
        
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.animation_frame += 1
            
            if self.animation_frame >= max_frames:
                if self.animation_state == "attack":
                    self.animation_state = "idle"
                self.animation_frame = 0
    
    def get_attack_rect(self):
        """Get the attack hitbox"""
        if not self.is_attacking:
            return None
        
        attack_x = self.rect.right if self.facing_right else self.rect.left - self.attack_width
        attack_y = self.rect.centery - self.attack_height // 2
        
        return pygame.Rect(attack_x, attack_y, self.attack_width, self.attack_height)
    
    def draw(self, surface, camera_x, camera_y):
        """Draw player"""
        # Calculate screen position
        screen_x = self.rect.x - camera_x
        screen_y = self.rect.y - camera_y
        
        # Draw placeholder rectangle (will be replaced with sprite)
        # Flicker if invulnerable
        if self.invulnerable and int(self.hurt_timer * 20) % 2 == 0:
            return  # Don't draw (flicker effect)
        
        # Draw player body
        pygame.draw.rect(surface, self.color, (screen_x, screen_y, self.rect.width, self.rect.height))
        
        # Draw direction indicator (simple line)
        if self.facing_right:
            pygame.draw.line(surface, (255, 255, 255), 
                           (screen_x + self.rect.width, screen_y + 10),
                           (screen_x + self.rect.width + 5, screen_y + 10), 2)
        else:
            pygame.draw.line(surface, (255, 255, 255),
                           (screen_x, screen_y + 10),
                           (screen_x - 5, screen_y + 10), 2)
        
        # Draw attack hitbox (debug)
        if self.is_attacking:
            attack_rect = self.get_attack_rect()
            if attack_rect:
                attack_screen_x = attack_rect.x - camera_x
                attack_screen_y = attack_rect.y - camera_y
                pygame.draw.rect(surface, (255, 0, 0), 
                               (attack_screen_x, attack_screen_y, attack_rect.width, attack_rect.height), 1)
