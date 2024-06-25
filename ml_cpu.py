'''
A CPU for the tic-tac-toe game that is based on a machine learning model.
It will use this insight to decide where to place it's "X".

Nathan Lutala (nlutala)
'''

from create_ttt_game_data import create_game_data
from sklearn import tree
from sklearn.model_selection import train_test_split
import numpy as np
import os

class MLCPU:
    def __init__(self, symbol="X"):
        self.symbol = symbol
        self.ttt_moves_tree = tree.DecisionTreeClassifier(criterion="entropy")
        self.data = []

        if self.symbol.upper() not in ["X", "O"]:
            raise ValueError("Incorrect input. Expected either 'X' or 'O'.")

        if "game_results_ttt.txt" not in os.listdir():
            create_game_data()

        with open("game_results_ttt.txt") as file:
            for row in file:
                self.data.append(row)

        # TODO: Add a step here that trains the machine learning model

    def get_symbol(self):
        return self.symbol
    
    def make_move(self, game_state: list):
        '''
        Param:
        game_state (list) - an object representing the current grid of the game

        Returns an int of the index to place the CPU's symbol
        '''
        # TODO: Add a step here that makes a move based on what's more likely
        # for it to get that W.
        pass
