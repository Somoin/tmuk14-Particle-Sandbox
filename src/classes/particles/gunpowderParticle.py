from particle import Particle
import random as rd

colors = [
    (62,45,45),
    (101,87,87),
    (120,110,115)
]


class GunpowderParticle(Particle):
    def __init__(self, grid, x, y):
        super().__init__("gunpowder", rd.choice(colors), grid, x ,y)
        self.flammable = True
        self.flammability = 5 # Multiplier of flammability
    
    def update(self, grid, x, y):
        if y == self.grid.rows-1: # out of bounds bottom
            return (x,y)
        
        # Gravity 
        down = moveDown(grid, x, y, self.gravity)
        if down != (x,y):
            return down
                
        downLeft = moveDownLeft(grid, x, y, self.gravity)
        if downLeft != (x,y):   
            return downLeft
        
        downRight = moveDownRight(grid, x, y, self.gravity)
        if downRight != (x,y):   
            return downRight
       
        return (x,y)
        
def moveDown(grid, x, y, gravity):
    startPos = (x,y)
    currPos = startPos
    for i in range(gravity):
        if y+i+1 == grid.rows:
            return currPos
        if grid.cells[x][y+1+i] is None: # move down
            currPos = (x,y+1+i) 
            
    if currPos != startPos:
        return currPos
    else:
        return (x,y)
    
def moveDownLeft(grid, x, y, gravity):
    startPos = (x,y)
    currPos = startPos
    for i in range(gravity):
        if x-i-1 == 0 or y+i+1 == grid.rows-1:
            return currPos
        if (x != 0) and grid.cells[x-1-i][y+1+i] is None: # move down left
            currPos =  (x-1-i,y+1+i)
            
    if currPos != startPos:
        return currPos
    else:
        return (x,y)
    
def moveDownRight(grid, x, y, gravity):
    startPos = (x,y)
    currPos = startPos
    for i in range(gravity):
        if x+i+1 == grid.cols-1 or y+i+1 == grid.rows-1:
            return currPos
        if (x != grid.cols-1) and grid.cells[x+1+i][y+1+i] is None: # move down right
            return (x+1+i,y+1+i)
            
    if currPos != startPos:
        return currPos
    else:
        return (x,y)