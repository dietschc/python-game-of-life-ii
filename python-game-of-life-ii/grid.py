from numpy import random

grid = []
rows = 10
cols = 10
rrand = random.randint(rows)
crand = random.randint(cols)

# Generate grid and fill with zeroes
def setup_grid():
    for x in range(rows):
        col = []
        for y in range(cols):
            col.append(0)
        grid.append(col)

    # Print random initial condition
    print("row rand: " + str( rrand) )
    print("col rand: " + str( crand) )

    # Set initial random seed position
    grid[rrand][crand] = 1

# Function to print entire grid matrix to the display
def output_grid():
    # Print whole matrix
    for x in grid:
        print(x)
    print() # blank line

# Look for living cells
def iterate_grid():
    row_current = ''
    col_current = ''

    for x in grid:
        for y in x:
            if y == 1:
                row_current = grid.index(x)
                col_current = x.index(y)

                # Debug currently selected row and column
                #print("row: " + str( row_current ))
                #print("column: " + str( col_current ))

                check_neighbors(row_current, col_current)

# Iterate through neighboring cells
def check_neighbors(row, col):
    row_neighbor = ''
    col_nieghbor = ''

    # Trick to read the rows and cols around current cell
    for x in range(-1, 2):
        for y in range(-1, 2):
            row_neighbor = row + x
            col_neighbor = col + y

            print("row: " + str( row_neighbor ))
            print("col: " + str( col_neighbor ))
            print("neighbor: " + str( row_neighbor ) + ", " + str( col_neighbor ))

            # Wrap-around when neighbors are below 0 or above 9
            if row_neighbor < 0:
                row_neighbor += rows
            elif row_neighbor > rows:
                row_neighbor -= rows

            if col_neighbor < 0:
                col_neighbor += cols
            elif col_neighbor > cols:
                col_neighbor -= cols

            print("neighbor normalized: " + str( row_neighbor ) + ", " + str( col_neighbor ))


# Main
if __name__=="__main__":
    setup_grid()
    output_grid()
    iterate_grid()

