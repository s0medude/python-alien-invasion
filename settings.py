import sys
import pygame

class Settings:
    def __init__(self):
        # Screen settings
        self.screen_width = 1200
        self.screen_heigth = 720
        self.bg_color = [0, 0, 0]
        self.bg_image = pygame.image.load('img/background.bmp')
        self.bg_image = pygame.transform.scale(self.bg_image, (self.screen_width, self.screen_heigth))
        self.bg_image_rect = self.bg_image.get_rect()
        self.bg_image_rect.left, self.bg_image_rect.top = (0,0)
        # Ship settings        
        self.ship_limit = 3
        #Bullet settings        
        self.bullet_width = 7
        self.bullet_height = 15
        self.bullet_color = (249, 166, 2)
        self.bullets_allowed = 7
        # Alien settings        
        self.fleet_alien_speed = 10        
        self.speedup_scale = 2
        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        # Initialize these values normally
        self.ship_speed = 1.5
        self.bullet_speed = 1.0
        self.alien_speed = 1.0
        self.fleet_direction = 1 

    def increase_speed(self, level=None):
        # Increase these attributtes according to the speedup_scale value 
        if level:
            self.ship_speed *= level
            self.bullet_speed *= level
            self.alien_speed *= level
        else:
            self.ship_speed *= self.speedup_scale
            self.bullet_speed *= self.speedup_scale
            self.alien_speed *= self.speedup_scale