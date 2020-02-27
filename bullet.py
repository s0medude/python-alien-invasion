import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, game):
        super().__init__()        
        self.screen = game.screen
        self.settings = game.settings
        self.color = self.settings.bullet_color
        # Create a bullet rect at (0,0) and then set the correct position
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)         
        self.rect.midtop = game.ship.rect.midtop
        # Store bullet's position as a decimal
        self.y = float(self.rect.y) 

    def update(self):
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)