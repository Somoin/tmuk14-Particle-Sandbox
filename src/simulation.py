from src.classes.grid import Grid


class Simulation:
    def __init__(self, window_width, window_height, cell_size):
        self.grid = Grid(window_width, window_height, cell_size)
        self.rows = self.grid.rows
        self.cols = self.grid.cols
        self.cells = self.grid.cells
        self.next_cells = Grid(window_width, window_height, cell_size) # Create a new grid for the next cells
        self.active_particles = set() # Create a set to store the active particles

    def draw(self, window):
        self.grid.draw(window)

    def add_particle(self, particle, x, y):
        if 0 <= x and x < self.cols and 0 <= y and y < self.rows and self.cells[x][y] is None:
            self.cells[x][y] = particle
            if not particle.static:
                self.active_particles.add((x,y))

    def remove_particle(self, x, y):
        if 0 <= x < self.cols and 0 <= y < self.rows:
            self.active_particles.discard((x,y))
            self.cells[x][y] = None
    
    def clear(self):
        for col in range(self.cols):
            for row in range(self.rows):
                self.cells[col][row] = None
        self.active_particles.clear()


    def update(self):
        new_active_particles = set()
        
        for x, y in self.active_particles:
            particle = self.cells[x][y]

            if particle is None or particle.static:
                continue

            
            pos = particle.update(self.grid, x, y)

            if pos == (-1, -1):
                self.cells[x][y] = None
                continue

            # Move particle if target cell is empty
            if self.cells[pos[0]][pos[1]] is None:
                self.cells[pos[0]][pos[1]] = particle
                self.cells[x][y] = None
                new_active_particles.add((pos[0], pos[1]))
            else:
                # If target cell is occupied, keep the original position
                new_active_particles.add((x, y))

            for dx in [-1, 0, 1]:
                for dy in [-1, 0, 1]:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < self.cols and 0 <= ny < self.rows:
                        neighbor = self.cells[nx][ny]
                        if neighbor is not None and not neighbor.static:
                            new_active_particles.add((nx, ny))

        self.active_particles = new_active_particles


    def update2(self):

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
                    if pos != (col, row):
                        self.active_particles.add(particle) # Add the particle to the update array

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
        
        
        
  
