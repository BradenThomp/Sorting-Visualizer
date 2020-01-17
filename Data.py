from random import randint
import pygame


class Data:

    my_list = []
    WHITE = (255,255,255)

    def populatelist(self):
        for i in range(0, self.size):
            self.my_list.append(randint(self.min, self.max))

    def __init__(self, min, max, size):
        self.min = min;
        self.max = max;
        self.size = size;
        self.populatelist()

    def draw(self, screen):
        for i in range(0, self.size):
            height = self.my_list[i]
            pygame.draw.rect(screen, self.WHITE, (50 + i*51, 200, 50, height))