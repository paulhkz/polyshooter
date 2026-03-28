import os
from word_retriever import WordRetriever
from story import Story, SolidHasHit

class Logic:
    def __init__(self) -> None:
        self.wordretriever = WordRetriever()

    def play(self) -> None:
        word = self.wordretriever.get_word()
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

def validate_input(input_str: str) -> str:
    """
    Purpose: removes leading 
    """
    return "".join(filter(lambda char: char.isalpha(), input_str)).strip().lower()


class SinglePlay:
    def __init__(self, word: str) -> None:
        self.word_list = list(word)
        self.word_list_lowererd_set = set(word.lower().replace(" ", ""))
        self.correct_guesses = set([])
        self.faulty_guesses = set([])

        self.story = Story()

    def guess_once(self, is_first_guess: bool = False) -> None:
        """
        Purpose: Let's the player guess one word/character. Also shows story stuff.
        If it's the first_guess, we don't want to display that the guess was invalid.
        """
        hidden_word = self.get_word()
        correct_guesses_ratio =  len(self.correct_guesses) / len(self.word_list_lowererd_set)
        self.story.display_last_guess_stats(self.correct_guesses, self.faulty_guesses, hidden_word, correct_guesses_ratio, is_first_guess)
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
