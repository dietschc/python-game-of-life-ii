# python-game-of-life-ii
My second attempt at implementing Conway's Game of Life in python.

The program generates an initial 2d array, fills it with zeros, and then fills the grid with a random initial seed.

The program then runs in a loop running the iterate_grid() function indefinately. The iterate_grid() function iterates the entire 2d grid and runs check_neighbors() and apply_game_rules() to every cell in the 2d array.

The check_neighbors() function uses a 2d for loop from the range of -1 to 2 to search for the cells around the current cell. There is also logic written in to account for if a neighbor is out of range, to wrap around to the other side of the grid.

Finally the apply_game_rules() function does what it sounds like, and applies the 4 rules for Conway's game of life to the currently selected cell. The changes are reflected in the nextGeneraion 2d array which will be copied to the current grid during the next iteration of iterate_grid().

Depending on the display mode, output will either go to CLI or GUI.

### Quick Use Example
```
$ ./grid.py --help
usage: grid.py [-h] [--verbose] [--cli] [--gui]

options:
  -h, --help  show this help message and exit
  --verbose   increase output verbosity
  --cli       run application in command line mode
  --gui       (default) run application in graphical mode

$ ./grid.py --cli

[1, 0, 1, 0, 1, 0, 1, 0, 0, 0]
[1, 0, 1, 0, 1, 0, 0, 1, 1, 1]
[0, 1, 1, 0, 1, 0, 0, 0, 0, 0]
[0, 0, 0, 0, 1, 0, 0, 1, 1, 0]
[0, 1, 1, 1, 1, 0, 0, 0, 1, 0]
[1, 0, 0, 1, 0, 0, 0, 0, 1, 0]
[0, 1, 0, 1, 1, 0, 0, 0, 1, 0]
[1, 0, 1, 1, 0, 0, 0, 0, 1, 1]
[0, 1, 0, 0, 1, 0, 1, 0, 0, 0]
[1, 0, 1, 0, 1, 0, 1, 0, 0, 1]
```
