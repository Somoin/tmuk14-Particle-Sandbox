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
from src.particle import Particle


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

# Static particles
concrete_particle = ConcreteParticle(start_grid, 1, 1)
wood_particle = WoodParticle(start_grid, 2, 2)
start_grid.cells[1][1] = concrete_particle
start_grid.cells[2][2] = wood_particle

pg.display.set_caption("Particle Sandbox")

simulation = Simulation(window_width, window_height, cell_size)

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
    
           
def particle_function(start_grid, particle, x, y, expected_pos):
    if particle.update(start_grid, x, y) != None:
        next_pos = particle.update(start_grid, x, y)
        print("Name: " + particle.name + "Next pos: " + str(next_pos))
    if particle.update(start_grid, x, y) == None and particle.static == True:
        return True
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

    simulation.clear()



def test_particle():
    assert particle_function(start_grid, concrete_particle, 1, 1, (1, 1)) == True 
    assert particle_function(start_grid, wood_particle, 2, 2, (2, 2)) == True 
    assert particle_function(start_grid, start_particle, grid_bounds[0], grid_bounds[1]-1, (grid_bounds[0], grid_bounds[1])) == True # Sand has fallen one cell down
    assert particle_function(start_grid, SandParticle(start_grid, grid_bounds[0], grid_bounds[1]), grid_bounds[0], grid_bounds[1], (grid_bounds[0], grid_bounds[1])) == True # Sand is not out of bounds

    water_grid = Grid(window_height, window_width, cell_size) # 3x3 grid
    water_particle = WaterParticle(water_grid, 1, 1, 100)
    assert particle_function(water_grid, water_particle, 1, 1, (1, 1 + water_particle.gravity)) == True

    new_concrete_particle = ConcreteParticle(water_grid, 1, 2) # Add concrete particle as obstacle
    water_grid.cells[1][2] = new_concrete_particle
    water_grid.cells[1][1] = water_particle
    assert particle_function(water_grid, water_particle, 1, 1, (0, 2)) == True

    new_water_particle = WaterParticle(water_grid, 1, 1, 0)
    assert particle_function(water_grid, new_water_particle, 1, 1, (-1, -1)) == True

    concrete_obstacle_1 = ConcreteParticle(water_grid, 0, 1)
    concrete_obstacle_2 = ConcreteParticle(water_grid, 0, 2)
    concrete_obstacle_3 = ConcreteParticle(water_grid, 1, 2)
    water_grid.cells[0][1] = concrete_obstacle_1
    water_grid.cells[0][2] = concrete_obstacle_2
    water_grid.cells[1][2] = concrete_obstacle_3
    water_grid.cells[1][1] = water_particle
    assert particle_function(water_grid, water_particle, 1, 1, (2, 2)) == True # Water moves to the right









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

