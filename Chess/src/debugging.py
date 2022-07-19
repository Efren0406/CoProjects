import pygame

def debug(info, x=0, y=0):
    SCREEN = pygame.display.get_surface()
    font = pygame.font.SysFont(None, 20)
    text = font.render(str(info), True, (255, 255, 255))
    SCREEN.blit(text, (x, y))
