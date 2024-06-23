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
    def __init__(self) -> None:
        # The CPU is always "X" and the user will be "O"
        self.symbol = "X"

    def get_symbol(self) -> str:
        return self.symbol

    def make_move(self, game_state: list) -> int:
        '''
        Param:
        game_state (list) - an object representing the current grid of the game

        Returns an int of the index to 
        '''
        free_indexes = [
            i for i in range(len(game_state)) if game_state[i] == ""
        ]

        return choice(free_indexes)
