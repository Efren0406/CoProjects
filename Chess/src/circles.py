import pygame

class Circle:
    def __init__(self, screen, width, height, margin):
        self.width = width
        self.height = height
        self.radius = width * .1
        self.color = None
        self.x = 0
        self.y = 0
        self.screen = screen
        self.margin = margin
    
    def draw(self, color, i, j):
        self.x = i * self.width + self.margin
        self.y = j * self.height + self.margin

        if color == 'white':
            self.color = pygame.Color(255, 255, 255)
        else:
            self.color = pygame.Color(0, 0, 0)

        pygame.draw.circle(self.screen, self.color, (self.x + self.width/2 , self.y + self.height/2), self.radius)