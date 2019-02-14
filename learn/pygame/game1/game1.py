import pygame

from settings import Settings
from rabbit import Rabbit
import game_functions as gf

def run_game():
    pygame.init()

    ai_setting=Settings()
    screen=pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))

    rabbit=Rabbit(ai_setting,screen)

    while True:
        gf.check_events(rabbit)
        rabbit.update()
        gf.update_screen(ai_setting,screen,rabbit)
run_game()