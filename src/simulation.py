from src.classes.grid import Grid
import pygame as pg # Remove after testing

class Chunk:
    def __init__(self, x, y, size, cell_size, window_width, window_height):
        self.x = x
        self.y = y
        self.size = size
        self.cell_size = cell_size
        self.cols = size // cell_size
        self.rows = size // cell_size
        self.cells = [] # List of cells in the chunk
        self.next_cells = Grid(window_width, window_height, cell_size)

        for _ in range(self.cols):
            cols = []
            for _ in range(self.rows):
                cols.append(None)
            self.cells.append(cols)
        
        

    def draw(self, window):
        for col in range(self.cols):
            for row in range(self.rows):
                color = (0,0,255,0.5)
                pg.draw.rect(window, color, (col * self.cell_size + self.x, row * self.cell_size + self.y, self.cell_size, self.cell_size), 1)
        pg.draw.rect(window, (255,0,0), (self.x, self.y, self.size, self.size), 1)
    

class Simulation:
    def __init__(self, window_width, window_height, cell_size):
        self.grid = Grid(window_width, window_height, cell_size)
        self.rows = self.grid.rows
        self.cols = self.grid.cols
        self.cells = self.grid.cells
        self.next_cells = Grid(window_width, window_height, cell_size) # Create a new grid for the next cells

        self.chunk_size = 64
        

        self.chunks = [] # List of chunks in the simulation
        self.chunk_cols = window_width // self.chunk_size
        self.chunk_rows = window_height // self.chunk_size
        self.chunk_self_cols = self.chunk_size // cell_size
        self.chunk_self_rows = self.chunk_size // cell_size

        for col in range(self.chunk_cols):
            row_chunks = []
            for row in range(self.chunk_rows):

                chunk = Chunk(col * self.chunk_size, row * self.chunk_size, self.chunk_size, cell_size, window_width, window_height)
                row_chunks.append(chunk)
            self.chunks.append(row_chunks)
        
        print(self.cols)
        print(self.rows)

        print(window_height, window_height % self.chunk_size)
        while window_width % self.chunk_size != 0:
            window_width += 1
        print("Recommendend width: " + str(window_height))
        assert window_width % self.chunk_size == 0, "Chunk size must divide grid width evenly"
        while window_height % self.chunk_size != 0:
            window_height += 1
        print("Recommendend height: " + str(window_height))
        assert window_height % self.chunk_size == 0, "Chunk size must divide grid height evenly"

    


    def draw(self, window):
        for col in range(self.chunk_cols):
            for row in range(self.chunk_rows):
                chunk = self.chunks[col][row] 
                chunk.draw(window)
        self.grid.draw(window)

    def add_particle(self, particle, x, y):
        if 0 <= x and x < self.cols and 0 <= y and y < self.rows and self.cells[x][y] is None:
            #self.cells[x][y] = particle
            print("selected chunk = " + str(x // self.chunk_self_cols) + " " +  str(y // self.chunk_self_rows))
            print("absolute = " + str(x) + " " + str(y))
            print("relative = " + str(x % self.chunk_self_cols) + " " + str(y % self.chunk_self_rows))
            print("reverted = " + str(x * self.chunk_self_cols + x % self.chunk_self_cols) + " " + str(y * self.chunk_self_rows + y % self.chunk_self_rows))
            selected_x = x // self.chunk_self_cols
            selected_y = y // self.chunk_self_rows
            rel_x = x % self.chunk_self_cols
            rel_y = y % self.chunk_self_rows
            self.chunks[selected_x][selected_y].cells[rel_x][rel_y] = particle
            
            

    def remove_particle(self, x, y):
        if 0 <= x < self.cols and 0 <= y < self.rows:
            #self.cells[x][y] = None
            selected_x = x // self.chunk_self_cols
            selected_y = y // self.chunk_self_rows
            rel_x = x % self.chunk_self_cols
            rel_y = y % self.chunk_self_rows
            self.chunks[selected_x][selected_y].cells[rel_x][rel_y] = None
    
    def clear(self):
        for col in range(self.cols):
            for row in range(self.rows):
                self.cells[col][row] = None

    def update_chunk(self, chunk):
        for col in range(chunk.cols):
            for row in range(chunk.rows):
                particle = chunk.cells[col][row]
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

    def update(self):
        update_array = [] # Create an array to store the particles that need to be updated

        for col in range(self.chunk_cols):
            for row in range(self.chunk_rows):
                self.update_chunk(self.chunks[col][row])
                    
                
        
        
        for col in range(self.cols):
            for row in range(self.rows):
                if self.next_cells.cells[col][row] is None:
                    self.remove_particle(col, row)
                else:
                    self.add_particle(self.next_cells.cells[col][row], col, row)
                    self.next_cells.cells[col][row] = None # Reset the next cells grid
        
        
        
  
