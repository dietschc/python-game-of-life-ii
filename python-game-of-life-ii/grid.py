from numpy import random

grid = []
epoch = []
rows = 10
cols = 10
xrand = random.randint(10)
yrand = random.randint(10)

# Grid setup code
# Generate grid and fill with zeroes
for x in range(rows):
    col = []
    for y in range(cols):
        col.append(0)
    grid.append(col)

# Print random initial condition
print("xrand: " + str( xrand) )
print("yrand: " + str( yrand) )

# Function to print entire grid matrix to the display
def output_grid():
    # Print whole matrix
    for x in grid:
        print(x)
    print() # print blank line

def iterate_grid():
    grid[xrand][yrand] = 1
    output_grid()

# Main
if __name__=="__main__":
    output_grid()
    iterate_grid()

