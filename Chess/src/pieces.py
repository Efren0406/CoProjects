from load_images import *
from circles import *

class Piece:
    def __init__(self, screen, width, height, margin):
        self.width = width
        self.height = height
        self.color = None
        self.type = 'empty'
        self.x = 0
        self.y = 0
        self.i = 0
        self.j = 0
        self.image = None
        self.image_margin = None
        self.screen = screen
        self.margin = margin
        self.selected = False
    
    def set_type(self, color, type):
        if type != 'empty':
            self.color = color
            self.type = type
            self.image, self.image_margin = Images().select(self.color, type, self.width, self.height)
    
    def select(self):
        self.selected = not self.selected

    def draw(self, i, j):
        self.i = i
        self.j = j

        if self.type != 'empty':
            self.x = self.i * self.width + self.margin
            self.y = self.j * self.height + self.margin
            self.screen.blit(self.image, (self.x + self.image_margin, self.y + self.image_margin))

    def draw_movements(self):
        circle = Circle(self.screen, self.width, self.height, self.margin)

        if self.type != 'empty':
            if self.type == 'p' or self.type == 'pawn':
                if self.color == 'white':
                    pass
                else:
                    circle.draw('black', self.i, self.j + 1)
                    if self.j == 1:
                        circle.draw('black', self.i, self.j + 2)
            # elif self.type == 'B' or self.type == 'bishop':
            # elif self.type == 'H' or self.type == 'horse':
            # elif self.type == 'T' or self.type == 'tower':
            # elif self.type == 'Q' or self.type == 'queen':
            # elif self.type == 'K' or self.type == 'king':