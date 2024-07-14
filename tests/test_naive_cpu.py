'''
Test the functionality of the NaiveCPU class

Nathan Lutala (nlutala)
'''
import unittest, random
from naive_cpu import NaiveCPU
from gamestate_ttt import GameState

class TestNaiveCPU(unittest.TestCase):
    def test_make_move_returns_index_that_is_not_already_taken(self):
        gs = GameState()
        naive_cpu = NaiveCPU()
        indexes_to_add_os = list(set([random.randint(0,8) for i in range(4)]))

        for index in indexes_to_add_os:
            gs.set_game_state(index, naive_cpu.get_symbol())

        assert naive_cpu.make_move(gs.get_available_positions()) not in indexes_to_add_os
