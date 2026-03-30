"""source/game.py"""
import sys
import os
import unittest
from unittest.mock import patch

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'source'))

from game import main

class TestMain(unittest.TestCase):
    @patch('game.play_game')
    def test_main_calls_play_game(self, mock_play_game):
        main()
        mock_play_game.assert_called_once()

if __name__ == '__main__':
    unittest.main()
