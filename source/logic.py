from word_retriever import WordRetriever
from story import Story

class Logic:
    def __init__(self):
        self.wordretriever = WordRetriever()
        self.story = Story()
        
    def play(self):
        word = self.wordretriever.get_word()
        single_play = SinglePlay(word)
        print(word)
        while True:
            single_play.display_word()
            user_input = input("Dein guess:")

            is_correct = single_play.add_input(user_input)
            if is_correct == 0:
                self.story.handle_correct_guess()
            elif is_correct == 2:
                self.story.handle_incorrect_guess()
                
def input_validator(input: str) -> bool:
    # TODO: strip
    pass

class SinglePlay:
    def __init__(self, word: str):
        self.word_list = list(word)
        self.correct_guesses = []
        self.faulty_guesses = []
        self.rem_guesses = 5

    def display_word(self):
        """
        Purpose: displays the word and hides the characters not guessed yet.
        """
        word = ""
        for c in self.word_list:
            if c in self.correct_guesses:
                word += c
            elif c.isspace():
                word += " "
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
            if character in self.word_list:
                if character not in self.correct_guesses:
                    self.correct_guesses.append(character)
            else:
                self.faulty_guesses.append(character)
                self.rem_guesses -= 1
