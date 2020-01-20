from abc import ABC, abstractmethod
import pygame, sys
import time


# abstract class to implement sorting algorithms following the strategy pattern
class Sorter(ABC):

    # window: the pygame window
    def __init__(self, window):
        self.window = window
        self.is_complete = False
        super().__init__()

    # data: Data to be pushed to pygame window
    # forces a pygame window update and clears queued events
    def force_update(self, data):
        # handle events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # update window and sleep
        self.window.fill((0, 0, 0))
        data.draw(self.window)
        pygame.display.update()
        time.sleep(0.02)

    @abstractmethod
    def sort(self, data):
        pass

