import pygame as pg

class Grid:
    def __init__(self, window_width, window_height, cell_size):
        self.rows = window_height // cell_size
        self.cols = window_width // cell_size
        self.cell_size = cell_size
        self.cells = []
        for _ in range(self.rows):
            for _ in range(self.cols):
                self.cells.append(None)
        
    def draw (self, window):
        for row in range(self.rows):
            for col in range(self.cols):
                pg.draw.rect(window, 'gray', (col * self.cell_size, row * self.cell_size, self.cell_size-1, self.cell_size-1))
