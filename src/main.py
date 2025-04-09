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

from enum import Enum

from configparser import ConfigParser



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

cursor_block_width = 10
cursor_block_height = 10

pg.init()



config_object = ConfigParser()


config_object.read("src/config.ini")
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
fps_counter = fps_counter(window, pg.font.Font(None, 30), clock, (255, 255, 255), (60, 25)) # fps_counter(window, font, clock, color, pos)

text_padding_x = 350
text_padding_y = 710 
text_display = TextDisplay(window, "", window_width - text_padding_x, window_height - text_padding_y, (255, 255, 255))



button_width = window_width*0.175
button_height = window_height*0.1125
button_padding_x = 12.3
button_padding_y_r1 = 1.45 # 1.45 for the first row of buttons
button_padding_y_r2 = 1.2 # 1.2 for the second row of buttons

sand_button = Button("src/images/sandbutton.png", window_width // button_padding_x, window_height // button_padding_y_r1, "src/images/sandbutton_hover.png", button_width, button_height)
water_button = Button("src/images/waterbutton.png", window_width // button_padding_x * 3.45, window_height // button_padding_y_r1, "src/images/waterbutton_hover.png", button_width, button_height)
concrete_button = Button("src/images/concretebutton.png", window_width // button_padding_x * 5.9, window_height // button_padding_y_r1, "src/images/concretebutton_hover.png", button_width, button_height)
fire_button = Button("src/images/firebutton.png", window_width // button_padding_x * 8.35, window_height // button_padding_y_r1, "src/images/firebutton_hover.png", button_width, button_height)
wood_button = Button("src/images/woodbutton.png", window_width // button_padding_x * 10.8, window_height // button_padding_y_r1,"src/images/woodbutton_hover.png", button_width, button_height)
gunpowder_button = Button("src/images/gunpowderbutton.png", window_width // button_padding_x, window_height // button_padding_y_r2, "src/images/gunpowderbutton_hover.png", button_width, button_height)

def particle_input(particle_type, cursor_type, grid, mouseX, mouseY):
    if particle_type == ParticleType.SAND:
        simulation.add_particle(SandParticle(simulation.grid, mouseX, mouseY), mouseX, mouseY)
    elif particle_type == ParticleType.WATER:
        simulation.add_particle(WaterParticle(simulation.grid, mouseX, mouseY, lifetime=250), mouseX, mouseY)
    elif particle_type == ParticleType.CONCRETE:
        simulation.add_particle(ConcreteParticle(simulation.grid, mouseX, mouseY), mouseX, mouseY)
    elif particle_type == ParticleType.SMOKE:
        simulation.add_particle(SmokeParticle(simulation.grid, mouseX, mouseY, lifetime=100), mouseX, mouseY)
    elif particle_type == ParticleType.WOOD:
        simulation.add_particle(WoodParticle(simulation.grid, mouseX, mouseY), mouseX, mouseY)
    elif particle_type == ParticleType.FIRE:
        simulation.add_particle(FireParticle(simulation.grid, mouseX, mouseY, lifetime=100, potency=2), mouseX, mouseY)
    elif particle_type == ParticleType.GUNPOWDER:
        simulation.add_particle(GunpowderParticle(simulation.grid, mouseX, mouseY), mouseX, mouseY)


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
                
            #print(particle_type.name)
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
                     
                
        mouseX = pg.mouse.get_pos()[0]//cell_size
        mouseY = pg.mouse.get_pos()[1]//cell_size

        # Particle spawning / removing on mousedown
        if left_click_down == True: # Registers when held down 
            if cursor_type == CursorMode.DEFAULT:
                particle_input(particle_type, cursor_type, simulation.grid, mouseX, mouseY)
                

            if cursor_type == CursorMode.BLOCK:
                for i in range(cursor_block_width):
                    for j in range(cursor_block_height):
                        mouseX = pg.mouse.get_pos()[0]//cell_size - cursor_block_height//2 + i
                        mouseY = pg.mouse.get_pos()[1]//cell_size - cursor_block_width//2 + j
                        particle_input(particle_type, cursor_type, simulation.grid, mouseX, mouseY)
            
        elif right_click_down == True: # Right mouse button
            if cursor_type == CursorMode.DEFAULT:
                simulation.remove_particle(mouseX, mouseY)
            elif cursor_type == CursorMode.BLOCK: 
                for i in range(cursor_block_width):
                    for j in range(cursor_block_height):
                        mouseX = pg.mouse.get_pos()[0]//cell_size - cursor_block_height//2 + i
                        mouseY = pg.mouse.get_pos()[1]//cell_size - cursor_block_width//2 + j
                        simulation.remove_particle(mouseX, mouseY)

                

              

        

        window.fill((0, 0, 0))
        sand_button.draw(window)
        water_button.draw(window)
        concrete_button.draw(window)
        fire_button.draw(window)
        wood_button.draw(window)
        gunpowder_button.draw(window)

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