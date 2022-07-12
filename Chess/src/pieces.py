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

class Bishop():
    def __init__(self):
        self.x = 0
        self. y = 0
        self.widht = 0
        self.height = 0

    def draw(self, screen, x , y, width, height, piece = 0):
        white_bishop = pygame.image.load(r'Chess\images\white_bishop.png')
        white_bishop = pygame.transform.scale(white_bishop, (width, height))
        black_bishop = pygame.image.load(r'Chess\images\black_bishop.png')
        black_bishop = pygame.transform.scale(black_bishop, (width, height))
        color = [white_bishop, black_bishop]
        screen.blit(color[piece], (x, y))

class Horse():
    def __init__(self):
        self.x = 0
        self. y = 0
        self.widht = 0
        self.height = 0

    def draw(self, screen, x , y, width, height, piece = 0):
        white_horse = pygame.image.load(r'Chess\images\white_horse.png')
        white_horse = pygame.transform.scale(white_horse, (width, height))
        black_horse = pygame.image.load(r'Chess\images\black_horse.png')
        black_horse = pygame.transform.scale(black_horse, (width, height))
        color = [white_horse, black_horse]
        screen.blit(color[piece], (x, y))

class Tower():
    def __init__(self):
        self.x = 0
        self. y = 0
        self.widht = 0
        self.height = 0

    def draw(self, screen, x , y, width, height, piece = 0):
        white_tower = pygame.image.load(r'Chess\images\white_tower.png')
        white_tower = pygame.transform.scale(white_tower, (width, height))
        black_tower = pygame.image.load(r'Chess\images\black_tower.png')
        black_tower = pygame.transform.scale(black_tower, (width, height))
        color = [white_tower, black_tower]
        screen.blit(color[piece], (x, y))

class Queen():
    def __init__(self):
        self.x = 0
        self. y = 0
        self.widht = 0
        self.height = 0

    def draw(self, screen, x , y, width, height, piece = 0):
        white_queen = pygame.image.load(r'Chess\images\white_queen.png')
        white_queen = pygame.transform.scale(white_queen, (width, height))
        black_queen = pygame.image.load(r'Chess\images\black_queen.png')
        black_queen = pygame.transform.scale(black_queen, (width, height))
        color = [white_queen, black_queen]
        screen.blit(color[piece], (x, y)) 
        #TRIKITAKATELAS

class Queen():
    def __init__(self):
        self.x = 0
        self. y = 0
        self.widht = 0
        self.height = 0

    def draw(self, screen, x , y, width, height, piece = 0):
        white_queen = pygame.image.load(r'Chess\images\white_queen.png')
        white_queen = pygame.transform.scale(white_queen, (width, height))
        black_queen = pygame.image.load(r'Chess\images\black_queen.png')
        black_queen = pygame.transform.scale(black_queen, (width, height))
        color = [white_queen, black_queen]
        screen.blit(color[piece], (x, y))