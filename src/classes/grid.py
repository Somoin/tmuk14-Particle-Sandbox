import pygame as pg

class Grid:
    def __init__(self, window_width, window_height, cell_size):
        self.rows = window_height // cell_size
        self.cols = window_width // cell_size
        self.cell_size = cell_size
        self.cells = []
        for _ in range(self.rows):
            row = []
            for _ in range(self.cols):
                row.append(None)
            self.cells.append(row)

        
    def draw (self, window): 
        for row in range(self.rows):
            for col in range(self.cols):
                color = 'gray'
                if self.cells[row][col] is not None:
                    particle = self.cells[row][col]
                    color = particle.color
                pg.draw.rect(window, color, (col * self.cell_size, row * self.cell_size, self.cell_size-1, self.cell_size-1))
