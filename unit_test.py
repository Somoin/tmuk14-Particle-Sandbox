import pytest
import pygame as pg
from main import ParticleType
from configparser import ConfigParser

from src.classes.button import Button
from src.classes.particles.sandParticle import SandParticle
from src.classes.particles.waterParticle import WaterParticle
from src.classes.particles.concreteParticle import ConcreteParticle
from src.classes.particles.smokeParticle import SmokeParticle
from src.classes.particles.woodParticle import WoodParticle
from src.classes.particles.fireParticle import FireParticle
from src.classes.particles.gunpowderParticle import GunpowderParticle
from src.classes.particles.virusParticle import VirusParticle
from src.classes.grid import Grid
from src.simulation import Simulation


pg.init()
config_object = ConfigParser()

config_object.read("config.ini")
cell_size = config_object.getint("CONFIG", "cell_size")
window_width = config_object.getint("CONFIG", "window_width")
window_height = config_object.getint("CONFIG", "window_height")
FPS = config_object.getint("CONFIG", "FPS")
window = pg.display.set_mode((window_width, window_height))

start_grid = Grid(window_width, window_height, cell_size)
start_particle = SandParticle(start_grid, 0,0)
start_grid.cells[0][0] = start_particle
grid_bounds = (start_grid.cols - 1, start_grid.rows - 1)

pg.display.set_caption("Particle Sandbox")

simulation = Simulation(window_width, window_height, cell_size)

def button_check_hover(x):
    button = Button("src/images/sandbutton.png", 0, 0, "src/images/sandbutton_hover.png", 100, 100)
    return button.check_mouse((x, x))

def button_check_press(x, particle_type):
    button = Button("src/images/waterbutton.png", 0, 0, "src/images/waterbutton_hover.png", 100, 100)
    if button.check_mouse((x, x)):
        return True if particle_type == ParticleType.WATER else False
           
def particle_function(start_grid, particle, x, y, expected_pos):
    next_pos = particle.update(start_grid, x, y)
    if next_pos == expected_pos:
        return True
    else:
        return False
    
amount_of_particles = 8
particle_order = [SandParticle, WaterParticle, ConcreteParticle, SmokeParticle, WoodParticle, FireParticle, GunpowderParticle, VirusParticle]
def simulation_adding():
    simulation.add_particle(SandParticle(simulation.grid, 0, 0), 0, 0)
    simulation.add_particle(WaterParticle(simulation.grid, 1, 0, 100), 1, 0)
    simulation.add_particle(ConcreteParticle(simulation.grid, 2, 0), 2, 0)
    simulation.add_particle(SmokeParticle(simulation.grid, 3, 0, 100), 3, 0)
    simulation.add_particle(WoodParticle(simulation.grid, 4, 0), 4, 0)
    simulation.add_particle(FireParticle(simulation.grid, 5, 0, 100, 2), 5, 0)
    simulation.add_particle(GunpowderParticle(simulation.grid, 6, 0), 6, 0)
    simulation.add_particle(VirusParticle(simulation.grid, 7, 0, 100, 100), 7, 0)

def simulation_removing():
    simulation.remove_particle(0, 0)
    simulation.remove_particle(1, 0)
    simulation.remove_particle(2, 0)
    simulation.remove_particle(3, 0)
    simulation.remove_particle(4, 0)
    simulation.remove_particle(5, 0)
    simulation.remove_particle(6, 0)
    simulation.remove_particle(7, 0)

# Check if the fire spread to the gunpowder
def fire_test():
    simulation.add_particle(FireParticle(simulation.grid, 0, 0, 100, 100), 0, 0) # 100% ignite chance
    simulation.add_particle(GunpowderParticle(simulation.grid, 1, 0), 1, 0)
   

# Integration tests as modules are interacting with each other
def test_simulation():
    simulation_adding()
    for i in range(amount_of_particles):
        assert isinstance(simulation.cells[i][0], particle_order[i]) == True # Check if the particles are the correct type
        assert simulation.cells[i][0].grid == simulation.grid # Check if the grid is set correctly
        assert simulation.cells[i][0].x == i # Check if the x position is set correctly
        assert simulation.cells[i][0].y == 0 # Check if the y position is set correctly
    
    simulation_removing()
    for i in range(amount_of_particles):
        assert simulation.cells[i][0] == None # Check if the particles are removed correctly

    simulation.clear()
    for i in range(simulation.cols):
        for j in range(simulation.rows):
            assert simulation.cells[i][j] == None # Check if the grid is cleared correctly
            assert simulation.next_cells.cells[i][j] == None # Check if the next cells are cleared correctly

    fire_test()
    simulation.update()
    assert isinstance(simulation.cells[1][0], FireParticle) == True # Check if the gunpowder turned into fire   

def test_particle():
    assert particle_function(start_grid, start_particle, grid_bounds[0], grid_bounds[1]-1, (grid_bounds[0], grid_bounds[1])) == True # Sand has fallen one cell down
    assert particle_function(start_grid, SandParticle(start_grid, grid_bounds[0], grid_bounds[1]), grid_bounds[0], grid_bounds[1], (grid_bounds[0], grid_bounds[1])) == True # Sand is not out of bounds

def test_answer():
    assert button_check_hover(10) == True
    assert button_check_press(10, ParticleType.WATER) == True
