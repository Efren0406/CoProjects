import pygame

pygame.init()

class Piece:
    def __init__(self, screen, width, height, margin):
        self.width = width
        self.height = height
        self.x = 0
        self.y = 0
        self.image = None
        self.screen = screen
        self.margin = margin
    
    def draw(self):
        pass

    def set_type(self):
        pass