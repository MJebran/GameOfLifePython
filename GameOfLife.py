import numpy as np

cells = [[2,0],[2,1],[2,2]]



def Get_living_Cells(cells, numRows, numCol):
    life_grid = np.zeros((numRows, numCol), dtype=int)
    for x in cells:
        life_grid[x[0],x[1]] = 1

    return life_grid
 

print(Get_living_Cells(cells,4,3))

def GetNextGeneration(cells):
    neighbors = [range(-1,1), range(-1,1)]
    if(cells[0:cells.shape[0],0:cells.shape[1]].any == 1):
        print("hit!")

GetNextGeneration(Get_living_Cells(cells, 4,3))

