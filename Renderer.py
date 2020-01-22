from Colors import *


# renders objects in the window
class Renderer:

    buttons = []
    data = None

    def __init__(self, window):
        self.window = window

    def register_buttons(self, buttons):
        self.buttons = buttons

    def render_buttons(self):
        for i in range(len(self.buttons)):
            self.buttons[i].draw(self.window)

    def refresh(self):
        self.window.fill(BLACK)

    def register_data(self, data):
        self.data = data

    def render_data(self):
        self.data.draw(self.window)
