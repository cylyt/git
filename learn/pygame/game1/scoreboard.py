import pygame.font

class Scoreboard():

    def __init__(self,ai_setting,screen):

        self.screen = screen
        self.ai_setting = ai_setting

        self.text_color = (30,30,30)
        self.font = pygame.font.SysFont(None,48)
        self.score = 0
        self.health_value = 194
        self.health_image = pygame.image.load("image/health.png")
        self.game_over_image = pygame.image.load("image/gameover.png")
        self.game_win_image = pygame.image.load("image/youwin.png")
    
    def show_health(self):

        if self.health_value>0:
            for health in range(self.health_value):
                self.screen.blit(self.health_image, (health+8, 8))
        else:
            self.screen.blit(self.game_over_image, (0, 0))
    
    def show_time(self):
        if pygame.time.get_ticks() >= self.ai_setting.win_time:
            self.screen.blit(self.game_win_image, (0, 0))
        else:
            win_time = self.font.render(str((self.ai_setting.win_time-pygame.time.get_ticks())//60000)+":"+str((self.ai_setting.win_time-pygame.time.get_ticks())//1000%60),True,(0,0,0))
            text_rect = win_time.get_rect()
            text_rect.topright = [self.ai_setting.screen_width,5]
            self.screen.blit(win_time,text_rect)

        


