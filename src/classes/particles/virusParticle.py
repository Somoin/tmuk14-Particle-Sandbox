from src.particle import Particle
import random as rd


colors = [
    (147,112,219),
    (102,51,153),
    (186,85,211)
]


class VirusParticle(Particle):
    def __init__(self, grid, x, y, lifetime, standard_lifetime):
        super().__init__("virus", rd.choice(colors), grid, x ,y)
        self.directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)] # 8 directions
        self.lifetime = lifetime
        self.standard_lifetime = standard_lifetime # Store the standard lifetime for color change
    
    def update(self, grid, x, y):
        if (self.lifetime == 0):
            return (-1,-1) # Particle is dead
        else:
            self.lifetime -= 1

        if y == self.grid.rows-1: # out of bounds bottom
            return (-1,-1)
        if x == 0: # out of bounds left
            return (-1,-1)
        if x == self.grid.cols-1: # out of bounds right
            return (-1,-1)
        if y == 0: # out of bounds top
            return (-1,-1)
        
        direction = rd.choice(self.directions) # Randomly choose a direction to move
        if (self.grid.cells[x+direction[0]][y+direction[1]] is not None):
            self.grid.cells[x+direction[0]][y+direction[1]] = VirusParticle(self.grid, x+direction[0], y+direction[1], lifetime=self.standard_lifetime, standard_lifetime=self.standard_lifetime) # Replace the particle with a virus particle
        return (x+direction[0], y+direction[1]) # Move in the chosen direction
        
        
        return (x,y)
        
