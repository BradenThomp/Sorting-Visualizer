from random import randint
import pygame
from Colors import *


class Data:

    def populatelist(self):
        for i in range(0, self.size):
            self.my_list.append(randint(self.min, self.max))

    def __init__(self, min, max, size):
        self.min = min
        self.max = max
        self.size = size
        self.my_list = []
        self.populatelist()

    def randomize(self, min, max, size):
        self.min = min
        self.max = max
        self.size = size
        self.my_list.clear()
        self.populatelist()

    def draw(self, screen):
        for i in range(0, self.size):
            height = self.my_list[i]
            pygame.draw.rect(screen, BLACK, (50 + i*50, 600, 50, -height))
            pygame.draw.rect(screen, WHITE, (51 + i*50, 600, 48, -height))

