from numpy import random

grid = []
rows = 10
cols = 10
rrand = random.randint(10)
crand = random.randint(10)

# Grid setup code
# Generate grid and fill with zeroes
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
    print() # print blank line

def iterate_grid():
    for x in grid:
        for y in x:
            if y == 1:
                print("row: " + str( grid.index(x) ))
                print("column: " + str( x.index(y) ))


# Main
if __name__=="__main__":
    output_grid()
    iterate_grid()

