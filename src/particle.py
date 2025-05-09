from src.classes.grid import Grid

class Particle:
    def __init__(self, name, color, grid, x, y, static=False, flammable=False, flammability=0, liquid=False):
        self.name = name
        self.color = color
        self.grid = grid
        self.x = x
        self.y = y
        self.flammable = False
        self.flammability = 0
        self.liquid = False
        self.static = False
        self.gravity = 2

    # Utilizes polymorphism to allow for different particle types to have different update methods
    def update(self, grid, x, y):
        pass
    
