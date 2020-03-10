import sys
import json
import pygame
from time import sleep

from scoreboard import ScoreBoard
from game_stats import GameStats
from settings import Settings
from bullet import Bullet
from button import Button
from alien import Alien
from ship import Ship


class AlienInvasion:
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width, self.settings.screen_heigth))
        pygame.display.set_caption("Alien INVASION by s0medude")
        self.stats = GameStats(self)
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        self._create_fleet()
        self.play_button = Button(self)
        self.levels_button = Button(self)
        self.button_levels_list = []
        self.scoreboard = ScoreBoard(self)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True
        elif event.key == pygame.K_q:
            sys.exit()
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
        elif event.key == pygame.K_p:
            if not self.stats.game_active:
                self.settings.initialize_dynamic_settings()
                self._start_game()
        elif event.key == pygame.K_r:
            self.stats.game_active = False
            self._reset_stats()
            pygame.mouse.set_visible(True)

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        if event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _check_mouse_events(self):
        mouse_pos = pygame.mouse.get_pos()
        if not self.levels_button.clicked:
            self._check_play_button(mouse_pos)
            self._check_main_levels_button(mouse_pos)
        else:
            self._check_level_button(mouse_pos)           
                      

    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._save_high_score()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self._check_mouse_events() 

    def _save_high_score(self):
        filename = 'high_score.json'
        with open(filename, 'w') as f:
            json.dump(self.stats.high_score, f)                      

    def _draw_bullet(self):
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _check_bullet_alien_collision(self):
        collisions = pygame.sprite.groupcollide(self.bullets, self.aliens, True, True)
        if collisions:
            for aliens in collisions.values():
                self.stats.score += self.settings.alien_points * len(aliens)
            self.scoreboard.prep_score()
            self.scoreboard.check_high_score()
        self._start_new_level()

    def _start_new_level(self):
        if not self.aliens:
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
            self.stats.level += 1
            self.scoreboard.prep_level()

    def _update_bullet(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collision()
        
    def _create_alien(self, alien_number, row_number):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        alien.x = alien_width + (2 * alien_width * alien_number)
        alien.rect.x = alien.x
        alien.rect.y = alien_height + (2 * alien_height * row_number)
        self.aliens.add(alien)

    def _create_fleet(self):
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size
        ship_height = self.ship.rect.height
        available_space_x = self.settings.screen_width - (2 * alien_width) 
        available_space_y = (self.settings.screen_heigth - (3 * alien_height) - ship_height)
        number_aliens_x = available_space_x // (2 * alien_width)   
        number_rows = available_space_y // (2 * alien_height)        
        for row_number in range(number_rows + 1):
            for alien_number in range(number_aliens_x + 1):
                self._create_alien(alien_number, row_number)     

    def _check_fleet_edges(self):
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_directions()
                break

    def _change_fleet_directions(self):
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_alien_speed
        self.settings.fleet_direction *= -1    

    def _ship_hit(self):
        if self.stats.ship_left > 0:
            self.stats.ship_left -= 1
            self.scoreboard.prep_ships()
            self.aliens.empty()
            self.bullets.empty()
            self._create_fleet()
            self.ship.center_ship()
            sleep(0.5)
        else:
            self.stats.game_active = False
            self._reset_stats()
            pygame.mouse.set_visible(True)

    def _check_ship_hit(self):
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit() 

    def _check_aliens_bottom(self):
        screen_rect =  self.screen.get_rect()
        for alien in self.aliens.sprites():
            if alien.rect.bottom >= screen_rect.bottom:
                self._ship_hit()
                break

    def _update_aliens(self):
        self._check_fleet_edges()
        self.aliens.update()     
        self._check_ship_hit()     
        self._check_aliens_bottom() 

    def _draw_main_buttons(self):
        if not self.stats.game_active and not self.levels_button.clicked:
            self.play_button.draw_button("START", 450, 360)
            self.levels_button.draw_button("LEVELS", 750, 360)
        elif not self.stats.game_active and self.levels_button.clicked:
            self._draw_level_buttons()
            
    def _draw_level_buttons(self):
        number_buttons_x, number_rows_y = 3, 3
        number = 1
        for row in range(number_rows_y):
            row += 1
            for level in range(number_buttons_x):
                level += 1         
                button = Button(self)
                button.rect.width, button.rect.height = 150, 50
                button.draw_button(f"Level {str(number)}", 300 * level, 180 * row)              
                number += 1
                self.button_levels_list.append(button)

    def _check_play_button(self, mouse_pos):        
        if self.play_button.check_button(mouse_pos) and not self.stats.game_active:  
            self._reset_stats()
            self._start_game()
        
    def _check_main_levels_button(self, mouse_pos):
        if self.levels_button.check_button(mouse_pos) and not self.stats.game_active:
            self._update_screen()
    
    def _check_level_button(self, mouse_pos):
        for button in self.button_levels_list:
            if button.check_button(mouse_pos) and not self.stats.game_active:
                i =  self.button_levels_list.index(button)
                self.stats.level += i
                self.settings.increase_speed(self.stats.level)                
                self._start_game()
                self.levels_button.clicked = False   

    def _reset_stats(self):
        self.settings.initialize_dynamic_settings()
        self.stats.reset_stats()
        self.levels_button.clicked = False

    def _start_game(self):
        self.stats.game_active = True
        self.scoreboard.prep_images()
        self.bullets.empty()
        self.aliens.empty()        
        self._create_fleet()
        self.ship.center_ship()
        pygame.mouse.set_visible(False)

    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)
        #self.screen.blit(self.settings.bg_image, self.settings.bg_image_rect)
        self.ship.blitme()
        self._draw_bullet()
        self.aliens.draw(self.screen)
        self.scoreboard.show_score()
        self._draw_main_buttons()
        pygame.display.flip()

    def run_game(self):
        while True:
            self._check_events()
            if self.stats.game_active:
                self.ship.update()
                self._update_bullet()
                self._update_aliens()
            self._update_screen()            

if __name__ == "__main__":
    ai = AlienInvasion()
    ai.run_game()
