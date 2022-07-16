import load_images
import circles


class Piece:
    def __init__(self, screen, width, height, margin, i, j):
        # Alto y ancho de las casillas
        self.width = width
        self.height = height
        # Propiedades de la pieza
        self.color = None
        self.type = 'empty'
        # Posicion en la ventana
        self.x = 0
        self.y = 0
        # Posicion en el tablero
        self.i = i
        self.j = j
        # Ajustes de la imagen de la pieza
        self.image = None
        self.image_margin = None
        self.screen = screen
        self.margin = margin
        # Indica si la pieza ha sido seleccionada
        self.selected = False
        # Variable para el peon pasado
        self.en_passand = False

    # <<<<<<<<<<
    #   Metodo que establece el tipo de pieza que sera y sus propiedades
    # >>>>>>>>>>
    def set_type(self, color, new_type):
        if new_type != 'empty':
            self.color = color
            self.type = new_type
            self.image, self.image_margin = load_images.select(self.color, new_type, self.width, self.height)
        elif new_type == 'empty':
            self.type = new_type

    # <<<<<<<<<<
    #   Metodo para establecer si la pieza ha diso seleccionada
    # >>>>>>>>>>
    def select(self):
        self.selected = not self.selected
        return self.selected

    # <<<<<<<<<<
    #   Metodo para mostrar la pieza en el tablero
    # >>>>>>>>>>
    def draw(self):
        if self.type != 'empty':
            self.x = self.i * self.width + self.margin
            self.y = self.j * self.height + self.margin
            self.screen.blit(self.image, (self.x + self.image_margin, self.y + self.image_margin))

    # <<<<<<<<<<
    #    Meotodo para mostrar los posibles movimientos de la pieza en el tablero
    # >>>>>>>>>>
    def draw_movements(self, turns, board, posible_movements):
        # Invoca la clase para mostrar los circulos de los posibles movimientso
        circle = circles.Circle(self.screen, self.width, self.height, self.margin)

        # Solo muestra los movimientos si el tipo de pieza ha sido señalado
        if self.type != 'empty':
            # ==========
            #   Movimientos del Peon
            # ==========
            if self.type in ('p', 'pawn'):
                # Elige las coordenadas de los movimientos segun el color
                coordenate = self.j - 1 if self.color == 'white' else self.j + 1
                if board[self.i][coordenate].type == 'empty':
                    circle.draw('green' if coordenate in (7, 0) else self.color, self.i, coordenate)
                    posible_movements[self.i][coordenate] = True
                # Dibuja un segundo posible movimiento en caso de estar en la posicion inicial
                if (self.j == 1 and self.color == 'black') or (self.j == 6 and self.color == 'white') and board[self.i][coordenate].type == 'empty' and board[self.i][coordenate - 1 if self.color == 'white' else coordenate + 1].type == 'empty':
                        circle.draw(self.color, self.i, coordenate - 1 if self.color == 'white' else coordenate + 1)
                        posible_movements[self.i][coordenate - 1 if self.color == 'white' else coordenate + 1] = True
                # Movimientos de Captura lado izquierdo
                if self.i - 1 >= 0:
                    # Diagonales
                    if board[self.i - 1][coordenate].color != self.color and board[self.i - 1][coordenate].type != 'empty':
                        circle.draw('green' if coordenate in (7, 0) else 'red', self.i - 1, coordenate)
                        posible_movements[self.i - 1][coordenate] = True
                    if board[self.i - 1][coordenate].color != self.color and board[self.i - 1][coordenate].type != 'empty':
                        circle.draw('green' if coordenate in (7, 0) else 'red', self.i + 1, coordenate)
                        posible_movements[self.i + 1][coordenate] = True
                    # Captura al paso
                    if board[self.i - 1][self.j].color != self.color and board[self.i - 1][self.j].en_passand and turns['previous move'] == (self.i - 1, self.j):
                        circle.draw('red', self.i - 1, coordenate)
                        posible_movements[self.i - 1][coordenate] = True
                # Movimientos de Captura lado derecho
                if self.i + 1 <= 7:
                    # Diagonales
                    if board[self.i + 1][coordenate].color != self.color and board[self.i + 1][coordenate].type != 'empty':
                        circle.draw('green' if coordenate in (7, 0) else 'red', self.i + 1, coordenate)
                        posible_movements[self.i + 1][coordenate] = True
                    if board[self.i + 1][coordenate].color != self.color and board[self.i + 1][coordenate].type != 'empty':
                        circle.draw('green' if coordenate in (7, 0) else 'red', self.i + 1, coordenate)
                        posible_movements[self.i + 1][coordenate] = True
                    # Captura al paso
                    if board[self.i + 1][self.j].color != self.color and board[self.i + 1][self.j].en_passand and turns['previous move'] == (self.i + 1, self.j):
                        circle.draw('red', self.i + 1, coordenate)
                        posible_movements[self.i + 1][coordenate] = True
            # ==========
            #   Movimientos del Alfil
            # ==========
            elif self.type in ('B', 'bishop'):
                # Banderas para detectar cuando una pieza se interpone en el camino del alfil
                d1, d2, d3, d4 = True, True, True, True
                # Recorre las 4 diagonales
                for i in range(1, 8):
                    # Diagonal superior izquierda
                    if self.i + i * -1 >= 0 and self.j + i * -1 >= 0:
                        if board[self.i + i * -1][self.j + i * -1].type == 'empty' and d1:
                            circle.draw(self.color, self.i + i * -1, self.j + i * -1)
                            posible_movements[self.i + i * -1][self.j + i * -1] = True
                        # Posible captura
                        elif d1:
                            if board[self.i + i * -1][self.j + i * -1].color != board[self.i][self.j].color and board[self.i + i * -1][self.j + i * -1].type != 'empty':
                                circle.draw('red', self.i + i * -1, self.j + i * -1)
                                posible_movements[self.i + i * -1][self.j + i * -1] = True
                            d1 = False
                    # Diagonal superior derecha
                    if self.i + i <= 7 and self.j + i * -1 >= 0:
                        if board[self.i + i][self.j + i * -1].type == 'empty' and d2:
                            circle.draw(self.color, self.i + i, self.j + i * -1)
                            posible_movements[self.i + i][self.j + i * -1] = True
                        # Posible captura
                        elif d2:
                            if board[self.i + i][self.j + i * -1].color != board[self.i][self.j].color and board[self.i + i][self.j + i * -1].type != 'empty':
                                circle.draw('red', self.i + i, self.j + i * -1)
                                posible_movements[self.i + i][self.j + i * -1] = True
                            d2 = False
                    # Diagonal inferior izquierda
                    if self.i + i * -1 >= 0 and self.j + i <= 7:
                        if board[self.i + i * -1][self.j + i].type == 'empty' and d3:
                            circle.draw(self.color, self.i + i * -1, self.j + i)
                            posible_movements[self.i + i * -1][self.j + i] = True
                        # Posible captura
                        elif d3:
                            if board[self.i + i * -1][self.j + i].color != board[self.i][self.j].color and board[self.i + i * -1][self.j + i].type != 'empty':
                                circle.draw('red', self.i + i * -1, self.j + i)
                                posible_movements[self.i + i * -1][self.j + i] = True
                            d3 = False
                    # Diagonal inferior derecha
                    if self.i + i <= 7 and self.j + i <= 7:
                        if board[self.i + i][self.j + i].type == 'empty' and d4:
                            circle.draw(self.color, self.i + i, self.j + i)
                            posible_movements[self.i + i][self.j + i] = True
                        # Posible captura
                        elif d4: 
                            if board[self.i + i][self.j + i].color != board[self.i][self.j].color and board[self.i + i][self.j + i].type != 'empty':
                                circle.draw('red', self.i + i, self.j + i)
                                posible_movements[self.i + i][self.j + i] = True
                            d4 = False
            # ==========
            #   Movimientos del Caballo
            # ==========
            elif self.type in ('H', 'horse'):
                # Izquierda
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
                # Arriba
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
                # Derecha
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
                # Abajo
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
            #   Movimientos de la Torre
            # ==========
            elif self.type in ('T', 'tower'):
                # Banderas para detectar si existe una pieza en el camino de la torre
                l1, l2, l3, l4 = True, True, True, True
                # Recorre las lineas verticales y horizontales
                for i in range(1, 8):
                    # Linea izquierda
                    if self.i + i * - 1 >= 0:
                        if board[self.i + i * -1][self.j].type == 'empty' and l1:
                            circle.draw(self.color, self.i + i * -1, self.j)
                            posible_movements[self.i + i * -1][self.j] = True
                        # Posible captura
                        elif l1:
                            if board[self.i + i * -1][self.j].color != board[self.i][self.j].color and board[self.i + i * -1][self.j].type != 'empty':
                                circle.draw('red', self.i + i * -1, self.j)
                                posible_movements[self.i + i * -1][self.j] = True
                            l1 = False
                    # Linea superior
                    if self.j + i * - 1 >= 0:
                        if board[self.i][self.j + i * -1].type == 'empty' and l2:
                            circle.draw(self.color, self.i, self.j + i * -1)
                            posible_movements[self.i][self.j + i * -1] = True
                        # Posible captura
                        elif l2:
                            if board[self.i][self.j + i * -1].color != board[self.i][self.j].color and board[self.i][self.j + i * -1].type != 'empty':
                                circle.draw('red', self.i, self.j + i * -1)
                                posible_movements[self.i][self.j + i * -1] = True
                            l2 = False
                    # Linea Derecha
                    if self.i + i <= 7:
                        if board[self.i + i][self.j].type == 'empty' and l3:
                            circle.draw(self.color, self.i + i, self.j)
                            posible_movements[self.i + i][self.j] = True
                        # Posible captura
                        elif l3:
                            if board[self.i + i][self.j].color != board[self.i][self.j].color and board[self.i + i][self.j].type != 'empty':
                                circle.draw('red', self.i + i, self.j)
                                posible_movements[self.i + i][self.j] = True
                            l3 = False
                    # Linea inferior
                    if self.j + i <= 7:
                        if board[self.i][self.j + i].type == 'empty' and l4:
                            circle.draw(self.color, self.i, self.j + i)
                            posible_movements[self.i][self.j + i] = True
                        # Posible captura
                        elif l4:
                            if board[self.i][self.j + i].color != board[self.i][self.j].color and board[self.i][self.j + i].type != 'empty':
                                circle.draw('red', self.i, self.j + i)
                                posible_movements[self.i][self.j + i] = True
                            l4 = False
            # ==========
            #   Movimientos de la Reina
            # ==========
            elif self.type in ('Q', 'queen'):
                # Banderas para detectar cuando una pieza se interpone en el camino de la reina
                d1, d2, d3, d4 = True, True, True, True
                l1, l2, l3, l4 = True, True, True, True
                # Recorre las 4 diagonales, lineas horizontal y vertical
                for i in range(1, 8):
                    # **********
                    #   Diagonales
                    # **********
                    # Diagonal superior izquierda
                    if self.i + i * -1 >= 0 and self.j + i * -1 >= 0:
                        if board[self.i + i * -1][self.j + i * -1].type == 'empty' and d1:
                            circle.draw(self.color, self.i + i * -1, self.j + i * -1)
                            posible_movements[self.i + i * -1][self.j + i * -1] = True
                        # Posible captura diagonal
                        elif d1:
                            if board[self.i + i * -1][self.j + i * -1].color != board[self.i][self.j].color and board[self.i + i * -1][self.j + i * -1].type != 'empty':
                                circle.draw('red', self.i + i * -1, self.j + i * -1)
                                posible_movements[self.i + i * -1][self.j + i * -1] = True
                            d1 = False
                    # Diagonal superior derecha
                    if self.i + i <= 7 and self.j + i * -1 >= 0:
                        if board[self.i + i][self.j + i * -1].type == 'empty' and d2:
                            circle.draw(self.color, self.i + i, self.j + i * -1)
                            posible_movements[self.i + i][self.j + i * -1] = True
                        # Posible captura diagonal
                        elif d2:
                            if board[self.i + i][self.j + i * -1].color != board[self.i][self.j].color and board[self.i + i][self.j + i * -1].type != 'empty':
                                circle.draw('red', self.i + i, self.j + i * -1)
                                posible_movements[self.i + i][self.j + i * -1] = True
                            d2 = False
                    # Diagonal inferior izquierda
                    if self.i + i * -1 >= 0 and self.j + i <= 7:
                        if board[self.i + i * -1][self.j + i].type == 'empty' and d3:
                            circle.draw(self.color, self.i + i * -1, self.j + i)
                            posible_movements[self.i + i * -1][self.j + i] = True
                        # Posible captura diagonal
                        elif d3:
                            if board[self.i + i * -1][self.j + i].color != board[self.i][self.j].color and board[self.i + i * -1][self.j + i].type != 'empty':
                                circle.draw('red', self.i + i * -1, self.j + i)
                                posible_movements[self.i + i * -1][self.j + i] = True
                            d3 = False
                    # Diagonal inferior derecha
                    if self.i + i <= 7 and self.j + i <= 7:
                        if board[self.i + i][self.j + i].type == 'empty' and d4:
                            circle.draw(self.color, self.i + i, self.j + i)
                            posible_movements[self.i + i][self.j + i] = True
                        # Posible captura diagonal
                        elif d4: 
                            if board[self.i + i][self.j + i].color != board[self.i][self.j].color and board[self.i + i][self.j + i].type != 'empty':
                                circle.draw('red', self.i + i, self.j + i)
                                posible_movements[self.i + i][self.j + i] = True
                            d4 = False
                    # **********
                    #   Lineas
                    # **********
                    # Linea izquierda
                    if self.i + i * -1 >= 0:
                        if board[self.i + i * -1][self.j].type == 'empty' and l1:
                            circle.draw(self.color, self.i + i * -1, self.j)
                            posible_movements[self.i + i * -1][self.j] = True
                        # Posible captura linea
                        elif l1:
                            if board[self.i + i * -1][self.j].color != board[self.i][self.j].color and board[self.i + i * -1][self.j].type != 'empty':
                                circle.draw('red', self.i + i * -1, self.j)
                                posible_movements[self.i + i * -1][self.j] = True
                            l1 = False
                    # Linea superior
                    if self.j + i * -1 >= 0:
                        if board[self.i][self.j + i * -1].type == 'empty' and l2:
                            circle.draw(self.color, self.i, self.j + i * -1)
                            posible_movements[self.i][self.j + i * -1] = True
                        # Posible captura linea
                        elif l2:
                            if board[self.i][self.j + i * -1].color != board[self.i][self.j].color and board[self.i][self.j + i * -1].type != 'empty':
                                circle.draw('red', self.i, self.j + i * -1)
                                posible_movements[self.i][self.j + i * -1] = True
                            l2 = False
                    # Linea inferior
                    if self.j + i <= 7:
                        if board[self.i][self.j + i].type == 'empty' and l4:
                            circle.draw(self.color, self.i, self.j + i)
                            posible_movements[self.i][self.j + i] = True
                        # Posible captura linea
                        elif l4:
                            if board[self.i][self.j + i].color != board[self.i][self.j].color and board[self.i][self.j + i].type != 'empty':
                                circle.draw('red', self.i, self.j + i)
                                posible_movements[self.i][self.j + i] = True
                            l4 = False
                    # Linea derecha
                    if self.i + i <= 7:
                        if board[self.i + i][self.j].type == 'empty' and l3:
                            circle.draw(self.color, self.i + i, self.j)
                            posible_movements[self.i + i][self.j] = True
                        # Posible captura linea
                        elif l3:
                            if board[self.i + i][self.j].color != board[self.i][self.j].color and board[self.i + i][self.j].type != 'empty':
                                circle.draw('red', self.i + i, self.j)
                                posible_movements[self.i + i][self.j] = True
                            l3 = False
            # ==========
            #   Movimientos del Rey
            # ==========
            elif self.type in ('k', 'king'):
                # Casilla superior izquierda
                if self.i - 1 >= 0 and self.j - 1 >= 0:
                    if board[self.i - 1][self.j - 1].type == 'empty':
                        circle.draw(self.color, self.i - 1, self.j - 1)
                        posible_movements[self.i - 1][self.j - 1] = True
                    # Posible captura diagonal
                    elif board[self.i - 1][self.j - 1].color != self.color:
                        circle.draw('red', self.i - 1, self.j - 1)
                        posible_movements[self.i - 1][self.j - 1] = True
                # Casilla izquierda
                if self.i - 1 >= 0:
                    if board[self.i - 1][self.j].type == 'empty':
                        circle.draw(self.color, self.i - 1, self.j)
                        posible_movements[self.i - 1][self.j] = True
                    # Posible captura linea
                    elif board[self.i - 1][self.j].color != self.color:
                        circle.draw('red', self.i - 1, self.j)
                        posible_movements[self.i - 1][self.j] = True
                # Casilla superior derecha
                if self.i + 1 <= 7 and self.j - 1 >= 0:
                    if board[self.i + 1][self.j - 1].type == 'empty':
                        circle.draw(self.color, self.i + 1, self.j - 1)
                        posible_movements[self.i + 1][self.j - 1] = True
                    # Posible captura diagonal
                    elif board[self.i + 1][self.j - 1].color != self.color:
                        circle.draw('red', self.i + 1, self.j - 1)
                        posible_movements[self.i + 1][self.j - 1] = True
                # Casilla superior
                if self.j - 1 >= 0:
                    if board[self.i][self.j - 1].type == 'empty':
                        circle.draw(self.color, self.i, self.j - 1)
                        posible_movements[self.i][self.j - 1] = True
                    # Posible captura linea
                    elif board[self.i][self.j - 1].color != self.color:
                        circle.draw('red', self.i, self.j - 1)
                        posible_movements[self.i][self.j - 1] = True
                # Casilla inferior izquierda
                if self.i - 1 >= 0 and self.j + 1 <= 7:
                    if board[self.i - 1][self.j + 1].type == 'empty':
                        circle.draw(self.color, self.i - 1, self.j + 1)
                        posible_movements[self.i - 1][self.j + 1] = True
                    # Posible captura diagonal
                    elif board[self.i - 1][self.j + 1].color != self.color:
                        circle.draw('red', self.i - 1, self.j + 1)
                        posible_movements[self.i - 1][self.j + 1] = True
                # Casilla inferior
                if self.j + 1 <= 7:
                    if board[self.i][self.j + 1].type == 'empty':
                        circle.draw(self.color, self.i, self.j + 1)
                        posible_movements[self.i][self.j + 1] = True
                    # Posible captura linea
                    elif board[self.i][self.j + 1].color != self.color:
                        circle.draw('red', self.i, self.j + 1)
                        posible_movements[self.i][self.j + 1] = True
                # Casilla inferior derecha
                if self.i + 1 <= 7 and self.j + 1 <= 7:
                    if board[self.i + 1][self.j + 1].type == 'empty':
                        circle.draw(self.color, self.i + 1, self.j + 1)
                        posible_movements[self.i + 1][self.j + 1] = True
                    # Posible captura diagonal
                    elif board[self.i + 1][self.j + 1].color != self.color: 
                        circle.draw('red', self.i + 1, self.j + 1)
                        posible_movements[self.i + 1][self.j + 1] = True
                # Casilla derecha
                if self.i + 1 <= 7:
                    if board[self.i + 1][self.j].type == 'empty':
                        circle.draw(self.color, self.i + 1, self.j)
                        posible_movements[self.i + 1][self.j] = True
                    # Posible captura linea
                    elif board[self.i + 1][self.j].color != self.color:
                        circle.draw('red', self.i + 1, self.j)
                        posible_movements[self.i + 1][self.j] = True

            return posible_movements
        else:
            return None

    # <<<<<<<<<<
        # Metodo que realiza el movimiento de la pieza
    # >>>>>>>>>>
    def move(self, board, i, j):
        board[i][j].set_type(self.color, self.type)

