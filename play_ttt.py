'''
This file is to be executed to play against the NaiveCPU or the MLCPU.

Nathan Lutala (nlutala)
'''

from gamestate_ttt import GameState
from naive_cpu import NaiveCPU

if __name__ == "__main__":
    gs = GameState()
    cpu = NaiveCPU()

    while not gs.is_done():
        for i in range(0, len(gs.get_game_state()), 3):
            print(" ".join(gs.get_game_state()[i:i+3]))
        
        user_position = int(input('''
Your turn.
Enter the position you would like to place your "O".
            '''))
        
        gs.set_game_state(user_position, "O")
        gs.set_game_state(cpu.make_move(gs.get_game_state()), cpu.get_symbol())

    if gs.outcome == "W":
        print("Unfortunately you lost that game.")
    elif gs.outcome == "D":
        print("It was a tie!")
    else:
        print("You won!")

    print("\nThe results of this game was written to a text file.")
