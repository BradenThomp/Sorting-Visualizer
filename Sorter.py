from abc import ABC, abstractmethod
import pygame
import time


class Sorter(ABC):

    def __init__(self, screen):
        self.screen = screen
        self.is_complete = False
        super().__init__()

    def updatescreen(self, data):
        self.screen.fill((0, 0, 0))
        data.draw(self.screen)
        pygame.display.update()
        time.sleep(0.2)

    @abstractmethod
    def sort(self, data):
        pass

