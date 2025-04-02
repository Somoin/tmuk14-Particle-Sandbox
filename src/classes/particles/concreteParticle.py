from particle import Particle
import random as rd

colors = [
    (125,116,116),
    (67,57,57),
    (45,40,40)
]


class ConcreteParticle(Particle):
    def __init__(self, grid, x, y):
        super().__init__("concrete", rd.choice(colors), grid, x ,y)
    
    def update(self, grid, x, y):
            return (x,y) # Always stay in place
        