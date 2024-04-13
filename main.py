import os
import time

from grid import Grid
from cell import Cell


# Main method defined here
def main():

    # Create new grid object
    myGrid = Grid(4, 8)

    # Run in infinite loop until ctl+c to break
    while True:
        os.system('clear')
        myGrid.get_all_cells()
        myGrid.apply_game_rules_to_all_cells()
        myGrid.set_all_cells_to_nextGen()
        print()

        # Delay for x seconds
        time.sleep(1)

 
if __name__ == '__main__':
    main()
