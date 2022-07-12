from load_images import *

class Piece:
    def __init__(self, screen, width, height, margin):
        self.width = width
        self.height = height
        self.color = None
        self.type = 'empty'
        self.x = 0
        self.y = 0
        self.image = None
        self.image_margin = None
        self.screen = screen
        self.margin = margin
    
    def set_type(self, color, type):
        if type != 'empty':
            self.color = color
            self.type = type
            self.image, self.image_margin = Images().select(self.color, type, self.width, self.height)

    def draw(self, i, j):
        if self.type != 'empty':
            self.x = i * self.width + self.margin
            self.y = j * self.height + self.margin
            self.screen.blit(self.image, (self.x + self.image_margin, self.y + self.image_margin))

    def draw_movements(self):
        i = int((self.x - self.margin)/self.width)
        j = int((self.y - self.margin)/self.height)

        # if self.type != 'empty':
        #     if self.type == 'p' or self.type == 'pawn':
        #         if j == 1:
                    
        #     elif self.type == 'B' or self.type == 'bishop':
        #     elif self.type == 'H' or self.type == 'horse':
        #     elif self.type == 'T' or self.type == 'tower':
        #     elif self.type == 'Q' or self.type == 'queen':
        #     elif self.type == 'K' or self.type == 'king':