

import pygame


WIDTH, HEIGHT = 87.5, 100

class Tile:
    def __init__(self, x, y, state=False):
    
        self.state = state

        self.color = "black" if self.state else "white"
        self.rect = pygame.Rect(x, y, WIDTH, HEIGHT)
        
        self.speed = 2

    def update(self):
        self.rect.y += self.speed

    def draw(self, screen):
        if self.color == "white":
            pygame.draw.rect(screen, "black", self.rect, 1)
        else:
            pygame.draw.rect(screen, self.color, self.rect)

    def get_height(self):
        return self.rect.y


    def get_state(self) -> bool:
        return state


    def set_color(self, color="green") -> None:
        self.color = color
        
