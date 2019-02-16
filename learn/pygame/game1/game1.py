import pygame
from pygame.locals import *
from settings import Settings
from rabbit import Rabbit
import game_functions as gf
from pygame.sprite import Group
from scoreboard import Scoreboard

def run_game():
    pygame.init()

    ai_setting=Settings()
    screen=pygame.display.set_mode((ai_setting.screen_width,ai_setting.screen_height))

    rabbit=Rabbit(ai_setting,screen)
    arrows=Group()
    bad_guys=Group()
    create_bad_guys = pygame.USEREVENT + 1
    pygame.time.set_timer(create_bad_guys,250)
    score = Scoreboard(ai_setting,screen)

    while True:
        gf.check_events(ai_setting,screen,rabbit,arrows,bad_guys)
        rabbit.update()
        rabbit.rotate()
        gf.update_arrows(screen,arrows,bad_guys)
        gf.update_bad_guys(ai_setting,screen,bad_guys,score)
        gf.update_screen(ai_setting,screen,rabbit,arrows,bad_guys,score)
run_game()