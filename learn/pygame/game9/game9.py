import pygame
import random

class Farmer(pygame.sprite.Sprite):
    
    def __init__(self,screenWidth,screenHeight):
        pygame.sprite.Sprite.__init__(self)
        self.imgs = ['./img/farmer.png']
        self.farmer = pygame.image.load(self.imgs[0].convert_alpha)
        self.direction_dice = {
                                'top': [0, (0, -1)],
                                'righttop': [1, (1, -1)],
                                'right': [2,(1, 0)],
                                'rigthbottom': [3, (1, 1)],
                                'bottom': [4, (0, 1)],
                                'leftbottom': [5, (-1, 1)],
                                'left': [6, (-1, 0)],
                                'lefttop': [7, (-1, -1)]
        }

        self.direction = 'left'
        self.farmerIdx = 0
        self.farmerIdNum = 0
        self.x, self.y = screenWidth/2, screenHeight/1.1
        self.speed = 5
        self.screenWidth, self.screenHeight = screenWidth, screenHeight
        self.move()
    
    def move(self,direction = 'left'):
        if direction != self.direction:
            self.direction = direction
            self.farmerIdx = 0
        else:
            self.farmerIdx += 1
            self.farmerIdx = self.farmerIdx % self.farmerIdNum
        farmerPos = self.farmerIdx *96, self.direction_dict[self.direction][0]*96 
        self.image = self.farmer.subsurface(farmerPos,(96, 96))
        self.rect = self.image.get_rect()
        self.x = self.x + self.direction_dict[self.direction[1][0]]*self.speed
        self.y = self.y + self.direction_dict[self.direction[1][1]]*self.speed
        self.rect.left, self.rect.top = self.x, self.y

        self.rect.right = self.screenWidth if self.rect.right > self.screenWidth else self.rect.right
        self.rect
    

class Food(pygame.sprite.Sprite):

    def __init__(self,screenWidth,screenHeight):
        pygame.sprite.Sprite.__init__(self)

        self.imgs = ["img/apple.png", "img/gold.png"]
        self.kind = random.randint(0,1)
        self.value = 10 if self.kind == 0 else 100

        self.speed = 3 if self.kind == 0 else 6
        self.image = pygame.image.load(self.imgs[self.kind]).convert_alpha()
        self.rect = self.image.get_rect()
        self.x = random.randint(0, screenWidth-self.rect.width)
        self.y = -50
        self.rect.left, self.rect.top = self.x, self.y
    
    def move(self):
        self.y += self.speed
        self.rect.top = self.y

    def draw(self,screen):
        screen.blit(self.image,self.rect)




def main():
    pygame.init()
    screenWidth = 800
    screenHeight = 600
    screen = pygame.display.set_mode([screenWidth,screenWidth])
    pygame.display.set_caption('gold')
    clock = pygame.time.Clock()
    foodGroup = pygame.sprite.Group()
    foodInterval = 100
    foodCount = 0
    
    

    while True:
        screen.fill([0,160,233])
        food = Food(screenWidth,screenHeight)
        food.move()
        food.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

if __name__ == '__main__':
    main()
