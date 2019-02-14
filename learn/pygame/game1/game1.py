import pygame
from pygame.locals import *
import math
import random

def run_game():
    pygame.init()
    width,height=640,480
    screen=pygame.display.set_mode((width,height))
#按键情况
    keys=[False,False,False,False]
#玩家位置
    playerpos=[100,100]
#玩家精度变量
    acc=[0,0]
#箭头变量
    arrows=[]
#定时器
    badtimer=100
    badtimer1=0
    badguys=[[640,100]]
#城堡血量
    healthvalue=194

    rabbit_img=pygame.image.load("image/dude.png")
    grass_img=pygame.image.load("image/grass.png")
    castle_img=pygame.image.load("image/castle.png")
    arrow_img=pygame.image.load("image/bullet.png")
    badguy_img=pygame.image.load("image/badguy.png")
    healthbar_img=pygame.image.load("image/healthbar.png")
    health_img=pygame.image.load("image/health.png")
    gameover_img=pygame.image.load("image/gameover.png")
    youwin_img=pygame.image.load("image/youwin.png")
    grass_x=width//grass_img.get_width()+1
    grass_y=height//grass_img.get_height()+1
    running=True
    #追踪是否胜利
    exitcode=False  
    #填充黑色
    screen.fill(0)
    #填草皮
    for x in range(grass_x):
        for y in range(grass_y):
            screen.blit(grass_img,(x*100,y*100))
    #放置城堡
    screen.blit(castle_img,(0,30))
    screen.blit(castle_img,(0,135))
    screen.blit(castle_img,(0,240))
    screen.blit(castle_img,(0,345))
    
    position=pygame.mouse.get_pos()
    angle=math.atan2(position[1]-(playerpos[1]+32),position[0]-(playerpos[0]+26))
    playerrot=pygame.transform.rotate(rabbit_img,360-angle*57.29)
    playerpos1=(playerpos[0]-playerrot.get_rect().width/2,playerpos[1]-playerrot.get_rect().height/2)
    screen.blit(playerrot,playerpos1)
    while True:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.flip()
run_game()