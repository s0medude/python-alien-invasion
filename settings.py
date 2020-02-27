import sys
import pygame

class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_heigth = 720
        self.bg_color = [0, 0, 0]
        self.bg_image = pygame.image.load('img/background.bmp')
        self.bg_image = pygame.transform.scale(self.bg_image, (self.screen_width, self.screen_heigth))
        self.bg_image_rect = self.bg_image.get_rect()
        self.bg_image_rect.left, self.bg_image_rect.top = (0,0)
        self.ship_speed = 1.5
        self.ship_limit = 3
        self.bullet_speed = 2.0
        self.bullet_width = 7
        self.bullet_height = 15
        self.bullet_color = (249, 166, 2)
        self.bullets_allowed = 5
        self.alien_speed = 1.0
        self.fleet_alien_speed = 10
        self.fleet_direction = 1 
        