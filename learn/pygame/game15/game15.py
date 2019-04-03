#连连看

import os
import pygame
from utils import *
from config import *

def main():
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    font = pygame.font.Font(os.path.join(ROOTDIR, '.font\font.TTF'),25)

    