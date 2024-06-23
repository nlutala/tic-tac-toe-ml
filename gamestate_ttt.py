'''
An object that collects all the data about the tic-tac-toe game.
The data will be used to help ensure seamless gameplay as well as
help write/append to a text file (which will be used as training data)
for the version of the CPU that uses a ML model.

Nathan Lutala (nlutala)
'''
class GameState:
    def __init__(self) -> None:
        '''
        self.outcome will either be set to:
        W (for win), D (for draw), L (loss)
        from the CPU's perspective
        '''
        self.outcome = ""
        # Set up the grid for the tic-tac-toe game
        self.game_state = ["" for i in range(9)]

    def get_game_state(self) -> list:
        return self.game_state
    
    def set_game_state(self, index: int, symbol: str) -> None:
        '''
        Adds the symbol of the player at the index of the game_state
        they have specified.

        Params:
        index (int) - the index of the game_state
        symbol (str) - either "X" or "O"
        '''
        if self.game_state[index] != "":
            raise ValueError(f"This position has already been taken. Place an {symbol} where there is a free space.")
        else:
            self.game_state[index] = symbol
