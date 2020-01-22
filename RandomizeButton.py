from Button import Button


# randomizes the data
class RandomizeButton(Button):

    def __init__(self, color, x, y, width, height, text=None, outline=None, data=None):
        super().__init__(color, x, y, width, height, text, outline)
        self.data = data

    def perform_function(self):
        self.data.randomize(10, 300, 64)

