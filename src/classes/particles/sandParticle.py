from particle import Particle


class SandParticle(Particle):
    def __init__(self, grid, x, y):
        super().__init__("sand", (194, 178, 128), grid, x ,y)
    
    def update(self, grid, x, y):
        if y == self.grid.rows-1:
            return (x,y)
        elif self.grid.cells[x][y+1] is None:
            return (x,y+1)   
        else:
            return (x,y)
        