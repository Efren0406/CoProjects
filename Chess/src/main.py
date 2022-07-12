from ast import Num
import pygame
import sys
from display_pieces import *
from selected_piece import *

pygame.init()
pygame.display.set_caption('Show Text')

size = width, height = 800, 800
margin = 60

screen = pygame.display.set_mode(size)

# Configuracion del tablero
board = [['x' for i in range(8)] for j in range(8)]

# Colores
brown_border = pygame.Color(51, 25, 0)
brown_bold = pygame.Color(102, 51, 0)
brown_light = pygame.Color(153, 76, 0)
white_light = pygame.Color(255, 255, 255)

# Letras izquierda
font = pygame.font.SysFont(None, 30)

text = font.render('A', True, white_light)
screen.blit(text, (30,90))

text1 = font.render('B', True, white_light)
screen.blit(text1, (30,170))

text3 = font.render('C', True, white_light)
screen.blit(text3, (30,260))

text4 = font.render('D', True, white_light)
screen.blit(text4, (30,345))

text5 = font.render('E', True, white_light)
screen.blit(text5, (30,430))

text6 = font.render('F', True, white_light)
screen.blit(text6, (30,515))

text7 = font.render('G', True, white_light)
screen.blit(text7, (30,600))

text8 = font.render('H', True, white_light)
screen.blit(text8, (30,690))

# Numeros casillas 
num = font.render('1', True, white_light)
screen.blit(num, (90,760))

num1 = font.render('2', True, white_light)
screen.blit(num1, (175,760))

num2 = font.render('3', True, white_light)
screen.blit(num2, (265,760))

num3 = font.render('4', True, white_light)
screen.blit(num3, (350,760))

num4 = font.render('5', True, white_light)
screen.blit(num4, (435,760))

num5 = font.render('6', True, white_light)
screen.blit(num5, (520,760))

num6 = font.render('7', True, white_light)
screen.blit(num6, (610,760))

num7 = font.render('8', True, white_light)
screen.blit(num7, (690,760))

# Dibujar Tablero
box_width = (width - 2*margin)/8
box_height = (height - 2*margin)/8

for i in range(8):
    for j in range(8):
        color = [brown_bold, brown_light]
        pygame.draw.rect(screen, color[i%2 + j%2 - 1], pygame.Rect(i * box_width + margin, j * box_height + margin, box_width, box_height))
        
# <<<<<<<
init_position(screen, board, box_width, box_height, margin)

# >>>>>>> 
while True:
    for event in pygame.event.get():
        mouse_position = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            i = int((mouse_position[0] - margin)//box_width)
            j = int((mouse_position[1] - margin)//box_height)
    
    display_pieces(screen, board, box_width, box_height, margin)

    pygame.display.flip()