DEFAULT_ATTEMPTS = 5

class Story:
    def __init__(self):
        self.rem_guesses = DEFAULT_ATTEMPTS

    def handle_correct_guess(self):
        print("congrats")

    def handle_incorrect_guess(self):
        self.rem_guesses -= 1
        if self.rem_guesses == 0:
            self.handle_game_over()
        else:
            print("guesses left:", rem_guesses)

    def handle_game_over(self):
        print("game over!")
        # TODO: Error?
        
    def handle_earth_saved(self):
        print("You saved the earth!")
