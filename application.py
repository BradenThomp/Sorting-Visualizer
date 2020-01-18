import sys, pygame
from Data import Data
from Button import Button
from BubbleSorter import BubbleSorter
from SelectionSorter import SelectionSorter
from Colors import *


class Application:

    def __init__(self):
        pygame.init()

        size = width, height = 1000, 900

        self.screen = pygame.display.set_mode(size)

        self.bubble_sorter_button = Button(BLACK, 350, 25, 300, 100, 'Bubble Sort', WHITE)
        self.selection_sorter_button = Button(BLACK, 350, 150, 300, 100, 'Selection Sort', WHITE)

        self.sorter = 0

        self.data = Data(0, 40, 10)

    def run(self):
        show_menu = True
        while 1:

            #event handler
            for event in pygame.event.get():
                pos = pygame.mouse.get_pos()

                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if self.bubble_sorter_button.isover(pos) and show_menu:
                        show_menu = self.prepare_data_interface()
                        self.sorter = BubbleSorter(self.screen)

                    if self.selection_sorter_button.isover(pos) and show_menu:
                        show_menu = self.prepare_data_interface()
                        self.sorter = SelectionSorter(self.screen)

            #display logic
            if show_menu:
                self.drawmenu()

            else:
                self.sorter.sort(self.data)
                if self.sorter.is_complete:
                    show_menu = True

            pygame.display.update()

    def drawmenu(self):
        self.screen.fill((0, 0, 0))
        self.bubble_sorter_button.draw(self.screen)
        self.selection_sorter_button.draw(self.screen)

    def prepare_data_interface(self):
        self.data.randomize(0, 40, 10)
        return False

    def event_handler(self):
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if self.bubble_sorter_button.isover(pos) and show_menu:
                    show_menu = self.prepare_data_interface()
                    self.sorter = BubbleSorter(self.screen)

                if self.selection_sorter_button.isover(pos) and show_menu:
                    show_menu = self.prepare_data_interface()
                    self.sorter = SelectionSorter(self.screen)


def main():
    my_app = Application()
    my_app.run()


if __name__ == "__main__":
    main()

