
import pygame

class Line():
    def __init__(self):
    
        self.color = "purple"
        self.rect = pygame.Rect(-10, (500 * 9) // 10, 350 + 40, 4) ## (x, y, width, height)

    def update(self):
        pass
    
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

