'''
A short script that plays 100 games to write the results to a text file
to eventually be used by a CPU that uses machine learning.

Nathan Lutala (nlutala)
'''

from gamestate_ttt import GameState
from naive_cpu import NaiveCPU
from secrets import choice


def create_game_data(games=100):
    '''
    Plays a game between two naive CPUs and writes the
    result of the game to a file called "game_results_ttt.txt"
    '''
    for i in range(games):
        gs = GameState()
        cpu_1 = NaiveCPU("X")
        cpu_2 = NaiveCPU("O")

        while gs.get_game_state().count("") != 0:
            # Let the Naive CPU put an item in place first
            try:
                index = cpu_1.make_move(gs.get_game_state())
                gs.set_game_state(index, cpu_1.get_symbol())

                index = cpu_2.make_move(gs.get_game_state())
                gs.set_game_state(index, cpu_2.get_symbol())
            except IndexError:
                break

        gs.write_results_to_file()


if __name__ == "__main__":
    create_game_data()
        