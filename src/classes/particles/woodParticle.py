from particle import Particle
import random as rd

colors = [
    (79,32,15),
    (149,69,32),
]


class WoodParticle(Particle):
    def __init__(self, grid, x, y):
        super().__init__("wood", rd.choice(colors), grid, x ,y)
        self.flammable = True # Wood is flammable


    def update(self, grid, x, y):
            return (x,y) # Always stay in place
        