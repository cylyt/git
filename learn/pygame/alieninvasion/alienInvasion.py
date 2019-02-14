import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    pygame.init()
    #创建游戏设置类
    ai_settings=Settings()

    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    ship=Ship(ai_settings,screen)


    while True:
        #事件检查循环
        gf.check_events(ship)
        ship.update()
        gf.update_screen(ai_settings,screen,ship)

run_game()     

