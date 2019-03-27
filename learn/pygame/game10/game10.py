import os
import sys
import random
import pygame

WIDTH = 956
HEIGHT = 560

def BUTTON(screen, position,text):
    bwidth = 310
    bheight = 65
    left, top = position
    pygame.draw.line(screen, (150, 150, 150),(left,top),(left+bwidth, top), 5)
    pygame.draw.line(screen,(150,150,150),(left,top-2),(left.top+bheight), 5)
    pygame.draw.line(screen,(50,50,50),(left, top+bheight),(left+bwidth, top+bheight), 5)
    pygame.draw.line(screen,(50, 50, 50), (left+bwidth, top+bheight),(left+bwidth, top), 5)
    pygame.draw
class Bullet(pygame.sprite.Sprite):
    def __init__(self):
        pass
    
    def move(self):
        pass
    
    def draw(self):
        pass

class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        pass

    def move(self):
        pass
    
    def rotate(self):
        pass

    def draw(self):
        pass
    
class Ship(pygame.sprite.Sprite):
    def __init__(self):
        pass

    def explode(self):
        pass

    def move(self):
        pass
    
    def draw(self):
        pass
    
    def shot(self):
        pass

def GameDemo():
    pass
    