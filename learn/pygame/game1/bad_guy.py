import pygame
from pygame.sprite import Sprite

class Bad_guy(Sprite):

    def __init__(self,ai_setting,screen):
        
        super(Bad_guy,self).__init__()
        self.ai_setting=ai_setting
        self.screen=screen
        self.screen_rect = self.screen.get_rect()

        self.image =  pygame.image.load("image/badguy.png")
        self.rect = self.image.get_rect()

        self.rect.x = self.screen_rect.width-10
        self.rect.y = 10

        self.x = float(self.rect.x)
    
    def update(self):
        self.x -= self.ai_setting.bad_guy_speed
        self.rect.x = self.x
    
    def blitme(self):
        self.screen.blit(self.image,self.rect)

