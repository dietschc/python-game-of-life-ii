from numpy import random
import os
import time
import copy

# Python CLI implementation of Conway's game of life
# (2nd attempt)
#
# March 22, 2024
# Coleman Dietsch
#
#
# 1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
# 2. Any live cell with two or three live neighbors lives on to the next generation.
# 3. Any live cell with more than three live neighbors dies, as if by overpopulation.
# 4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
#
#


grid = []
nextGeneration = []
ROWS = 10
COLS = 10

# Setup function that zeroes out grid and adds random seed
def setup_grid():
    # Generate initial grid and fill with zeroes
    for x in range(ROWS):
        col = []
        for y in range(COLS):
            col.append(0)
        grid.append(col)

    #
    # Some test shapes
    #
    # Box
    #grid[4][4] = 1
    #grid[4][5] = 1
    #grid[5][4] = 1
    #grid[5][5] = 1

    # Spinner
    #grid[4][4] = 1
    #grid[4][5] = 1
    #grid[4][6] = 1
    #

    # Randomize grid
    for x in range(random.randint(ROWS * COLS)):
        rrand = random.randint(ROWS)
        crand = random.randint(COLS)

        grid[rrand][crand] = 1

    output_grid()

# Function to print entire grid matrix to the display
def output_grid():
    for x in grid:
        print(x)
    print() # blank line

# Go through each cell and apply game rules to it
def iterate_grid():
    global nextGeneration
    global grid

    row_current = ''
    col_current = ''

    # Copy current grid to nextGeneration
    # nextGeneration is modified based on the current grid and copied back at the end
    nextGeneration = copy.deepcopy(grid)

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            #print("grid row index: " + str( y ))
            #print("grid column index: " + str( x ))

            row_current = y
            col_current = x
            neighbor_count_current = 0

            neighbor_count_current = check_neighbors(row_current, col_current)
            #print("cell: " + str( row_current) + ", " + str( col_current ) +  " neighbors: " + str( neighbor_count_current ) + "\n")

            apply_game_rules(row_current, col_current, neighbor_count_current)

    # Copy the nextGeneration to current grid for the next iteration
    grid = copy.deepcopy(nextGeneration)

    output_grid()

# Iterate through neighboring cells
def check_neighbors(row, col):
    row_neighbor = 0
    col_nieghbor = 0
    neighbor_count = 0

    # Algorithm to read the ROWS and COLS around current cell
    for x in range(-1, 2):
        for y in range(-1, 2):
            row_neighbor = row + x
            col_neighbor = col + y

            # Check to see if neighbor is current cell and skip if it is
            if row == row_neighbor and col == col_neighbor:
                #print("this cell is: " + str( row_neighbor ) + ", " + str( col_neighbor ))
                continue

            # Wrap-around when neighbors are below 0 or above COLS/ROWS max values
            if row_neighbor < 0:
                row_neighbor += ROWS
            elif row_neighbor >= ROWS:
                row_neighbor -= ROWS

            if col_neighbor < 0:
                col_neighbor += COLS
            elif col_neighbor >= COLS:
                col_neighbor -= COLS

            # Debug warning - This will print 8 times
            #print("neighbor: " + str( row_neighbor ) + ", " + str( col_neighbor ) + " alive? " + str(  grid[row_neighbor][col_neighbor] ))

            # Check if neighbor is alive in the current grid
            if grid[row_neighbor][col_neighbor]:
                neighbor_count += 1

    return neighbor_count


# The 4 rules of Conway's Game of Life
def apply_game_rules(row, col, count):
    # If cell is alive in current grid
    if grid[row][col]:
        # 1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
        if count < 2:
            #print("Underpopulation - less than 2 neighbors; " + str( row ) + ", " + str( col ) + " dies now...\n")
            nextGeneration[row][col] = 0

        # 2. Any live cell with two or three live neighbors lives on to the next generation.
        # Do nothing

        # 3. Any live cell with more than three live neighbors dies, as if by overpopulation.
        if count > 3:
            #print("Overpopulation - more than 3 neighbors; " + str( row ) + ", " + str( col ) + " dies now...\n")
            nextGeneration[row][col] = 0
   
   # Else cell is dead
    else:
    # 4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        if count == 3:
            #print("Reproduction - returns " + str( row ) + ", " + str( col ) + " to life\n")
            nextGeneration[row][col] = 1


# Main
if __name__ == "__main__":
    count = 0

    os.system('clear')
    setup_grid()
    time.sleep(3)

    while True:
        os.system('clear')
        count += 1
        iterate_grid()
        print("iteration count: " + str( count ))
        time.sleep(3)

    

