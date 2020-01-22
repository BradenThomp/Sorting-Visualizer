from random import randint
from Colors import *
import pygame

# singular data bar drawn on screen
class DataPoint:

    def __init__(self, min, max):
        self.height = randint(min, max)

    # i is the index data lies in an array
    # draws data to the screen
    def draw(self, screen, i):
        pygame.draw.rect(screen, BLACK, (44 + i * 13, 600, 13, -self.height))
        pygame.draw.rect(screen, WHITE, (45 + i * 13, 600, 12, -self.height))