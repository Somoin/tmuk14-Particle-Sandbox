import pygame as pg

pg.init()

WINDOW_WIDTH = 1000
WINDOW_HEIGHT = 800
FPS = 120

window = pg.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pg.display.set_caption("Particle Sandbox")

clock = pg.time.Clock()

def main():
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()

        window.fill((0, 0, 0))

        pg.display.update()
        clock.tick(FPS)



if __name__ == "__main__":
    main()