from cell import *

class Board:
    def __init__(self):
        self.table = []
        for i in range(3):
            row = []
            for j in range(3):
                cell = Cell('')
                row.append(cell)
            self.table.append(row)
        self.turn = 'X'
    
    def get_turn(self):
        return self.turn
    
    def get_table(self):
        return self.table

    def change_turn(self):
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'
    
    def check_Horizontal(self):
        turn = self.get_turn()
        count = 0
        table = self.get_table()
        row = 0
        while col < 3:
            if table[row][col] == turn:
                count = count + 1
            i
            

    def find_winner(self):