import sys
import pygame
from pygame.locals import *

class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_heigth = 800
        self.bg_color = (255, 255, 255) 
        self.bg_image = Background(self, 'img/backgroud.bmp', [0, 0])

class Background(pygame.sprite.Sprite):
    def __init__(self, settings, pathname, location):
        pygame.sprite.Sprite.__init__(self)
        self.path = pygame.image.load(pathname)
        self.image = pygame.transform.scale(self.path, (settings.screen_width, settings.screen_heigth))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location
