import pygame as pg
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

from classes.fps_counter import fps_counter # Import fps_counter class from classes/fps_counter.py

pg.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800
FPS = 120

window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Particle Sandbox")

clock = pg.time.Clock()

fps_counter = fps_counter(window, pg.font.Font(None, 30), clock, (255, 255, 255), (60, 25)) # fps_counter(window, font, clock, color, pos)

def main():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        window.fill((0, 0, 0))


        fps_counter.update() # Update the fps_counter
        fps_counter.render() # Render the fps_counter


        pg.display.update()
        clock.tick(FPS) # clock ticks at the specified FPS

        



if __name__ == "__main__":
    main()