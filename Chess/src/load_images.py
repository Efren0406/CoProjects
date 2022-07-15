import pygame

class Images:
    def select(self, color, type, width, height):
        if color == 'white':
            if type == 'p' or type == 'pawn':
                image = pygame.image.load(r'images\white_pawn.png')
                image = pygame.transform.scale(image, (width - 25, height - 25))
                image_margin = 12.5
            elif type == 'B' or type == 'bishop':
                image = pygame.image.load(r'images\white_bishop.png')
                image = pygame.transform.scale(image, (width - 10, height - 10))
                image_margin = 5
            elif type == 'H' or type == 'horse':
                image = pygame.image.load(r'images\white_horse.png')
                image = pygame.transform.scale(image, (width - 10, height - 10))
                image_margin = 5
            elif type == 'T' or type == 'tower':
                image = pygame.image.load(r'images\white_tower.png')
                image = pygame.transform.scale(image, (width - 10, height - 10))
                image_margin = 5
            elif type == 'Q' or type == 'queen':
                image = pygame.image.load(r'images\white_queen.png')
                image = pygame.transform.scale(image, (width + 1, height + 1))
                image_margin = 0
            elif type == 'K' or type == 'king':
                image = pygame.image.load(r'images\white_king.png')
                image = pygame.transform.scale(image, (width + 1, height + 1))
                image_margin = 0
        if color == 'black':
            if type == 'p' or type == 'pawn':
                image = pygame.image.load(r'images\black_pawn.png')
                image = pygame.transform.scale(image, (width - 25, height - 25))
                image_margin = 12.5
            elif type == 'B' or type == 'bishop':
                image = pygame.image.load(r'images\black_bishop.png')
                image = pygame.transform.scale(image, (width - 10, height - 10))
                image_margin = 5
            elif type == 'H' or type == 'horse':
                image = pygame.image.load(r'images\black_horse.png')
                image = pygame.transform.scale(image, (width - 10, height - 10))
                image_margin = 5
            elif type == 'T' or type == 'tower':
                image = pygame.image.load(r'images\black_tower.png')
                image = pygame.transform.scale(image, (width - 10, height - 10))
                image_margin = 5
            elif type == 'Q' or type == 'queen':
                image = pygame.image.load(r'images\black_queen.png')
                image = pygame.transform.scale(image, (width + 1, height + 1))
                image_margin = 0
            elif type == 'K' or type == 'king':
                image = pygame.image.load(r'images\black_king.png')
                image = pygame.transform.scale(image, (width + 1, height + 1))
                image_margin = 0

        return image, image_margin
