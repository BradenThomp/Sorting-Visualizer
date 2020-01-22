import pygame
from SorterButton import SorterButton
from RandomizeButton import RandomizeButton
from Colors import *
from Data import Data
from EventHandler import EventHandler
from Renderer import Renderer
from BubbleSorter import BubbleSorter
from SelectionSorter import SelectionSorter
from InsertionSorter import InsertionSorter
from MergeSorter import MergeSorter
from QuickSorter import QuickSorter


class Application:

    sorter = None

    def __init__(self, window):
        pygame.init()
        self.window = window
        self.event_handler = EventHandler()
        self.renderer = Renderer(window)
        self.data = Data(10, 300, 64)
        self.buttons = [RandomizeButton(BLACK, 25, 25, 125, 25, 'Randomize Data', WHITE, self.data),
                        SorterButton(BLACK, 175, 25, 125, 25, 'Bubble Sort', WHITE, BubbleSorter(self.renderer), self.data),
                        SorterButton(BLACK, 325, 25, 125, 25, 'Selection Sort', WHITE, SelectionSorter(self.renderer), self.data),
                        SorterButton(BLACK, 475, 25, 125, 25, 'Insertion Sort', WHITE, InsertionSorter(self.renderer), self.data),
                        SorterButton(BLACK, 625, 25, 125, 25, 'Merge Sort', WHITE, MergeSorter(self.renderer), self.data),
                        SorterButton(BLACK, 775, 25, 125, 25, 'Quick Sort', WHITE, QuickSorter(self.renderer), self.data)
                        ]
        self.event_handler.register_buttons(self.buttons)
        self.renderer.register_buttons(self.buttons)
        self.renderer.register_data(self.data)

    def run(self):
        while 1:
            # check if any new events have occured
            self.event_handler.handle_events()

            # render window
            self.renderer.refresh()
            self.renderer.render_buttons()
            self.renderer.render_data()

            # update display
            pygame.display.update()


def main():
    window = pygame.display.set_mode((925, 650))
    app = Application(window)
    app.run()


if __name__ == "__main__":
    main()


