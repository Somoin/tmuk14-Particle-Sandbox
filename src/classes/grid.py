import pygame as pg

class Grid:
    def __init__(self, x, y, chunk_size, window_width, window_height, cell_size):
        self.x = x
        self.y = y
        self.chunk_size = chunk_size
        self.rows = window_height // cell_size
        self.cols = window_width // cell_size
        self.cell_size = cell_size
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
                    pg.draw.rect(window, color, (self.x + col * self.cell_size, self.y + row * self.cell_size, self.cell_size, self.cell_size))
