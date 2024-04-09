import numpy as np

from numpy import random


class Grid:
    matrix = []
    rows = 0
    cols = 0
    
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
        for x in range(random.randint(rows * cols)):
            rrand = random.randint(rows)
            crand = random.randint(cols)
            self.matrix[rrand][crand].rez_cell()


#    @classmethod
#    def copy_matrix(matrix):
#        self.matrix = matrix

    def get_rows(self):
        return self.rows

    def get_cols(self):
        return self.cols

    def get_matrix(self):
        return self.matrix

    def get_cell(self, row, col):
        return self.matrix[row][col].get_cell_life_status()

    def get_all_cells(self):
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                print(self.matrix[row][col].get_cell_life_status(), end='')

            print() # blank line


class Cell:
#    previousGen = 0
#    currentGen = 0
#    nextGen = 0

    alive = 0
    neighbor_count = 0

    def get_cell_life_status(self):
        return self.alive

    def kill_cell(self):
        self.alive = 0

    def rez_cell(self):
        self.alive = 1



# Main method defined here
def main():

    myGrid = Grid(4, 8)
    print(f'Rows: {myGrid.get_rows()}')
    print(f'Cols: {myGrid.get_cols()}')
#    print(f'Matrix: \n{myGrid.get_matrix()}')
#    print(f'Cell Specified: \n{myGrid.get_cell(1,1)}')
    print('All cells: ')
    myGrid.get_all_cells()
 
 
if __name__ == '__main__':
    main()
