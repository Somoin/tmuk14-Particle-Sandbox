from particle import Particle
from classes.particles.smokeParticle import SmokeParticle
import random as rd

colors = [
    (242,125,12),
    (240,127,19)
]


class FireParticle(Particle):
    def __init__(self, grid, x, y, lifetime, potency):
        super().__init__("fire", rd.choice(colors), grid, x ,y)
        self.max_lifetime = lifetime # The max lifetime of the fire particle in frames
        self.potency = potency # The chance of fire spreading to a flammable particle
        self.lifetime = self.max_lifetime 
        self.smoke_lifetime = 10
        self.smoke_potency = 1  # The chance of creating smoke when burning a flammable particle

    def create_smoke(self, x, y):
        if y > 0 and self.grid.cells[x][y-1] is None:
            if rd.randint(0, 100) <= self.smoke_potency:
                self.grid.cells[x][y-1] = SmokeParticle(self.grid, x, y-1, self.smoke_lifetime) # Create smoke particle above the fire particle

    def burn(self, x, y):
        self.create_smoke(x, y) # Create smoke particle above the fire particle
        curr_lifetime = self.lifetime
        if self.grid.cells[x][y] is not None: # If the cell to the specified direction is flammable burn it and replace it
            Particle = self.grid.cells[x][y]
            if Particle.flammable == True:
                
                if rd.randint(0, 100) <= self.potency:
                    self.grid.cells[x][y] = FireParticle(self.grid, x, y, self.max_lifetime, self.potency) # Replace the particle with a fire particle
                
            return (x,y)
        

    def update(self, grid, x, y):           
        # Lifetime decrement
        
        self.lifetime -= 1
        if self.lifetime <= 0: 
            return (-1,-1) # Particle dies

        if x > 0:
            self.burn(x-1, y) # Check left
            if y > 0:
                self.burn(x-1, y-1) # Check top left
            if y < self.grid.rows - 1:
                self.burn(x-1, y+1) # Check bottom left
        if x < self.grid.cols - 1: # Check right
            self.burn(x+1, y)
            if y > 0:
                self.burn(x+1, y-1) # Check top right
            if y < self.grid.rows - 1:
                self.burn(x+1, y+1) # Check bottom right
        if y > 0: # Check up
            self.burn(x, y-1)
        if y < self.grid.rows - 1: # Check down
            self.burn(x, y+1)

        return (x,y)
       
        