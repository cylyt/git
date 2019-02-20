import pygame
from bird import Bird
from pipe import Pipe
from pygame.locals import *

screen_width, screen_height = 640, 480

def main():

    pygame.init()
    screen = pygame.display.set_mode((screen_width,screen_height), 0, 32)
    background_img = pygame.image.load("image/background.png")
    gameover_img = pygame.image.load("image/gameover.png")

    font = pygame.font.SysFont("arial", 24)
    clock = pygame.time.Clock()
    bird = Bird(screen_width,screen_height)
    pipes = []
    time0 = 0
    time_interval = 2
    Score = 0
    running = True

    while running:

        screen.fill(0)
        for x in range(screen_width // background_img.get_width() + 1):
            for y in range(screen_height // background_img.get_height() + 1):
                screen.blit(background_img, (x*100, y*100))
            time_passed = clock.tick()/1000

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    exit(0)
                
                if event.type == pygame.KEYDOWN:
                    if event.key == K_SPACE:
                        bird.cur_jump_height = 0
                        bird.is_jump = True

        bird.update(time_passed)
        screen.blit(bird.rotated_bird, bird.rect)
        if bird.is_dead():
            running = False

        time1 = pygame.time.get_ticks() / 1000
        if time1 - time0 > time_interval:
            time0 = time1
            pipes.append(Pipe(screen_height,screen_width))
        for i, pipe in enumerate(pipes):
            pipe.update(time_passed)
            for p in pipe.pipe:
                screen.blit(p.img, p.rect)
            if bird.rect.left > pipe.x + Pipe.pipeHead().width and not pipe.add_score:
                Score += 1
                pipe.add_score =True 
            if pipe.x + pipe.pipeHead().width < 0:
                pipes.pop(i)

            if pygame.sprite.spritecollide(bird, pipe.pipe,False, None):
                if bird.rect.left < pipe.x + (pipe.pipeHead().width + pipe.pipeBody().width)/2:
                    running = False

            scoreText = font.render('Score: ' + str(Score), True, (0,0,0))
            scoreRect = scoreText.get_rect()
            scoreRect.topleft = [10,10]
            screen.blit(scoreText, scoreRect)
            pygame.display.flip()
            pygame.display.update()
    screen.blit(gameover_img,(0,0))
    pygame.display.flip()
    pygame.display.update()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit(0)

if __name__ == "__main__":
    main()

        







