'''
A CPU for the tic-tac-toe game that is based on a machine learning model.
It will use this insight to decide where to place it's "X".

Nathan Lutala (nlutala)
'''

from create_ttt_game_data import create_game_data
from sklearn.datasets import load_iris
from sklearn import tree
import os

class MLCPU:
    def __init__(self, symbol="X"):
        self.symbol = symbol
        self.ttt_moves_tree = tree.DecisionTreeClassifier(criterion="entropy")
        self.data = []
        self.target = []

        if self.symbol.upper() not in ["X", "O"]:
            raise ValueError("Incorrect input. Expected either 'X' or 'O'.")

        if "game_results_ttt.txt" not in os.listdir():
            create_game_data()

        with open("game_results_ttt.txt") as file:
            for row in file:
                row_to_add = list(row[:len(row)-1])
                row_to_add = self._prep_data(row_to_add)
                self.data.append(row_to_add[:len(row_to_add)-1])
                self.target.append(row_to_add[-1])

    def get_symbol(self):
        return self.symbol
    
    def _prep_data(self, row: list) -> list:
        '''
        Replaces all Xs with 1s and Os with -1s, and replaces
        Ws with 1, Ds with 0 and Ls with -1

        Params:
        row (list) - a list in the game_results_ttt.txt file

        Retuns a new list of 1, -1 and either W, D or L
        '''
        new_row = []

        for r in row:
            if r == "X" or r == "W":
                new_row.append(1)
            elif r == "O" or r == "L":
                new_row.append(-1)
            elif r == "_" or r == "D":
                new_row.append(0)
            else:
                new_row.append(r)

        return new_row
    
    def make_move(self, game_state: list):
        '''
        Param:
        game_state (list) - an object representing the current grid of the game

        Returns an int of the index to place the CPU's symbol
        '''
        # TODO: Add a step here that makes a move based on what's more likely
        # for it to get that W.
