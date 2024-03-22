from numpy import random
import os
import time


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
rows = 10
cols = 10

# Generate grid and fill with zeroes
def setup_grid():
    seedCount = 0

    for x in range(rows):
        col = []
        for y in range(cols):
            col.append(0)
        grid.append(col)

    for x in range(random.randint(rows * cols)):
        rrand = random.randint(rows)
        crand = random.randint(cols)

        # Debug random initial conditions
        #print("row rand: " + str( rrand) )
        #print("col rand: " + str( crand) + "\n")

        # Set initial random seed position
        grid[rrand][crand] = 1
        seedCount += 1

    #print("seed count " + str( seedCount ))
    output_grid()

# Function to print entire grid matrix to the display
def output_grid():
    for x in grid:
        print(x)
    print() # blank line

# Look for living cells, apply the game rules to each cell
def iterate_grid():
    global nextGeneration
    global grid

    row_current = ''
    col_current = ''

    # Copy current grid to nextGeneration
    # nextGeneration is modified based on the current grid and copied back at the end
    nextGeneration = grid

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            #print("grid row index: " + str( y ))
            #print("grid column index: " + str( x ))

            row_current = y
            col_current = x
            neighbor_count_current = 0

            # Debug currently selected row and column
            #print("cell value: " + str( y ))
            #print("cell row: " + str( row_current ))
            #print("cell column: " + str( col_current ) + "\n")

            neighbor_count_current = check_neighbors(row_current, col_current)
            #print("cell has x neighbors: " + str( neighbor_count_current ))

            apply_game_rules(row_current, col_current, neighbor_count_current)

    print("Advancing to next generation")
    print("########################################################\n")

    # Copy the nextGeneration to current grid for the next iteration
    grid = nextGeneration
    output_grid()

# Iterate through neighboring cells
def check_neighbors(row, col):
    row_neighbor = ''
    col_nieghbor = ''
    neighbor_count = 0

    # Algorithm to read the rows and cols around current cell
    for x in range(-1, 2):
        for y in range(-1, 2):
            row_neighbor = row + x
            col_neighbor = col + y

            # Debug neighbor
            #print("row: " + str( row_neighbor ))
            #print("col: " + str( col_neighbor ))
            #print("neighbor: " + str( row_neighbor ) + ", " + str( col_neighbor ))

            # Check to see if neighbor is current cell and skip if it is
            if row == row_neighbor and col == col_neighbor:
                print("this cell is: " + str( row_neighbor ) + ", " + str( col_neighbor ))
                continue

            # Wrap-around when neighbors are below 0 or above cols/rows max values
            if row_neighbor < 0:
                row_neighbor += rows
            elif row_neighbor >= rows:
                row_neighbor -= rows

            if col_neighbor < 0:
                col_neighbor += cols
            elif col_neighbor >= cols:
                col_neighbor -= cols

            # Debug warning - This will print 8 times
            #print("neighbor normalized: " + str( row_neighbor ) + ", " + str( col_neighbor ))

            # Check if neighbor is alive in the current grid
            if grid[row_neighbor][col_neighbor]:
                neighbor_count += 1

    #print("cell neighbors: " + str( neighbor_count ))
    return neighbor_count


# The 4 rules of Conway's Game of Life
def apply_game_rules(row, col, count):

    # Debug inputs
    #print("applying game rules to: " + str( row ) + ", " + str( col ))
    #print("# of neighbors: " + str( count ))
    #print("dead or alve? " + str( grid[row][col] )) 

    # If cell is alive in current grid
    if grid[row][col]:
        # 1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
        if count < 2:
            print("Underpopulation - less than 2 neighbors; " + str( row ) + ", " + str( col ) + " dies now...\n")
            nextGeneration[row][col] = 0

        # 2. Any live cell with two or three live neighbors lives on to the next generation.
        # Do nothing

        # 3. Any live cell with more than three live neighbors dies, as if by overpopulation.
        if count > 3:
            print("Overpopulation - more than 3 neighbors; " + str( row ) + ", " + str( col ) + " dies now...\n")
            nextGeneration[row][col] = 0
   
   # Else cell is dead
    else:
    # 4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        if count == 3:
            print("Reproduction - returns " + str( row ) + ", " + str( col ) + " to life\n")
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

    

