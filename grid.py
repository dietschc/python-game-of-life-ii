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

        # Randomize grid
        for x in range(random.randint(rows * cols) + 3):
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

    def get_all_cells(self):
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                print(self.matrix[row][col].get_cell_life_status(), end='')

            print() # blank line

    # Setters
    def set_all_cells_to_nextGen(self):
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                self.matrix[row][col].iterate_cell()

    def set_cell_to_nextGen(self, row, col):
        return self.matrix[row][col].iterate_cell()