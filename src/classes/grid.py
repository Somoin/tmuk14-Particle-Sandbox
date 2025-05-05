import pygame as pg
import random

class Grid:
    def __init__(self, window_width, window_height, cell_size):
        self.rows = window_height // cell_size
        self.cols = window_width // cell_size
        self.cell_size = cell_size
        self.draw_size = cell_size // 2
        self.cells = []
        for _ in range(self.cols):
            cols = []
            for _ in range(self.rows):
                cols.append(None)
            self.cells.append(cols)

    def calculate_color(self, color, addition = 10):
        r = color[0] + addition
        g = color[1] + addition
        b = color[2] + addition

        if r < 0: r = 0
        if g < 0: g = 0
        if b < 0: b = 0
        if r > 255: r = 255
        if g > 255: g = 255
        if b > 255: b = 255
        return (r, g, b)
        
    def draw (self, window): 
        for col in range(self.cols):
            for row in range(self.rows):
                color = (30,30,30)
                if self.cells[col][row] is not None:
                    particle = self.cells[col][row]
                    color = particle.color
                    cs = self.cell_size
                    ds = self.draw_size

                    c1 = particle.colors[particle.colorOrder[0]]
                    c2 = particle.colors[particle.colorOrder[1]]
                    c3 = particle.colors[particle.colorOrder[2]]
                   
                    pg.draw.rect(window, c1, (col * cs, row * cs, ds, ds)) # top left
                    pg.draw.rect(window, c2, (col * cs+ds, row * cs, ds, ds)) # top right
                    pg.draw.rect(window, c3, (col * cs, row * cs+ds, ds, ds)) # bottom left
                    pg.draw.rect(window, color, (col * cs+ds, row * cs+ds, ds, ds)) # bottom right
               
                   
