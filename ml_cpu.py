'''
A CPU for the tic-tac-toe game that is based on a machine learning model.
It will use this insight to decide where to place it's "X".

Nathan Lutala (nlutala)
'''

from secrets import choice
from sklearn import tree
import os

class MLCPU:
    def __init__(self, symbol="X"):
        self.symbol = symbol
        self.ttt_tree = tree.DecisionTreeClassifier()
        self.data = []
        self.target = []

        if self.symbol.upper() not in ["X", "O"]:
            raise ValueError("Incorrect input. Expected either 'X' or 'O'.")

        with open("ttt_good_moves.txt") as file:
            for row in file:
                row_to_add = list(row[:len(row)-1])
                row_to_add = self._prep_data(row_to_add)
                self.data.append(row_to_add[:len(row_to_add)-1])
                self.target.append(row_to_add[-1])

        self.ttt_tree.fit(self.data, self.target)

    def get_symbol(self):
        return self.symbol
    
    def _prep_data(self, row: list) -> list:
        '''
        Replaces all Xs with 1s and Os with -1s, and replaces
        _s with 0s

        Params:
        row (list) - a list in the ttt_good_moves.txt file

        Retuns a new list of 1, -1, 0s and numbers [0-8]
        '''
        new_row = []

        for r in row:
            if r == "X":
                new_row.append(1)
            elif r == "O":
                new_row.append(-1)
            elif r == "_":
                new_row.append(0)
            else:
                new_row.append(r)

        return new_row
    
    def make_move(self, game_state: list, available_moves: list):
        '''
        Param:
        game_state (list) - a list representing the current grid of the game
        available_moves (list) - a list representing all the available spaces

        Returns an int of the index to place the CPU's symbol
        '''
        game_state = self._prep_data(game_state)
        move = int(self.ttt_tree.predict([game_state])[0])

        if move in available_moves:
            return move
        else:
            return choice(available_moves)
