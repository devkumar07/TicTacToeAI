from Cell import *

class Board:
    def __init__(self):
        self.table = []
        i = 0
        while i < 3:
            row = [Cell(), Cell(), Cell()]
            self.table.append(row)
            i = i + 1
        self.turn = 'X'
    
    def get_turn(self):
        return self.turn
    
    def new_game(self):
        self.table = []
        i = 0
        while i < 3:
            row = [Cell(), Cell(), Cell()]
            self.table.append(row)
            i = i + 1
        self.turn = 'X'
    
    def get_table(self):
        table = []
        i = 0
        while i < 3:
            row = []
            row.append(self.table[i][0].get_state())
            row.append(self.table[i][1].get_state())
            row.append(self.table[i][2].get_state())
            table.append(row)
            i = i + 1
        print(table)
        return table

    def change_turn(self):
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'
    
    def check_Horizontal(self):
        turn = self.turn
        table = self.table
        row = 0
        col = 0
        while row < 3:
            if col == 3:
                return True
            elif table[row][col].get_state() == turn:
                col = col + 1
            else:
                col = 0
                row = row + 1
        return False

    def check_Vertical(self):
        turn = self.turn
        table = self.table
        row = 0
        col = 0
        while col < 3:
            if row == 3:
                return True
            elif table[row][col].get_state() == turn:
                row = row + 1
            else:
                row = 0
                col = col + 1
        return False

    def check_Diagnols(self):
        status = True
        row = 0
        col = 0
        turn = self.get_turn
        while row < 3 and col < 3:
            value = self.table[row][col].get_state()
            if value != turn:
                status = False
            row = row + 1
            col = col + 1

        if status == False:
            row = 0
            col = 2
            while row < 2 and col >=0:
                value = self.table[row][col].get_state()
                if value != turn:
                    status = False
                row = row + 1
                col = col - 1

        return status


    def find_winner(self):
        if self.check_Diagnols() or self.check_Horizontal() or self.check_Vertical():
            return self.get_turn()
        return ' '
    
    def is_empty(self, row, col):
        table = self.table
        print(table[0])
        print(len(table[0][0].get_state()))
        if self.table[row][col].get_state() == ' ':
            return True
        return False
    
    def update_cell(self, row, col):
        if self.is_empty(row,col):
            turn = self.get_turn()
            if turn == 'X':
                self.table[row][col].make_X()
                self.change_turn()
            else:
                self.table[row][col].make_O()
                self.change_turn()
