from src.classes.grid import Grid


class Simulation:
    def __init__(self, window_width, window_height, cell_size):
        self.grid = Grid(window_width, window_height, cell_size)
        self.rows = self.grid.rows
        self.cols = self.grid.cols
        self.cells = self.grid.cells
        self.next_cells = Grid(window_width, window_height, cell_size) # Create a new grid for the next cells

    def draw(self, window):
        self.grid.draw(window)

    def add_particle(self, particle, x, y):
        if 0 <= x and x < self.cols and 0 <= y and y < self.rows and self.cells[x][y] is None:
            self.cells[x][y] = particle

    def remove_particle(self, x, y):
        if 0 <= x < self.cols and 0 <= y < self.rows:
            self.cells[x][y] = None
    
    def clear(self):
        for col in range(self.cols):
            for row in range(self.rows):
                self.cells[col][row] = None

    def update(self):
        update_array = [] # Create an array to store the particles that need to be updated

        for col in range(self.cols):
            for row in range(self.rows):
                particle = self.cells[col][row]
                if particle is None:
                    continue
                else:
                    if particle.static == True: # Only update non-static particles
                        self.next_cells.cells[col][row] = particle # Keep the original position
                        continue

                    pos = particle.update(self.grid, col, row)


                    if pos == (-1, -1): # Particle dies
                        self.next_cells.cells[col][row] = None
                    else:
                        if self.next_cells.cells[pos[0]][pos[1]] is None:
                            self.next_cells.cells[pos[0]][pos[1]] = particle
                        else:
                            self.next_cells.cells[col][row] = particle # Keep the original position if the new one is occupied
                    
                

        
        for col in range(self.cols):
            for row in range(self.rows):
                if self.next_cells.cells[col][row] is None:
                    self.remove_particle(col, row)
                else:
                    self.add_particle(self.next_cells.cells[col][row], col, row)
                    self.next_cells.cells[col][row] = None # Reset the next cells grid
        
        
        
  
