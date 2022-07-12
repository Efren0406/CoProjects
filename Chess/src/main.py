from ast import Num
import pygame
import sys

pygame.init()
pygame.display.set_caption('Show Text')

screen_info = pygame.display.Info()
size = width, height = screen_info.current_h - screen_info.current_h * .10, screen_info.current_h - screen_info.current_h * .10 
margin = height * .075

screen = pygame.display.set_mode(size)

# Configuracion del tablero

# Colores
brown_border = pygame.Color(51, 25, 0)
brown_bold = pygame.Color(102, 51, 0)
brown_light = pygame.Color(153, 76, 0)
white_light = pygame.Color(255, 255, 255)

# Letras izquierda
font = pygame.font.SysFont(None, int(margin/2))
letter_space = height * .107142857143

for i in range(8):
    text = font.render(chr(65 + i), True, white_light)
    num = font.render(str(i + 1), True, white_light)
    screen.blit(text, (margin/2, i * letter_space + (3 * margin/2)))
    screen.blit(num, (i * letter_space + (3 * margin/2), width - (2 * margin/3)))

# Dibujar Tablero
box_width = (width - 2*margin)/8
box_height = (height - 2*margin)/8

for i in range(8):
    for j in range(8):
        color = [brown_bold, brown_light]
        pygame.draw.rect(screen, color[i%2 + j%2 - 1], pygame.Rect(i * box_width + margin, j * box_height + margin, box_width, box_height))
        
# <<<<<<<

# >>>>>>> 
while True:
    for event in pygame.event.get():
        mouse_position = pygame.mouse.get_pos()
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            i = int((mouse_position[0] - margin)//box_width)
            j = int((mouse_position[1] - margin)//box_height)
    
    pygame.display.flip()