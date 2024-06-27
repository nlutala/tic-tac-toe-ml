'''
This file is to be executed to play against the NaiveCPU or the MLCPU.

Nathan Lutala (nlutala)
'''

from gamestate_ttt import GameState
from naive_cpu import NaiveCPU


if __name__ == "__main__":
    gs = GameState()
    cpu = NaiveCPU()

    taken_places = ["_" for i in range(9)]

    while not gs.is_done():
        for i in range(len(gs.get_game_state())):
            if gs.get_game_state()[i] == "_":
                taken_places[i] = i
            else:
                taken_places[i] = "X"
            
        print('''
The grid below shows the numbers you can enter to place your "O".
Places marked with an "X" are places that have already been used.
''')
        for i in range(0, len(taken_places), 3):
            print(taken_places[i:i+3])

        print("")

        for i in range(0, len(gs.get_game_state()), 3):
            print(gs.get_game_state()[i:i+3])
        
        user_position = int(input('''
Your turn.
Enter the position you would like to place your "O".
            '''))
        
        gs.set_game_state(user_position, "O")
        if gs.is_done():
            break
        else:
            gs.set_game_state(cpu.make_move(gs.get_game_state()), cpu.get_symbol())

    gs.write_results_to_file()

    if gs.outcome == "W":
        print("Unfortunately you lost that game.")
    elif gs.outcome == "D":
        print("It was a tie!")
    else:
        print("You won!")

    print("\nThe results of this game was written to a text file called: game_results_ttt.txt")
