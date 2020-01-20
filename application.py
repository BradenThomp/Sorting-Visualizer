import sys
import pygame
from Button import Button
from Colors import *
from Data import Data
from BubbleSorter import BubbleSorter
from SelectionSorter import SelectionSorter
from InsertionSorter import InsertionSorter
from MergeSorter import MergeSorter
from QuickSorter import QuickSorter


class Application:

    window = None
    sorter = None
    data = None
    randomize_data_button = Button(BLACK, 25, 25, 125, 25, 'Randomize Data', WHITE)
    bubble_sorter_button = Button(BLACK, 175, 25, 125, 25, 'Bubble Sort', WHITE)
    selection_sorter_button = Button(BLACK, 325, 25, 125, 25, 'Selection Sort', WHITE)
    insertion_sorter_button = Button(BLACK, 475, 25, 125, 25, 'Insertion Sort', WHITE)
    merge_sorter_button = Button(BLACK, 625, 25, 125, 25, 'Merge Sort', WHITE)
    quick_sorter_button = Button(BLACK, 775, 25, 125, 25, 'Quick Sort', WHITE)

    @staticmethod
    def initialize():
        pygame.init()
        Application.window = pygame.display.set_mode((925, 650))
        Application.data = Data(10, 300, 64)

    @staticmethod
    def handle_events():
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # checks if any GUI button has been pressed
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Application.randomize_data_button.is_over(pos):
                    Application.data.randomize(10, 300, 64)
                if Application.bubble_sorter_button.is_over(pos):
                    Application.run_sort(BubbleSorter(Application.window))
                if Application.selection_sorter_button.is_over(pos):
                    Application.run_sort(SelectionSorter(Application.window))
                if Application.insertion_sorter_button.is_over(pos):
                    Application.run_sort(InsertionSorter(Application.window))
                if Application.merge_sorter_button.is_over(pos):
                    Application.run_sort(MergeSorter(Application.window))
                if Application.quick_sorter_button.is_over(pos):
                    Application.run_sort(QuickSorter(Application.window))

    @staticmethod
    def update_window():
        # clear window
        Application.window.fill((0, 0, 0))
        # redraw buttons
        Application.randomize_data_button.draw(Application.window)
        Application.bubble_sorter_button.draw(Application.window)
        Application.selection_sorter_button.draw(Application.window)
        Application.insertion_sorter_button.draw(Application.window)
        Application.merge_sorter_button.draw(Application.window)
        Application.quick_sorter_button.draw(Application.window)
        Application.data.draw(Application.window)
        # refresh display
        pygame.display.update()

    # sorter is any sorting algorithm extended from the abstract class Sorter
    # hides menu and starts sorting algorithm
    @staticmethod
    def run_sort(sorter):
        Application.sorter = sorter
        Application.sorter.sort(Application.data)


def main():
    Application.initialize()

    # application super loop
    while 1:
        Application.handle_events()

        Application.update_window()


if __name__ == "__main__":
    main()


