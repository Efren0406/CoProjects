import pygame
import sys
from pieces import *
from display_pieces import *
from circles import *

pygame.init()
pygame.display.set_caption('Show Text')

screen_info = pygame.display.Info()
size = width, height = screen_info.current_h - screen_info.current_h * .10, screen_info.current_h - screen_info.current_h * .10 
margin = height * .075

screen = pygame.display.set_mode(size)

# Turnos
turns = {'color': 'white', 'number': 0}

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
            pygame.draw.rect(screen, color[i%2 + j%2 - 1], pygame.Rect(i * box_width + margin, j * box_height + margin, box_width, box_height))
    
    color_turn_text = 'blancas' if turns['color'] == 'white' else 'negras'
    
    text = font.render('turno de las: ' + color_turn_text, True, white_light)
    screen.blit(text, (width/2, margin/3))

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

# <<<<<<<
board[1][3].set_type('black', 'p')
board[1][3].en_passand = True
board[0][3].set_type('white', 'p')
board[4][3].set_type('black', 'p')
board[4][3].en_passand = True
board[3][3].set_type('white', 'p')
board[2][3].set_type('black', 'p')
board[2][3].en_passand = True
board[6][4].set_type('black', 'p')
board[6][3].en_passand = True
board[7][4].set_type('white', 'p')
# >>>>>>> 
while True:
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        mouse_position = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            i = int((mouse_position[0] - margin)//box_width)
            j = int((mouse_position[1] - margin)//box_height)
            if posible_movements[i][j] and selected_piece[0]:
                board[selected_piece[1]][selected_piece[2]].move()
            if previous_piece == (-1, -1) or previous_piece == (i, j) or not board[previous_piece[0]][previous_piece[1]].selected:
                previous_piece = i, j
                selected_piece[0] = board[i][j].select()
                selected_piece[1] = i
                selected_piece[2] = j
            elif previous_piece != (i, j):
                board[previous_piece[0]][previous_piece[1]].select()
                board[i][j].select()
                selected_piece[0] = board[i][j].select()
                selected_piece[1] = i
                selected_piece[2] = j
                previous_piece = i, j
    
    draw_board()
    display_pieces(board, turns, posible_movements)

    pygame.display.flip()