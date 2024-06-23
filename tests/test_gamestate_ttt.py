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
        index = cpu.make_move(gs.get_game_state())
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
        index = cpu.make_move(gs.get_game_state())
        gs.set_game_state(index, cpu.get_symbol())

        # Let the human (myself) put an item in the same place the CPU did
        free_spaces = [i for i in range(len(gs.get_game_state())) if gs.get_game_state()[i] == ""]
        gs.set_game_state(choice(free_spaces), "O")

        assert gs.is_done() == False
        assert gs.outcome == ""

    def test_gamestate_is_done_method_after_all_places_are_filled(self):
        base_dir = os.path.dirname(__file__)
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

        output_file = os.path.join(base_dir, "game_results_ttt.txt")

        assert gs.is_done() == True
        assert os.path.isfile(output_file)
        assert gs.outcome != ""

        os.remove(output_file)
