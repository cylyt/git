import pygame
from pygame.sprite import Sprite

class Arrow(Sprite):

    def __init__(self,ai_setting,screen,rabbit):

        super(Arrow,self).__init__()
        self.ai_setting = ai_setting
        self.screen = screen
        self.image = pygame.image.load("image/bullet.png")
        self.rect = pygame.Rect(0,0,self.image.get_rect().width,self.image.get_rect().height)

        self.rect[0] = rabbit.rect[0]
        self.rect[1] = rabbit.rect[1]+rabbit.rect_height/2

        self.x = float(self.rect.x)

        self.speed_factor = ai_setting.arrow_speed

    def update(self):
        self.x += self.speed_factor
        self.rect.x=self.x

    def draw_arrow(self):
        self.screen.blit(self.image,self.rect)








