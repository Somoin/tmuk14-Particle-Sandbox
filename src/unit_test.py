import pytest
import pygame as pg
from configparser import ConfigParser

from classes.button import Button
from classes.particles.sandParticle import SandParticle
from classes.grid import Grid

pg.init()
config_object = ConfigParser()

config_object.read("config.ini")
cell_size = config_object.getint("CONFIG", "cell_size")
window_width = config_object.getint("CONFIG", "window_width")
window_height = config_object.getint("CONFIG", "window_height")
FPS = config_object.getint("CONFIG", "FPS")
window = pg.display.set_mode((window_width, window_height))

pg.display.set_caption("Particle Sandbox")


def button_check_hover(x):
    button = Button("images/sandbutton.png", 0, 0, "images/sandbutton_hover.png", 100, 100)
    return button.check_hover((x, x))




start_grid = Grid(window_width, window_height, cell_size)
start_particle = SandParticle(start_grid, 0, 0)
start_grid.cells[0][0] = start_particle
grid_bounds = (start_grid.cols-1, start_grid.rows-1)


def particle_function(start_grid, particle, x, y, expected_pos):
    next_pos = particle.update(start_grid, x, y)
    if next_pos == (expected_pos):
        return True
    else: 
        return False

def test_particle():
    assert particle_function(start_grid, start_particle, 0, 0, (0,1)) == True # Sand has fallen one cell down
    assert particle_function(start_grid, SandParticle(start_grid, grid_bounds[0], grid_bounds[1]), grid_bounds[0], grid_bounds[1], (grid_bounds[0], grid_bounds[1])) == True # Sand is not out of bounds
    
def test_answer():
    assert button_check_hover(10) == True