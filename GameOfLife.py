import numpy as np

cells = [[2,0],[2,1],[2,2]]



def Get_living_Cells(cells, numRows, numCol):
    life_grid = np.zeros((numRows, numCol), dtype=int)
    for x in cells:
        life_grid[x[0],x[1]] = 1

    # print(life_grid)
    return life_grid
 

print(Get_living_Cells(cells,4,3))

# Write a python function that accepts a numpy array representing the current board and 
# returns a numpy representing the next generation of living cells (assume that cells out of bounds of the board immediately die).  
# (Don't use any loops here!)

def GetNextGeneration(cells):
    counts = np.zeros((cells.shape[0], cells.shape[1]))

    left = slice(0,cells.shape[0]), slice(0, cells.shape[1] - 1)
    right = slice(0,cells.shape[0]), slice(1, cells.shape[1])
    up = slice(0,cells.shape[0] - 1), slice(0, cells.shape[1])
    down = slice(1,cells.shape[0]), slice(0, cells.shape[1])
    down_left = slice(1,cells.shape[0]), slice(0, cells.shape[1] - 1)
    down_right = slice(1,cells.shape[0]), slice(1, cells.shape[1])
    up_left = slice(0,cells.shape[0] - 1), slice(0, cells.shape[1] - 1)
    up_right = slice(0,cells.shape[0] - 1), slice(1, cells.shape[1])

    counts[left] += cells[right]
    counts[right] += cells[left]
    counts[up] += cells[down]
    counts[down] += cells[up]
    counts[down_left] += cells[up_right]
    counts[up_right] += cells[down_left]
    counts[down_right] += cells[up_left]
    counts[up_left] += cells[down_right]

    will_live = (counts == 2)&(cells == 1 ) | (cells == 1)
    # TODO
    # create 2D array of arrays like the first structure

    print(counts)
    return will_live

    # result = (
    #     cells[0:cells.shape[0]-1, 0:cells.shape[1]-1] +
    #     cells[0:cells.shape[0], 0:cells.shape[1]-1] +
    #     cells[0:cells.shape[0]-1, 0:cells.shape[1]-1]
    # )
    # return result

GetNextGeneration(Get_living_Cells(cells, 4,3))


