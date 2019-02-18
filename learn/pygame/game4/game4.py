import sys
import pygame
import random
from pygame.locals import *

#滑雪者
class SkierClass(pygame.sprite.Sprite):

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.direction = 0
        self.images = ["image/skier_forward.png","image/skier_right1.png","image/skier_right2.png","image/skier_left2.png","image/skier_left1.png"]
        self.person = pygame.image.load(self.images[self.direction])
        self.rect = self.person.get_rect()
        self.speed = [self.direction,6-abs(self.direction)*2]

    def turn(self,num):
        self.direction +=num
        self.direction = max(-2,self.direction)
        self.direction = min(2,self.direction)
        center = self.rect.center
        self.person = pygame.image.load(self.images[self.direction])
        self.rect = self.person.get_rect()
        self.rect.center = center
        self.speed = [self.direction,6-abs(self.direction)*2]
        return self.speed
    def move(self):
        self.rect.centerx +=self.speed[0]
        self.rect.centerx = max(20,self.rect.centerx)
        self.rect.centerx = min(620,self.rect.centerx)

class ObstacleClass(pygame.sprite.Sprite):

    def __init__(self,img_path,location,attribute):
        pygame.sprite.Sprite.__init__(self)
        self.img_path = img_path
        self.image = pygame.iamge.load(self.img_path)
        self.location = location
        self.rect = self.image.get_rect()
        self.rect.center = self.location
        self.attribute = attribute
        self.passed = False

    def move(self,num):
        self.rect.centery = self.location[1]-num
    
    def create_obstacles(s,e,num=10):
        obstacles = pygame.sprite.Group()
        locations = []
        for i in range(num):
            row = random.randint(s,e)
            col = random.randint(0,9)
            location = [col*64+20,row*64+20]
            if location not in locations:
                locations.append(location)
                attribute = random.choice(["tree","flasg"])
                img_path = "image/tree.png" if attribute == "tree" else "image/flag.png"
                obstacle = ObstacleClass(img_path,location,attribute)
                obstacles.add(obstacle)
        return obstacles
    
    def AddObstacles(obstacles0,obstacles1):
        obstacles = pygame.sprite.Group()
        for obstacle in obstacles0:
            obstacles.add(obstacle)
        for obstacle in obstacles1:
            obstacle.add(obstacle)
        return obstacles

def Show_Start_Interface(Demo,width,height):
    Demo.fill(255,255,255)
    tfont = pygame.font.Font("font/simkai.ttf",width//4)
    cfont = pygame.font.Font("font/simkai.ttf",width//20)

def main():

    pygame.init()
    
    screen = pygame.display.set_mode((640,640))
    clock = pygame.time.Clock()
    skier = SkierClass()
    distance = 0

    speed = [0,6]

    def update():
        screen.fill([255,255,255])
        screen.blit(skier.person,skier.rect)
        pygame.display.flip()

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    speed == skier.turn(-1)
                elif event.key == pygame.K_RIGHT:
                    speed == skier.turn(1)
        skier.move()
        update()
        clock.tick(40)


    
if __name__ == "__main__":
    main()

