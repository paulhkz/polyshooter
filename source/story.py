DEFAULT_ATTEMPTS = 5

class Story:
    def __init__(self):
        self.incorrect_guesses = 5
    
    def handle_correct_guess(self):
        print("congrats")
    
    def handle_incorrect_guess(self):
        self.incorrect_guesses -= 1
        print("guesses left:", self.incorrect_guesses)