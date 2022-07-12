import pygame

class Circle:
    def __init__(self, screen, width, height, margin):
        self.width = width
        self.height = height
        self.radius = width * .2
        self.color = pygame.Color(255, 255, 255)
        self.x = 0
        self.y = 0
        self.screen = screen
        self.margin = margin
    
    def draw(self, i, j):
        self.x = i * self.width + self.margin
        self.y = j * self.height + self.margin

        pygame.draw.circle(self.screen, self.color, (self.x + self.width/2 , self.y + self.height/2), self.radius)