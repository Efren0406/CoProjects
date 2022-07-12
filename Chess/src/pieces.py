from turtle import heading
import pygame

pygame.init()

# Objeto de Peon
class Pawn():
    def __init__(self, color):
        self.x = 0
        self.y = 0
        self.width = 0
        self.height = 0
        self.color = color

    def draw(self, screen, x, y, width, height):
        white_pawn = pygame.image.load(r'images\white_pawn.png')
        white_pawn = pygame.transform.scale(white_pawn, (width - 25, height - 25))
        black_pawn = pygame.image.load(r'images\black_pawn.png')
        black_pawn = pygame.transform.scale(black_pawn, (width - 25, height - 25))
        color = [white_pawn, black_pawn]
        screen.blit(color[self.color], (x + 12.5, y + 12.5))
    
    def draw_movements(self, screen, x, y, widht, height):
        pass

# Objeto de Alfil
class Bishop():
    def __init__(self, color):
        self.x = 0
        self. y = 0
        self.widht = 0
        self.height = 0
        self.color = color

    def draw(self, screen, x , y, width, height):
        white_bishop = pygame.image.load(r'images\white_bishop.png')
        white_bishop = pygame.transform.scale(white_bishop, (width - 10, height - 10))
        black_bishop = pygame.image.load(r'images\black_bishop.png')
        black_bishop = pygame.transform.scale(black_bishop, (width - 10, height - 10))
        color = [white_bishop, black_bishop]
        screen.blit(color[self.color], (x + 5, y + 5))

# Objeto de Caballo
class Horse():
    def __init__(self, color):
        self.x = 0
        self. y = 0
        self.widht = 0
        self.height = 0
        self.color = color

    def draw(self, screen, x , y, width, height):
        white_horse = pygame.image.load(r'images\white_horse.png')
        white_horse = pygame.transform.scale(white_horse, (width - 20, height - 20))
        black_horse = pygame.image.load(r'images\black_horse.png')
        black_horse = pygame.transform.scale(black_horse, (width - 20, height - 20))
        color = [white_horse, black_horse]
        screen.blit(color[self.color], (x + 10, y + 10))

# Objeto de Torre
class Tower():
    def __init__(self, color):
        self.x = 0
        self. y = 0
        self.widht = 0
        self.height = 0
        self.color = color

    def draw(self, screen, x , y, width, height):
        white_tower = pygame.image.load(r'images\white_tower.png')
        white_tower = pygame.transform.scale(white_tower, (width - 20, height - 20))
        black_tower = pygame.image.load(r'images\black_tower.png')
        black_tower = pygame.transform.scale(black_tower, (width - 20, height - 20))
        color = [white_tower, black_tower]
        screen.blit(color[self.color], (x + 10, y + 10))

# Objeto de Reina
class Queen():
    def __init__(self, color):
        self.x = 0
        self. y = 0
        self.widht = 0
        self.height = 0
        self.color = color

    def draw(self, screen, x , y, width, height):
        white_queen = pygame.image.load(r'images\white_queen.png')
        white_queen = pygame.transform.scale(white_queen, (width, height))
        black_queen = pygame.image.load(r'images\black_queen.png')
        black_queen = pygame.transform.scale(black_queen, (width, height))
        color = [white_queen, black_queen]
        screen.blit(color[self.color], (x, y)) 
        #TRIKITAKATELAS

# Objeto de Rey
class King():
    def __init__(self, color):
        self.x = 0
        self. y = 0
        self.widht = 0
        self.height = 0
        self.color = color

    def draw(self, screen, x , y, width, height):
        white_king = pygame.image.load(r'images\white_king.png')
        white_king = pygame.transform.scale(white_king, (width, height))
        black_king = pygame.image.load(r'images\black_king.png')
        black_king = pygame.transform.scale(black_king, (width, height))
        color = [white_king, black_king]
        screen.blit(color[self.color], (x, y))

# Piezas Blancas
white_pawns = [Pawn(0) for i in range(8)]
white_bishops = [Bishop(0) for i in range(8)]
white_horses = [Horse(0) for i in range(8)]
white_towers = [Tower(0) for i in range(8)]
white_queen = Queen(0)
white_king = King(0)

# Piezas Negras
black_pawns = [Pawn(1) for i in range(8)]
black_bishops = [Bishop(1) for i in range(8)]
black_horses = [Horse(1) for i in range(8)]
black_towers = [Tower(1) for i in range(8)]
black_queen = Queen(1)
black_king = King(1)