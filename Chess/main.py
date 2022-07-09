import pygame, sys 
pygame.init()


print("HELLO")

size = width, height = 800, 800

screen = pygame.display.set_mode(size)

color1 = (194, 150, 102)
color2 = (180, 130, 81)

for j in range(8):
    for i in range(8):
        if i%2 == 0:
            pygame.draw.rect(screen, color1, pygame.Rect(30 + i * ((width-60)/8), 30 + j * ((width-60)/8), (width-60)/8, (height-60)/8))
        else:
            pygame.draw.rect(screen, color2, pygame.Rect(30 + i * ((width-60)/8), 30, (width-60)/8, (height-60)/8))

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pygame.display.flip()