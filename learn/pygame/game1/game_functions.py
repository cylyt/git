import sys
import pygame
from arrow import Arrow
from bad_guy import Bad_guy



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

def check_mousedown_event(ai_settings,screen,rabbit,arrows):
    new_arrow = Arrow(ai_settings,screen,rabbit)
    arrows.add(new_arrow)


def check_events(ai_setting,screen,rabbit,arrows,bad_guys):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event,rabbit)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event,rabbit)
        elif event.type == pygame.MOUSEBUTTONDOWN:
            check_mousedown_event(ai_setting,screen,rabbit,arrows)
        elif event.type == pygame.MOUSEBUTTONUP:
            bad_guy = Bad_guy(ai_setting,screen)
            bad_guys.add(bad_guy)


def get_grass(ai_setting,screen):
    grass_img = pygame.image.load("image/grass.png")
    grass_x = ai_setting.screen_width//grass_img.get_width()+1
    grass_y = ai_setting.screen_height//grass_img.get_height()+1
    for x in range(grass_x):
        for y in range(grass_y):
            screen.blit(grass_img,(x*100,y*100))

def get_castles(screen):
    castle_img = pygame.image.load("image/castle.png")
    screen.blit(castle_img,(0,30))
    screen.blit(castle_img,(0,135))
    screen.blit(castle_img,(0,240))
    screen.blit(castle_img,(0,345))

def get_health_bar(screen):
    healthbar_img = pygame.image.load("image/healthbar.png")
    screen.blit(healthbar_img,(5,5))



def update_screen(ai_setting,screen,rabbit,arrows,bad_guys,score):
    screen.fill(ai_setting.bg_color)
    get_grass(ai_setting,screen)
    get_castles(screen)  
    get_health_bar(screen)
    for arrow in arrows.sprites():
        arrow.draw_arrow()
    rabbit.blitme()
    for bad_guy in bad_guys.sprites():
        bad_guy.blitme()
    score.show_health()
    score.show_time()
    pygame.display.flip()

def update_arrows(screen,arrows,bad_guys):

    arrows.update()

    for arrow in arrows.copy():
        if arrow.rect.right >= screen.get_rect().right:
            arrows.remove(arrow)
        elif arrow.rect.bottom >= screen.get_rect().bottom:
            arrows.remove(arrow)    

    collisions = pygame.sprite.groupcollide(arrows,bad_guys,True,True)   

def update_bad_guys(ai_setting,screen,bad_guys,score):
    
    bad_guys.update()

    for bad_guy in bad_guys.copy():
        if bad_guy.rect.left <= 0:
            bad_guys.remove(bad_guy)
        elif bad_guy.rect.left < 64:
            score.health_value -= 5
            bad_guys.remove(bad_guy)

            


    