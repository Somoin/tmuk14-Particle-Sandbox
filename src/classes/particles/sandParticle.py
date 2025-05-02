from particle import Particle
from classes.particles.waterParticle import WaterParticle
import random as rd


colors = [
    (246,215,176),
    (242,210,169),
    (236,204,162),
    (231,196,150),
    (225,191,146)
]


class SandParticle(Particle):
    def __init__(self, grid, x, y):
        super().__init__("sand", rd.choice(colors), grid, x ,y)
    
    def update(self, grid, x, y):
        if y == self.grid.rows-1: # out of bounds bottom
            return (x,y)
        
        # Gravity 
        startPos = (x,y)
        currPos = startPos
        for i in range(self.gravity):
            if y+i+1 == self.grid.rows-1:
                return currPos
            if self.grid.cells[x][y+1+i] is None: # move down
                currPos = (x,y+1+i) 
                
        if currPos != startPos:
            return currPos
        
        if (x != 0) and self.grid.cells[x-1][y+1] is None: # move down left
            return (x-1,y+1)
        if (x != self.grid.cols-1) and self.grid.cells[x+1][y+1] is None: # move down right
            return (x+1,y+1)
       
        return (x,y)
        