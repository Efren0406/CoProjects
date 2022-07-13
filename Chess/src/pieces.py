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
        self.en_passand = False
    
    def set_type(self, color, type):
        if type != 'empty':
            self.color = color
            self.type = type
            self.image, self.image_margin = Images().select(self.color, type, self.width, self.height)
        elif type == 'empty':
            self.type = type
    
    def select(self):
        self.selected = not self.selected
        return self.selected

    def draw(self):
        if self.type != 'empty':
            self.x = self.i * self.width + self.margin
            self.y = self.j * self.height + self.margin
            self.screen.blit(self.image, (self.x + self.image_margin, self.y + self.image_margin))

    def draw_movements(self, turns, board, posible_movements):
        circle = Circle(self.screen, self.width, self.height, self.margin)

        if self.type != 'empty':
            # Movimientos del Peon
            if self.type == 'p' or self.type == 'pawn':
                # Elige las coordenadas de los movimientos segun el color 
                coordenate = self.j - 1 if self.color == 'white' else self.j + 1
                if board[self.i][coordenate].type == 'empty':
                    circle.draw(self.color, self.i, coordenate)
                    posible_movements[self.i][coordenate] = True
                # Dibuja un segundo posible movimiento en caso de estar en la posicion inicial
                if (self.j == 1 and self.color == 'black') or (self.j == 6 and self.color == 'white'):
                    if board[self.i][coordenate].type == 'empty' and board[self.i][coordenate - 1 if self.color == 'white' else coordenate + 1].type == 'empty':
                        circle.draw(self.color, self.i, coordenate - 1 if self.color == 'white' else coordenate + 1)
                        posible_movements[self.i][coordenate - 1 if self.color == 'white' else coordenate + 1] = True
                # Movimientos de Captura lado izquierdo
                if self.i - 1 >= 0:
                    # Diagonales
                    if board[self.i - 1][coordenate].color != self.color and board[self.i - 1][coordenate].type != 'empty':
                        circle.draw('red', self.i - 1, coordenate)
                        posible_movements[self.i - 1][coordenate] = True
                    if board[self.i - 1][coordenate].color != self.color and board[self.i - 1][coordenate].type != 'empty':
                        circle.draw('red', self.i + 1, coordenate)
                        posible_movements[self.i + 1][coordenate] = True
                    # Captura al paso
                    if board[self.i - 1][self.j].color != self.color and board[self.i - 1][self.j].en_passand and turns['previous move'] == (self.i - 1, self.j):
                        circle.draw('red', self.i - 1, coordenate)
                        posible_movements[self.i - 1][coordenate] = True
                # Movimientos de Captura lado derecho
                if self.i + 1 <= 7:
                    # Diagonales
                    if board[self.i + 1][coordenate].color != self.color and board[self.i + 1][coordenate].type != 'empty':
                        circle.draw('red', self.i + 1, coordenate)
                        posible_movements[self.i + 1][coordenate] = True
                    if board[self.i + 1][coordenate].color != self.color and board[self.i + 1][coordenate].type != 'empty':
                        circle.draw('red', self.i + 1, coordenate)
                        posible_movements[self.i + 1][coordenate] = True
                    # Captura al paso
                    if board[self.i + 1][self.j].color != self.color and board[self.i + 1][self.j].en_passand and turns['previous move'] == (self.i + 1, self.j):
                        circle.draw('red', self.i + 1, coordenate)
                        posible_movements[self.i + 1][coordenate] = True
            elif self.type == 'B' or self.type == 'bishop':
                d1, d2, d3, d4 = True, True, True, True
                for i in range(1, 8):
                    if self.i + i * -1 >= 0 and self.j + i * -1 >= 0:
                        if board[self.i + i * -1][self.j + i * -1].type == 'empty' and d1:
                            circle.draw(self.color, self.i + i * -1, self.j + i * -1)
                            posible_movements[self.i + i * -1][self.j + i * -1] = True
                        elif d1:
                            if board[self.i + i * -1][self.j + i * -1].color != board[self.i][self.j].color and board[self.i + i * -1][self.j + i * -1].type != 'empty':
                                circle.draw('red', self.i + i * -1, self.j + i * -1)
                                posible_movements[self.i + i * -1][self.j + i * -1] = True
                            d1 = False
                    if self.i + i <= 7 and self.j + i * -1 >= 0:
                        if board[self.i + i][self.j + i * -1].type == 'empty' and d2:
                            circle.draw(self.color, self.i + i, self.j + i * -1)
                            posible_movements[self.i + i][self.j + i * -1] = True
                        elif d2:
                            if board[self.i + i][self.j + i * -1].color != board[self.i][self.j].color and board[self.i + i][self.j + i * -1].type != 'empty':
                                circle.draw('red', self.i + i, self.j + i * -1)
                                posible_movements[self.i + i][self.j + i * -1] = True
                            d2 = False
                    if self.i + i * -1 >= 0 and self.j + i <= 7:
                        if board[self.i + i * -1][self.j + i].type == 'empty' and d3:
                            circle.draw(self.color, self.i + i * -1, self.j + i)
                            posible_movements[self.i + i * -1][self.j + i] = True
                        elif d3:
                            if board[self.i + i * -1][self.j + i].color != board[self.i][self.j].color and board[self.i + i * -1][self.j + i].type != 'empty':
                                circle.draw('red', self.i + i * -1, self.j + i)
                                posible_movements[self.i + i * -1][self.j + i] = True
                            d3 = False
                    if self.i + i <= 7 and self.j + i <= 7:
                        if board[self.i + i][self.j + i].type == 'empty' and d4:
                            circle.draw(self.color, self.i + i, self.j + i)
                            posible_movements[self.i + i][self.j + i] = True
                        elif d4: 
                            if board[self.i + i][self.j + i].color != board[self.i][self.j].color and board[self.i + i][self.j + i].type != 'empty':
                                circle.draw('red', self.i + i, self.j + i)
                                posible_movements[self.i + i][self.j + i] = True
                            d4 = False
            # elif self.type == 'H' or self.type == 'horse':
            elif self.type == 'T' or self.type == 'tower':
                l1, l2, l3, l4 = True, True, True, True
                for i in range(1, 8):
                    if self.i + i * - 1 >= 0:
                        if board[self.i + i * -1][self.j].type == 'empty' and l1:
                            circle.draw(self.color, self.i + i * -1, self.j)
                            posible_movements[self.i + i * -1][self.j] = True
                        elif l1:
                            if board[self.i + i * -1][self.j].color != board[self.i][self.j].color and board[self.i + i * -1][self.j].type != 'empty':
                                circle.draw('red', self.i + i * -1, self.j)
                                posible_movements[self.i + i * -1][self.j] = True
                            l1 = False
                    if self.j + i * - 1 >= 0:
                        if board[self.i][self.j + i * -1].type == 'empty' and l2:
                            circle.draw(self.color, self.i, self.j + i * -1)
                            posible_movements[self.i][self.j + i * -1] = True
                        elif l2:
                            if board[self.i][self.j + i * -1].color != board[self.i][self.j].color and board[self.i][self.j + i * -1].type != 'empty':
                                circle.draw('red', self.i, self.j + i * -1)
                                posible_movements[self.i][self.j + i * -1] = True
                            l2 = False
                    if self.i + i <= 7:
                        if board[self.i + i][self.j].type == 'empty' and l3:
                            circle.draw(self.color, self.i + i, self.j)
                            posible_movements[self.i + i][self.j] = True
                        elif l3:
                            if board[self.i + i][self.j].color != board[self.i][self.j].color and board[self.i + i][self.j].type != 'empty':
                                circle.draw('red', self.i + i, self.j)
                                posible_movements[self.i + i][self.j] = True
                            l3 = False
                    if self.j + i <= 7:
                        if board[self.i][self.j + i].type == 'empty' and l4:
                            circle.draw(self.color, self.i, self.j + i)
                            posible_movements[self.i][self.j + i] = True
                        elif l4:
                            if board[self.i][self.j + i].color != board[self.i][self.j].color and board[self.i][self.j + i].type != 'empty':
                                circle.draw('red', self.i, self.j + i)
                                posible_movements[self.i][self.j + i] = True
                            l4 = False
            # elif self.type == 'Q' or self.type == 'queen':
            # elif self.type == 'K' or self.type == 'king':

            return posible_movements
        
    def move(self, board, i, j):
        board[i][j].set_type(self.color, self.type)