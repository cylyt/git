import pygame
import sys


if __name__ == "__main__": 

    pygame.init()

    print_a=pygame.USEREVENT+1
    pygame.time.set_timer(print_a,250)   

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()        
            elif event.type == print_a:
                print('a')