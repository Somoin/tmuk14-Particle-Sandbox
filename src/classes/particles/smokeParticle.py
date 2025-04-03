from particle import Particle
import random as rd

colors = [
    (65,63,68),
    (127,72,95)
]


class SmokeParticle(Particle):
    def __init__(self, grid, x, y, lifetime):
        super().__init__("smoke", rd.choice(colors), grid, x ,y)
        self.lifetime = lifetime**2
    
    def update(self, grid, x, y):

        # Lifetime decrement
        self.lifetime -= 1
        if self.lifetime <= 0:
            return (-1,-1) # Particle dies

        if y == 0: # out of bounds bottom
            return (-1,-1)
        elif self.grid.cells[x][y-1] is None: # move up
            return (x,y-1)   
        elif (x != 0) and self.grid.cells[x-1][y-1] is None: # move up left
            return (x-1,y-1)
        elif (x != self.grid.cols-1) and self.grid.cells[x+1][y-1] is None: # move up right
            return (x+1,y-1)
        else: # stay in place
            return (x,y)
        