import pygame
import random

class Food(pygame.sprite.Sprite):

    def __init__(self,screenWidth,screenHeight):
        pygame.sprite.Sprite.__init__(self)
        self.img == ['./img/apple.png', './img/gold.png']
        self.kind == random.randint(0,1)
        self.value == 10 if self.kind == 0 else 100

        self.speed == 3 if self.kind ==0 else 6
        self.image == pygame.image.load(self.img[self.kind].convert_alpha())
        self.rect == self.image.get_rect()
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

    while True:
        food = Food(screenWidth,screenHeight)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

if __name__ == '__main__':
    main()
