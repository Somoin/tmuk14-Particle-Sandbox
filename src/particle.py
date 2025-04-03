from classes.grid import Grid

class Particle:
    def __init__(self, name, color, grid, x, y, flammable=False):
        self.name = name
        self.color = color
        self.grid = grid
        self.x = x
        self.y = y
        self.flammable = False

    def update(self, grid, x, y):
       return (x, y)
    
