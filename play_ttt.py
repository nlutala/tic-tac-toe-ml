'''
This file is to be executed to play against the NaiveCPU or the MLCPU.

Nathan Lutala (nlutala)
'''

from gamestate_ttt import GameState
from naive_cpu import NaiveCPU
from tkinter import *
from tkinter import ttk, messagebox

class PlayTTT(ttk.Frame):
    def __init__(self, master=None) -> None:
        '''
        Creates the home page of the game
        '''
        self.master = master
        super().__init__(master, padding=20)
        self.pack()

        # Make the frame follow a grid format
        self.grid()

        # Add content to the frame
        ttk.Label(self, 
                  text="Tic-tac-Toe",
                  font="Kenney-Future"
                  ).grid(column=0, row=0, pady=5)
        Button(self, 
                text="Instructions",
                font="Kenney-Future",
                command=self.show_instructions
                ).grid(column=0, row=1, pady=5)
        Button(self, 
                text="Play Against Naive CPU",
                font="Kenney-Future",
                command=None).grid(column=0, row=2, pady=5)
        Button(self, 
                text="Play Against CPU using Machine Learning Model", 
                font="Kenney-Future",
                command=None).grid(column=0, row=3, pady=5)
        Button(self, 
                text="Quit", 
                font="Kenney-Future",
                command=root.destroy).grid(column=0, row=4, pady=5)
        
    def get_root(self):
        return self.master
    
    def show_instructions(self):
        messagebox.showinfo(
            title="Instructions", 
            message="The aim of the game is to get 3 'O's " +
                    "vertically, horizontally or diagonally " +
                    "before the CPU."
        )


root = Tk()
play_ttt = PlayTTT(root)
play_ttt.mainloop()

# button = ttk.Button(content)

# if __name__ == "__main__":
#     gs = GameState()
#     cpu = NaiveCPU()

#     while not gs.is_done():
#         for i in range(0, len(gs.get_game_state()), 3):
#             print(" ".join(gs.get_game_state()[i:i+3]))
        
#         user_position = int(input('''
# Your turn.
# Enter the position you would like to place your "O".
#             '''))
        
#         gs.set_game_state(user_position, "O")
#         gs.set_game_state(cpu.make_move(gs.get_game_state()), cpu.get_symbol())

#     if gs.outcome == "W":
#         print("Unfortunately you lost that game.")
#     elif gs.outcome == "D":
#         print("It was a tie!")
#     else:
#         print("You won!")

#     print("\nThe results of this game was written to a text file.")
