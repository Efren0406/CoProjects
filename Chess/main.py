import pygame
import sys

pygame.init()

size = width, height = 800, 800

screen = pygame.display.set_mode(size)

# Colores
brown_border = pygame.Color(51, 25, 0)
brown_bold = pygame.Color(102, 51, 0)
brown_light = pygame.Color(153, 76, 0)

# Dibujar Tablero
def build_board(board):


# Piezas
# imagenes
white_pawn = pygame.image.load(r'Chess\white_pawn.png')
white_pawn = pygame.transform.scale(white_pawn, (width/8, height/8))
black_pawn = pygame.image.load(r'Chess\black_pawn.png')
black_pawn = pygame.transform.scale(black_pawn, (width/8, height/8))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()