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

