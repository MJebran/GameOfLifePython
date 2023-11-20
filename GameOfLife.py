import numpy as np

cells = [[2,0],[2,1],[2,2]]



def Get_living_Cells(cells, numRows, numCol):
    life_grid = np.zeros((numRows, numCol), dtype=int)
    for x in cells:
        life_grid[x[0],x[1]] = 1

    return life_grid
 

print(Get_living_Cells(cells,4,3))
# Write a python function that accepts a numpy array representing the current board and 
# returns a numpy representing the next generation of living cells (assume that cells out of bounds of the board immediately die).  
# (Don't use any loops here!)

def GetNextGeneration(cells):
    result = (
        cells[0:cells.shape[0]-1, 0:cells.shape[1]-1] +
        cells[0:cells.shape[0], 0:cells.shape[1]-1] +
        cells[0:cells.shape[0]-1, 0:cells.shape[1]-1]
    )
    return result

GetNextGeneration(Get_living_Cells(cells, 4,3))

