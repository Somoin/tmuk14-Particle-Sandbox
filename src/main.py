import pygame as pg
from classes.grid import Grid
from classes.fps_counter import fps_counter # Import fps_counter class from classes/fps_counter.py

from classes.particles.particle import SandParticle

pg.init()

cell_size = 20
window_width = 1000
window_height = 800
FPS = 120

window = pg.display.set_mode((window_width, window_height))
pg.display.set_caption("Particle Sandbox")

clock = pg.time.Clock()

grid = Grid(window_width, window_height, cell_size)


# Temp
grid.cells[0][0] = SandParticle()

fps_counter = fps_counter(window, pg.font.Font(None, 30), clock, (255, 255, 255), (60, 25)) # fps_counter(window, font, clock, color, pos)

def main():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        window.fill((0, 0, 0))
        grid.draw(window)


        fps_counter.update() # Update the fps_counter
        fps_counter.render() # Render the fps_counter


        pg.display.update()
        clock.tick(FPS) # clock ticks at the specified FPS

        



if __name__ == "__main__":
    main()