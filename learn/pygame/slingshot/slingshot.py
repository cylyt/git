# coding: utf-8

import pygame
import math
import sys

#取符号函数
def sign(a):
    return (a>0)-(a<0)

#定义颜色
black=0,0,0
white=255,255,255

k=1e7           #距离缩放参数
m=5.9742e24     #地球质量
M=1897.7e27     #木星质量
G=6.67259e-17   #万有引力常量
t=1e4         #时间缩放参数

pos_x=0         #地球坐标
pos_y=400
earth=pos_x,pos_y
vel_x=80       #地球速度
vel_y=60
jupiter=700,300
v_j=0.3          #木星速度

pygame.init()
screen=pygame.display.set_mode((800,600))
font=pygame.font.Font("C:/Windows/Fonts/simhei.ttf",30)
text=font.render("木星引力弹弓",1,white)
pygame.display.set_caption("引力弹弓模拟")

e=pygame.image.load("earth.png").convert_alpha()
j=pygame.image.load("jupiter.png").convert_alpha()

while True:
    for event in pygame.event.get():
        if event.type in (pygame.QUIT,pygame.KEYDOWN):
            sys.exit()

    screen.fill(black)

    jupiter=jupiter[0]-v_j,jupiter[1] #木星位移
    screen.blit(j,jupiter) #画木星
    #地木坐标差
    delta_x=(jupiter[0]-earth[0])*k
    delta_y=(jupiter[1]-earth[1])*k
    #地木距离的平方
    r2=delta_x**2+delta_y**2
    #引力
    F=G*m*M/r2
    #地木夹角
    theta=math.acos(delta_x/r2**0.5)
    #X,Y轴分力
    fx=abs(F*math.cos(theta))*sign(delta_x)
    fy=abs(F*math.sin(theta))*sign(delta_y)
    #X,Y轴加速度
    ax=fx/m
    ay=fy/m
    #地球速度变化
    vel_x+=ax*t
    vel_y+=ay*t
    #地球位移变化
    pos_x+=vel_x*t/k
    pos_y+=vel_y*t/k
    earth=int(pos_x),int(pos_y)
    screen.blit(e,earth)

    v='地球速度%.2f km/s' %((vel_x**2+vel_y**2)**0.5)
    speed=font.render(v,1,white)
    screen.blit(text,(150,100))
    screen.blit(speed,(200,50))

    pygame.display.update()