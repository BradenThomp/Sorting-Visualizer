from Sorter import Sorter


class DataController:
    sorter = Sorter

    def __init__(self, data):
        self.data = data

    def set_sorter(self, sorter):
        self.sorter = sorter

    def perform_sort(self):
        self.sorter.sort(self.data)


