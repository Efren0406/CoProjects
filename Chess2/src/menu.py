# General libraries
import pygame
import sys


# Local libraries
import load_images

# <<<<<<<<<<
# Initialize the pygame window
# <<<<<<<<<<
pygame.init()

# Set window properties
pygame.display.set_caption("Chess")

SCREEN_INFO = pygame.display.Info()
SCREEN_WIDTH = SCREEN_INFO.current_h - SCREEN_INFO.current_h * .1
SCREEN_HEIGHT = SCREEN_INFO.current_h - SCREEN_INFO.current_h * .1
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

MARGIN = SCREEN_HEIGHT * .075

# box width and height
BOX_WIDTH = SCREEN_WIDTH/8
BOX_HEIGHT = SCREEN_HEIGHT/8
# Menu font
MENU_FONT = pygame.font.SysFont(None, int(SCREEN_HEIGHT * .05))

# Colores
BORDER_1 = pygame.Color(153, 76, 0)
BORDER_2 = pygame.Color(102, 51, 0)


# function that draw the menu
def draw_menu():
    rowDirection = [0, 1, 0, -1]
    columnDirection = [1, 0, -1, 0]
    row = 0
    column = 0
    direction = 0
    colors = [BORDER_1, BORDER_2]

    # Draw the squares on the border
    for x in range(28):
        print(row, column, rowDirection[direction], columnDirection[direction], direction)
        pygame.draw.rect(SCREEN,
                         colors[x % 2],
                         pygame.Rect(column * BOX_WIDTH,
                                     row * BOX_HEIGHT,
                                     BOX_WIDTH,
                                     BOX_WIDTH))
        if (column >= 0 and column < 8
           and row >= 0 and column < 8):
            row += rowDirection[direction]
            column += columnDirection[direction]
        else:
            direction = (direction + 1) % 4
            row += rowDirection[direction]
            column += columnDirection[direction]

    pieces = ['p', 'B', 'H', 'T', 'Q', 'K']
    start = [SCREEN_WIDTH/2 - 3 * BOX_WIDTH,
             SCREEN_HEIGHT/2 - BOX_HEIGHT]
    i = 0

    for piece in pieces:
        image, image_margin = load_images.select('white',
                                                 piece,
                                                 BOX_WIDTH,
                                                 BOX_HEIGHT)
        SCREEN.blit(image,
                    (i * BOX_WIDTH + start[0], start[1] + image_margin))
        i += 1


while True:
    SCREEN.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            mouse_position = pygame.mouse.get_pos()

    draw_menu()

    pygame.display.flip()
