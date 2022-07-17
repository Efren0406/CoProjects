# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#               Libraries
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
import pygame
import sys

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#               Local Modules
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
import pieces
import display_pieces

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#           Initiate Pygame and window
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
pygame.init()

# Set window name
pygame.display.set_caption('Chess')

SCREEN_INFO = pygame.display.Info()
SIZE = SCREEN_INFO.current_h - SCREEN_INFO.current_h * .10
SCREEN = pygame.display.set_mode((SIZE, SIZE))

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#               Constants
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Board border size
MARGIN = SIZE * .075

# Colors
BROWN_BORDER = pygame.Color(51, 25, 0)
BROWN_BOLD = pygame.Color(102, 51, 0)
BROWN_LIGHT = pygame.Color(153, 76, 0)
WHITE_LIGHT = pygame.Color(255, 255, 255)

# Adjust for board coordenates
LETTER_SPACE = SIZE * .107142857143

# Text font
FONT = pygame.font.SysFont(None, int(MARGIN/2))

# Tamaño de las casillas del tablero
BOX_WIDTH = (SIZE - 2*MARGIN)/8
BOX_HEIGHT = (SIZE - 2*MARGIN)/8

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#               Variables
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Turn Register
turns = {'color': 'white', 'number': 0, 'previous move': (-1, -1)}

# Allowed movements and selected piece coordenates
posible_movements = [[False for i in range(8)] for j in range(8)]
se_piece = [False, 0, 0]

# Previous piece coordenates
pr_piece = -1, -1

# Generates an empty piece in every
board = [
            [pieces.Piece(SCREEN, BOX_WIDTH,
                          BOX_HEIGHT, MARGIN,
                          i, j) for j in range(8)] for i in range(8)
        ]

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#               Functions
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


def draw_board():
    """
    This Function draws the board squares,
    the letter coordenates and the number coordenates
    """
    # Shows the player turn
    color_turn_text = 'blancas' if turns['color'] == 'white' else 'negras'
    text = FONT.render('turno de las: ' + color_turn_text, True, WHITE_LIGHT)
    SCREEN.blit(text, (SIZE/2, MARGIN/3))

    # Draw the board squares
    for a in range(8):
        for b in range(8):
            color = [BROWN_BOLD, BROWN_LIGHT]
            pygame.draw.rect(SCREEN, color[a % 2 + b % 2 - 1],
                             pygame.Rect(a * BOX_WIDTH + MARGIN,
                             b * BOX_HEIGHT + MARGIN, BOX_WIDTH, BOX_HEIGHT))

    # Draw the board coordenates
    for i in range(8):
        text = FONT.render(chr(65 + i), True, WHITE_LIGHT)
        num = FONT.render(str(i + 1), True, WHITE_LIGHT)
        SCREEN.blit(text, (MARGIN/2, i * LETTER_SPACE + (3 * MARGIN/2)))
        SCREEN.blit(num, (i * LETTER_SPACE + (3 * MARGIN/2),
                          SIZE - (2 * MARGIN/3)))


# Set the initial board position
display_pieces.initial_position(board)

# >>>>>>>
# Seccion para pruebas
# <<<<<<<
board[2][3].set_type('white', 'K')
board[4][4].set_type('black', 'K')
# <<<<<<<

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
#               Main loop
# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
while True:
    # Clears the window
    SCREEN.fill((0, 0, 0))

    for event in pygame.event.get():
        mouse_position = pygame.mouse.get_pos()
        # Closes the window
        if event.type == pygame.QUIT:
            sys.exit()
        # When a click is detected
        if event.type == pygame.MOUSEBUTTONUP:
            # Get the mouse coordenates on the board
            i = int((mouse_position[0] - MARGIN)//BOX_WIDTH)
            j = int((mouse_position[1] - MARGIN)//BOX_HEIGHT)
            # When a permitted movement is clicked
            if posible_movements[i][j] and se_piece[0]:
                # Makes the piece movement
                board[se_piece[1]][se_piece[2]].move(board, i, j)
                # Makes the en-passand capture if permitted
                if board[se_piece[1]][se_piece[2]].type in ('p', 'pawn'):
                    if abs(se_piece[2] - j) == 2:
                        board[i][j].en_passand = True
                    if (board[i][j + (1 if board[se_piece[1]][se_piece[2]].color == 'white' else -1)].en_passand
                       and board[i][j + (1 if board[se_piece[1]][se_piece[2]].color == 'white' else -1)].color != board[se_piece[1]][se_piece[2]].color):
                        board[i][j + (1 if board[se_piece[1]][se_piece[2]].color == 'white' else -1)].set_type('white', 'empty')
                board[se_piece[1]][se_piece[2]].set_type('white', 'empty')
                board[pr_piece[0]][pr_piece[1]].select()
                # Change the player turn
                if turns['color'] == 'white':
                    turns['color'] = 'black'
                else:
                    turns['color'] = 'white'
                turns['number'] += 1
                turns['previous move'] = i, j
                # Restore the allowed movements
                posible_movements = [
                                        [False for x in range(8)]
                                        for y in range(8)
                                    ]
            # Just cange select a piece if it's its color turn
            if turns['color'] == board[i][j].color:
                # Select or deselect the clicked piece
                if (pr_piece in ((-1, -1), (i, j))
                   or not board[pr_piece[0]][pr_piece[1]].selected):
                    pr_piece = i, j
                    se_piece[0] = board[i][j].select()
                    se_piece[1] = i
                    se_piece[2] = j
                # Deselect the piece if other's clicked
                elif pr_piece != (i, j):
                    board[pr_piece[0]][pr_piece[1]].select()
                    board[i][j].select()
                    se_piece[0] = board[i][j].select()
                    se_piece[1] = i
                    se_piece[2] = j
                    previous_piece = i, j

    # Upgrades the board and show the allow movements
    draw_board()
    posible_movements = display_pieces.display(board, turns, posible_movements)

    pygame.display.flip()

