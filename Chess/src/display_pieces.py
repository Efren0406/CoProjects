from string import hexdigits
import pygame
import pygame
from pieces import *

def display_pieces(screen, box_width, box_height):
    width, height = pygame.display.get_window_size()

def init_position(screen, box_width, box_height, margin):
    width, height = pygame.display.get_window_size()

    # Piezas Blancas
    index = 0
    for pawn in white_pawns:
        pawn.draw(screen, index * box_width + margin, 6 * box_height + margin, box_width, box_height)
        index += 1
    
    white_bishops[0].draw(screen, 2 * box_width + margin, 7 * box_height + margin, box_width, box_height)
    white_bishops[1].draw(screen, 5 * box_width + margin, 7 * box_height + margin, box_width, box_height)

    white_horses[0].draw(screen, box_width + margin, 7 * box_height + margin, box_width, box_height)
    white_horses[1].draw(screen, 6 * box_width + margin, 7 * box_height + margin, box_width, box_height)

    white_towers[0].draw(screen, margin, 7 * box_height + margin, box_width, box_height)
    white_towers[1].draw(screen, 7 * box_width + margin, 7 * box_height + margin, box_width, box_height)

    white_queen.draw(screen, 3 * box_width + margin, 7 * box_height + margin, box_width, box_height)

    white_king.draw(screen, 4 * box_width + margin, 7 * box_height + margin, box_width, box_height)

    # Piezas Negras
    index = 0
    for pawn in black_pawns:
        pawn.draw(screen, index * box_width + margin, box_height + margin, box_width, box_height)
        index += 1

    black_bishops[0].draw(screen, 2 * box_width + margin, margin, box_width, box_height)
    black_bishops[1].draw(screen, 5 * box_width + margin, margin, box_width, box_height)

    # black_horses[0].draw(screen, box_width + margin, margin, box_width, box_height)
    # black_horses[1].draw(screen, 6 * box_width + margin, margin, box_width, box_height)

    # black_towers[0].draw(screen, margin, margin, box_width, box_height)
    # black_towers[1].draw(screen, 7 * box_width + margin, margin, box_width, box_height)

    # black_queen.draw(screen, 3 * box_width + margin, margin, box_width, box_height)

    # black_king.draw(screen, 4 * box_width + margin, margin, box_width, box_height)