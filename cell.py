class Cell:
    def __init__(self):
        self.state = ' '
    
    def get_state(self):
        return self.state
    
    def initialize(self):
        self.state = ' '

    def make_X(self):
        self.state = 'X'
    
    def make_O(self):
        self.state = 'O'