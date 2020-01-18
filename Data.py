from random import randint
import pygame
from Colors import *


class Data:

    def populate_list(self):
        for i in range(0, self.size):
            self.my_list.append(randint(self.min, self.max))

    def __init__(self, min, max, size):
        self.min = min
        self.max = max
        self.size = size
        self.my_list = []
        self.populate_list()

    def randomize(self, min, max, size):
        self.min = min
        self.max = max
        self.size = size
        self.my_list.clear()
        self.populate_list()

    def draw(self, screen):
        for i in range(0, self.size):
            height = self.my_list[i]
            pygame.draw.rect(screen, BLACK, (25 + i*25, 600, 25, -height))
            pygame.draw.rect(screen, WHITE, (26 + i*25, 600, 24, -height))

