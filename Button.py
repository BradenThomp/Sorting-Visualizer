import pygame


class Button:
    def __init__(self, color, x, y, width,height, text=None, outline=None):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.outline = outline

    def draw(self, screen):
        # draw button outline
        if self.outline:
            pygame.draw.rect(screen, self.outline, (self.x-2, self.y-2, self.width+4, self.height+4), 0)

        # draw button
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 0)

        # draw button text
        if self.text:
            font = pygame.font.SysFont('comicsans', 20)
            text = font.render(self.text, 1, (255, 255, 255))
            screen.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y + (self.height/2 - text.get_height()/2)))

    # pos: position of mouse cursor
    # returns true if cursor is over button otherwise returns false
    def is_over(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

    def perform_function(self):
        pass
