from load_images import *
from circles import *

class Piece:
    def __init__(self, screen, width, height, margin, i, j):
        self.width = width
        self.height = height
        self.color = None
        self.type = 'empty'
        self.x = 0
        self.y = 0
        self.i = i
        self.j = j
        self.image = None
        self.image_margin = None
        self.screen = screen
        self.margin = margin
        self.selected = False
        self.posible_movement = False
    
    def set_type(self, color, type):
        if type != 'empty':
            self.color = color
            self.type = type
            self.image, self.image_margin = Images().select(self.color, type, self.width, self.height)
    
    def select(self):
        print(self.i, self.j)
        self.selected = not self.selected

    def draw(self):
        if self.type != 'empty':
            self.x = self.i * self.width + self.margin
            self.y = self.j * self.height + self.margin
            self.screen.blit(self.image, (self.x + self.image_margin, self.y + self.image_margin))

    def draw_movements(self, board):
        circle = Circle(self.screen, self.width, self.height, self.margin)

        if self.type != 'empty':
            if self.type == 'p' or self.type == 'pawn':
                coordenate = self.j - 1 if self.color == 'white' else self.j + 1
                circle.draw(self.color, self.i, coordenate)
                if self.j == 1 or self.j == 6:
                    circle.draw(self.color, self.i, coordenate - 1 if self.color == 'white' else coordenate + 1)
            elif self.type == 'B' or self.type == 'bishop':
                d1, d2, d3, d4 = True, True, True, True
                for i in range(1, 8):
                    if self.i + i * -1 >= 0 and self.j + i * -1 >= 0:
                        if board[self.i + i * -1][self.j + i * -1].type == 'empty' and d1:
                            circle.draw(self.color, self.i + i * -1, self.j + i * -1)
                        else:
                            d1 = False
                    if self.i + i <= 7 and self.j + i * -1 >= 0:
                        if board[self.i + i][self.j + i * -1].type == 'empty' and d2:
                            circle.draw(self.color, self.i + i, self.j + i * -1)
                        else:
                            d2 = False
                    if self.i + i * -1 >= 0 and self.j + i <= 7:
                        if board[self.i + i * -1][self.j + i].type == 'empty' and d3:
                            circle.draw(self.color, self.i + i * -1, self.j + i)
                        else:
                            d3 = False
                    if self.i + i <= 7 and self.j + i <= 7:
                        if board[self.i + i][self.j + i].type == 'empty' and d4:
                            circle.draw(self.color, self.i + i, self.j + i)
                        else: 
                            d4 = False
            # elif self.type == 'H' or self.type == 'horse':
            # elif self.type == 'T' or self.type == 'tower':
            # elif self.type == 'Q' or self.type == 'queen':
            # elif self.type == 'K' or self.type == 'king':