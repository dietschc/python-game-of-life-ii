from grid import Grid
from cell import Cell

# Main method defined here
def main():

    myGrid = Grid(4, 8)
    print(f'Rows: {myGrid.get_rows()}')
    print(f'Cols: {myGrid.get_cols()}')
#    print(f'Matrix: \n{myGrid.get_matrix()}')
#    print(f'Cell Specified: \n{myGrid.get_cell(1,1)}')
    print('All cells: ')
    myGrid.get_all_cells()
    # myGrid.set_all_cells_to_nextGen()
    # print(myGrid.get_cell(1, 1))
    # myGrid.set_cell_to_nextGen(1, 1)
    print("\nCell neighbors: " + str( myGrid.get_cell_neighbors(1, 1) ))
    print("\nCell neighbors: " + str( myGrid.set_cell_neighbor_count(1, 1) ))
    # myGrid.get_all_cells()    
 
 
if __name__ == '__main__':
    main()
