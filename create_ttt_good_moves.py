'''
A short script that plays 100 games to write the results to a text file
to eventually be used by a CPU that uses machine learning.

Nathan Lutala (nlutala)
'''

from gamestate_ttt import GameState
from secrets import choice
import os


def write_results_to_file(grid: list, move: int) -> None:
    '''
    Write the move the user inputted and the grid to a file.

    Params:
    grid (list) - a representation of the grid as a list
    move (int) - the index that the user would put their "X"
    '''
    if "ttt_good_moves.txt" not in os.listdir('assets'):
        with open("assets/ttt_good_moves.txt", "w") as file:
            file.write("".join(grid) + str(move) + "\n")
    else:
        with open("assets/ttt_good_moves.txt", "a") as file:
            file.write("".join(grid) + str(move) + "\n")

def learn_from_real_game_data() -> None:
    '''
    Different random scenarios where the cpu has lost and removes
    one of each player's moves at random from game_results_ttt.txt.
    Then you are prompted to act as if you're the cpu to know what
    move you should have made and write it to "ttt_good_moves.txt".
    '''
    game_states = []
    if "game_results_ttt.txt" in os.listdir('assets'):
        with open("assets/game_results_ttt.txt", "r") as file:
            for row in file:
                gs = GameState()
                game_state = list(row)[:len(row)-2]

                player_positions = [
                    i for i in range(len(game_state))
                    if game_state[i] == "O"    
                ]

                remove_player_position = choice(player_positions)

                game_state[remove_player_position] = "_"

                cpu_positions = [
                    i for i in range(len(game_state))
                    if game_state[i] == "X"    
                ]

                remove_cpu_position = choice(cpu_positions)

                game_state[remove_cpu_position] = "_"

                game_states.append(game_state)

    for game in game_states:
        for i in range(len(game)):
            gs = GameState()

            if game[i] != "_":
                gs.set_game_state(i, game[i])

            taken_places = ["_" for i in range(9)]

            for i in range(len(gs.get_game_state())):
                if gs.get_game_state()[i] == "_":
                    taken_places[i] = i
                else:
                    taken_places[i] = "X"

            for i in range(0, len(taken_places), 3):
                print(taken_places[i:i+3])

            print("")

            print("This is how the current grid looks like below: \n")

            for i in range(0, len(gs.get_game_state()), 3):
                print(gs.get_game_state()[i:i+3])

            available_positions = gs.get_available_positions()
            best_choice = int(input('''
If you were the player represented with the X, what would be your next move to
win the game?
'''))
        
            while best_choice not in available_positions:
                print("There was something wrong with your input.")
                best_choice = int(input('''
If you were the player represented with the X, what would be your next move to
win the game?
'''))

            write_results_to_file(gs.get_game_state(), best_choice)


if __name__ == "__main__":
    learn_from_real_game_data()
        