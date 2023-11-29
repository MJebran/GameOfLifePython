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

    # A live cell dies if it has fewer than two live neighbors.
    # A live cell with two or three live neighbors lives on to the next generation.
    # A live cell with more than three live neighbors dies.
    # A dead cell will be brought back to live if it has exactly three live neighbors.

    will_live = (counts == 2)&(cells == 1 ) | (counts == 3)
    print(counts)
    print(will_live)

    # TODO
    # create 2D array of arrays like the first structure
    next_generation = will_live.astype(int)
    print(np.array(next_generation))

    return np.array(next_generation)


#### TESTS #####
assert Get_living_Cells({(2,0),(2,1),(2,2)}, 5, 3).tolist() == [[0,0,0],[0,0,0],[1,1,1],[0,0,0],[0,0,0]]
assert Get_living_Cells({(0,1),(1,1),(2,1)}, 4, 2).tolist() == [[0,1],[0,1],[0,1],[0,0]]

assert np.array_equal(GetNextGeneration(np.array([[0,0,0],[0,0,0],[1,1,1],[0,0,0],[0,0,0]])), np.array([[0,0,0],[0,1,0],[0,1,0],[0,1,0],[0,0,0]]))
assert np.array_equal(GetNextGeneration(np.array([[0,0,0],[0,1,0],[0,1,0],[0,1,0],[0,0,0]])), np.array([[0,0,0],[0,0,0],[1,1,1],[0,0,0],[0,0,0]]))


import turtle

array_to_draw = GetNextGeneration(Get_living_Cells(cells, 5,3))

def draw_array (array):
    for i in range(array.shape[0]):
        for j in range(array.shape[1]):
            turtle.goto(50 * j, i * 50)
            turtle.pendown()

            if array[i, j] == 1:
                turtle.begin_fill()
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(50)
            turtle.right(90)
            turtle.forward(50)
            if array[i, j] == 1:
                turtle.end_fill()

            turtle.penup()
    turtle.done()

draw_array(array_to_draw)

