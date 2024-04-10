from grid import Grid
from cell import Cell

# Main method defined here
def main():

    myGrid = Grid(4, 8)

    print('All cells: ')
    myGrid.get_all_cells()
    myGrid.set_all_cells_neighbor_count()
    myGrid.apply_game_rules_to_all_cells()
    myGrid.set_all_cells_to_nextGen()

    print()
    myGrid.get_all_cells()
    myGrid.set_all_cells_neighbor_count()
    myGrid.apply_game_rules_to_all_cells()
    myGrid.set_all_cells_to_nextGen()




    # print("\nCell neighbors: " + str( myGrid.set_cell_neighbor_count(1, 1) ))
    # myGrid.get_all_cells()    
    # print("\nCell neighbors: " + str( myGrid.get_cell_neighbors(1, 1) ))

    # myGrid.set_all_cells_to_nextGen()
    # myGrid.set_all_cells_neighbor_count()
    # print("\nCell neighbors: " + str( myGrid.get_cell_neighbors(1, 1) )) # should be 0

    # myGrid.apply_game_rules_to_cell(1, 1, 3)
    myGrid.apply_game_rules_to_all_cells()
    # print(myGrid.get_cell(1, 1))
    # myGrid.set_all_cells_to_nextGen()
    # print(myGrid.get_cell(1, 1))

 
if __name__ == '__main__':
    main()
