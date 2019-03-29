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
    pygame.draw.line(screen,(150,150,150),(left,top-2),(left,top+bheight), 5)
    pygame.draw.line(screen,(50,50,50),(left, top+bheight),(left+bwidth, top+bheight), 5)
    pygame.draw.line(screen,(50, 50, 50), (left+bwidth, top+bheight),(left+bwidth, top), 5)
    pygame.draw.rect(screen,(100,100,100),(left,top,bwidth,bheight))
    font = pygame.font.Font('./font/simkai.ttf', 50)
    text_render = font.render(text, 1, (255, 0, 0))
    return screen.blit(text_render,(left + 50, top + 10))

def start_inferface(screen):
    clock = pygame.time.Clock()
    while True:
        button_1 = BUTTON(screen,(330, 190), '单人模式')
        button_2 = BUTTON(screen,(330, 305), '双人模式')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_1.collidepoint(pygame.mouse.get_pos()):
                    return 1
                elif button_2.collidepoint(pygame.mouse.get_pos()):
                    return 2

        clock.tick(60)
        pygame.display.update()


class Bullet(pygame.sprite.Sprite):
    def __init__(self,position,idx):
        pygame.sprite.Sprite.__init__(self)
        self.imgs = ['./imgs/bullet.png']
        self.image = pygame.image.load(self.imgs[0]).convert_alpha()
        self.image = pygame.transform.scale(self.image, (10,10))
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = position
        self.position = position
        self.speed = 8
        self.playerIdx = idx

    def move(self):
        self.position = self.position[0], self.position[1]-self.speed
        self.rect.left, self.rect.top = self.position
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)

class Asteroid(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.imgs = ['./imgs/asteroid.png']
        self.image = pygame.image.load(self.imgs[0]).convert_alpha
        self.rect = self.image.get_rect()
        self.position = (random.randrange(20, WIDTH-20), -64)
        self.rect.left, self.rect.top = self.position
        self.speed = random.randrange(3, 9)
        self.angle = 0
        self.angular_velocity = 

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

def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    num_player = start_inferface(screen)



if __name__ == '__main__':
    main()    