import pygame
import math

class Rabbit():

    def __init__(self,ai_setting,screen):

        self.ai_setting=ai_setting
        self.screen=screen
        self.image=pygame.image.load("image/dude.png")
        self.rect=self.image.get_rect()
        self.screen_rect=screen.get_rect()
        self.rect_width=self.rect.width
        self.rect_height=self.rect.height
    

        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False

        self.rect.center=(100,300)
        self.center_x = float(self.rect.center[0])
        self.center_y = float(self.rect.center[1])

        self.position = pygame.mouse.get_pos()


    def update(self):

        if self.moving_right and (self.rect[0] + self.rect_width) < self.screen_rect.right:
            self.center_x += self.ai_setting.move_speed
        if self.moving_left and self.rect[0] > 0:
            self.center_x -= self.ai_setting.move_speed
        if self.moving_up and self.rect[1]> 0:
            self.center_y -= self.ai_setting.move_speed
        if self.moving_down and (self.rect[1] + self.rect_height) < self.screen_rect.bottom:
            self.center_y += self.ai_setting.move_speed
        
        self.rect=[self.center_x,self.center_y]

        
    def rotate(self):
        angle = math.atan2(self.position[1]-self.center_y,self.position[0]-self.center_x)
        self.image = pygame.transform.rotate(self.image,360-angle*57.29)
        print(angle*60)
        self.center_x = self.center_x-self.image.get_rect().width/2
        self.center_y = self.center_y-self.image.get_rect().height/2
        self.rect=[self.center_x,self.center_y]
        

    def blitme(self):
        self.screen.blit(self.image,self.rect)




