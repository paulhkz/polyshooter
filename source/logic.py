"""
handles all the input logic
"""
import os
from word_retriever import get_word_repo
from story import Story, SolidHasHit

WORD_REPO_NAME = "wordrepo.txt"

def play_game() -> None:
    """
    Purpose: entry for the game play
    """
    word_repo = get_word_repo(WORD_REPO_NAME)
    word = word_repo.pop()
    single_play = SinglePlay(word)
    print(word)

    single_play.guess_once(True)
    while True:
        try:
            os.system("clear")

            single_play.guess_once()
        except SolidHasHit:
            os.kill(os.getpid(), 14)
            break

class SinglePlay:
    """
    Purpose: a class having all the relevant information for a single play-through
    """
    def __init__(self, word: str) -> None:
        self.word_list = list(word)
        self.word_list_lowererd_set = set(word.lower().replace(" ", ""))
        self.correct_guesses: set[str] = set([])
        self.faulty_guesses: set[str] = set([])

        self.story = Story()

    def guess_once(self, is_first_guess: bool = False) -> None:
        """
        Purpose: Let's the player guess one word/character. Also shows story stuff.
        If it's the first_guess, we don't want to display that the guess was invalid.
        """
        hidden_word = self.get_word()
        correct_guesses_ratio = (
            len(self.correct_guesses) / len(self.word_list_lowererd_set)
        )
        self.story.display_guess_feedback(
            self.correct_guesses, self.faulty_guesses, is_first_guess
        )
        self.story.display_calibration(hidden_word, correct_guesses_ratio)
        user_input = input("Dein guess:")
        self.add_input(validate_input(user_input))

    def add_input(self, user_input: str) -> None:
        """
        Purpose: adds the characters from the input to the internal correct/fauly guesses-list.
        """
        for character in user_input:
            if character in self.word_list_lowererd_set:
                if character not in self.correct_guesses:
                    self.correct_guesses.add(character)
                    self.story.handle_correct_guess()

            else:
                if character not in self.faulty_guesses:
                    self.faulty_guesses.add(character)
                    self.story.handle_incorrect_guess()

        if len(self.correct_guesses) == len(self.word_list_lowererd_set):
            self.story.handle_earth_saved()

    def get_word(self) -> str:
        """
        Purpose: returns the word and hides the characters not guessed yet.
        """
        word = ""
        for c in self.word_list:
            if c.lower() in self.correct_guesses:
                word += c
                word += " "
            elif c.isspace():
                word += "\n"
            else:
                word += "_"
                word += " "

        return word

def validate_input(input_str: str) -> str:
    """
    Purpose: removes leading 
    """
    return "".join(filter(lambda char: char.isalpha(), input_str)).strip().lower()
