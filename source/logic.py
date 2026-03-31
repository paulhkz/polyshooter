"""
handles all the input logic
"""
import os
from word_retriever import get_word_repo
from story import Story, SolidHasHit

WORD_REPO_NAME = "wordrepo.txt"

def run_guess_loop(single_play: SinglePlay, word: str, heading_to_player: bool) -> bool:
    """
    Purpose: run the guess loop for one word.
    Returns True if the player won, False if SolidHasHit was raised.
    If heading_to_player is True, kills the process on SolidHasHit instead of returning False.
    """
    single_play.guess_once(True)
    while True:
        try:
            os.system("clear")
            if single_play.guess_once():
                return True
        except SolidHasHit:
            if heading_to_player:
                os.kill(os.getpid(), 14)
            print("Oh oh. Der Körper ist eingeschlagen.")
            print(
                "Es stellt sich unter genauerer Untersuchung heraus, "
                f"dass es den Namen '{word}' hatte."
            )
            os.system("sleep 7")
            return False


def play_game() -> None:
    """
    Purpose: entry for the game play
    """
    word_repo = get_word_repo(WORD_REPO_NAME)

    word = word_repo.pop()
    single_play = SinglePlay(word)
    single_play.story.show_prelude()
    run_guess_loop(single_play, word, heading_to_player=True)

    while len(word_repo) > 0:
        word = word_repo.pop()
        single_play = SinglePlay(word)
        if not single_play.story.show_continuing_scene():
            break
        os.system("clear")
        run_guess_loop(single_play, word, heading_to_player=False)

class SinglePlay:
    """
    Purpose: a class having all the relevant information for a single play-through
    """
    def __init__(self, word: str) -> None:
        self.__word_list = list(word)
        self.__word_list_lowered_set = set(word.lower().replace(" ", ""))
        self.__correct_guesses: set[str] = set([])
        self.__faulty_guesses: set[str] = set([])

        self.story = Story()

    def guess_once(self, is_first_guess: bool = False) -> bool:
        """
        Purpose: Let's the player guess one word/character. Also shows story stuff.
        If it's the first_guess, we don't want to display that the guess was invalid.
        Returns True if the player has won, False otherwise.
        Throws a SolidHasHit-Exception if the body hit the ground.
        """
        hidden_word = self.get_word()
        correct_guesses_ratio = (
            len(self.__correct_guesses) / len(self.__word_list_lowered_set)
        )
        self.story.display_guess_feedback(
            self.__correct_guesses, self.__faulty_guesses, is_first_guess
        )
        self.story.display_calibration(hidden_word, correct_guesses_ratio)
        user_input = input("Dein guess:")
        if self.__add_input(validate_input(user_input)):
            return True
        return False

    def get_word(self) -> str:
        """
        Purpose: returns the word and hides the characters not guessed yet.
        """
        word = ""
        for c in self.__word_list:
            if c.lower() in self.__correct_guesses:
                word += c
                word += " "
            elif c.isspace():
                word += "\n"
            else:
                word += "_"
                word += " "

        return word

    def __add_input(self, user_input: str) -> bool:
        """
        Purpose: adds the characters from the input to the internal correct/faulty guesses-list.
        Returns True if the player has won. False otherwise.
        """
        for character in user_input:
            if character in self.__word_list_lowered_set:
                if character not in self.__correct_guesses:
                    self.__correct_guesses.add(character)
                    self.story.handle_correct_guess()

            else:
                if character not in self.__faulty_guesses:
                    self.__faulty_guesses.add(character)
                    self.story.handle_incorrect_guess()

        if len(self.__correct_guesses) == len(self.__word_list_lowered_set):
            self.story.handle_earth_saved("".join(self.__word_list))
            return True
        return False

def validate_input(input_str: str) -> str:
    """
    Purpose: filters the input for non-alphabetic characters, trims it and lower-cases it
    """
    return "".join(filter(lambda char: char.isalpha(), input_str)).strip().lower()
