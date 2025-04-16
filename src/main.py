from enum import Enum
from configparser import ConfigParser
import pygame as pg
from classes.button import Button
from simulation import Simulation

from classes.fps_counter import fps_counter # Import fps_counter class from classes/fps_counter.py
from classes.particles.sandParticle import SandParticle
from classes.particles.waterParticle import WaterParticle
from classes.particles.concreteParticle import ConcreteParticle
from classes.particles.smokeParticle import SmokeParticle
from classes.particles.woodParticle import WoodParticle
from classes.particles.fireParticle import FireParticle
from classes.particles.gunpowderParticle import GunpowderParticle
from classes.text_display import TextDisplay




class ParticleType(Enum):
    SAND = 1
    WATER = 2
    CONCRETE = 3
    AIR = 4
    SMOKE = 5
    WOOD = 6
    FIRE = 7
    GUNPOWDER = 8
    GAS = 9
    #default = AIR

class CursorMode(Enum):
    DEFAULT = 1
    BLOCK = 2

CURSOR_BLOCK_WIDTH = 10
CURSOR_BLOCK_HEIGHT = 10

pg.init()

config_object = ConfigParser()



if len(config_object.read("config.ini")) > 0:
    cell_size = config_object.getint("CONFIG", "cell_size")
    window_width = config_object.getint("CONFIG", "window_width")
    window_height = config_object.getint("CONFIG", "window_height")
    FPS = config_object.getint("CONFIG", "FPS")
else:
    config_object["CONFIG"] = {
        "cell_size": 8,
        "window_width": 1280,
        "window_height": 800,
        "FPS": 120
    }

    with open("config.ini", "w") as config_file:
        config_object.write(config_file)

    config_object.read("config.ini")
    cell_size = config_object.getint("CONFIG", "cell_size")
    window_width = config_object.getint("CONFIG", "window_width")
    window_height = config_object.getint("CONFIG", "window_height")
    FPS = config_object.getint("CONFIG", "FPS")



window = pg.display.set_mode((window_width, window_height))
pg.display.set_caption("Particle Sandbox")

clock = pg.time.Clock()

simulation_width = window_width
simulation_height = round(window_height - (window_height*0.375))
simulation = Simulation(simulation_width, simulation_height, cell_size)
fps_counter = fps_counter(window, pg.font.Font(None, 30), clock, (255, 255, 255), (60, 25))

TEXT_PADDING_X = 350
TEXT_PADDING_Y = 785
text_display = TextDisplay(window, "", window_width - TEXT_PADDING_X, window_height - TEXT_PADDING_Y, (255, 255, 255))

button_width = window_width*0.175
button_height = window_height*0.1125

sand_button = Button("images/sandbutton.png", 120, 550, "images/sandbutton_hover.png", button_width, button_height)
water_button = Button("images/waterbutton.png", 370, 550, "images/waterbutton_hover.png", button_width, button_height)
concrete_button = Button("images/concretebutton.png", 620, 550, "images/concretebutton_hover.png", button_width, button_height)
fire_button = Button("images/firebutton.png", 870, 550, "images/firebutton_hover.png", button_width, button_height)
wood_button = Button("images/woodbutton.png", 1120, 550,"images/woodbutton_hover.png", button_width, button_height)
gunpowder_button = Button("images/gunpowderbutton.png", 120, 675, "images/gunpowderbutton_hover.png", button_width, button_height)
buttons = [sand_button, water_button, concrete_button, fire_button, wood_button, gunpowder_button]

def particle_input(particle_type, mouse_x, mouse_y): # Adds particle to the simulation based on mouse coordinates
    if particle_type == ParticleType.SAND:
        particle = SandParticle(simulation.grid, mouse_x, mouse_y)
        simulation.add_particle(particle, mouse_x, mouse_y)
    elif particle_type == ParticleType.WATER:
        particle = WaterParticle(simulation.grid, mouse_x, mouse_y, lifetime=250)
        simulation.add_particle(particle, mouse_x, mouse_y)
    elif particle_type == ParticleType.CONCRETE:
        particle = ConcreteParticle(simulation.grid, mouse_x, mouse_y)
        simulation.add_particle(particle, mouse_x, mouse_y)
    elif particle_type == ParticleType.SMOKE:
        particle = SmokeParticle(simulation.grid, mouse_x, mouse_y, lifetime=100)
        simulation.add_particle(particle, mouse_x, mouse_y)
    elif particle_type == ParticleType.WOOD:
        particle = WoodParticle(simulation.grid, mouse_x, mouse_y)
        simulation.add_particle(particle, mouse_x, mouse_y)
    elif particle_type == ParticleType.FIRE:
        particle = FireParticle(simulation.grid, mouse_x, mouse_y, lifetime=100, potency=2)
        simulation.add_particle(particle, mouse_x, mouse_y)
    elif particle_type == ParticleType.GUNPOWDER:
        particle = GunpowderParticle(simulation.grid, mouse_x, mouse_y)
        simulation.add_particle(particle, mouse_x, mouse_y)


