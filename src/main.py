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

from enum import Enum

class ParticleType(Enum):
    SAND = 1
    WATER = 2
    CONCRETE = 3
    AIR = 4
    SMOKE = 5
    WOOD = 6 
    FIRE = 7
    GUNPOWDER = 8
    #default = AIR

class CursorMode(Enum):
    DEFAULT = 1
    BLOCK = 2

cursor_block_width = 10
cursor_block_height = 10


pg.init()


cell_size = 8
window_width = 1000
window_height = 800
FPS = 120

window = pg.display.set_mode((window_width, window_height))
pg.display.set_caption("Particle Sandbox")

clock = pg.time.Clock()

simulation = Simulation(window_width, window_height-300, cell_size)
fps_counter = fps_counter(window, pg.font.Font(None, 30), clock, (255, 255, 255), (60, 25)) # fps_counter(window, font, clock, color, pos)

sand_button = Button("src/images/sandbutton.png", 100, 550, "src/images/sandbutton_hover.png")
water_button = Button("src/images/waterbutton.png", 300, 550, "src/images/waterbutton_hover.png")
concrete_button = Button("src/images/concretebutton.png", 500, 550, "src/images/concretebutton_hover.png")
fire_button = Button("src/images/firebutton.png", 700, 550, "src/images/firebutton_hover.png")
wood_button = Button("src/images/woodbutton.png", 900, 550, "src/images/woodbutton_hover.png")
gunpowder_button = Button("src/images/gunpowderbutton.png", 100, 650, "src/images/gunpowderbutton_hover.png")


text_pos_x = 650
text_pos_y = 15
def display_current_particle(display_text, pos_x, pos_y):
    text = pg.font.Font(None, 30).render("Current Particle: " + display_text, True, (255, 255, 255))
    text_rect = text.get_rect(topleft=(pos_x, pos_y))
    window.blit(text, text_rect)


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
                print(particle_type.name)


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

                display_current_particle(particle_type.name, text_pos_x, text_pos_y)
             
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
        

        fps_counter.update() # Update the fps_counter
        fps_counter.render() # Render the fps_counter

        display_current_particle(particle_type.name, text_pos_x, text_pos_y)
        pg.display.update()
        clock.tick(FPS) # clock ticks at the specified FPS


        pg.display.flip()
        
if __name__ == "__main__":
    main()