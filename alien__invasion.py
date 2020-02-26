import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()  
        self.settings = Settings()      
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_heigth))
        self.ship = Ship(self)
        pygame.display.set_caption("ALIEN INVASION")

    def _check_events(self):
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.settings.bg_image.image, self.settings.bg_image.rect)
        self.ship.blitme()
        pygame.display.flip()

    def run_game(self):
        while True:  
            self._check_events()  
            self._update_screen()        
            

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()