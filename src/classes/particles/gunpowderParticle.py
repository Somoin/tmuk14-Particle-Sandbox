from particle import Particle
import random as rd

colors = [
    (62,45,45),
    (101,87,87),
    (120,110,115)
]


class GunpowderParticle(Particle):
    def __init__(self, grid, x, y):
        super().__init__("gunpowder", rd.choice(colors), grid, x ,y)
        self.flammable = True
        self.flammability = 5 # Multiplier of flammability
    
    def update(self, grid, x, y):
        if y == self.grid.rows-1: # out of bounds bottom
            return (x,y)
        elif self.grid.cells[x][y+1] is None: # move down
            return (x,y+1)   
        elif (x != 0) and self.grid.cells[x-1][y+1] is None: # move down left
            return (x-1,y+1)
        elif (x != self.grid.cols-1) and self.grid.cells[x+1][y+1] is None: # move down right
            return (x+1,y+1)
        else: # stay in place
            return (x,y)
        