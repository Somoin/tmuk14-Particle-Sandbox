from particle import Particle
import random as rd

sand_colors = [
    (246,215,176),
    (242,210,169),
    (236,204,162),
    (231,196,150),
    (225,191,146)
]


class SandParticle(Particle):
    def __init__(self, grid, x, y):
        super().__init__("sand", rd.choice(sand_colors), grid, x ,y)
    
    def update(self, grid, x, y):
        if y == self.grid.rows-1:
            return (x,y)
        elif self.grid.cells[x][y+1] is None:
            return (x,y+1)   
        else:
            return (x,y)
        