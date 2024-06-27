'''
Test the functionality of the GameState class

Nathan Lutala (nlutala)
'''
from gamestate_ttt import GameState
from naive_cpu import NaiveCPU
from secrets import choice
import os, unittest

class TestGameState(unittest.TestCase):
    def test_gamestate_raises_value_error_if_player_tries_to_put_symbol_on_taken_place(self):
        gs = GameState()

        # Let the Naive CPU put an item in place first
        cpu = NaiveCPU()
        index = cpu.make_move(gs.get_available_positions())
        gs.set_game_state(index, cpu.get_symbol())

        # Let the human (myself) put an item in the same place the CPU did
        with self.assertRaises(ValueError):
            gs.set_game_state(index, "O")

        # Let the Naive CPU put an item in the same place again
        with self.assertRaises(ValueError):
            gs.set_game_state(index, cpu.get_symbol())

    def test_gamestate_is_done_method_after_two_moves(self):
        gs = GameState()

        # Let the Naive CPU put an item in place first
        cpu = NaiveCPU()
        index = cpu.make_move(gs.get_available_positions())
        gs.set_game_state(index, cpu.get_symbol())

        # Let the human (myself) put an item in the same place the CPU did
        free_spaces = gs.get_available_positions()
        gs.set_game_state(choice(free_spaces), "O")

        assert gs.is_done() == False
        assert gs.outcome == ""

    def test_gamestate_is_done_method_after_all_places_are_filled(self):
        base_dir = os.path.dirname(__file__)
        gs = GameState()
        cpu = NaiveCPU()

        while gs.get_game_state().count("_") != 0:
            # Let the Naive CPU put an item in place first
            index = cpu.make_move(gs.get_available_positions())
            gs.set_game_state(index, cpu.get_symbol())

            # Let the human (myself) put an item in the same place the CPU did
            try:
                gs.set_game_state(choice(gs.get_available_positions()), "O")
            except IndexError:
                break

        gs.write_results_to_file()

        parent_directory = os.path.abspath(os.path.join(base_dir, os.pardir))
        output_file = os.path.join(parent_directory, "assets", "game_results_ttt.txt")
        print(output_file)

        assert gs.is_done() == True
        assert os.path.isfile(output_file)
        assert gs.outcome != ""

        os.remove(output_file)
