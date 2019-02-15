import pygame

from settings import Settings
from rabbit import Rabbit
import game_functions as gf
from pygame.sprite import Group
from bad_guy import Bad_guy

def run_game():
    pygame.init()

    ai_setting=Settings()
    screen=pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))

    rabbit=Rabbit(ai_setting,screen)
    arrows=Group()
    bad_guys=Group()
    

    while True:
        gf.check_events(ai_setting,screen,rabbit,arrows)
        rabbit.update()
        gf.create_bad_guys(ai_setting,screen,bad_guys)
        gf.update_arrows(screen,arrows)
        gf.update_screen(ai_setting,screen,rabbit,arrows,bad_guys)
run_game()