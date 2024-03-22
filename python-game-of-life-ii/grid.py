from numpy import random

grid = []
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

    for x in range(random.randint(rows)):
        rrand = random.randint(rows)
        crand = random.randint(cols)

        # Print random initial conditions
        print("row rand: " + str( rrand) )
        print("col rand: " + str( crand) + "\n")

        # Set initial random seed position
        grid[rrand][crand] = 1
        seedCount += 1

    print("seed count " + str( seedCount ))

# Function to print entire grid matrix to the display
def output_grid():
    for x in grid:
        print(x)
    print() # blank line

# Look for living cells
def iterate_grid():
    row_current = ''
    col_current = ''
    cell_count = 0

    for x in grid:
        for y in x:
            if y == 1:
                row_current = grid.index(x)
                col_current = x.index(y)
                cell_count += 1

                # Debug currently selected row and column
                print("row: " + str( row_current ))
                print("column: " + str( col_current ) + "\n")

                #check_neighbors(row_current, col_current)

    print("living cell count: " + str( cell_count ))

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

            print("neighbor normalized: " + str( row_neighbor ) + ", " + str( col_neighbor ))

            if grid[row_neighbor][col_neighbor]:
                neighbor_count += 1

    print("cell neighbors: " + str( neighbor_count ))


# Main
if __name__ == "__main__":
    setup_grid()
    output_grid()
    iterate_grid()

