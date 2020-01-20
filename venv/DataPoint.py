from random import randint
from Colors import *
import pygame


class DataPoint:

    def __init__(self, min, max):
        self.height = randint(min, max)

    def draw(self, screen, i):
        pygame.draw.rect(screen, BLACK, (44 + i * 13, 600, 13, -self.height))
        pygame.draw.rect(screen, WHITE, (45 + i * 13, 600, 12, -self.height))