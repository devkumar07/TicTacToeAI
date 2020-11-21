class Cell:
    def __init__(self, state):
        self.state = state
    
    def get_state(self):
        return self.state

    def make_X(self):
        self.state = 'X'
    
    def make_Y(self):
        self.state = 'Y
        
