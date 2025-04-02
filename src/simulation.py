from classes.grid import Grid

class Simulation:
    def __init__(self, window_width, window_height, cell_size):
        self.grid = Grid(window_width, window_height, cell_size)
        self.rows = self.grid.rows
        self.cols = self.grid.cols
        self.cells = self.grid.cells

    def draw(self, window):
        self.grid.draw(window)

    def add_particle(self, particle, x, y):
        if 0 <= x < self.cols and 0 <= y < self.rows and self.cells[x][y] is None:
            self.cells[x][y] = particle

    def remove_particle(self, x, y):
        if 0 <= x < self.cols and 0 <= y < self.rows:
            self.cells[x][y] = None

    def update(self):
        for row in range(self.rows):
            for col in range(self.cols):
                particle = self.cells[row][col]
                if particle is not None:
                    particle.update()