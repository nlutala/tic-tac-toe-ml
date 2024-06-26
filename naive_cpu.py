'''
A CPU for the tic-tac-toe game that makes random decisions as to where it will
place it's "X"

Nathan Lutala (nlutala)
'''
from secrets import choice

class NaiveCPU:
    '''
    An object for the naive CPU to play tic-tac-toe against.
    '''
    def __init__(self, symbol="X") -> ValueError:
        '''
        Param:
        symbol (str) - rather a character (either "X" or "O").
        By default the CPU is always "X" and the user will be "O"
        '''
        self.symbol = symbol

        if self.symbol.upper() not in ["X", "O"]:
            raise ValueError("Incorrect input. Expected either 'X' or 'O'.")

    def get_symbol(self) -> str:
        return self.symbol

    def make_move(self, free_indexes: list) -> int:
        '''
        Param:
        game_state (list) - a list of all the indexes that can be used

        Returns an int of the index to place the CPU's symbol
        '''
        return choice(free_indexes)
