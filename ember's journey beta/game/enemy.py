"""
Enemy System - Hollow Soldiers and other enemies
"""

import pygame
import random

class Enemy:
    """Base enemy class"""
    
    def __init__(self, x, y, variant="hollow_soldier"):
        """Initialize enemy"""
        self.rect = pygame.Rect(x, y, 16, 24)
        self.variant = variant
        
        # Stats based on variant
        self.setup_stats()
        
        # Physics
        self.velocity_x = 0
        self.velocity_y = 0
        self.gravity = 800
        self.on_ground = False
        
        # AI State
        self.state = "patrol"  # patrol, chase, attack, idle
        self.facing_right = True
        
        # Patrol behavior
        self.patrol_start_x = x
        self.patrol_range = 80
        self.patrol_speed = 30
        
        # Detection
        self.detection_range = 100
        self.attack_range = 40
        
        # Attack
        self.is_attacking = False
        self.attack_timer = 0
        self.attack_duration = 0.4
        self.attack_cooldown = 1.0
        self.attack_cooldown_timer = 0
        
        # Health
        self.is_dead = False
        self.death_timer = 0
        self.death_duration = 0.3
        
        # Animation
        self.animation_state = "idle"
        self.animation_frame = 0
        self.animation_timer = 0
        self.animation_speed = 0.15
        
        # Visual
        self.color = (153, 27, 27)  # Dark red
    
    def setup_stats(self):
        """Setup stats based on enemy variant"""
        if self.variant == "hollow_soldier":
            self.health = 3
            self.max_health = 3
            self.damage = 1
            self.move_speed = 40
        # Add more variants here later
    
    def update(self, dt, player, collision_tiles):
        """Update enemy AI and physics"""
        if self.is_dead:
            self.death_timer += dt
            return
        
        # Update cooldowns
        if self.attack_cooldown_timer > 0:
            self.attack_cooldown_timer -= dt
        
        if self.attack_timer > 0:
            self.attack_timer -= dt
            if self.attack_timer <= 0:
                self.is_attacking = False
        
        # AI Logic
        self.update_ai(player)
        
        # Apply gravity
        self.velocity_y += self.gravity * dt
        if self.velocity_y > 500:
            self.velocity_y = 500
        
        # Apply movement
        self.rect.x += self.velocity_x * dt
        self.handle_collision(collision_tiles, 'horizontal')
        
        self.rect.y += self.velocity_y * dt
        self.handle_collision(collision_tiles, 'vertical')
        
        # Update animation
        self.update_animation(dt)
    
    def update_ai(self, player):
        """Update AI state machine"""
        # Calculate distance to player
        distance = abs(self.rect.centerx - player.rect.centerx)
        
        if distance <= self.attack_range and self.on_ground:
            # Attack player
            self.state = "attack"
            self.velocity_x = 0
            
            if self.attack_cooldown_timer <= 0:
                self.attack()
        
        elif distance <= self.detection_range:
            # Chase player
            self.state = "chase"
            
            if player.rect.centerx > self.rect.centerx:
                self.velocity_x = self.move_speed
                self.facing_right = True
            else:
                self.velocity_x = -self.move_speed
                self.facing_right = False
        
        else:
            # Patrol
            self.state = "patrol"
            self.patrol()
    
    def patrol(self):
        """Simple patrol behavior"""
        # Move in patrol range
        if self.facing_right:
            self.velocity_x = self.patrol_speed
            
            if self.rect.x > self.patrol_start_x + self.patrol_range:
                self.facing_right = False
        else:
            self.velocity_x = -self.patrol_speed
            
            if self.rect.x < self.patrol_start_x - self.patrol_range:
                self.facing_right = True
    
    def attack(self):
        """Initiate attack"""
        self.is_attacking = True
        self.attack_timer = self.attack_duration
        self.attack_cooldown_timer = self.attack_cooldown
        self.animation_state = "attack"
        self.animation_frame = 0
    
    def check_hit(self, attack_rect):
        """Check if enemy is hit by attack"""
        if attack_rect and self.rect.colliderect(attack_rect):
            return True
        return False
    
    def check_player_hit(self, player_rect):
        """Check if enemy's attack hits player"""
        if not self.is_attacking:
            return False
        
        attack_rect = self.get_attack_rect()
        if attack_rect and player_rect.colliderect(attack_rect):
            return True
        return False
    
    def get_attack_rect(self):
        """Get attack hitbox"""
        if not self.is_attacking:
            return None
        
        attack_width = 25
        attack_height = 20
        attack_x = self.rect.right if self.facing_right else self.rect.left - attack_width
        attack_y = self.rect.centery - attack_height // 2
        
        return pygame.Rect(attack_x, attack_y, attack_width, attack_height)
    
    def take_damage(self, amount):
        """Enemy takes damage, returns True if dead"""
        self.health -= amount
        
        # Knockback
        knockback = 50
        self.velocity_x = knockback if self.rect.centerx < 160 else -knockback
        self.velocity_y = -100
        
        if self.health <= 0:
            self.die()
            return True
        
        return False
    
    def die(self):
        """Enemy death"""
        self.is_dead = True
        self.death_timer = 0
        self.animation_state = "death"
        self.animation_frame = 0
    
    def handle_collision(self, tiles, direction):
        """Handle collision with tiles"""
        self.on_ground = False
        
        for tile in tiles:
            tile_rect = pygame.Rect(tile['x'], tile['y'], tile['width'], tile['height'])
            
            if self.rect.colliderect(tile_rect):
                if direction == 'horizontal':
                    if self.velocity_x > 0:
                        self.rect.right = tile_rect.left
                        # Turn around when hitting wall during patrol
                        if self.state == "patrol":
                            self.facing_right = False
                    elif self.velocity_x < 0:
                        self.rect.left = tile_rect.right
                        if self.state == "patrol":
                            self.facing_right = True
                    self.velocity_x = 0
                
                elif direction == 'vertical':
                    if self.velocity_y > 0:
                        self.rect.bottom = tile_rect.top
                        self.velocity_y = 0
                        self.on_ground = True
                    elif self.velocity_y < 0:
                        self.rect.top = tile_rect.bottom
                        self.velocity_y = 0
    
    def update_animation(self, dt):
        """Update animation frames"""
        self.animation_timer += dt
        
        frame_counts = {
            'idle': 2,
            'walk': 3,
            'attack': 2,
            'death': 3
        }
        
        max_frames = frame_counts.get(self.animation_state, 1)
        
        if self.animation_timer >= self.animation_speed:
            self.animation_timer = 0
            self.animation_frame += 1
            
            if self.animation_frame >= max_frames:
                if self.animation_state == "death":
                    self.animation_frame = max_frames - 1  # Stay on last frame
                else:
                    self.animation_frame = 0
    
    def draw(self, surface, camera_x, camera_y):
        """Draw enemy"""
        if self.is_dead and self.death_timer > self.death_duration:
            return  # Don't draw after death animation
        
        screen_x = self.rect.x - camera_x
        screen_y = self.rect.y - camera_y
        
        # Fade out during death
        alpha = 255
        if self.is_dead:
            alpha = int(255 * (1 - self.death_timer / self.death_duration))
        
        # Draw placeholder (will be replaced with sprite)
        color = tuple(int(c * (alpha / 255)) for c in self.color)
        pygame.draw.rect(surface, color, (screen_x, screen_y, self.rect.width, self.rect.height))
        
        # Draw direction indicator
        if self.facing_right:
            pygame.draw.line(surface, (255, 255, 255),
                           (screen_x + self.rect.width, screen_y + 10),
                           (screen_x + self.rect.width + 4, screen_y + 10), 1)
        else:
            pygame.draw.line(surface, (255, 255, 255),
                           (screen_x, screen_y + 10),
                           (screen_x - 4, screen_y + 10), 1)
        
        # Draw health bar
        if not self.is_dead and self.health < self.max_health:
            bar_width = 16
            bar_height = 3
            health_ratio = self.health / self.max_health
            
            # Background
            pygame.draw.rect(surface, (50, 50, 50),
                           (screen_x, screen_y - 6, bar_width, bar_height))
            # Health
            pygame.draw.rect(surface, (255, 0, 0),
                           (screen_x, screen_y - 6, int(bar_width * health_ratio), bar_height))
