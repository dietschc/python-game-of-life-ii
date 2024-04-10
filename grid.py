from numpy import random

from cell import Cell


# The grid contains a 2d array filled with cell objects
class Grid:
    matrix = []
    rows = 0
    cols = 0
    
    # Grid class constructor
    def __init__(self, rows, cols):
        self.rows = rows
        self.cols = cols

        # Generate initial grid and fill with dead cells
        for row in range(rows):
            tempCol = []
            for col in range(cols):
                tempCol.append(Cell())
            self.matrix.append(tempCol)

        # Randomize the grid by resurrecting a random number of dead cells
        for x in range(random.randint(rows * cols) + 3): # Arbitrary non-zero number
            rrand = random.randint(rows)
            crand = random.randint(cols)
            self.matrix[rrand][crand].rez_cell()
            
            # Advance cell to generation 0
            self.matrix[rrand][crand].iterate_cell()

    # Getters
    def get_rows(self):
        return self.rows

    def get_cols(self):
        return self.cols

    def get_matrix(self):
        return self.matrix

    def get_cell(self, row, col):
        return self.matrix[row][col].get_cell_gen_status()
    
    def get_cell_neighbors(self, row, col):
        return self.matrix[row][col].get_cell_neighbor_count()

    def get_all_cells(self):
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                print(self.matrix[row][col].get_cell_life_status(), end='')
            print() # blank line

    def get_cell_neighbor_count(self, row, col):
        row_neighbor = 0
        col_neighbor = 0
        neighbor_count = 0

        # Algorithm to read the self.rows and self.cols around current cell
        for x in range(-1, 2):
            for y in range(-1, 2):
                row_neighbor = row + x
                col_neighbor = col + y

                # Check to see if neighbor is current cell and skip if it is
                if row == row_neighbor and col == col_neighbor:
                    #print("this cell is: " + str( row_neighbor ) + ", " + str( col_neighbor ))
                    continue

                # Wrap-around when neighbors are below 0 or above self.cols/self.rows max values
                if row_neighbor < 0:
                    row_neighbor += self.rows
                elif row_neighbor >= self.rows:
                    row_neighbor -= self.rows

                if col_neighbor < 0:
                    col_neighbor += self.cols
                elif col_neighbor >= self.cols:
                    col_neighbor -= self.cols

                # Debug warning - This will print 8 times
                #print("neighbor: " + str( row_neighbor ) + ", " + str( col_neighbor ) + " alive? " + str(  grid[row_neighbor][col_neighbor] ))

                # Check if neighbor is alive in the current grid
                if self.matrix[row_neighbor][col_neighbor].get_cell_life_status():
                    neighbor_count += 1

        # return self.matrix[row][col].set_cell_neighbor_count(neighbor_count)
        return neighbor_count
    
    
    # Setters
    def set_all_cells_to_nextGen(self):
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                self.matrix[row][col].iterate_cell()

    def set_cell_to_nextGen(self, row, col):
        return self.matrix[row][col].iterate_cell()
    
    def set_all_cells_neighbor_count(self):
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                neighborCount = self.get_cell_neighbor_count(row, col)
                self.matrix[row][col].set_cell_neighbor_count(neighborCount)

    def set_cell_neighbor_count(self, row, col, count):
        return self.matrix[row][col].set_cell_neighbor_count(count)
    
