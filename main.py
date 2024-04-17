import os
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

from matplotlib import colormaps
from grid import Grid
from cell import Cell


# Main method defined here
def main():

    # Create new grid object
    myGrid = Grid(12, 24)

    print(myGrid.get_all_cells())

    # CLI mode
    # Run in infinite loop until ctl+c to break
    # while True:
    #     os.system('clear')
    # myGrid.print_all_cells()
    # myGrid.apply_game_rules_to_all_cells()
    # myGrid.set_all_cells_to_nextGen()
    # print()

    #     # Delay for x seconds
    #     time.sleep(1)

    # Matplotlib animation code - run our iterate_grid() function every update
    plt.rcParams["figure.figsize"] = [10, 6]
    plt.rcParams["figure.autolayout"] = True

    fig, ax = plt.subplots()
    fig.patch.set_facecolor('black')
    ax.set_axis_off()

    def update(frame):
        global generationCount

        # Iterate our grid every update
        myGrid.apply_game_rules_to_all_cells()
        myGrid.set_all_cells_to_nextGen()

        # Clear buffer to prevent animation slowdown
        ax.clear()

        # Hide axis, use custom colormap
        ax.set_axis_off()
        ax.matshow(myGrid.get_all_cells(), cmap=colormaps['bone'])

    anim = animation.FuncAnimation(fig, update, frames=20, interval=50)
    plt.show()

 
if __name__ == '__main__':
    main()
