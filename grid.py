#!/usr/bin/env python3


#
# Python CLI implementation of Conway's game of life
# (2nd attempt)
#
# March 22, 2024
# Coleman Dietsch
#
#
# 1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
# 2. Any live cell with two or three live neighbors lives on to the next generation.
# 3. Any live cell with more than three live neighbors dies, as if by overpopulation.
# 4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
#


#
# Importing the required modules
#
import argparse
import os
import time
import copy
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from numpy import random


#
# Globals and constants
#
grid = []
nextGeneration = []
ROWS = 12
COLS = 32


#
# Argument parser
#
parser = argparse.ArgumentParser()
parser.add_argument("--verbose", help="increase output verbosity", action="store_true")
parser.add_argument("--cli", help="run application in command line mode", action="store_true")
parser.add_argument("--gui", help="(default) run application in graphical mode", action="store_true")
args = parser.parse_args()
if args.verbose:
    print("verbosity turned on")
    if args.cli:
        print("Running in CLI mode")
    if args.gui:
        print("Running in GUI mode")


#
# Functions
#
# Setup function that zeroes out grid and adds random seed
def setup_grid():
    # Generate initial grid and fill with zeroes
    for x in range(ROWS):
        col = []
        for y in range(COLS):
            col.append(0)
        grid.append(col)

    #
    # Some test shapes
    #
    # Box
    #grid[4][4] = 1
    #grid[4][5] = 1
    #grid[5][4] = 1
    #grid[5][5] = 1

    # Spinner
    #grid[4][4] = 1
    #grid[4][5] = 1
    #grid[4][6] = 1
    #

    # Randomize grid
    #for x in range(0): # lazy shortcut to bypass loop
    for x in range(random.randint(ROWS * COLS)):
        rrand = random.randint(ROWS)
        crand = random.randint(COLS)

        grid[rrand][crand] = 1


# CLI function to print entire grid matrix to the display
def output_grid():
    for x in grid:
        print(x)
    print() # blank line


# Go through each cell and apply game rules to it
def iterate_grid():
    global nextGeneration
    global grid

    row_current = 0
    col_current = 0

    # Copy current grid to nextGeneration
    # nextGeneration is modified based on the current grid and copied back at the end
    nextGeneration = copy.deepcopy(grid)

    for x in range(len(grid)):
        for y in range(len(grid[x])):
            row_current = x
            col_current = y
            neighbor_count_current = 0

            neighbor_count_current = check_neighbors(row_current, col_current)
            #print("cell: " + str( row_current) + ", " + str( col_current ) +  " neighbors: " + str( neighbor_count_current ) + "\n")

            apply_game_rules(row_current, col_current, neighbor_count_current)

    # Copy the nextGeneration to current grid for the next iteration
    grid = copy.deepcopy(nextGeneration)


# Iterate through neighboring cells
def check_neighbors(row, col):
    row_neighbor = 0
    col_nieghbor = 0
    neighbor_count = 0
    
    # Algorithm to read the ROWS and COLS around current cell
    for x in range(-1, 2):
        for y in range(-1, 2):
            row_neighbor = row + x
            col_neighbor = col + y

            # Check to see if neighbor is current cell and skip if it is
            if row == row_neighbor and col == col_neighbor:
                #print("this cell is: " + str( row_neighbor ) + ", " + str( col_neighbor ))
                continue

            # Wrap-around when neighbors are below 0 or above COLS/ROWS max values
            if row_neighbor < 0:
                row_neighbor += ROWS
            elif row_neighbor >= ROWS:
                row_neighbor -= ROWS

            if col_neighbor < 0:
                col_neighbor += COLS
            elif col_neighbor >= COLS:
                col_neighbor -= COLS

            # Debug warning - This will print 8 times
            #print("neighbor: " + str( row_neighbor ) + ", " + str( col_neighbor ) + " alive? " + str(  grid[row_neighbor][col_neighbor] ))

            # Check if neighbor is alive in the current grid
            if grid[row_neighbor][col_neighbor]:
                neighbor_count += 1

    return neighbor_count


# The 4 rules of Conway's Game of Life
def apply_game_rules(row, col, count):
    # If cell is alive in current grid
    if grid[row][col]:
        # 1. Any live cell with fewer than two live neighbors dies, as if by underpopulation.
        if count < 2:
            #print("Underpopulation - less than 2 neighbors; " + str( row ) + ", " + str( col ) + " dies now...\n")
            nextGeneration[row][col] = 0

        # 2. Any live cell with two or three live neighbors lives on to the next generation.
        # Do nothing

        # 3. Any live cell with more than three live neighbors dies, as if by overpopulation.
        if count > 3:
            #print("Overpopulation - more than 3 neighbors; " + str( row ) + ", " + str( col ) + " dies now...\n")
            nextGeneration[row][col] = 0
   
   # Else cell is dead
    else:
    # 4. Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
        if count == 3:
            #print("Reproduction - returns " + str( row ) + ", " + str( col ) + " to life\n")
            nextGeneration[row][col] = 1


#
# Main
#
if __name__ == "__main__":
    # Always initialize grid
    setup_grid()

    # If running with the cli flag run command line mode
    if args.cli:

        # Run in infinite loop until ctl+c to break
        while True:
            os.system('clear')
            output_grid()
            iterate_grid()
            time.sleep(1)

    # Run in GUI mode by default
    else:
        # Matplotlib animation code - run our iterate_grid() function every update
        plt.rcParams["figure.figsize"] = [6, 6]
        plt.rcParams["figure.autolayout"] = True

        fig, ax = plt.subplots()
        ax.set_axis_off()

        def update(i):
            # Iterate our grid every update
            iterate_grid()
            ax.imshow(grid)

        anim = animation.FuncAnimation(fig, update, frames=20, interval=50)
        plt.show()

