import load_images
import circles
import debugging
import move_record


record = move_record.Record()


class Piece:
    """
    This class has all the pieces properties like
    movements, the kind of piece, position on the board, etc.
    """
    def __init__(self, screen, width, height, margin, i, j):
        # Height and width of every board box
        self.width = width
        self.height = height
        # Piece properties
        self.color = None
        self.type = 'empty'
        self.id = 2
        # Window piece position
        self.x = 0
        self.y = 0
        # Board position
        self.i = i
        self.j = j
        # Piece image
        self.image = None
        self.image_margin = None
        self.screen = screen
        self.margin = margin
        # True if the piece is selected
        self.selected = False
        # true if the pawn moved twice
        self.en_passand = False
        self.dir = None
        # True if the king has castle
        self.castle = None

    # <<<<<<<<<<
    #   This sets the piece properties
    # >>>>>>>>>>
    def set_type(self, color, new_type):
        if new_type != 'empty':
            self.color = color
            self.type = new_type
            self.image, self.image_margin = load_images.select(self.color, new_type,
                                                               self.width, self.height)
            if self.type in ('p', 'pawn') and self.color == 'white':
                self.dir = -1
            elif self.type in ('p', 'pawn'):
                self.dir = 1

            if self.type in ('B', 'H', 'T', 'bishop', 'tower', 'horse'):
                self.id = id
            elif self.type in ('Q', 'K', 'p', 'pawn', 'king', 'queen'):
                self.id = 2
        elif new_type == 'empty':
            self.type = new_type

    # <<<<<<<<<<
    #   Sets 'self.selected' true, if the piece is selected
    # >>>>>>>>>>
    def select(self):
        self.selected = not self.selected
        return self.selected

    # <<<<<<<<<<
    #   Show the piece on the board
    # >>>>>>>>>>
    def draw(self):
        if self.type != 'empty':
            self.x = self.i * self.width + self.margin
            self.y = self.j * self.height + self.margin
            self.screen.blit(self.image, (self.x + self.image_margin,
                                          self.y + self.image_margin))

    # <<<<<<<<<<
    #    Show the allowed movements
    # >>>>>>>>>>
    def draw_movements(self, turns, board, posible_movements):
        # Object of the circle draw in the board
        circle = circles.Circle(self.screen, self.width,
                                self.height, self.margin)

        if self.type != 'empty':
            # ==========
            #   Pawn Movements
            # ==========
            if self.type in ('p', 'pawn'):
                # Forward movement
                coordenate = self.j - 1 if self.color == 'white' else self.j + 1
                if board[self.i][coordenate].type == 'empty':
                    circle.draw('green' if coordenate in (7, 0) else self.color, self.i, coordenate)
                    posible_movements[self.i][coordenate] = True
                # Draw a second movement forward if posible
                if ((self.j == 1 and self.color == 'black') or (self.j == 6 and self.color == 'white')) and board[self.i][coordenate].type == 'empty' and board[self.i][coordenate - 1 if self.color == 'white' else coordenate + 1].type == 'empty':
                        circle.draw(self.color, self.i, coordenate - 1 if self.color == 'white' else coordenate + 1)
                        posible_movements[self.i][coordenate - 1 if self.color == 'white' else coordenate + 1] = True
                # Left capture movements
                if self.i - 1 >= 0:
                    # Diagonal
                    if board[self.i - 1][coordenate].color != self.color and board[self.i - 1][coordenate].type != 'empty':
                        circle.draw('green' if coordenate in (7, 0) else 'red', self.i - 1, coordenate)
                        posible_movements[self.i - 1][coordenate] = True
                    if board[self.i - 1][coordenate].color != self.color and board[self.i - 1][coordenate].type != 'empty':
                        circle.draw('green' if coordenate in (7, 0) else 'red', self.i + 1, coordenate)
                        posible_movements[self.i + 1][coordenate] = True
                    # En-passant capture
                    if board[self.i - 1][self.j].color != self.color and board[self.i - 1][self.j].en_passand and turns['previous move'] == (self.i - 1, self.j):
                        circle.draw('red', self.i - 1, coordenate)
                        posible_movements[self.i - 1][coordenate] = True
                # Right capture movementes
                if self.i + 1 <= 7:
                    # Diagonal
                    if board[self.i + 1][coordenate].color != self.color and board[self.i + 1][coordenate].type != 'empty':
                        circle.draw('green' if coordenate in (7, 0) else 'red', self.i + 1, coordenate)
                        posible_movements[self.i + 1][coordenate] = True
                    if board[self.i + 1][coordenate].color != self.color and board[self.i + 1][coordenate].type != 'empty':
                        circle.draw('green' if coordenate in (7, 0) else 'red', self.i + 1, coordenate)
                        posible_movements[self.i + 1][coordenate] = True
                    # En-passant capture
                    if board[self.i + 1][self.j].color != self.color and board[self.i + 1][self.j].en_passand and turns['previous move'] == (self.i + 1, self.j):
                        circle.draw('red', self.i + 1, coordenate)
                        posible_movements[self.i + 1][coordenate] = True
            # ==========
            #   Bishop movements
            # ==========
            elif self.type in ('B', 'bishop'):
                # This flags are true if a piece is on a posible movement
                d1, d2, d3, d4 = True, True, True, True
                # Check all the diagonals
                for i in range(1, 8):
                    # Upper left diagonal
                    if self.i + i * -1 >= 0 and self.j + i * -1 >= 0:
                        if board[self.i + i * -1][self.j + i * -1].type == 'empty' and d1:
                            circle.draw(self.color, self.i + i * -1, self.j + i * -1)
                            posible_movements[self.i + i * -1][self.j + i * -1] = True
                        # Posible capture
                        elif d1:
                            if board[self.i + i * -1][self.j + i * -1].color != board[self.i][self.j].color and board[self.i + i * -1][self.j + i * -1].type != 'empty':
                                circle.draw('red', self.i + i * -1, self.j + i * -1)
                                posible_movements[self.i + i * -1][self.j + i * -1] = True
                            d1 = False
                    # Upper right diagonal
                    if self.i + i <= 7 and self.j + i * -1 >= 0:
                        if board[self.i + i][self.j + i * -1].type == 'empty' and d2:
                            circle.draw(self.color, self.i + i, self.j + i * -1)
                            posible_movements[self.i + i][self.j + i * -1] = True
                        # Posible capture
                        elif d2:
                            if board[self.i + i][self.j + i * -1].color != board[self.i][self.j].color and board[self.i + i][self.j + i * -1].type != 'empty':
                                circle.draw('red', self.i + i, self.j + i * -1)
                                posible_movements[self.i + i][self.j + i * -1] = True
                            d2 = False
                    # Lower left diagonal
                    if self.i + i * -1 >= 0 and self.j + i <= 7:
                        if board[self.i + i * -1][self.j + i].type == 'empty' and d3:
                            circle.draw(self.color, self.i + i * -1, self.j + i)
                            posible_movements[self.i + i * -1][self.j + i] = True
                        # Posible capture
                        elif d3:
                            if board[self.i + i * -1][self.j + i].color != board[self.i][self.j].color and board[self.i + i * -1][self.j + i].type != 'empty':
                                circle.draw('red', self.i + i * -1, self.j + i)
                                posible_movements[self.i + i * -1][self.j + i] = True
                            d3 = False
                    # Lower right diagonal
                    if self.i + i <= 7 and self.j + i <= 7:
                        if board[self.i + i][self.j + i].type == 'empty' and d4:
                            circle.draw(self.color, self.i + i, self.j + i)
                            posible_movements[self.i + i][self.j + i] = True
                        # Posible cpature
                        elif d4:
                            if board[self.i + i][self.j + i].color != board[self.i][self.j].color and board[self.i + i][self.j + i].type != 'empty':
                                circle.draw('red', self.i + i, self.j + i)
                                posible_movements[self.i + i][self.j + i] = True
                            d4 = False
            # ==========
            #   Horse Movements
            # ==========
            elif self.type in ('H', 'horse'):
                # Left
                if self.i - 2 >= 0 and self.j + 1 <= 7:
                    if board[self.i - 2][self.j + 1].type == 'empty':
                        circle.draw(self.color, self.i - 2, self.j + 1)
                        posible_movements[self.i - 2][self.j + 1] = True
                    elif board[self.i - 2][self.j + 1].color != self.color:
                        circle.draw('red', self.i - 2, self.j + 1)
                        posible_movements[self.i - 2][self.j + 1] = True
                if self.i - 2 >= 0 and self.j - 1 >= 0:
                    if board[self.i - 2][self.j - 1].type == 'empty':
                        circle.draw(self.color, self.i - 2, self.j - 1)
                        posible_movements[self.i - 2][self.j - 1] = True
                    elif board[self.i - 2][self.j - 1].color != self.color:
                        circle.draw('red', self.i - 2, self.j - 1)
                        posible_movements[self.i - 2][self.j - 1] = True
                # Up
                if self.i - 1 >= 0 and self.j + 2 <= 7:
                    if board[self.i - 1][self.j + 2].type == 'empty':
                        circle.draw(self.color, self.i - 1, self.j + 2)
                        posible_movements[self.i - 1][self.j + 2] = True
                    elif board[self.i - 1][self.j + 2].color != self.color:
                        circle.draw('red', self.i - 1, self.j + 2)
                        posible_movements[self.i - 1][self.j + 2] = True
                if self.i + 1 <= 7 and self.j + 2 <= 7:
                    if board[self.i + 1][self.j + 2].type == 'empty':
                        circle.draw(self.color, self.i + 1, self.j + 2)
                        posible_movements[self.i + 1][self.j + 2] = True
                    elif board[self.i + 1][self.j + 2].color != self.color:
                        circle.draw('red', self.i + 1, self.j + 2)
                        posible_movements[self.i + 1][self.j + 2] = True
                # Right
                if self.i + 2 <= 7 and self.j - 1 >= 0:
                    if board[self.i + 2][self.j - 1].type == 'empty':
                        circle.draw(self.color, self.i + 2, self.j - 1)
                        posible_movements[self.i + 2][self.j - 1] = True
                    elif board[self.i + 2][self.j - 1].color != self.color:
                        circle.draw('red', self.i + 2, self.j - 1)
                        posible_movements[self.i + 2][self.j - 1] = True
                if self.i + 2 <= 7 and self.j + 1 <= 7:
                    if board[self.i + 2][self.j + 1].type == 'empty':
                        circle.draw(self.color, self.i + 2, self.j + 1)
                        posible_movements[self.i + 2][self.j + 1] = True
                    elif board[self.i + 2][self.j + 1].color != self.color:
                        circle.draw('red', self.i + 2, self.j + 1)
                        posible_movements[self.i + 2][self.j + 1] = True
                # Down
                if self.i - 1 >= 0 and self.j - 2 >= 0:
                    if board[self.i - 1][self.j - 2].type == 'empty':
                        circle.draw(self.color, self.i - 1, self.j - 2)
                        posible_movements[self.i - 1][self.j - 2] = True
                    elif board[self.i - 1][self.j - 2].color != self.color:
                        circle.draw('red', self.i - 1, self.j - 2)
                        posible_movements[self.i - 1][self.j - 2] = True
                if self.i + 1 <= 7 and self.j - 2 >= 0:
                    if board[self.i + 1][self.j - 2].type == 'empty':
                        circle.draw(self.color, self.i + 1, self.j - 2)
                        posible_movements[self.i + 1][self.j - 2] = True
                    elif board[self.i + 1][self.j - 2].color != self.color:
                        circle.draw('red', self.i + 1, self.j - 2)
                        posible_movements[self.i + 1][self.j - 2] = True
            # ==========
            #   Rook Movements
            # ==========
            elif self.type in ('T', 'tower'):
                # This flags are true if a piece is in a posible movement
                l1, l2, l3, l4 = True, True, True, True
                # Analize the vertical an horizontal lines
                for i in range(1, 8):
                    # Left line
                    if self.i + i * - 1 >= 0:
                        if board[self.i + i * -1][self.j].type == 'empty' and l1:
                            circle.draw(self.color, self.i + i * -1, self.j)
                            posible_movements[self.i + i * -1][self.j] = True
                        # Posible capture
                        elif l1:
                            if board[self.i + i * -1][self.j].color != board[self.i][self.j].color and board[self.i + i * -1][self.j].type != 'empty':
                                circle.draw('red', self.i + i * -1, self.j)
                                posible_movements[self.i + i * -1][self.j] = True
                            l1 = False
                    # Upper line
                    if self.j + i * - 1 >= 0:
                        if board[self.i][self.j + i * -1].type == 'empty' and l2:
                            circle.draw(self.color, self.i, self.j + i * -1)
                            posible_movements[self.i][self.j + i * -1] = True
                        # Posible capture
                        elif l2:
                            if board[self.i][self.j + i * -1].color != board[self.i][self.j].color and board[self.i][self.j + i * -1].type != 'empty':
                                circle.draw('red', self.i, self.j + i * -1)
                                posible_movements[self.i][self.j + i * -1] = True
                            l2 = False
                    # Right line
                    if self.i + i <= 7:
                        if board[self.i + i][self.j].type == 'empty' and l3:
                            circle.draw(self.color, self.i + i, self.j)
                            posible_movements[self.i + i][self.j] = True
                        # Posible capture
                        elif l3:
                            if board[self.i + i][self.j].color != board[self.i][self.j].color and board[self.i + i][self.j].type != 'empty':
                                circle.draw('red', self.i + i, self.j)
                                posible_movements[self.i + i][self.j] = True
                            l3 = False
                    # Lower line
                    if self.j + i <= 7:
                        if board[self.i][self.j + i].type == 'empty' and l4:
                            circle.draw(self.color, self.i, self.j + i)
                            posible_movements[self.i][self.j + i] = True
                        # Posible capture
                        elif l4:
                            if board[self.i][self.j + i].color != board[self.i][self.j].color and board[self.i][self.j + i].type != 'empty':
                                circle.draw('red', self.i, self.j + i)
                                posible_movements[self.i][self.j + i] = True
                            l4 = False
            # ==========
            #   Queen movements
            # ==========
            elif self.type in ('Q', 'queen'):
                # This flags are true if a piece is in a posible movement
                d1, d2, d3, d4 = True, True, True, True
                l1, l2, l3, l4 = True, True, True, True
                # Analize all the diagonals, vertical, and horizontal lines
                for i in range(1, 8):
                    # Upper left diagonal
                    if self.i + i * -1 >= 0 and self.j + i * -1 >= 0:
                        if board[self.i + i * -1][self.j + i * -1].type == 'empty' and d1:
                            circle.draw(self.color, self.i + i * -1, self.j + i * -1)
                            posible_movements[self.i + i * -1][self.j + i * -1] = True
                        # Posible capture
                        elif d1:
                            if board[self.i + i * -1][self.j + i * -1].color != board[self.i][self.j].color and board[self.i + i * -1][self.j + i * -1].type != 'empty':
                                circle.draw('red', self.i + i * -1, self.j + i * -1)
                                posible_movements[self.i + i * -1][self.j + i * -1] = True
                            d1 = False
                    # Upper right diagonal
                    if self.i + i <= 7 and self.j + i * -1 >= 0:
                        if board[self.i + i][self.j + i * -1].type == 'empty' and d2:
                            circle.draw(self.color, self.i + i, self.j + i * -1)
                            posible_movements[self.i + i][self.j + i * -1] = True
                        # Posible capture
                        elif d2:
                            if board[self.i + i][self.j + i * -1].color != board[self.i][self.j].color and board[self.i + i][self.j + i * -1].type != 'empty':
                                circle.draw('red', self.i + i, self.j + i * -1)
                                posible_movements[self.i + i][self.j + i * -1] = True
                            d2 = False
                    # Lower left diagonal
                    if self.i + i * -1 >= 0 and self.j + i <= 7:
                        if board[self.i + i * -1][self.j + i].type == 'empty' and d3:
                            circle.draw(self.color, self.i + i * -1, self.j + i)
                            posible_movements[self.i + i * -1][self.j + i] = True
                        # Posible capture
                        elif d3:
                            if board[self.i + i * -1][self.j + i].color != board[self.i][self.j].color and board[self.i + i * -1][self.j + i].type != 'empty':
                                circle.draw('red', self.i + i * -1, self.j + i)
                                posible_movements[self.i + i * -1][self.j + i] = True
                            d3 = False
                    # Lower right diagonal
                    if self.i + i <= 7 and self.j + i <= 7:
                        if board[self.i + i][self.j + i].type == 'empty' and d4:
                            circle.draw(self.color, self.i + i, self.j + i)
                            posible_movements[self.i + i][self.j + i] = True
                        # Posible capture
                        elif d4:
                            if board[self.i + i][self.j + i].color != board[self.i][self.j].color and board[self.i + i][self.j + i].type != 'empty':
                                circle.draw('red', self.i + i, self.j + i)
                                posible_movements[self.i + i][self.j + i] = True
                            d4 = False
                    # Left line
                    if self.i + i * -1 >= 0:
                        if board[self.i + i * -1][self.j].type == 'empty' and l1:
                            circle.draw(self.color, self.i + i * -1, self.j)
                            posible_movements[self.i + i * -1][self.j] = True
                        # Posible capture
                        elif l1:
                            if board[self.i + i * -1][self.j].color != board[self.i][self.j].color and board[self.i + i * -1][self.j].type != 'empty':
                                circle.draw('red', self.i + i * -1, self.j)
                                posible_movements[self.i + i * -1][self.j] = True
                            l1 = False
                    # Upper line
                    if self.j + i * -1 >= 0:
                        if board[self.i][self.j + i * -1].type == 'empty' and l2:
                            circle.draw(self.color, self.i, self.j + i * -1)
                            posible_movements[self.i][self.j + i * -1] = True
                        # Posible capture
                        elif l2:
                            if board[self.i][self.j + i * -1].color != board[self.i][self.j].color and board[self.i][self.j + i * -1].type != 'empty':
                                circle.draw('red', self.i, self.j + i * -1)
                                posible_movements[self.i][self.j + i * -1] = True
                            l2 = False
                    # Lower line
                    if self.j + i <= 7:
                        if board[self.i][self.j + i].type == 'empty' and l4:
                            circle.draw(self.color, self.i, self.j + i)
                            posible_movements[self.i][self.j + i] = True
                        # Posible capture
                        elif l4:
                            if board[self.i][self.j + i].color != board[self.i][self.j].color and board[self.i][self.j + i].type != 'empty':
                                circle.draw('red', self.i, self.j + i)
                                posible_movements[self.i][self.j + i] = True
                            l4 = False
                    # Right line
                    if self.i + i <= 7:
                        if board[self.i + i][self.j].type == 'empty' and l3:
                            circle.draw(self.color, self.i + i, self.j)
                            posible_movements[self.i + i][self.j] = True
                        # Posible capture
                        elif l3:
                            if board[self.i + i][self.j].color != board[self.i][self.j].color and board[self.i + i][self.j].type != 'empty':
                                circle.draw('red', self.i + i, self.j)
                                posible_movements[self.i + i][self.j] = True
                            l3 = False
            # ==========
            #   King movements
            # ==========
            elif self.type in ('K', 'king'):
                # Upper left box
                if self.i - 1 >= 0 and self.j - 1 >= 0:
                    if self.king_movement_allowed(board, self.i - 1, self.j - 1):
                        if board[self.i - 1][self.j - 1].type == 'empty':
                            circle.draw(self.color, self.i - 1, self.j - 1)
                            posible_movements[self.i - 1][self.j - 1] = True
                        # Posible capture
                        elif board[self.i - 1][self.j - 1].color != self.color:
                            circle.draw('red', self.i - 1, self.j - 1)
                            posible_movements[self.i - 1][self.j - 1] = True
                # Left box
                if self.i - 1 >= 0:
                    if self.king_movement_allowed(board, self.i - 1, self.j):
                        if board[self.i - 1][self.j].type == 'empty':
                            circle.draw(self.color, self.i - 1, self.j)
                            posible_movements[self.i - 1][self.j] = True
                        # Posible capture
                        elif board[self.i - 1][self.j].color != self.color:
                            circle.draw('red', self.i - 1, self.j)
                            posible_movements[self.i - 1][self.j] = True
                # Upper right box
                if self.i + 1 <= 7 and self.j - 1 >= 0:
                    if self.king_movement_allowed(board, self.i + 1, self.j - 1):
                        if board[self.i + 1][self.j - 1].type == 'empty':
                            circle.draw(self.color, self.i + 1, self.j - 1)
                            posible_movements[self.i + 1][self.j - 1] = True
                        # Posible capture
                        elif board[self.i + 1][self.j - 1].color != self.color:
                            circle.draw('red', self.i + 1, self.j - 1)
                            posible_movements[self.i + 1][self.j - 1] = True
                # Lower box
                if self.j - 1 >= 0:
                    if self.king_movement_allowed(board, self.i, self.j - 1):
                        if board[self.i][self.j - 1].type == 'empty':
                            circle.draw(self.color, self.i, self.j - 1)
                            posible_movements[self.i][self.j - 1] = True
                        # Possible capture
                        elif board[self.i][self.j - 1].color != self.color:
                            circle.draw('red', self.i, self.j - 1)
                            posible_movements[self.i][self.j - 1] = True
                # Lower left box
                if self.i - 1 >= 0 and self.j + 1 <= 7:
                    if self.king_movement_allowed(board, self.i - 1, self.j + 1):
                        if board[self.i - 1][self.j + 1].type == 'empty':
                            circle.draw(self.color, self.i - 1, self.j + 1)
                            posible_movements[self.i - 1][self.j + 1] = True
                        # Possible capture
                        elif board[self.i - 1][self.j + 1].color != self.color:
                            circle.draw('red', self.i - 1, self.j + 1)
                            posible_movements[self.i - 1][self.j + 1] = True
                # Lower box
                if self.j + 1 <= 7:
                    if self.king_movement_allowed(board, self.i, self.j + 1):
                        if board[self.i][self.j + 1].type == 'empty':
                            circle.draw(self.color, self.i, self.j + 1)
                            posible_movements[self.i][self.j + 1] = True
                        # Possible capture
                        elif board[self.i][self.j + 1].color != self.color:
                            circle.draw('red', self.i, self.j + 1)
                            posible_movements[self.i][self.j + 1] = True
                # Bottom right box
                if self.i + 1 <= 7 and self.j + 1 <= 7:
                    if self.king_movement_allowed(board, self.i + 1, self.j + 1):
                        if board[self.i + 1][self.j + 1].type == 'empty':
                            circle.draw(self.color, self.i + 1, self.j + 1)
                            posible_movements[self.i + 1][self.j + 1] = True
                        # Possible capture
                        elif board[self.i + 1][self.j + 1].color != self.color:
                            circle.draw('red', self.i + 1, self.j + 1)
                            posible_movements[self.i + 1][self.j + 1] = True
                # Right box
                if self.i + 1 <= 7:
                    if self.king_movement_allowed(board, self.i + 1, self.j):
                        if board[self.i + 1][self.j].type == 'empty':
                            circle.draw(self.color, self.i + 1, self.j)
                            posible_movements[self.i + 1][self.j] = True
                        # Possible capture
                        elif board[self.i + 1][self.j].color != self.color:
                            circle.draw('red', self.i + 1, self.j)
                            posible_movements[self.i + 1][self.j] = True

                # Castle movement
                if not record.is_in_record(self.type, self.id, self.color):
                    if (board[self.i - 3][self.j].type == 'empty'
                       and board[self.i - 2][self.j].type == 'empty'
                       and board[self.i - 1][self.j].type == 'empty'
                       and self.king_movement_allowed(board, self.i - 2, self.j)
                       and self.king_movement_allowed(board, self.i - 1, self.j)
                       and not record.is_in_record('T', 0, self.color)):
                        circle.draw(self.color, self.i - 2, self.j)
                        posible_movements[self.i - 2][self.j] = True
                    if (board[self.i + 2][self.j].type == 'empty'
                       and board[self.i + 1][self.j].type == 'empty'
                       and self.king_movement_allowed(board, self.i + 2, self.j)
                       and self.king_movement_allowed(board, self.i + 1, self.j)
                       and not record.is_in_record('T', 1, self.color)):
                        circle.draw(self.color, self.i + 2, self.j)
                        posible_movements[self.i + 2][self.j] = True


            return posible_movements

        return None

    # <<<<<<<<<<
        # Metodo que realiza el movimiento de la pieza
    # >>>>>>>>>>
    def king_movement_allowed(self, board, i, j):
        # Flags
        d1, d2, d3, d4 = True, True, True, True
        L1, L2, L3, L4 = True, True, True, True

        for x in range(1, 8):
            # Diagonals
            if i + x * - 1 >= 0 and j + x * - 1 >= 0 and d1:
                if board[i + x * - 1][j + x * - 1].color != self.color:
                    if (board[i + x * - 1][j + x * - 1].type in ('Q', 'B', 'queen', 'bishop')
                       or (board[i + x * - 1][j + x * - 1].type in ('K', 'king') and x == 1)):
                        return False
                    elif (board[i + x * - 1][j + x * - 1].type in ('p', 'pawn')
                         and board[i + x * - 1][j + x * - 1].dir == 1
                         and x == 1):
                        return False
                if board[i + x * - 1][j + x * - 1].type in ('T', 'p', 'K', 'king', 'tower', 'pawn'):
                    d1 = False
            if i + x <= 7 and j + x * - 1 >= 0 and d2:
                if board[i + x][j + x * - 1].color != self.color:
                    if (board[i + x][j + x * - 1].type in ('Q', 'B', 'queen', 'bishop')
                       or (board[i + x][j + x * - 1].type in ('K', 'king') and x == 1)):
                        return False
                    elif (board[i + x][j + x * - 1].type in ('p', 'pawn') 
                         and board[i + x][j + x * - 1].dir == 1
                         and x == 1):
                        return False
                if board[i + x][j + x * - 1].type in ('T', 'p', 'K', 'king', 'tower', 'pawn'):
                    d2 = False
            if i + x * - 1 >= 0 and j + x <= 7 and d3:
                if board[i + x * - 1][j + x].color != self.color:
                    if (board[i + x * - 1][j + x].type in ('Q', 'B', 'queen', 'bishop')
                       or (board[i + x * - 1][j + x].type in ('K', 'king') and x == 1)):
                        return False
                    elif (board[i + x * - 1][j + x].type in ('p', 'pawn') 
                         and board[i + x * - 1][j + x].dir == -1
                         and x == 1):
                        return False
                if board[i + x * - 1][j + x].type in ('T', 'p', 'K', 'king', 'tower', 'pawn'):
                    d3 = False
            if i + x <= 7 and j + x <= 7 and d4:
                if board[i + x][j + x].color != self.color:
                    if (board[i + x][j + x].type in ('Q', 'B', 'queen', 'bishop')
                       or (board[i + x][j + x].type in ('K', 'king') and x == 1)):
                        return False
                    elif (board[i + x][j + x].type in ('p', 'pawn') 
                         and board[i + x][j + x].dir == -1
                         and x == 1):
                        return False
                if board[i + x][j + x].type in ('T', 'p', 'K', 'king', 'tower', 'pawn'):
                    d4 = False

            # Lines
            if i - x >= 0 and L1:
                if ((board[i - x][j].type in ('T', 'Q', 'tower', 'queen')
                   or (board[i - x][j].type in ('K', 'king') and x == 1))
                   and board[i - x][j].color != self.color):
                    return False
                if board[i - x][j].type in ('B', 'p', 'K', 'king', 'bishop', 'pawn'):
                    L1 = False
            if j - x >= 0 and L2: 
                if ((board[i][j - x].type in ('T', 'Q', 'tower', 'queen')
                   or (board[i][j - x].type in ('K', 'king') and x == 1))
                   and board[i][j - x].color != self.color):
                    return False
                if board[i][j - x].type in ('B', 'p', 'K', 'king', 'bishop', 'pawn'):
                    L2 = False
            if i + x <= 7 and L3:
                if ((board[i + x][j].type in ('T', 'Q', 'tower', 'queen')
                   or (board[i + x][j].type in ('K', 'king') and x == 1))
                   and board[i + x][j].color != self.color):
                    return False
                if board[i + x][j].type in ('B', 'p', 'K', 'king', 'bishop', 'pawn'):
                    L3 = False
            if j + x <= 7 and L4:
                if ((board[i][j + x].type in ('T', 'Q', 'tower', 'queen')
                   or (board[i][j + x].type in ('K', 'king') and x == 1))
                   and board[i][j + x].color != self.color):
                    return False
                if board[i][j + x].type in ('B', 'p', 'K', 'king', 'bishop', 'pawn'):
                    L4 = False

            # L moves
            if i - 2 >= 0 and j - 1 >= 0:
                if (board[i - 2][j - 1].type in ('H', 'horse')
                   and board[i - 2][j - 1].color != self.color):
                    return False
            if i - 2 >= 0 and j + 1 <= 7:
                if (board[i - 2][j + 1].type in ('H', 'horse')
                   and board[i - 2][j + 1].color != self.color):
                    return False
            if i - 1 >= 0 and j - 2 >= 0:
                if (board[i - 1][j - 2].type in ('H', 'horse')
                   and board[i - 1][j - 2].color != self.color):
                    return False
            if i + 1 <= 7 and j - 2 >= 0:
                if (board[i + 1][j - 2].type in ('H', 'horse')
                   and board[i + 1][j - 2].color != self.color):
                    return False
            if i + 2 <= 7 and j - 1 >= 0:
                if (board[i + 2][j - 1].type in ('H', 'horse')
                   and board[i + 2][j - 1].color != self.color):
                    return False
            if i + 2 <= 7 and j + 1 <= 7:
                if (board[i + 2][j + 1].type in ('H', 'horse')
                   and board[i + 2][j + 1].color != self.color):
                    return False
            if i - 1 >= 0 and j + 2 <= 7:
                if (board[i - 1][j + 2].type in ('H', 'horse')
                   and board[i - 1][j + 2].color != self.color):
                    return False
            if i + 1 <= 7 and j + 2 <= 7:
                if (board[i + 1][j + 2].type in ('H', 'horse')
                   and board[i + 1][j + 2].color != self.color):
                    return False

        return True

    # <<<<<<<<<<
        # Metodo que realiza el movimiento de la pieza
    # >>>>>>>>>>
    def move(self, board, i, j):
        board[i][j].set_type(self.color, self.type)

