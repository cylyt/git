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
    def __init__(self,idx,position):
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
        self.image = pygame.image.load(self.imgs[0]).convert_alpha()
        self.rect = self.image.get_rect()
        self.position = (random.randrange(20, WIDTH-20), -64)
        self.rect.left, self.rect.top = self.position
        self.speed = random.randrange(3, 9)
        self.angle = 0
        self.angular_velocity = random.randrange(1,5)
        self.rotate_ticks = 3
    def move(self):
        self.position = self.position[0], self.position[1] + self.speed
        self.rect.left ,self.rect.top = self.position
    
    def rotate(self):
        self.rotate_ticks -= 1
        if self.rotate_ticks == 0:
            self.angle = (self.angle + self.angular_velocity) % 360
            orig_rect = self.image.get_rect()
            rot_image = pygame.transform.rotate(self.image, self.angle)
            rot_rect = orig_rect.copy()
            rot_rect.center = rot_image.get_rect().center
            rot_image = rot_image.subsurface(rot_rect).copy()
            self.image = rot_image
            self.rotate_ticks = 3


    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
class Ship(pygame.sprite.Sprite):
    def __init__(self, idx):
        pygame.sprite.Sprite.__init__(self)
        self.imgs = ['./imgs/ship.png', './imgs/ship_exploded.png']
        self.image = pygame.image.load(self.imgs[0]).convert_alpha()
        self.explode_img = pygame.image.load(self.imgs[1]).convert_alpha
        self.position = {'x': random.randrange(-10, 918), 'y': random.randrange(-10, 520)}
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = self.position['x'], self.position['y']

        self.speed = {'x': 10, 'y': 5}
        self.playerIdx = idx
        self.cooling_time = 0
        self.explode_step = 0

    def explode(self,screen):
        img = self.explode_img.subsurface((48*(self.explode_step-1), 0), (48, 48))
        screen.blit(img, (self.position['x'], self.position['y']))
        self.explode_step += 1

    def move(self, direction):
        if direction == 'left':
            self.position['x'] = max(-self.speed['x'] + self.position['x'], -10)
        elif direction == 'right':
            self.position['x'] = min(self.speed['x'] + self.position['x'], 918 )
        elif direction == 'up':
            self.position['y'] = max(-self.speed['y'] + self.position['y'], -10)
        elif direction == 'down':
            self.position['y'] = min(self.speed['y'] + self.position['y'], 520)
        self.rect.left, self.rect.top = self.position['x'], self.position['y']

    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def shot(self):
        return Bullet(self.playerIdx, (self.rect.center[0] - 5, self.position['y'] - 5))

def GameDemo(num_player, screen):
    font = pygame.font.Font('./font/simkai.ttf', 20)
    bg_imgs = ['./imgs/bg_big.png', './imgs/seamless_space.png', './imgs/space3.jpg']
    bg_move_dis = 0
    bg_1 = pygame.image.load(bg_imgs[0]).convert()
    bg_2 = pygame.image.load(bg_imgs[1]).convert()
    bg_3 = pygame.image.load(bg_imgs[2]).convert()

    playerGroup = pygame.sprite.Group()
    bulletGroup = pygame.sprite.Group()
    asteroidGroup = pygame.sprite.Group()

    asteroid_ticks = 90
    for i in range(num_player):
        playerGroup.add(Ship(i+1))
    clock = pygame.time.Clock()

    Score_1 = 0
    Score_2 = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        pressed_keys = pygame.key.get_pressed()
        i = -1
        for player in playerGroup:
            i += 1
            direction = None
            if i == 0:
                if pressed_keys[pygame.K_UP]:
                    direction = 'up'
                elif pressed_keys[pygame.K_DOWN]:
                    direction = 'down'
                elif pressed_keys[pygame.K_LEFT]:
                    direction = 'left'
                elif pressed_keys[pygame.K_RIGHT]:
                    direction = 'right'
                if direction:
                    player.move(direction)
                if pressed_keys[pygame.K_j]:
                    if player.cooling_time == 0:
                        bulletGroup.add(player.shot())
                        player.cooling_time = 20
            elif i == 1:
                if pressed_keys[pygame.K_w]:
                    direction = 'up'
                elif pressed_keys[pygame.K_s]:
                    direction = 'down'
                elif pressed_keys[pygame.K_a]:
                    direction = 'left'
                elif pressed_keys[pygame.K_d]:
                    direction = 'right'
                if direction:
                    player.move(direction)
                if pressed_keys[pygame.K_SPACE]:
                    if player.colling_time == 0:
                        bulletGroup.add(player.shot())
                        player.colling_time = 20
            if player.cooling_time > 0:
                player.cooling_time -= 1
        if (Score_1 + Score_2) < 500:
            background = bg_1
        elif(Score_1 + Score_2) <1500:
            background = bg_2
        else:
            background = bg_3
        
        screen.blit(background, (0, -background.get_rect().height +bg_move_dis))
        screen.blit(background, (0, bg_move_dis))
        bg_move_dis = (bg_move_dis + 2) % background.get_rect().height

        if asteroid_ticks == 0:
            asteroid_ticks = 90
            asteroidGroup.add(Asteroid())
        else:
            asteroid_ticks -= 1
        
        for player in playerGroup:
            if pygame.sprite.spritecollide(player, asteroidGroup, True, None):
                player.explode_step = 1
            elif player.explode_step > 0:
                if player.explode_step >3:
                    playerGroup.remove(player)
                    if len(playerGroup) == 0:
                        return
                
                else:
                    player.explode(screen)
            else:
                player.draw(screen)
        
        for bullet in bulletGroup:
            bullet.move()
            if pygame.sprite.spritecollide(bullet, asteroidGroup, True, None):
                bulletGroup.remove(bullet)
                if bullet.playerIdx == 1:
                    Score_1 += 1
                else:
                    Score_2 += 1
            else:
                bullet.draw(screen)

        for asteroid in asteroidGroup:
            asteroid.move()
            asteroid.rotate()
            asteroid.draw(screen)

        Score_1_text = '玩家一得分： %s' % Score_1
        Score_2_text = '玩家二得分： %s' % Score_2
        text_1 = font.render(Score_1_text, True, (0, 0, 225))
        text_2 = font.render(Score_2_text, True, (255, 0, 0))
        screen.blit(text_1, (2, 5))
        screen.blit(text_2, (2, 35))
        pygame.display.update()
        clock.tick(60)

def end_interface(screen):
    clock = pygame.time.Clock()
    while True:
        button_1 = BUTTON(screen,(330, 190), '重新开始')
        button_2 = BUTTON(screen,(330, 305), '退出游戏')
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if button_1.collidepoint(pygame.mouse.get_pos()):
                    return
                elif button_2.collidepoint(pygame.mouse.get_pos()):
                    pygame.exit()
                    sys.exit()
        clock.tick(60)
        pygame.display.update()
                  


def main():
    pygame.init()
    pygame.font.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    num_player = start_inferface(screen)
    if num_player == 1:
        while True:
            GameDemo(num_player = 1, screen = screen)
            end_interface(screen)
    else:
        while True:
            GameDemo(num_player = 2, screen = screen)
            end_interface(screen)



if __name__ == '__main__':
    main()    