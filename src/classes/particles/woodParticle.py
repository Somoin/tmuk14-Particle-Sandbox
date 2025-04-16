from particle import Particle
import random as rd

colors = [
    (79,32,15),
    (149,69,32),
]


class WoodParticle(Particle):
    def __init__(self, grid, x, y):
        super().__init__("wood", rd.choice(colors), grid, x ,y)
        self.static = True
        self.flammable = True # Wood is flammable
        self.flammability = 1
        


    #def update(self, grid, x, y): # Not needed for static particles
    #        return (x,y) # Always stay in place
        