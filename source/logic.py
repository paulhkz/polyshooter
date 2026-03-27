from word_retriever import WordRetriever
from story import Story
import sys

class Logic:
    def __init__(self):
        self.wordretriever = WordRetriever()

    def play(self):
        word = self.wordretriever.get_word()
        single_play = SinglePlay(word)
        print(word)
        while True:
            single_play.display_word()
            user_input = input("Dein guess:")

            is_correct = single_play.add_input(validate_input(user_input))

def validate_input(input: str) -> bool:
    return input.strip().lower()

class SinglePlay:
    def __init__(self, word: str):
        self.word_list = list(word)
        self.word_list_lowererd_set = set(word.lower().replace(" ", ""))
        self.correct_guesses = set([])
        self.faulty_guesses = set([])

        self.story = Story()

    def display_word(self):
        """
        Purpose: displays the word and hides the characters not guessed yet.
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

        print(word)
        
    def add_input(self, user_input: str) -> int:
        """
        Purpose: adds the characters from the input to the internal correct/fauly guesses-list.
        Returns:
            0 if character(s) was/were correctly guessed
            1 if character(s) was/were already guessed
            2 if at least one character was wrongly guessed
        """
        for character in user_input:
            if character in self.word_list_lowererd_set:
                if character not in self.correct_guesses:
                    self.correct_guesses.add(character)
                    self.story.handle_correct_guess()
                else:
                    self.story.handle_correct_guess()

            else:
                if character not in self.faulty_guesses:
                    self.faulty_guesses.add(character)
                    self.story.handle_incorrect_guess()
                else:
                    self.story.handle_incorrect_guess()

        if len(self.correct_guesses) == len(self.word_list_lowererd_set):
            self.story.handle_earth_saved()
