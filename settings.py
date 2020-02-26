import sys
import pygame
from pygame.locals import *

class Settings:
    def __init__(self):
        self.screen_width = 1200
        self.screen_heigth = 720
        self.bg_color = [255, 255, 255]
        self.bg_image = Background()
        self.ship_speed = 10

class Background():
    def __init__(self):
        self.image = pygame.image.load('img/background.jpg')
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = (0,0)