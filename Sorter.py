from abc import ABC, abstractmethod
import pygame, sys
import time


class Sorter(ABC):

    def __init__(self, window):
        self.window = window
        self.is_complete = False
        super().__init__()

    def force_update(self, data):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        self.window.fill((0, 0, 0))
        data.draw(self.window)
        pygame.display.update()
        time.sleep(0.02)

    @abstractmethod
    def sort(self, data):
        pass

