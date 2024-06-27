'''
A short script that plays 100 games to write the results to a text file
to eventually be used by a CPU that uses machine learning.

Nathan Lutala (nlutala)
'''

from gamestate_ttt import GameState
from naive_cpu import NaiveCPU
from secrets import choice
import os


def write_results_to_file(grid: list, move: int) -> None:
    '''
    Write the move the user inputted and the grid to a file.

    Params:
    grid (list) - a representation of the grid as a list
    move (int) - the index that the user would put their "X"
    '''
    if "ttt_good_moves.txt" not in os.listdir():
        with open("ttt_good_moves.txt", "w") as file:
            file.write("".join(grid) + str(move) + "\n")
    else:
        with open("ttt_good_moves.txt", "a") as file:
            file.write("".join(grid) + str(move) + "\n")

def create_game_data(games=100) -> None:
    '''
    Generates 100 different random scenarios between you and
    the CPU and writes the grid and your move to a file called
    "ttt_good_moves.txt"

    Params:
    games (int) - optional integer value for how many situations
    to generate. The default is set to 100.
    '''
    for i in range(games):
        gs = GameState()
        cpu_1 = NaiveCPU("X")
        cpu_2 = NaiveCPU("O")

        moves = [0, 1, 2, 3, 4]
        index = choice(moves)

        for i in range(index):
            cpu_1_turn = cpu_1.make_move(gs.get_available_positions())
            gs.set_game_state(cpu_1_turn, cpu_1.get_symbol())

            cpu_2_turn = cpu_2.make_move(gs.get_available_positions())
            gs.set_game_state(cpu_2_turn, cpu_2.get_symbol())

        if gs.is_done():
            games += 1
            continue
        else:
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

def create_game_data_real() -> None:
    '''
    Different random scenarios where the cpu has lost and removes
    one of each player's moves at random from game_results_ttt.txt.
    Then you are prompted to act as if you're the cpu to know what
    move you should have made and write it to "ttt_good_moves.txt".
    '''
    game_states = []
    if "game_results_ttt.txt" in os.listdir():
        with open("game_results_ttt.txt", "r") as file:
            for row in file:
                gs = GameState()
                game_state = list(row)[:len(row)-2]

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
    # create_game_data()
    create_game_data_real()
        