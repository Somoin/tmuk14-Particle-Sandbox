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

        
    def draw (self, window): 
        for col in range(self.cols):
            for row in range(self.rows):
                color = (30,30,30)
                if self.cells[col][row] is not None:
                    particle = self.cells[col][row]
                    color = particle.color
                    cs = self.cell_size
                    ds = self.draw_size
                    c1 = (color[0]-10, color[1]-10, color[2]-10)
                    c2 = (color[0]-5, color[1]-5, color[2]-5)
                    c3 = (color[0]-2, color[1]-2, color[2]-2)
                    pg.draw.rect(window, c1, (col * cs, row * cs, ds, ds)) # top left
                    pg.draw.rect(window, c2, (col * cs+ds, row * cs, ds, ds)) # top right
                    pg.draw.rect(window, c3, (col * cs, row * cs+ds, ds, ds)) # bottom left
                    pg.draw.rect(window, color, (col * cs+ds, row * cs+ds, ds, ds)) # bottom right
               
                   
