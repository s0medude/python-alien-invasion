import pygame
from pygame.sprite import Sprite 

class Alien(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.image = pygame.image.load('img/alien.png')
        self.scale = pygame.transform.scale(self.image, (0, 0))
        self.rect = self.scale.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height
        self.x = float(self.rect.x)