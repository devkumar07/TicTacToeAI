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
    
    def equals3(self, a, b, c):
        return a == b and b == c and a!= ' '
    def get_turn(self):
        return self.turn

    def set_turn(self,t):
        self.turn = t    
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
        return table

    def change_turn(self):
        if self.turn == 'X':
            self.turn = 'O'
        else:
            self.turn = 'X'

    def make_turn(self,t):
        self.turn = t

    def find_winner(self):
        row = 0
        col = 0
        winner = 'null'
        while row < 3:
            if self.equals3(self.table[row][0].get_state(), self.table[row][1].get_state(), self.table[row][2].get_state()):
                winner = self.table[row][0].get_state()
            row = row + 1

        while col < 3:
            if self.equals3(self.table[0][col].get_state(), self.table[1][col].get_state(), self.table[2][col].get_state()):
                winner = self.table[0][col].get_state()
            col = col + 1

        if self.equals3(self.table[0][0].get_state(), self.table[1][1].get_state(), self.table[2][2].get_state()):
            winner = self.table[0][0].get_state()

        if self.equals3(self.table[2][0].get_state(), self.table[1][1].get_state(), self.table[0][2].get_state()):
            winner = self.table[2][0].get_state()
        
        filled = self.is_filled()

        if filled == True and winner == 'null':
            winner = 'Tie'
              
        return winner

    
    def is_empty(self, row, col):
        if self.table[row][col].get_state() == ' ':
            return True
        return False
    
    def is_filled(self):
        for i in range(3):
            for j in range(3):
                if self.table[i][j].get_state() == ' ':
                    return False
        return True
    
    def update_cell(self, row, col):
        if self.is_empty(row,col):
            turn = self.get_turn()
            if turn == 'X':
                self.table[row][col].make_X()
                self.change_turn()
            else:
                self.table[row][col].make_O()
                self.change_turn()
    def AIMove(self):
        best_x = 0
        best_y = 0
        bestScore = -1000
        result = self.find_winner()
        print('AI PLAYING')
        print(self.get_table())
        if self.is_filled() == False:
            for i in range(3):
                for j in range(3):
                    if self.table[i][j].get_state() == ' ':
                        print('New iteration')
                        self.table[i][j].make_O()
                        self.set_turn('X')
                        score = self.minimax(True)
                        self.table[i][j].initialize()
                        if score > bestScore:
                            bestScore = score
                            best_x = i
                            best_y = j
            self.table[best_x][best_y].make_O()
            print('AI post decision')
            print(self.get_table())
            print(bestScore)
            self.set_turn('X')
    
    def minimax(self,isHuman):
        result = self.find_winner()
        if result == 'X':
            print('winner X!')
            return -1
        if result == 'O':
            print('winner O!')
            return 1
        if result == 'Tie':
            print('Tie!')
            return 0
        if isHuman:
            bestScore = 1000
            for i in range(3):
                for j in range(3):
                    if self.table[i][j].get_state() == ' ':
                        #print('turn: ',self.get_turn())
                        self.table[i][j].make_X()
                        self.set_turn('O')
                        print(self.get_table())
                        score = self.minimax(False)
                        self.table[i][j].initialize()
                        bestScore = min(score, bestScore)
            return bestScore

        else:
            bestScore = -1000
            for i in range(3):
                for j in range(3):
                    if self.table[i][j].get_state() == ' ':
                        #print('turn: ',self.get_turn())
                        self.table[i][j].make_O()
                        self.set_turn('X')
                        print(self.get_table())
                        score = self.minimax(True)
                        self.table[i][j].initialize()
                        bestScore = max(score, bestScore)
            return bestScore




