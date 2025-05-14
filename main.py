from enum import Enum
from configparser import ConfigParser
import pygame as pg
from src.classes.button import Button
from src.simulation import Simulation

from src.classes.fps_counter import fps_counter # Import fps_counter class from classes/fps_counter.py
from src.classes.particles.sandParticle import SandParticle
from src.classes.particles.waterParticle import WaterParticle
from src.classes.particles.concreteParticle import ConcreteParticle
from src.classes.particles.smokeParticle import SmokeParticle
from src.classes.particles.woodParticle import WoodParticle
from src.classes.particles.fireParticle import FireParticle
from src.classes.particles.gunpowderParticle import GunpowderParticle
from src.classes.particles.virusParticle import VirusParticle
from src.classes.text_display import TextDisplay
from src.effects import Effects
from src.classes.animation import Animation




class ParticleType(Enum): # Enum for particle types
    SAND = 1
    WATER = 2
    CONCRETE = 3
    AIR = 4
    SMOKE = 5
    WOOD = 6
    FIRE = 7
    GUNPOWDER = 8
    GAS = 9
    VIRUS = 10
    #default = AIR

class CursorMode(Enum): # Enum for cursor modes
    DEFAULT = 1
    BLOCK = 2

CURSOR_BLOCK_WIDTH = 10 # Width and height of the cursor block
CURSOR_BLOCK_HEIGHT = 10

pg.init()

config_object = ConfigParser()

if len(config_object.read("config.ini")) > 0: # Reads the config file if it exists
    cell_size = config_object.getint("CONFIG", "cell_size")
    window_width = config_object.getint("CONFIG", "window_width")
    window_height = config_object.getint("CONFIG", "window_height")
    FPS = config_object.getint("CONFIG", "FPS")
else: # Creates a new config file if it doesn't exist
    config_object["CONFIG"] = { 
        "cell_size": 8,
        "window_width": 1280,
        "window_height": 800,
        "FPS": 120
    }

    with open("config.ini", "w") as config_file: # Writes the config file
        config_object.write(config_file)

    config_object.read("config.ini")
    cell_size = config_object.getint("CONFIG", "cell_size")
    window_width = config_object.getint("CONFIG", "window_width")
    window_height = config_object.getint("CONFIG", "window_height")
    FPS = config_object.getint("CONFIG", "FPS")



window = pg.display.set_mode((window_width, window_height)) # Main window
pg.display.set_caption("Particle Sandbox")

clock = pg.time.Clock()

simulation_width = window_width # Width and height for the simulation
simulation_height = round(window_height - (window_height*0.375))
simulation = Simulation(simulation_width, simulation_height, cell_size)
effects = Effects(simulation)
fps_counter = fps_counter(window, pg.font.Font(None, 30), clock, (255, 255, 255), (60, 25))

text_display = TextDisplay(window, "", 930, 15, (255, 255, 255))

button_width = window_width*0.175
button_height = window_height*0.1125

sand_button = Button("src/images/sandbutton.png", 120, 550, "src/images/sandbutton_hover.png", button_width, button_height, True)
water_button = Button("src/images/waterbutton.png", 370, 550, "src/images/waterbutton_hover.png", button_width, button_height, True)
concrete_button = Button("src/images/concretebutton.png", 620, 550, "src/images/concretebutton_hover.png", button_width, button_height, True)
fire_button = Button("src/images/firebutton.png", 870, 550, "src/images/firebutton_hover.png", button_width, button_height, True)
wood_button = Button("src/images/woodbutton.png", 1120, 550,"src/images/woodbutton_hover.png", button_width, button_height, True)
gunpowder_button = Button("src/images/gunpowderbutton.png", 120, 675, "src/images/gunpowderbutton_hover.png", button_width, button_height, True)
virus_button = Button("src/images/virusbutton.png", 370, 675, "src/images/virusbutton_hover.png", button_width, button_height, True)
eyeofrah_button = Button("src/images/eyeofrahbutton.png", 120, 550, "src/images/eyeofrahbutton_hover.png", button_width, button_height, False)
ignite_button = Button("src/images/ignitebutton.png", 370, 550, "src/images/ignitebutton_hover.png", button_width, button_height, False)
cellsize_button = Button("src/images/cellsizebutton.png", 120, 550, "src/images/cellsizebutton_hover.png", button_width, button_height, False)
gravity_button = Button("src/images/gravitybutton.png", 370, 550, "src/images/gravitybutton_hover.png", button_width, button_height, False)

page_1_buttons = [sand_button, water_button, concrete_button, fire_button, wood_button, gunpowder_button, virus_button]
page_2_buttons = [eyeofrah_button, ignite_button]
page_3_buttons = [cellsize_button, gravity_button]


eye_of_rah_sheet = Animation("src/images/eyeofrah-Sheet.png", 4, 500) # Create an instance of the Animation class
for i in range(eye_of_rah_sheet.no_frames): # Create a list of animation frames
    eye_of_rah_sheet.frame_list.append(eye_of_rah_sheet.get_frame(i, 80, 80, 5, 5, (0, 0, 0)))

ignite_sheet = Animation("src/images/ignite-Sheet.png", 5, 500) # Create an instance of the Animation class
for i in range(ignite_sheet.no_frames): # Create a list of animation frames
    ignite_sheet.frame_list.append(ignite_sheet.get_frame(i, 80, 80, 2, 2, (0, 0, 0)))

