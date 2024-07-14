'''
Test the functionality of the MLCPU class

Nathan Lutala (nlutala)
'''
import unittest
from ml_cpu import MLCPU
from naive_cpu import NaiveCPU
from gamestate_ttt import GameState

class TestMLCPU(unittest.TestCase):
    def test_make_move_returns_index_that_is_not_already_taken(self):
        gs = GameState()
        naive_cpu = NaiveCPU("O")
        ml_cpu = MLCPU("X")

        gs.set_game_state(
            naive_cpu.make_move(gs.get_available_positions()), naive_cpu.get_symbol()
        )

        game_state = gs.get_game_state()
        available_positions = gs.get_available_positions()

        assert game_state[ml_cpu.make_move(game_state, available_positions)] == "_"
