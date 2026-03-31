"""source/story.py"""
import unittest
from unittest.mock import patch

from source.story import Story, SolidHasHit, MAX_ATTEMPTS

class TestStoryGuessHandling(unittest.TestCase):
    """correct/incorrect guess-tracking"""

    def test_correct_guess_does_not_raise(self):
        story = Story()
        story.handle_correct_guess() # must not raise

    def test_incorrect_guess_below_limit_does_not_raise(self):
        story = Story()
        for _ in range(MAX_ATTEMPTS - 1):
            story.handle_incorrect_guess()

    @patch('builtins.print')
    def test_game_over_raised_after_max_incorrect_guesses(self, _mock_print):
        story = Story()
        with self.assertRaises(SolidHasHit):
            for _ in range(MAX_ATTEMPTS):
                story.handle_incorrect_guess()

class TestStoryDisplayFeedback(unittest.TestCase):
    """Story.display_guess_feedback"""

    @patch('builtins.print')
    def test_nothing_happened_when_no_hits_and_not_first_guess(self, mock_print):
        story = Story()
        story.display_guess_feedback(set(), set(), is_first_guess=False)
        output = " ".join(str(c) for c in mock_print.call_args_list)
        self.assertIn("Nichts", output)

    @patch('builtins.print')
    def test_no_nothing_happened_on_first_guess(self, mock_print):
        # when we start the game we do not want that message there
        story = Story()
        story.display_guess_feedback(set(), set(), is_first_guess=True)
        output = " ".join(str(c) for c in mock_print.call_args_list)
        self.assertNotIn("Nichts", output)

    @patch('builtins.print')
    def test_single_correct_hit_prints_richtig(self, mock_print):
        story = Story()
        story.handle_correct_guess()
        story.display_guess_feedback({'a'}, set(), is_first_guess=False)
        output = " ".join(str(c) for c in mock_print.call_args_list)
        self.assertIn("Richtig", output)

    @patch('builtins.print')
    def test_multiple_correct_hits_shows_count(self, mock_print):
        story = Story()
        story.handle_correct_guess()
        story.handle_correct_guess()
        story.display_guess_feedback({'a', 'b'}, set(), is_first_guess=False)
        output = " ".join(str(c) for c in mock_print.call_args_list)
        self.assertIn("2 Mal", output)

    @patch('builtins.print')
    def test_single_faulty_hit_prints_oh_nein(self, mock_print):
        story = Story()
        story.handle_incorrect_guess()
        story.display_guess_feedback(set(), {'z'}, is_first_guess=False)
        output = " ".join(str(c) for c in mock_print.call_args_list)
        self.assertIn("Oh nein", output)

    @patch('builtins.print')
    def test_multiple_faulty_hits_shows_count(self, mock_print):
        story = Story()
        story.handle_incorrect_guess()
        story.handle_incorrect_guess()
        story.display_guess_feedback(set(), {'z', 'x'}, is_first_guess=False)
        output = " ".join(str(c) for c in mock_print.call_args_list)
        self.assertIn("2 Mal", output)

    @patch('builtins.print')
    def test_hit_counters_reset_after_display(self, _mock_print):
        story = Story()
        story.handle_correct_guess()
        story.display_guess_feedback({'a'}, set(), is_first_guess=False)
        # second call should show "Nichts" since counters were reset
        story.display_guess_feedback({'a'}, set(), is_first_guess=False)
        last_output = " ".join(
            str(c) for c in _mock_print.call_args_list
        )
        self.assertIn("Nichts", last_output)

class TestStoryDisplayCalibration(unittest.TestCase):
    """Story.display_calibration"""

    @patch('builtins.print')
    def test_zero_ratio_calls_print(self, mock_print):
        story = Story()
        story.display_calibration("_ _ _ _", 0.0)
        output = " ".join(str(c) for c in mock_print.call_args_list)
        self.assertIn("0.00%", output)

class TestStoryShowContinuingScene(unittest.TestCase):
    """Story.show_continuing_scene"""

    @patch('source.story.os.system')
    @patch('builtins.print')
    @patch('builtins.input', return_value='y')
    def test_yes_returns_true(self, _mock_input, _mock_print, _mock_os):
        story = Story()
        self.assertTrue(story.show_continuing_scene())

    @patch('source.story.os.system')
    @patch('builtins.print')
    @patch('builtins.input', side_effect=['n', ''])
    def test_other_returns_false(self, _mock_input, _mock_print, _mock_os):
        story = Story()
        self.assertFalse(story.show_continuing_scene())
        self.assertFalse(story.show_continuing_scene())

if __name__ == '__main__':
    unittest.main()