def particle_input(particle_type, mouse_x, mouse_y): # Adds particle to the simulation based on mouse coordinates

    if particle_type == ParticleType.SAND:
        particle = SandParticle(simulation.grid, mouse_x, mouse_y)
        simulation.add_particle(particle, mouse_x, mouse_y)
    elif particle_type == ParticleType.WATER:
        particle = WaterParticle(simulation.grid, mouse_x, mouse_y, lifetime=100)
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
        if mouse_x < 0 or mouse_x > simulation.grid.cols-1 or mouse_y < 0 or mouse_y > simulation.grid.rows-1:
            return

        if simulation.grid.cells[mouse_x][mouse_y] is not None:
            if simulation.grid.cells[mouse_x][mouse_y].flammable == True:
                simulation.remove_particle(mouse_x, mouse_y)
        
        simulation.add_particle(particle, mouse_x, mouse_y)

    elif particle_type == ParticleType.GUNPOWDER:
        particle = GunpowderParticle(simulation.grid, mouse_x, mouse_y)
        simulation.add_particle(particle, mouse_x, mouse_y)

    elif particle_type == ParticleType.VIRUS:
        particle = VirusParticle(simulation.grid, mouse_x, mouse_y, lifetime=100, standard_lifetime=100)
        simulation.add_particle(particle, mouse_x, mouse_y)


def main(): 

    # Animation variables
    last_update = pg.time.get_ticks()
    current_frame = 0
    
    eye_of_rah_active = False
    ignis_active = False

    current_page = 1

    particle_type = ParticleType.AIR
    cursor_type = CursorMode.DEFAULT

    left_click_down = False
    right_click_down = False

    while True: # Game loop
        for event in pg.event.get(): # Event handling
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

                        # Debug Keyboard input
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_1:
                    current_page = 1
                    for button in page_1_buttons:
                        button.enabled = True
                    for button in page_2_buttons:
                        button.enabled = False
                    for button in page_3_buttons:
                        button.enabled = False
                if event.key == pg.K_2:
                    current_page = 2
                    for button in page_1_buttons:
                        button.enabled = False
                    for button in page_2_buttons:
                        button.enabled = True
                    for button in page_3_buttons:
                        button.enabled = False
                if event.key == pg.K_3:
                    current_page = 3
                    for button in page_1_buttons:
                        button.enabled = False
                    for button in page_2_buttons:
                        button.enabled = False
                    for button in page_3_buttons:
                        button.enabled = True
                if event.key == pg.K_c:
                    simulation.clear()

                # Changing cursor type
                if event.key == pg.K_q:
                    if cursor_type == CursorMode.DEFAULT:
                        cursor_type = CursorMode.BLOCK
                    else:
                        cursor_type = CursorMode.DEFAULT

            if event.type == pg.MOUSEBUTTONDOWN: #Registers when clicked once
                if sand_button.check_mouse(pg.mouse.get_pos()):
                    particle_type = ParticleType.SAND
                if water_button.check_mouse(pg.mouse.get_pos()):
                    particle_type = ParticleType.WATER
                if concrete_button.check_mouse(pg.mouse.get_pos()):
                    particle_type = ParticleType.CONCRETE
                if fire_button.check_mouse(pg.mouse.get_pos()):
                    particle_type = ParticleType.FIRE
                if wood_button.check_mouse(pg.mouse.get_pos()):
                    particle_type = ParticleType.WOOD
                if gunpowder_button.check_mouse(pg.mouse.get_pos()):
                    particle_type = ParticleType.GUNPOWDER
                if virus_button.check_mouse(pg.mouse.get_pos()):
                    particle_type = ParticleType.VIRUS
                if eyeofrah_button.check_mouse(pg.mouse.get_pos()):
                    eye_of_rah_active = True
                    last_update = pg.time.get_ticks()
                    effects.eye_of_rah()
                if ignite_button.check_mouse(pg.mouse.get_pos()):
                    ignis_active = True
                    effects.ignis()
                if cellsize_button.check_mouse(pg.mouse.get_pos()):
                    print("Cell size")
                if gravity_button.check_mouse(pg.mouse.get_pos()):
                    print("Gravity")
                    

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

        #Draw and update
        window.fill((0, 0, 0))

        if current_page == 1:
            for button in page_1_buttons:
                button.draw(window)
        elif current_page == 2:
            for button in page_2_buttons:
                button.draw(window)
        elif current_page == 3:
            for button in page_3_buttons:
                button.draw(window)


        simulation.draw(window)
        simulation.update()

        text_display.text = "CURRENT PARTICLE: " + particle_type.name
        text_display.draw()

        fps_counter.update() # Update the fps_counter
        fps_counter.render() # Render the fps_counter

        # Draw the Eye of Rah animation
        if eye_of_rah_active == True:
            window.blit(eye_of_rah_sheet.frame_list[current_frame], (400, 80)) # Draw the current frame of the animation
            if pg.time.get_ticks() - last_update >= eye_of_rah_sheet.cooldown:
                current_frame += 1 
                last_update = pg.time.get_ticks()  
                if current_frame >= len(eye_of_rah_sheet.frame_list):
                    eye_of_rah_active = False # Stops the animation after one cycle
                    current_frame = 0
                    
        # Draw the ignite animation
        if ignis_active == True:
            window.blit(ignite_sheet.frame_list[current_frame], (580, 80)) # Draw the current frame of the animation
            if pg.time.get_ticks() - last_update >= ignite_sheet.cooldown:
                current_frame += 1 
                last_update = pg.time.get_ticks()  
                if current_frame >= len(ignite_sheet.frame_list):
                    ignis_active = False
                    current_frame = 0
            
        pg.display.update()
        clock.tick(FPS) # clock ticks at the specified FPS

        pg.display.flip()

if __name__ == "__main__":
    main()
