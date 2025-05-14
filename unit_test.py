import pytest
import pygame as pg
from main import ParticleType
from configparser import ConfigParser

from src.classes.button import Button
from src.classes.particles.sandParticle import SandParticle
from src.classes.grid import Grid


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


def button_check_hover(x):
    button = Button("src/images/sandbutton.png", 0, 0, "src/images/sandbutton_hover.png", 100, 100, True)
    return button.check_mouse((x, x))

def button_check_press(x, particle_type):
    element_buttons = ["sandbutton", "waterbutton", "concretebutton", "firebutton", "woodbutton", "gunpowderbutton", "virusbutton"]
    elements = ["SAND", "WATER", "CONCRETE", "FIRE", "WOOD", "GUNPOWDER", "VIRUS"]
    buttons = []
    for i, y in enumerate(element_buttons):
        # Create a button for each element, different position for the buttons
        buttons.append(Button("src/images/" + y + ".png", i*100, i*100, "src/images/" + y + "_hover.png", 100, 100, True))
    for i in range(len(buttons)):
        if buttons[i].check_mouse((x, x)):
                return True if particle_type.name == elements[i] else False
        
    """sand_button = Button("src/images/sandbutton.png", 0, 0, "src/images/sandbutton_hover.png", 100, 100, True)
    water_button = Button("src/images/waterbutton.png", 100, 100, "src/images/waterbutton_hover.png", 100, 100, True)
    concrete_button = Button("src/images/concretebutton.png", 200, 200, "src/images/concretebutton_hover.png", 100, 100, True)

    if sand_button.check_mouse((x, x)):
        return True if particle_type == ParticleType.SAND else False
    if water_button.check_mouse((x, x)):
        return True if particle_type == ParticleType.WATER else False
    if concrete_button.check_mouse((x, x)):
        return True if particle_type == ParticleType.CONCRETE else False"""
        

           
def particle_function(start_grid, particle, x, y, expected_pos):
    next_pos = particle.update(start_grid, x, y)
    if next_pos == expected_pos:
        return True
    else:
        return False

def test_particle():
    assert particle_function(start_grid, start_particle, grid_bounds[0], grid_bounds[1]-1, (grid_bounds[0], grid_bounds[1])) == True # Sand has fallen one cell down
    assert particle_function(start_grid, SandParticle(start_grid, grid_bounds[0], grid_bounds[1]), grid_bounds[0], grid_bounds[1], (grid_bounds[0], grid_bounds[1])) == True # Sand is not out of bounds

def test_answer():
    assert button_check_hover(10) == True
    
    # 10, 110, ..., 610 are the positions of the buttons
    assert button_check_press(10, ParticleType.SAND) == True
    assert button_check_press(110, ParticleType.WATER) == True
    assert button_check_press(210, ParticleType.CONCRETE) == True
    assert button_check_press(310, ParticleType.FIRE) == True
    assert button_check_press(410, ParticleType.WOOD) == True
    assert button_check_press(510, ParticleType.GUNPOWDER) == True
    assert button_check_press(610, ParticleType.VIRUS) == True

