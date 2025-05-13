import pytest
import pygame as pg
from main import ParticleType
from configparser import ConfigParser

from src.classes.button import Button
from src.classes.particles.sandParticle import SandParticle
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
    
def simulation_adding():
    pass

def test_particle():
    assert particle_function(start_grid, start_particle, grid_bounds[0], grid_bounds[1]-1, (grid_bounds[0], grid_bounds[1])) == True # Sand has fallen one cell down
    assert particle_function(start_grid, SandParticle(start_grid, grid_bounds[0], grid_bounds[1]), grid_bounds[0], grid_bounds[1], (grid_bounds[0], grid_bounds[1])) == True # Sand is not out of bounds

def test_answer():
    assert button_check_hover(10) == True
    assert button_check_press(10, ParticleType.WATER) == True
