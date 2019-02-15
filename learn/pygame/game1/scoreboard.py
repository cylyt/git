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

    def update_health(self):

        
        self.score_rect = self.scroe_image.get_rect()
        self.score_rect.right = self.screen_rect.right - 20
        self.score_rect.top = 20    
    
    def show_health(self):
        for health in range(self.health_value):
            self.screen.blit(self.health_image, (health+8, 8))

