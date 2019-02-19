import pygame
import random

class pipeHead(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.pipe_head = pygame.image.load("image/pipe_head.png")
        self.img = self.pip_head
        self.rect = self.pipe_head.get_rect()
        self.height = self.pipe_head.get_height()
        self.width = self.pipe_head.get_width()
    
class pipeBody(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.pipe_body = pygame.image.load("image/pipe_body.png")
        self.img = self.pipe_body
        self.rect = self.pipe_body.get_rect()
        self.height = self.pipe_body.get_height()
        self.width = self.pipe_body.get_width()

class Pipe():
    def __init__(self,screen_width,screen_height):

        self.screen_width = screen_width
        self.screen_height = screen_height
        self.max_pipe_body = (self.screen_height - 2*pipeHead().height)//pipeBody.height
        self.interspace = 8
        self.n_up_pipe_body = random.randint(0,self.max_pipe_body-self.interspace)
        self.n_down_pipe_body = self.max_pipe_body - self.interspace - self.n_up_pipe_body
        self.x = 600
        self.speed = 100
        self.add_score = False
        self.construct_pipe()

    def construct_pipe(self):
        self.pipe = pygame.sprite.Group()

        for i in range(self.n_up_pipe_body):
            pipe_body = pipeBody()
            pipe_body.rect.left, pipe_body.rect.top = self.x, i*pipe_body.height
            self.pipe.add(pipe_body)
        pipe_head = pipeHead()
        pipe_head.rect.left, pipe_head.rect.top =self.x - (pipeHead().width - pipeBody().width)/2,self.n_up_pipe_body*pipeBody().height
        self.pipe.add(pipe_head)

        for i in range(self.n_down_pipe_body):
            pipe_body = pipeBody()
            pipe_body.rect.left, pipe_body.rect.top = self.x, self.screen_height-(i+1)*pipeBody().height
            self.pipe.add(pipe_body)
        pipe_head = pipeHead()
        pipe_head.rect.left, pipe_head.rect.top = self.x - (pipeHead().width - pipeBody().width)/2,self.screen_height-self.n_down_pipe_body*pipeBody().height-pipeHead().height
        self.pipe.add(pipe_head)

    def update(self,time_passed):
        self.x -= time_passed * self.speed
        self.construct_pipe()



        