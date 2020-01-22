from abc import ABC, abstractmethod
import pygame
import sys
import time


# abstract class to implement sorting algorithms following the strategy pattern
class Sorter(ABC):

    # window: the pygame window
    def __init__(self, renderer):
        self.renderer = renderer
        self.is_complete = False
        super().__init__()

    # data: Data to be pushed to pygame window
    # forces a pygame window update and clears queued events
    def force_update(self):

        # handle events
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # update window and sleep
        self.renderer.refresh()
        self.renderer.render_data()
        pygame.display.update()
        time.sleep(0.02)

    @abstractmethod
    def sort(self, data):
        pass

