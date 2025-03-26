import pygame as pg
from grid import Grid

pg.init()

cell_size = 20
window_width = 1000
window_height = 800
FPS = 120

window = pg.display.set_mode((window_width, window_height))
pg.display.set_caption("Particle Sandbox")

clock = pg.time.Clock()

grid = Grid(window_width, window_height, cell_size)

def main():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        window.fill((0, 0, 0))
        grid.draw(window)

        pg.display.update()
        clock.tick(FPS)



if __name__ == "__main__":
    main()