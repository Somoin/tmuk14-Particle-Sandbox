from particle import Particle
import random as rd

colors = [
    (148,142,142),
    (154,146,144),
    (141,139,137),
    (139,139,139),
    (133,133,133)
]


class ConcreteParticle(Particle):
    def __init__(self, grid, x, y):
        super().__init__("concrete", rd.choice(colors), grid, x ,y)
    
    def update(self, grid, x, y):
            return (x,y) # Always stay in place
        