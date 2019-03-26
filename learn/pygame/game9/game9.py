import pygame
import random
import os
import sys

def getScore():
    if os.path.isfile('score'):
        with open('score','r') as f:
            score = f.readline().strip()
            if not score:
                score = 0
    else:
        score = 0
    return score

def saveScore(score):
    with open('score', 'w') as f:
        f.write(score)


class Farmer(pygame.sprite.Sprite):
    
    def __init__(self,screenWidth,screenHeight):
        pygame.sprite.Sprite.__init__(self)
        self.imgs = ['./img/farmer.png']
        self.farmer = pygame.image.load(self.imgs[0]).convert_alpha()
        self.direction_dict = {
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
        self.farmerIdNum = 8
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
        self.x = self.x + self.direction_dict[self.direction][1][0]*self.speed
        self.y = self.y + self.direction_dict[self.direction][1][1]*self.speed
        self.rect.left, self.rect.top = self.x, self.y

        self.rect.right = self.screenWidth if self.rect.right > self.screenWidth else self.rect.right
        self.rect.left = 0 if self.rect.left <0 else self.rect.left
        self.rect.top = 0 if self.rect.top <0 else self.rect.top
        self.rect.bottom = self.screenHeight if self.rect.bottom >self.screenHeight else self.rect.bottom
    
    def draw(self,screen):
        screen.blit(self.image, self.rect)

    

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

def GameOver(screen,width,height,score,highest):
    score.fill((255,255,255))
    tfont = pygame.font.Font('./font/simkai.tff',width//10)
    cfont = pygame.font.Font('./font/simkai.tff',width//20)
    title = tfont.render('GameOver', True, (255, 0, 0))
    content = cfont.render('Score: %s, Highest: %s' %(score, highest))
    trect = title.get_rect()
    trect.midtop = (width/2, height/4)
    crect = content.get_rect()
    crect.midtop = (width/2, height/2)
    screen.blit(title, trect)
    screen.blit(content, crect)
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                return




def main():
    pygame.init()
    screenWidth = 800
    screenHeight = 600
    screen = pygame.display.set_mode([screenWidth,screenHeight])
    pygame.display.set_caption('gold')
    clock = pygame.time.Clock()
    farmer = Farmer(screenWidth,screenHeight)
    foodGroup = pygame.sprite.Group()
    foodInterval = 100
    foodCount = 0
    direction = 'left'
    font = pygame.font.Font('./font/simkai.ttf',20)
    score = 0
    maxDown = 20

    while True:
        if maxDown < 0:
            highest = getScore()
            if int(highest) < score:
                saveScore(str(score))
            GameOver(screen,screenWidth,screenHeight,score,highest)
        screen.fill([0,160,233])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_LEFT]:
            if direction in ['top', 'bottom','right']:
                direction = 'left'
            elif direction == 'left':
                farmer.move(direction)
        if key_pressed[pygame.K_RIGHT]:
            if direction in ['top', 'bottom','left']:
                direction = 'right'
            elif direction == 'right':
                farmer.move(direction)
        if key_pressed[pygame.K_UP]:
            if direction in ['right', 'bottom','left']:
                direction = 'top'
            elif direction == 'top':
                farmer.move(direction)
        if key_pressed[pygame.K_DOWN]:
            if direction in ['right', 'top','left']:
                direction = 'bottom'
            elif direction == 'bottom':
                farmer.move(direction)  
        farmer.draw(screen)

        foodCount += 1
        if foodCount > foodInterval:
            food = Food(screenWidth,screenHeight)
            foodGroup.add(food)
            foodCount = 0
        for food in foodGroup:
            food.move()
            if pygame.sprite.collide_rect(food, farmer):
                foodGroup.remove(food)
                score += food.value
                continue
            if food.rect.top > screenHeight:
                foodGroup.remove(food)
                if food.kind == 0:
                    maxDown -= 1
                continue
            food.draw(screen)

        lift_text = font.render("Life: "+str(maxDown),1,(0,0,0))
        score_text = font.render("Score: "+str(score),1,(0,0,0))
        screen.blit(score_text,[10,10])
        screen.blit(lift_text,[10,35])
        pygame.display.flip()
        clock.tick(60)


if __name__ == '__main__':
    main()
