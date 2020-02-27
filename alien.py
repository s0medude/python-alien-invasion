import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.settings = game.settings
        self.image = pygame.image.load('img/alien.png')
        self.image = pygame.transform.scale(self.image, (80, 80))
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width // 2
        self.rect.y = self.rect.height // 2
        self.x = float(self.rect.x)

    def check_edges(self):
        if self.rect.right >= self.screen_rect.right or self.rect.left <= 0:
            return True
    
    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x =  self.x

   
