import sys
import time
import random
import pygame
from config import *

class gemSprit(pygame.sprite.Sprite):
    def __init__(self, img_path, size, position, downlen, **kwargs):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_path)
        self.image = pygame.transform.smoothscale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.left ,self.rect.top = position
        self.downlen = downlen
        self.target_x = position[0]
        self.target_y = position[1] + downlen
        self.type = img_path.split('/')[-1].split('.')[0]
        self.fixed = False
        self.speed_x = 10
        self.speed_y = 10
        self.direction = 'down'
    
    def move(self):
        if self.direction == 'down':
            self.rect.top = min(self.target_y, self.rect.top +self.speed_y)
            if self.target_y == self.rect.top:
                self.fixed = True
        elif self.direction == 'up':
            self.rect.top = max(self.target_y, self.rect.top - self.speed_y)
            if self.target_y == self.rect.top:
                self.fixed = True
        elif self.direction == 'left':
            self.rect.left = max(self.target_x,self.rect.left-self.speed_x)
            if self.target_x == self.rect.left:
                self.fixed = True
        elif self.direction == 'right':
            self.rect.left = min(self.target_x, self.rect.left + self.speed_x)
            if self.target_x == self.rect.left:
                self.fixed = True

    def getPosition(self):
        return self.rect.left, self.rect.top
    
    def setPosition(self,position):
        self.rect.left, self.rect.top = position

class gemGame():
    def __init__(self, screen, font, gem_imgs, **lwwargs):
        self.screen = screen
        self.font = font
        self.gem_imgs = gem_imgs
        self.reset()
    
    def start(self):
        clock = pygame.time.Clock()
        overall_moving = True
        individual_moving = False
        gem_selected_xy = None
        gem_selected_xy2 = None
        swap_again = False
        add_score = 0
        add_score_showtimes = 10
        time_pre = int(time.time())

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONUP:
                    if (not overall_moving) and (not individual_moving) and (not add_score):
                        position = pygame.mouse.get_pos()
                        if gem_selected_xy is None:
                            gem_selected_xy = self.checkSelected(position)



    