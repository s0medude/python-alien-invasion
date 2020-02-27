import sys
import pygame

class Settings:
    def __init__(self):
        self.screen_width = 1000
        self.screen_heigth = 720
        self.bg_color = [0, 0, 0]
        self.bg_image = Background(self)
        self.ship_speed = 5.0
        self.bullet_speed = 2.0
        self.bullet_width = 4
        self.bullet_height = 15
        self.bullet_color = (249, 166, 2)
        self.bullets_allowed = 3

class Background():
    def __init__(self, settings):
        self.image = pygame.image.load('img/background.bmp')
        self.screen = pygame.transform.scale(self.image, (settings.screen_width, settings.screen_heigth))
        self.rect = self.screen.get_rect()
        self.rect.left, self.rect.top = (0,0)