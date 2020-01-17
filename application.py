import sys, pygame
from Data import Data
from DataController import DataController
from BubbleSorter import BubbleSorter


class Application:

    def __init__(self):
        pygame.init()

        size = width, height = 1000, 900

        self.screen = pygame.display.set_mode(size)

        self.data_controller = DataController(Data(0, 40, 10))
        self.data_controller.set_sorter(BubbleSorter(self.screen))

    def run(self):
        while 1:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
            self.data_controller.perform_sort()
            pygame.display.update()


def main():
    my_app = Application()
    my_app.run()


if __name__ == "__main__":
    main()

