from grid import Grid
from cell import Cell

# Main method defined here
def main():

    myGrid = Grid(4, 8)

    print('Start cells: ')
    myGrid.get_all_cells()
    # print(myGrid.get_cell(1, 2))

    # myGrid.set_all_cells_neighbor_count()
    myGrid.apply_game_rules_to_all_cells()
    myGrid.set_all_cells_to_nextGen()
    print()
    myGrid.get_all_cells()

    # myGrid.set_all_cells_neighbor_count()
    myGrid.apply_game_rules_to_all_cells()
    myGrid.set_all_cells_to_nextGen()
    print()
    myGrid.get_all_cells()

 
if __name__ == '__main__':
    main()
