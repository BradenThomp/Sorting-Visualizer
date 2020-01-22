import pygame
import sys


# handles all events that occur in the application
class EventHandler:

    buttons = []

    def __init__(self):
        pass

    def register_buttons(self, buttons):
        self.buttons = buttons

    def handle_events(self):
        for event in pygame.event.get():
            pos = pygame.mouse.get_pos()

            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # checks if any GUI button has been pressed and acts accordingly
            if event.type == pygame.MOUSEBUTTONDOWN:
                for i in range(len(self.buttons)):
                    if self.buttons[i].is_over(pos):
                        self.buttons[i].perform_function()



