from classes.grid import Grid

class Particle:
    def __init__(self, name, color, grid, x, y, flammable=False, flammability=0):
        self.name = name
        self.color = color
        self.grid = grid
        self.x = x
        self.y = y
        self.flammable = False
        self.flammability = 0

    def update(self, grid, x, y):
       return (x, y)
    
