'''
A short script that plays 100 games to write the results to a text file
to eventually be used by a CPU that uses machine learning.

Nathan Lutala (nlutala)
'''

from gamestate_ttt import GameState
from naive_cpu import NaiveCPU
from secrets import choice


if __name__ == "__main__":
    for i in range(100):
        gs = GameState()
        cpu = NaiveCPU()

        while gs.get_game_state().count("") != 0:
            # Let the Naive CPU put an item in place first
            index = cpu.make_move(gs.get_game_state())
            gs.set_game_state(index, cpu.get_symbol())

            # Let the human (myself) put an item in the same place the CPU did
            free_spaces = [i for i in range(len(gs.get_game_state())) if gs.get_game_state()[i] == ""]
            try:
                gs.set_game_state(choice(free_spaces), "O")
            except IndexError:
                break

        gs.write_results_to_file()
        