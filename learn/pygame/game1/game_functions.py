import sys
import pygame


def check_keydown_events(event,rabbit):
    if event.key == pygame.K_d:
        rabbit.moving_right = True
    if event.key == pygame.K_a:
        rabbit.moving_left = True
    if event.key == pygame.K_w:
        rabbit.moving_up = True
    if event.key == pygame.K_s:
        rabbit.moving_down = True   
def check_keyup_events(event,rabbit):
    if event.key == pygame.K_d:
        rabbit.moving_right = False
    if event.key == pygame.K_a:
        rabbit.moving_left = False
    if event.key == pygame.K_w:
        rabbit.moving_up = False
    if event.key == pygame.K_s:
        rabbit.moving_down = False  

def check_events(rabbit):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,rabbit)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,rabbit)

def update_screen(ai_setting,screen,rabbit):
    screen.fill(ai_setting.bg_color)
    rabbit.blitme()
    pygame.display.flip()