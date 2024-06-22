import random

class NaiveCPU:
    '''
    An object for the naive CPU to play tic-tac-toe against.
    '''
    def __init__(self, symbol: str) -> None:
        '''
        Param:
        symbol (str) - a character either "X" or "O"
        '''
        self.symbol = symbol

    def get_symbol(self) -> str:
        return self.get_symbol

    def make_move(self, game_state: list) -> int:
        '''
        Param:
        game_state (list) - an object representing the current grid of the game

        Returns an int of the index to 
        '''
        free_indexes = [
            i for i in range(len(game_state)) if game_state[i] == ""
        ]

        return free_indexes[random.randint(0,len(free_indexes))]

