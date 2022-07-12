import pygame
import sys
from display_pieces import *

pygame.init()
pygame.display.set_caption('Show Text')

size = width, height = 800, 800
margin = 60

screen = pygame.display.set_mode(size)

# Colores
brown_border = pygame.Color(51, 25, 0)
brown_bold = pygame.Color(102, 51, 0)
brown_light = pygame.Color(153, 76, 0)
white_light = pygame.Color(255, 255, 255)

# Letras
font = pygame.font.Font('freesansbold.ttf', 30)
text = font.render("A")

# Dibujar Tablero
box_width = (width - 2*margin)/8
box_height = (height - 2*margin)/8

for i in range(8):
    for j in range(8):
        color = [brown_bold, brown_light]
        pygame.draw.rect(screen, color[i%2 + j%2 - 1], pygame.Rect(i * box_width + margin, j * box_height + margin, box_width, box_height))

<<<<<<< HEAD
screen.blit(text, (10,10,20,20)) 
        
=======
init_position(screen, box_width, box_height, margin)

>>>>>>> 04dbe2be9ea4406c28e7bcab85272d70d411228f
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    

    pygame.display.flip()