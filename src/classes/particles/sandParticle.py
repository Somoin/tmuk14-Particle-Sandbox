from particle import Particle


class SandParticle(Particle):
    def __init__(self, grid, x, y):
        super().__init__("sand", (194, 178, 128), grid, x ,y)
    
    def update(self, grid, x, y):
        
        if self.grid.cells[x][y+1] is None:
            print('m')
            return (x,y+1)   
        else:
            print('n')
            return (x,y)
        