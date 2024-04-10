class Cell:
    previousGen = 0
    currentGen = 0
    nextGen = 0
    # neighborCount = 0

    def get_cell_life_status(self):
        return self.currentGen

    def get_cell_gen_status(self):
        return f'''
        Previous: {self.previousGen}
        Current: {self.currentGen}
        Next: {self.nextGen}
        '''
    
    # def get_cell_neighborCount(self):
    #     return self.neighborCount
    
    # def set_cell_neighborCount(self, count):
    #     self.neighborCount = count
    #     return self.neighborCount    

    def kill_cell(self):
        self.nextGen = 0
        return self.nextGen

    def rez_cell(self):
        self.nextGen = 1
        return self.nextGen

    def iterate_cell(self):
        self.previousGen = self.currentGen
        self.currentGen = self.nextGen
        # Empty nextGen at end
        #self.nextGen = 0


