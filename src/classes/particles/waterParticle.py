from particle import Particle
import random as rd

colors = [
    #(15,94,156),
    (35,137,218),
    (28,163,236),
    #(90,188,216),
    #(116,204,244)
]


class WaterParticle(Particle):
    def __init__(self, grid, x, y):
        super().__init__("water", rd.choice(colors), grid, x ,y)
        self.liquid = True
        self.direction = 0
        if rd.choice([True, False]):
            self.direction = 0 #left
        else:
            self.direction = 1 #right
                

    def update(self, grid, x, y):
        if rd.randint(0, 100) <= 5:
            if self.direction == 0:
                self.direction = 1 #right
            else:
                self.direction = 0 #left
        
        if rd.randint(0, 100) <= 5:
            self.color = rd.choice(colors) # Randomly change color every frame
        if y == self.grid.rows-1: # out of bounds bottom
            return (x,y)
        elif self.grid.cells[x][y+1] is None: # move down
            return (x,y+1)   
        elif (x != 0) and self.grid.cells[x-1][y+1] is None: # move down left
            return (x-1,y+1)
        elif (x != self.grid.cols-1) and self.grid.cells[x+1][y+1] is None: # move down right
            return (x+1,y+1)
        if (x != 0) and self.grid.cells[x-1][y] is None and self.direction == 0:
            return(x-1,y)
        if (x != self.grid.cols-1) and self.grid.cells[x+1][y] is None and self.direction == 1:
            return(x+1,y)
        else: #stay in place
            return (x,y)