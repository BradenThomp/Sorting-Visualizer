from Button import Button
from Sorter import Sorter


# sorts the data based on the assigned algorithm
class SorterButton(Button):

    # sorter: the algorithm to be applied to sort data
    # data: the data to be sorted
    def __init__(self, color, x, y, width, height, text=None, outline=None, sorter=None, data=None):
        super().__init__(color, x, y, width, height, text, outline)
        self.sorter = sorter
        self.data = data

    def perform_function(self):
        self.sorter.sort(self.data)
