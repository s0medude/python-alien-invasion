import pygame

class Button():
    def __init__(self, game):
        self.screen = game.screen
        self.screen_rect = self.screen.get_rect()
        self.width, self.height =  200, 50
        self.color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 48)
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.clicked = True

    def prep_msg(self, msg):
        self.msg_image = self.font.render(msg, True, self.text_color, self.color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self, msg, x, y):     
        self.rect.center = (x, y)
        self.prep_msg(msg)   
        self.screen.fill(self.color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_button(self, mouse_pos=None):
        if mouse_pos is not None:
            self.clicked = self.rect.collidepoint(mouse_pos)
            return self.clicked
        return self.clicked