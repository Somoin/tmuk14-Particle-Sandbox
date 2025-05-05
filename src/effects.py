import simulation
import random
from classes.particles.sandParticle import SandParticle
from classes.particles.fireParticle import FireParticle

class Effects:
    def __init__(self, simulation : simulation):
        self.simulation = simulation

   
    def eye_of_rah(self):
        for col in range(self.simulation.cols):
            for row in range(self.simulation.rows):
                if self.simulation.cells[col][row] is not None:
                    self.simulation.remove_particle(col, row) # Remove the particle from the grid
                    self.simulation.add_particle(SandParticle(self.simulation.grid, col, row), col, row)

    def ignis(self):
        for col in range(self.simulation.cols):
            for row in range(self.simulation.rows):
                if self.simulation.cells[col][row] is not None:
                    if self.simulation.cells[col][row].flammable == True:     
                        self.simulation.remove_particle(col, row) # Remove the particle from the grid
                        self.simulation.add_particle(FireParticle(self.simulation.grid, col, row, random.randint(10,100), 2), col, row)