import pygame
from pieces import *

def display_pieces(screen, board, box_width, box_height, margin):
    width, height = pygame.display.get_window_size()
    brown_bold = pygame.Color(102, 51, 0)
    brown_light = pygame.Color(153, 76, 0)

    for i in range(8):
        for j in range(8):
            piece = board[i][j]

            if piece == 'x':
                color = [brown_bold, brown_light]
                pygame.draw.rect(screen, color[i%2 + j%2 - 1], pygame.Rect(i * box_width + margin, j * box_height + margin, box_width, box_height))
            if piece[0] == 'w':
                if piece[1] == 'p':
                    pawn = int(piece[2])
                    white_pawns[pawn].draw(screen, i * box_width + margin, j * box_height + margin, box_width, box_height)
                elif piece[1] == 'B':
                    bishop = int(piece[2])
                    white_bishops[bishop].draw(screen, i * box_width + margin, j * box_height + margin, box_width, box_height)
                elif piece[1] == 'H':
                    horse = int(piece[2])
                    white_horses[horse].draw(screen, i * box_width + margin, j * box_height + margin, box_width, box_height)
                elif piece[1] == 'T':
                    tower = int(piece[2])
                    white_towers[tower].draw(screen, i * box_width + margin, j * box_height + margin, box_width, box_height)
                elif piece[1] == 'Q':
                    white_queen.draw(screen, i * box_width + margin, j * box_height + margin, box_width, box_height)
                elif piece[1] == 'K':
                    white_king.draw(screen, i * box_width + margin, j * box_height + margin, box_width, box_height)
            elif piece[0] == 'b':
                if piece[1] == 'p':
                    pawn = int(piece[2])
                    black_pawns[pawn].draw(screen, i * box_width + margin, j * box_height + margin, box_width, box_height)
                elif piece[1] == 'B':
                    bishop = int(piece[2])
                    black_bishops[bishop].draw(screen, i * box_width + margin, j * box_height + margin, box_width, box_height)
                elif piece[1] == 'H':
                    horse = int(piece[2])
                    black_horses[horse].draw(screen, i * box_width + margin, j * box_height + margin, box_width, box_height)
                elif piece[1] == 'T':
                    tower = int(piece[2])
                    black_towers[tower].draw(screen, i * box_width + margin, j * box_height + margin, box_width, box_height)
                elif piece[1] == 'Q':
                    black_queen.draw(screen, i * box_width + margin, j * box_height + margin, box_width, box_height)
                elif piece[1] == 'K':
                    black_king.draw(screen, i * box_width + margin, j * box_height + margin, box_width, box_height)

def init_position(screen, board, box_width, box_height, margin):
    width, height = pygame.display.get_window_size()

    # Piezas Blancas
    for i in range(8):
        board[i][6] = 'wp' + str(i)
    
    board[2][7] = 'wB1'
    board[5][7] = 'wB2'

    board[1][7] = 'wH1'
    board[6][7] = 'wH1'

    board[0][7] = 'wT1'
    board[7][7] = 'wT2'

    board[3][7] = 'wQ'

    board[4][7] = 'wK'

    # Piezas Negras
    for i in range(8):
        board[i][1] = 'bp' + str(i)

    board[2][0] = 'bB1'
    board[5][0] = 'bB2'

    board[1][0] = 'bH1'
    board[6][0] = 'bH2'

    board[0][0] = 'bT1'
    board[7][0] = 'bT2'

    board[3][0] = 'bQ'

    board[4][0] = 'bK'