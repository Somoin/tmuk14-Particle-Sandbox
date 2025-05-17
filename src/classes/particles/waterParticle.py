from src.particle import Particle
import random as rd

colors = [
    #(15,94,156),
    (35,137,218),
    (28,163,236),
    #(90,188,216),
    #(116,204,244)
]


class WaterParticle(Particle):
    def __init__(self, grid, x, y, lifetime):
        super().__init__("water", rd.choice(colors), grid, x ,y)
        self.liquid = True
        self.direction = 0
        self.lifetime = lifetime
        self.velocity = 3
        if rd.choice([True, False]):
            self.direction = 0 #left
        else:
            self.direction = 1 #right
          

    def update(self, grid, x, y):

        if self.lifetime <= 0:
            return (-1,-1) # Particle dies


        if (x != grid.cols-1) and grid.cells[x+1][y] is not None:
            self.direction = 0 #left
        elif (x != 0) and grid.cells[x-1][y] is not None:
            self.direction = 1 #right

        if rd.randint(0, 100) <= 5:
            self.color = rd.choice(colors) # Randomly change color every frame

        if grid.cells[x][y-1] is not None and y != 0:
            if (grid.cells[x][y-1].name in ('sand', 'gunpowder')):
                tmp = grid.cells[x][y-1]
                grid.cells[x][y-1] = WaterParticle(grid, x, y-1, self.lifetime)
                grid.cells[x][y] = tmp
                return (x,y-1)

        if y == grid.rows-1: # out of bounds bottom
            return (x,y)

        # Gravity 
        down = moveDown(grid, x, y, self.gravity)
        if down != (x,y):
            return down
        
        downleft = moveDownLeft(grid, x, y, self.velocity)
        if downleft != (x,y):
            return downleft
    
        downright = moveDownRight(grid, x, y, self.velocity)
        if downright != (x,y):
            return downright


        # Move left
        left = moveLeft(grid, x, y, self.direction, self.velocity)
        if left != (x,y):
            self.lifetime -= 1
            return left
        
        # Move right
        right = moveRight(grid, x, y, self.direction, self.velocity)
        if right != (x,y):
            self.lifetime -= 1
            return right

        return (x,y) # Stay in place if no movement is possible


def moveLeft(grid, x, y, direction, velocity):
    startPos = (x,y)
    currPos = startPos
    for i in range(velocity):
        if x-i == 0:
            return currPos
        if (x != 0) and grid.cells[x-1-i][y] is None and direction == 0:
            currPos = (x-i-1,y)
        else:
            return currPos
    
    if startPos != currPos:
        return currPos
    else:
        return (x,y)

def moveRight(grid, x, y, direction, velocity):
    startPos = (x,y)
    currPos = startPos
    for i in range(velocity):
        if x+i == grid.cols-1:
            return currPos
        if (x != grid.cols-1) and grid.cells[x+1+i][y] is None and direction == 1:
            return(x+i+1,y)
        else:
            return currPos
    
    if startPos != currPos:
        return currPos
    else:
        return (x,y)

def moveDown(grid, x, y, gravity):
    startPos = (x,y)
    currPos = startPos
    for i in range(gravity):
        if y+i+1 == grid.rows:
            return currPos
        elif grid.cells[x][y+1+i] is None: # move down
            currPos = (x,y+1+i) 
        else:
            return currPos 
            
    if currPos != startPos:
        return currPos
    else:
        return (x,y)
    
def moveDownLeft(grid, x, y, gravity):
    startPos = (x,y)
    currPos = startPos
    for i in range(gravity):
        if x-i == 0 or y+i+1 == grid.rows-1:
            return currPos
        elif (x != 0) and grid.cells[x-1-i][y+1+i] is None: # move down left
            currPos =  (x-1-i,y+1+i)
        else:
            return currPos 
            
    if currPos != startPos:
        return currPos
    else:
        return (x,y)
    
def moveDownRight(grid, x, y, gravity):
    startPos = (x,y)
    currPos = startPos
    for i in range(gravity):
        if x+i == grid.cols-1 or y+i+1 == grid.rows-1:
            return currPos
        elif (x != grid.cols-1) and grid.cells[x+1+i][y+1+i] is None: # move down right
            return (x+1+i,y+1+i)
        else:
            return currPos 
            
    if currPos != startPos:
        return currPos
    else:
        return (x,y)