"""source/logic.py"""
import sys
import os
import unittest
from unittest.mock import patch, Mock

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'source'))

from logic import validate_input, SinglePlay, run_guess_loop
from story import SolidHasHit

class TestValidateInput(unittest.TestCase):
    """validate_input"""

    def test_uppercase_is_lowercased(self):
        self.assertEqual(validate_input("ABC"), "abc")

    def test_non_alpha_chars_removed(self):
        self.assertEqual(validate_input("a1b!c?"), "abc")

    def test_spaces_removed(self):
        self.assertEqual(validate_input("a b c"), "abc")

    def test_numbers_removed(self):
        self.assertEqual(validate_input("1234"), "")

    def test_empty_string(self):
        self.assertEqual(validate_input(""), "")

class TestSinglePlayGetWord(unittest.TestCase):
    """SinglePlay._SinglePlay__get_word"""

    def test_all_hidden_initially(self):
        play = SinglePlay("word")
        self.assertEqual(play._SinglePlay__get_word(), "_ _ _ _ ")

    def test_guessed_letter_revealed(self):
        play = SinglePlay("wword")
        play._SinglePlay__correct_guesses.add('w')
        self.assertEqual(play._SinglePlay__get_word(), "w w _ _ _ ")

    def test_all_letters_revealed(self):
        play = SinglePlay("word")
        play._SinglePlay__correct_guesses = {'w', 'o', 'r', 'd'}
        self.assertEqual(play._SinglePlay__get_word(), "w o r d ")

    def test_space_in_word_becomes_newline(self):
        play = SinglePlay("a b")
        self.assertIn("\n", play._SinglePlay__get_word())

class TestSinglePlayAddInput(unittest.TestCase):
    """SinglePlay._SinglePlay__add_input"""

    def setUp(self):
        self.play = SinglePlay("word")

    def test_correct_letter_added_to_correct_guesses(self):
        self.play._SinglePlay__add_input("w")
        self.assertIn("w", self.play._SinglePlay__correct_guesses)

    def test_wrong_letter_added_to_faulty_guesses(self):
        self.play._SinglePlay__add_input("z")
        self.assertIn("z", self.play._SinglePlay__faulty_guesses)

    def test_partial_correct_guess_returns_false(self):
        self.assertFalse(self.play._SinglePlay__add_input("w"))

    @patch('os.system')
    @patch('builtins.print')
    def test_all_letters_guessed_returns_true(self, _mock_print, _mock_os):
        self.assertTrue(self.play._SinglePlay__add_input("word"))

    @patch('builtins.print')
    def test_game_over_after_enough_wrong_guesses(self, _mock_print):
        with self.assertRaises(SolidHasHit):
            self.play._SinglePlay__add_input("zxqv")

class TestSinglePlayGuessOnce(unittest.TestCase):
    """SinglePlay.guess_once"""

    @patch('builtins.input', return_value='w')
    @patch('builtins.print')
    def test_not_won_returns_false(self, _mock_print, _mock_input):
        play = SinglePlay("word")
        self.assertFalse(play.guess_once(is_first_guess=True))

    @patch('builtins.input', side_effect=['w', 'o', 'r', 'd'])
    @patch('os.system')
    @patch('builtins.print')
    def test_correct_guesses_eventually_win(self, _mock_print, _mock_os, _mock_input):
        play = SinglePlay("word")
        play.guess_once(is_first_guess=True) # guesses 'w'
        play.guess_once() # guesses 'o'
        play.guess_once() # guesses 'r'
        self.assertTrue(play.guess_once()) # guesses 'd' → win

class TestRunGuessLoop(unittest.TestCase):
    """run_guess_loop"""

    @patch('os.system')
    @patch('builtins.print')
    def test_player_wins_returns_true(self, _mock_print, _mock_os):
        play = SinglePlay("word")
        play.guess_once = Mock(side_effect=[False, True])
        result = run_guess_loop(play, "word", heading_to_player=False)
        self.assertTrue(result)

    @patch('os.system')
    @patch('builtins.print')
    def test_solid_hits_other_team_returns_false(self, _mock_print, _mock_os):
        play = SinglePlay("word")
        play.guess_once = Mock(side_effect=[False, SolidHasHit()])
        result = run_guess_loop(play, "word", heading_to_player=False)
        self.assertFalse(result)

    @patch('os.kill')
    @patch('os.system')
    @patch('builtins.print')
    def test_solid_hits_player_calls_os_kill(self, _mock_print, _mock_os, mock_kill):
        play = SinglePlay("word")
        play.guess_once = Mock(side_effect=[False, SolidHasHit()])
        run_guess_loop(play, "word", heading_to_player=True)
        self.assertTrue(mock_kill.called)

if __name__ == '__main__':
    unittest.main()
