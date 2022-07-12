import pygame
import pygame
from pieces import *

def display_pieces(screen, box_width, box_height, board):
    width, height = pygame.display.get_window_size()

def init_position(screen, board, box_width, box_height, margin):
    width, height = pygame.display.get_window_size()

    # Piezas Blancas
    index = 0
    for pawn in white_pawns:
        pawn.draw(screen, index * box_width + margin, 6 * box_height + margin, box_width, box_height)
        board[index][6] = 'wp' + str(index)
        index += 1
    
    white_bishops[0].draw(screen, 2 * box_width + margin, 7 * box_height + margin, box_width, box_height)
    white_bishops[1].draw(screen, 5 * box_width + margin, 7 * box_height + margin, box_width, box_height)
    board[2][7] = 'wB1'
    board[5][7] = 'wB2'

    white_horses[0].draw(screen, box_width + margin, 7 * box_height + margin, box_width, box_height)
    white_horses[1].draw(screen, 6 * box_width + margin, 7 * box_height + margin, box_width, box_height)
    board[1][7] = 'wH1'
    board[6][7] = 'wH1'

    white_towers[0].draw(screen, margin, 7 * box_height + margin, box_width, box_height)
    white_towers[1].draw(screen, 7 * box_width + margin, 7 * box_height + margin, box_width, box_height)
    board[0][7] = 'wT1'
    board[7][7] = 'wT2'

    white_queen.draw(screen, 3 * box_width + margin, 7 * box_height + margin, box_width, box_height)
    board[3][7] = 'wQ'

    white_king.draw(screen, 4 * box_width + margin, 7 * box_height + margin, box_width, box_height)
    board[4][7] = 'wK'

    # Piezas Negras
    index = 0
    for pawn in black_pawns:
        pawn.draw(screen, index * box_width + margin, box_height + margin, box_width, box_height)
        board[index][1] = 'bp' + str(index)
        index += 1

    black_bishops[0].draw(screen, 2 * box_width + margin, margin, box_width, box_height)
    black_bishops[1].draw(screen, 5 * box_width + margin, margin, box_width, box_height)
    board[2][0] = 'bB1'
    board[5][0] = 'bB2'

    black_horses[0].draw(screen, box_width + margin, margin, box_width, box_height)
    black_horses[1].draw(screen, 6 * box_width + margin, margin, box_width, box_height)
    board[1][0] = 'bH1'
    board[6][0] = 'bH2'

    black_towers[0].draw(screen, margin, margin, box_width, box_height)
    black_towers[1].draw(screen, 7 * box_width + margin, margin, box_width, box_height)
    board[0][0] = 'bT1'
    board[7][0]

    black_queen.draw(screen, 3 * box_width + margin, margin, box_width, box_height)
    board[3][0] = 'bQ'

    black_king.draw(screen, 4 * box_width + margin, margin, box_width, box_height)
    board[4][0] = 'bK'