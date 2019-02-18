#精灵类 生产动画
import pygame

class MySprite(pygame.sprite.Sprite):

    def __init__(self,targe):
        pygame.sprite.Sprite.__init__(self):
        