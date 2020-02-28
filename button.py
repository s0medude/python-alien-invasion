import pygame.font

class Button:
    def __init__(self, game, msg):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height =  200, 50
        self.color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.prep_msg(msg)

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def draw_level_button(self):
        self.x = self.width + (2 * self.width)
        self.rect.left = self.x 
        self.draw_button()