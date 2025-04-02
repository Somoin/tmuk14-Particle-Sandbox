from classes.grid import Grid

class Particle:
    def __init__(self, name, color, grid, x, y):
        self.name = name
        self.color = color
        self.grid = grid
        self.x = x
        self.y = y

    def update(self, grid, x, y):
       return (x, y)

