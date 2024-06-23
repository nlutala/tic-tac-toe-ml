'''
An object that collects all the data about the tic-tac-toe game.
The data will be used to help ensure seamless gameplay as well as
help write/append to a text file (which will be used as training data)
for the version of the CPU that uses a ML model.

Nathan Lutala (nlutala)
'''
import os

class GameState:
    def __init__(self, write_to_file=True) -> None:
        '''
        self.outcome will either be set to:
        W (for win), D (for draw), L (loss)
        from the CPU's perspective

        Parameter
        write_to_file (bool) - optional boolean value for whether to write to a
        text file
        '''
        self.outcome = ""
        # Set up the grid for the tic-tac-toe game
        self.game_state = ["" for i in range(9)]
        self.write_to_file = write_to_file

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

    def is_done(self) -> bool:
        '''
        Method to determine whether the game is done and who won.

        Returns True if there is a winner or all parts of the grid
        have been filled out. False otherwise
        '''
        is_done = True

        if self.game_state[0] == self.game_state[1] and self.game_state[1] == self.game_state[2] and self.game_state[0] != "":
            if self.game_state[0] == "X":
                self.outcome = "W"
            else:
                self.outcome = "L"
        elif self.game_state[3] == self.game_state[4] and self.game_state[4] == self.game_state[5] and self.game_state[3] != "":
            if self.game_state[3] == "X":
                self.outcome = "W"
            else:
                self.outcome = "L"
        elif self.game_state[6] == self.game_state[7] and self.game_state[7] == self.game_state[8] and self.game_state[6] != "":
            if self.game_state[6] == "X":
                self.outcome = "W"
            else:
                self.outcome = "L"
        elif self.game_state[0] == self.game_state[3] and self.game_state[3] == self.game_state[6] and self.game_state[0] != "":
            if self.game_state[0] == "X":
                self.outcome = "W"
            else:
                self.outcome = "L"
        elif self.game_state[1] == self.game_state[4] and self.game_state[4] == self.game_state[7] and self.game_state[1] != "":
            if self.game_state[1] == "X":
                self.outcome = "W"
            else:
                self.outcome = "L"
        elif self.game_state[2] == self.game_state[5] and self.game_state[5] == self.game_state[8] and self.game_state[2] != "":
            if self.game_state[2] == "X":
                self.outcome = "W"
            else:
                self.outcome = "L"
        elif self.game_state[0] == self.game_state[4] and self.game_state[4] == self.game_state[8] and self.game_state[0] != "":
            if self.game_state[0] == "X":
                self.outcome = "W"
            else:
                self.outcome = "L"
        elif self.game_state[2] == self.game_state[4] and self.game_state[4] == self.game_state[6] and self.game_state[2] != "":
            if self.game_state[2] == "X":
                self.outcome = "W"
            else:
                self.outcome = "L"
        elif self.game_state.count("") == 0:
            self.outcome = "D"
        else:
            is_done = False

        if is_done:
            self._write_results_to_file()
        
        return is_done

    def _write_results_to_file(self) -> None:
        '''
        Private function to write the results of the game to a file
        '''
        if "game_results_ttt.txt" not in os.listdir():
            with open("game_results_ttt.txt", "w") as file:
                file.write("".join(self.game_state) + self.outcome)
        else:
            with open("game_results_ttt.txt", "a") as file:
                file.write("".join(self.game_state) + self.outcome)
