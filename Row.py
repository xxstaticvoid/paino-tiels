

from Tile import Tile
from Tile import WIDTH, HEIGHT


from typing import List
import random

class Row:
    def __init__(self):
        self.tiles: List[Tile] = [] 
        self.decided = random.choice([0, 1, 2, 3])    ##Choose which tile in row is black
        
        for x in range(4):
            if x == self.decided:    ##If decided, instantiate as black
                tile = Tile(x * (WIDTH), -1 * (HEIGHT), True)
            else:
                tile = Tile(x * (WIDTH), -1 * (HEIGHT), False)
                
            self.tiles.append(tile)    ##Add to row

        self.is_alive = True



    def update(self):
        for tile in self.tiles:
            tile.update()


    def draw(self, screen):
        for tile in self.tiles:
            tile.draw(screen)

    def get_height(self):
        return self.tiles[0].get_height()

    def get_decided(self):
        return self.decided

    def kill_row(self, option: bool = False):
        self.is_alive = option

    def is_killed(self) -> bool:
        return not self.is_alive
    


    

