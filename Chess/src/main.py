# Librerias
import pygame
import sys

# Archivos locales
from pieces import *
from display_pieces import *
from circles import *

# Inicializa la ventana
pygame.init()
pygame.display.set_caption('Chess')
screen_info = pygame.display.Info()
size = width, height = screen_info.current_h - screen_info.current_h * .10, screen_info.current_h - screen_info.current_h * .10
screen = pygame.display.set_mode(size)

margin = height * .075

# Turnos
turns = {'color': 'white', 'number': 0, 'previous move': (-1, -1)}

# Posibles Movimientos de la pieza seleccionada
posible_movements = [[False for i in range(8)] for j in range(8)]
selected_piece = [False, 0, 0]

# Colores
brown_border = pygame.Color(51, 25, 0)
brown_bold = pygame.Color(102, 51, 0)
brown_light = pygame.Color(153, 76, 0)
white_light = pygame.Color(255, 255, 255)

# Fuente para las letras
font = pygame.font.SysFont(None, int(margin/2))
letter_space = height * .107142857143

# Tamaño de las casillas del tablero
box_width = (width - 2*margin)/8
box_height = (height - 2*margin)/8

# Dibujar Tablero
def draw_board():
    for i in range(8):
        for j in range(8):
            color = [brown_bold, brown_light]
            # Dibuja los rectangulos del tablero
            pygame.draw.rect(screen, color[i%2 + j%2 - 1], pygame.Rect(i * box_width + margin, j * box_height + margin, box_width, box_height))

    # Texto para mostrar el de quien es turno
    color_turn_text = 'blancas' if turns['color'] == 'white' else 'negras'

    text = font.render('turno de las: ' + color_turn_text, True, white_light)
    screen.blit(text, (width/2, margin/3))

    # Dibuja las coordenadas en el tablero
    for i in range(8):
        text = font.render(chr(65 + i), True, white_light)
        num = font.render(str(i + 1), True, white_light)
        screen.blit(text, (margin/2, i * letter_space + (3 * margin/2)))
        screen.blit(num, (i * letter_space + (3 * margin/2), width - (2 * margin/3)))

# Dibujar Posicion Inicial de las Piezas
board = [[Piece(screen, box_width, box_height, margin, i, j) for j in range(8)] for i in range(8)]
initial_position(board)

# Coordenadas pieza seleccionada
previous_piece = -1, -1

# >>>>>>>
#Seccion para pruebas
# <<<<<<<
board[3][3].set_type('white', 'Q')
board[4][4].set_type('black', 'K')
# <<<<<<<

while True:
    # Borra la pantalla
    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        # Obtiene la posicion del mouse en la ventana
        mouse_position = pygame.mouse.get_pos()
        # Evento de cerrar la ventana
        if event.type == pygame.QUIT:
            sys.exit()
        # <<<<<<<<<<
        #   Evento de click en la pantalla
        # <<<<<<<<<<
        if event.type == pygame.MOUSEBUTTONUP:
            # Coordenadas de la casilla donde se esta haciendo click
            i = int((mouse_position[0] - margin)//box_width)
            j = int((mouse_position[1] - margin)//box_height)
            # <<<<<<<<<<
            #   Se ejecuta si la se hay una pieza seleccionada y se clica un movimiento permitido para esa pieza
            # <<<<<<<<<<
            if posible_movements[i][j] and selected_piece[0]:
                # Realiza el movimiento de la pieza seleccionada
                board[selected_piece[1]][selected_piece[2]].move(board, i, j)
                # Realiza la captura al paso si la pieza es un peon y las condiciones se cumplen
                if board[selected_piece[1]][selected_piece[2]].type == 'p' or board[selected_piece[1]][selected_piece[2]].type == 'pawn':
                    if abs(selected_piece[2] - j) == 2:
                        board[i][j].en_passand = True
                    if board[i][j + (1 if board[selected_piece[1]][selected_piece[2]].color == 'white' else -1)].en_passand and board[i][j + (1 if board[selected_piece[1]][selected_piece[2]].color == 'white' else -1)].color != board[selected_piece[1]][selected_piece[2]].color:
                        board[i][j + (1 if board[selected_piece[1]][selected_piece[2]].color == 'white' else -1)].set_type('white', 'empty')
                # Al mover la pieza vacia la casilla de donde proviene
                board[selected_piece[1]][selected_piece[2]].set_type('white', 'empty')
                board[previous_piece[0]][previous_piece[1]].select()
                # Pasa al siguiente turno
                if turns['color'] == 'white':
                    turns['color'] = 'black'
                else:
                    turns['color'] = 'white'
                turns['number'] += 1
                turns['previous move'] = i, j
                # Vacia los movimientos posibles de la pieza seleccionada
                posible_movements = [[False for x in range(8)] for y in range(8)]
            # SOlo se podra seleccionar la pieza si es el turno de su color
            if turns['color'] == board[i][j].color:
                # Selecciona o deselecciona la pieza al dar click en ella
                if previous_piece == (-1, -1) or previous_piece == (i, j) or not board[previous_piece[0]][previous_piece[1]].selected:
                    previous_piece = i, j
                    selected_piece[0] = board[i][j].select()
                    selected_piece[1] = i
                    selected_piece[2] = j
                # Deselecciona la pieza si se selecciona otra diferente
                elif previous_piece != (i, j):
                    board[previous_piece[0]][previous_piece[1]].select()
                    board[i][j].select()
                    selected_piece[0] = board[i][j].select()
                    selected_piece[1] = i
                    selected_piece[2] = j
                    previous_piece = i, j

    # Muestra en pantalla las piezas y los posibles movimientos
    draw_board()
    posible_movements = display_pieces(board, turns, posible_movements)

    pygame.display.flip()
