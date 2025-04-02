import pygame as pg
#from classes.grid import Grid
from classes.button import Button
from simulation import Simulation 

from classes.fps_counter import fps_counter # Import fps_counter class from classes/fps_counter.py

from classes.particles.sandParticle import SandParticle
from enum import Enum

class ParticleType(Enum):
    SAND = 1
    WATER = 2
    CEMENT = 3
    AIR = 4

pg.init()



cell_size = 20
window_width = 1000
window_height = 800
FPS = 120

window = pg.display.set_mode((window_width, window_height))
pg.display.set_caption("Particle Sandbox")

clock = pg.time.Clock()

#grid = Grid(window_width, window_height-300, cell_size)
simulation = Simulation(window_width, window_height-300, cell_size, clock)
fps_counter = fps_counter(window, pg.font.Font(None, 30), clock, (255, 255, 255), (60, 25)) # fps_counter(window, font, clock, color, pos)

sand_button = Button("src/images/sandbutton.png", 100, 550, "src/images/sandbutton_hover.png")
water_button = Button("src/images/waterbutton.png", 300, 550, "src/images/waterbutton_hover.png")
cement_button = Button("src/images/cementbutton.png", 500, 550, "src/images/cementbutton_hover.png")




def main():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                
                mouseX = pg.mouse.get_pos()[0]//cell_size
                mouseY = pg.mouse.get_pos()[1]//cell_size
                
               
                if pg.mouse.get_pressed()[0] == 1: # Left mouse button
                    simulation.add_particle(SandParticle(simulation.grid, mouseX, mouseY), mouseX, mouseY)
                if pg.mouse.get_pressed()[2] == 1: # Right mouse button
                    simulation.remove_particle(mouseX, mouseY)

                if sand_button.check_press(pg.mouse.get_pos()):
                    print("Sand Button Pressed")
                   
                if water_button.check_press(pg.mouse.get_pos()):
                    print("Water Button Pressed")
                   
                if cement_button.check_press(pg.mouse.get_pos()):
                    print("Cement Button Pressed")
                  

        

        window.fill((0, 0, 0))
        sand_button.draw(window)
        water_button.draw(window)
        cement_button.draw(window)

        simulation.draw(window)
       

        #grid.draw(window)
        simulation.update()
        

        fps_counter.update() # Update the fps_counter
        fps_counter.render() # Render the fps_counter


        pg.display.update()
        clock.tick(FPS) # clock ticks at the specified FPS


        pg.display.flip()
        
if __name__ == "__main__":
    main()