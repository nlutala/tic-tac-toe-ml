'''
Test the functionality of the NaiveCPU class
'''
import unittest, random
from naive_cpu import NaiveCPU

class TestNaiveCPU(unittest.TestCase):
    def test_make_move_returns_index_that_is_not_already_taken(self):
        indexes_to_add_os = list(set([random.randint(0,8) for i in range(4)]))
        game_state = ["" for i in range(9)]

        for index in indexes_to_add_os:
            game_state[index] = "O"

        naive_cpu = NaiveCPU("X")
        assert game_state[naive_cpu.make_move(game_state)] == ""