def main():

    particle_type = ParticleType.AIR
    cursor_type = CursorMode.DEFAULT

    left_click_down = False
    right_click_down = False

    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1: # Left mouse button held
                left_click_down = True
            elif event.type == pg.MOUSEBUTTONUP and event.button == 1: # Left mouse button released
                left_click_down = False
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 3: # Right mouse button held
                right_click_down = True
            elif event.type == pg.MOUSEBUTTONUP and event.button == 3: # Right mouse button released
                right_click_down = False


            if event.type == pg.MOUSEBUTTONDOWN: #Registers when clicked once
                if sand_button.check_press(pg.mouse.get_pos()):
                    print("Sand Button Pressed")
                    particle_type = ParticleType.SAND
                if water_button.check_press(pg.mouse.get_pos()):
                    print("Water Button Pressed")
                    particle_type = ParticleType.WATER
                if concrete_button.check_press(pg.mouse.get_pos()):
                    print("Concrete Button Pressed")
                    particle_type = ParticleType.CONCRETE
                if fire_button.check_press(pg.mouse.get_pos()):
                    print("Fire Button Pressed")
                    particle_type = ParticleType.FIRE
                if wood_button.check_press(pg.mouse.get_pos()):
                    print("Wood Button Pressed")
                    particle_type = ParticleType.WOOD
                if gunpowder_button.check_press(pg.mouse.get_pos()):
                    print("Gunpowder Button Pressed")
                    particle_type = ParticleType.GUNPOWDER

            # Debug Keyboard input
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    particle_type = ParticleType.SAND
                    print("Sand Key Pressed")
                if event.key == pg.K_2:
                    particle_type = ParticleType.WATER
                    print("Water Key Pressed")
                if event.key == pg.K_3:
                    particle_type = ParticleType.CONCRETE
                    print("Cement Key Pressed")
                if event.key == pg.K_4:
                    particle_type = ParticleType.SMOKE
                    print("Smoke Key Pressed")
                if event.key == pg.K_5:
                    particle_type = ParticleType.WOOD
                    print("Wood Key Pressed")
                if event.key == pg.K_6:
                    particle_type = ParticleType.FIRE
                    print("Fire Key Pressed")
                if event.key == pg.K_7:
                    particle_type = ParticleType.GUNPOWDER
                    print("Gunpowder Key Pressed")
                if event.key == pg.K_8:
                    particle_type = ParticleType.GAS
                    print("Air Key Pressed")
                if event.key == pg.K_c:
                    simulation.clear()

                # Changing cursor type
                if event.key == pg.K_q:
                    if cursor_type == CursorMode.DEFAULT:
                        cursor_type = CursorMode.BLOCK
                    else:
                        cursor_type = CursorMode.DEFAULT


        mouse_x = pg.mouse.get_pos()[0]//cell_size
        mouse_y = pg.mouse.get_pos()[1]//cell_size

        # Particle spawning / removing on mousedown
        if left_click_down is True: # Registers when held down
            if cursor_type == CursorMode.DEFAULT:
                particle_input(particle_type, mouse_x, mouse_y)


            if cursor_type == CursorMode.BLOCK:
                for i in range(CURSOR_BLOCK_WIDTH):
                    for j in range(CURSOR_BLOCK_HEIGHT):
                        mouse_x = pg.mouse.get_pos()[0]//cell_size - CURSOR_BLOCK_WIDTH//2 + i
                        mouse_y = pg.mouse.get_pos()[1]//cell_size - CURSOR_BLOCK_HEIGHT//2 + j
                        particle_input(particle_type, mouse_x, mouse_y)

        elif right_click_down is True: # Right mouse button
            if cursor_type == CursorMode.DEFAULT:
                simulation.remove_particle(mouse_x, mouse_y)
            elif cursor_type == CursorMode.BLOCK:
                for i in range(CURSOR_BLOCK_WIDTH):
                    for j in range(CURSOR_BLOCK_HEIGHT):
                        mouse_x = pg.mouse.get_pos()[0]//cell_size - CURSOR_BLOCK_WIDTH//2 + i
                        mouse_y = pg.mouse.get_pos()[1]//cell_size - CURSOR_BLOCK_HEIGHT//2 + j
                        simulation.remove_particle(mouse_x, mouse_y)

        window.fill((0, 0, 0))
        for button in buttons:
            button.draw(window)

        simulation.draw(window)
        simulation.update()

        text_display.text = "CURRENT PARTICLE: " + particle_type.name
        text_display.draw()

        fps_counter.update() # Update the fps_counter
        fps_counter.render() # Render the fps_counter

        pg.display.update()
        clock.tick(FPS) # clock ticks at the specified FPS


        pg.display.flip()

if __name__ == "__main__":
    main()
