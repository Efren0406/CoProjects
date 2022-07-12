from re import X
from turtle import heading
import pygame

pygame.init()


class Pawn():
    def __init__(self):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0

    def draw(self, screen, x, y, width, height, piece = 0):
        white_pawn = pygame.image.load(r'Chess\images\white_pawn.png')
        white_pawn = pygame.transform.scale(white_pawn, (width, height))
        black_pawn = pygame.image.load(r'Chess\images\black_pawn.png')
        black_pawn = pygame.transform.scale(black_pawn, (width, height))
        color = [white_pawn, black_pawn]
        screen.blit(color[piece], (x, y))