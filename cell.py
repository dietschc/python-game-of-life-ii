class Cell:
    previousGen = 0
    currentGen = 0
    nextGen = 0

    neighbor_count = 0

    def get_cell_life_status(self):
        return self.currentGen

    def get_cell_gen_status(self):
        return f'''
        Previous: {self.previousGen}
        Current: {self.currentGen}
        Next: {self.nextGen}
        '''
    
    def get_cell_neighbor_count(self):
        return self.neighbor_count
    
    def set_cell_neighbor_count(self, count):
        self.neighbor_count = count    

    def kill_cell(self):
        self.nextGen = 0

    def rez_cell(self):
        self.nextGen = 1

    def iterate_cell(self):
        self.previousGen = self.currentGen
        self.currentGen = self.nextGen
        # Empty nextGen at end
        self.nextGen = 0

