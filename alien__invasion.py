import sys
import pygame
from settings import Settings
from bullet import Bullet
from alien import Alien
from ship import Ship

class AlienInvasion:
    def __init__(self):
        pygame.init()        
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_heigth))
        pygame.display.set_caption("ALIEN INVASION by s0medude")
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()    
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
     
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:           
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)                
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
    
    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _draw_bullet(self):
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()  

    def _update_bullet(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)  

    def _create_fleet(self):
       alien = Alien(self)
       alien_width = alien.rect.width
       available_space_x = self.settings.screen_width - (2 * alien_width)
       number_aliens_x = available_space_x // (2 * alien_width)
       for alien_number in range(number_aliens_x + 1):
           alien = Alien(self)
           alien.x = alien_width + (2 * alien_width * alien_number)
           alien.rect.x = alien.x
           self.aliens.add(alien)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        self.screen.blit(self.settings.bg_image.image, self.settings.bg_image.rect)
        self.ship.blitme()    
        self._draw_bullet()    
        self.aliens.draw(self.screen)      
        pygame.display.flip()

    def run_game(self):
        while True:  
            self._check_events()   
            self.ship.update()             
            self._update_bullet()          
            self._update_screen()        
            
if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
