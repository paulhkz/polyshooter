import os

DEFAULT_ATTEMPTS = 3

class Story:
    def __init__(self):
        self.rem_guesses = DEFAULT_ATTEMPTS
        self.current_stats = CurrentStatsDisplay()

        self.show_prelude()
    
    def show_prelude(self):
        os.system("clear")
        os.system("clear")

        print("""
        Ein unbekanntes Portal ist über der Erde aufgegangen.
        Du und ein Team sind dabei, das ganze genauer zu inspezieren...
        """)
        print()
        
        user_input = input(f"\r{'Enter drücken um weiter zu gehen, "s", um die Story zu überspringen':>150}")
        if user_input.lower().strip() == 's':
            return

        os.system("clear")
        print("""
        Plötzlich seht ihr, wie Objekte aus diesem Portal kommen.
        Genauere Analysen zeigen, dass diese Objekte Johnson-Körper sind, das sind spezielle Polyeder.
        Ein Körper ist bereits auf die Erde eingeschlagen und hat ein riesiges Loch hinterlassen.
        """)
        print()

        user_input = input(f"\r{'Enter drücken um weiter zu gehen, "s", um die Story zu überspringen':>150}")
        if user_input.lower().strip() == 's':
            return
        
        os.system("clear")
        print("""
        Zum Glück habt ihr spezialisierte LASER, welcher jedes beliebige Objekt zu Grunde machen kann.
        Dieser muss aber die Topologie des zu treffenden Körpers wissen, sonst kann er nicht treffen.
        Nun ist es eure Aufgabe, den Namen der Polyeder herauszufinden, damit der LASER sich korrekt kalibrieren kann!
        Aber passt lieber auf, die Körper fallen schnell, ihr habt nicht unendlich Versuche!
        """)
        print()

        user_input = input(f"\r{'Enter drücken, um zu starten':>150}")



    def handle_correct_guess(self):
        self.current_stats.increase_correct()

    def handle_incorrect_guess(self):
        self.rem_guesses -= 1
        if self.rem_guesses == 0:
            self.handle_game_over()
        else:
            self.current_stats.increase_faulty()
            

    def handle_game_over(self):
        # TODO: Error?
        pass
        
    def handle_earth_saved(self):
        # TODO
        pass
        
    def display_last_guess_stats(self, correct: set, faulty: set):
        self.current_stats.show(self.rem_guesses, correct, faulty)
        self.current_stats = CurrentStatsDisplay()

class CurrentStatsDisplay:
    def __init__(self):
        self.correct = 0
        self.faulty = 0
        
    def increase_correct(self):
        self.correct += 1
    
    def increase_faulty(self):
        self.faulty += 1
    
    def show(self, rem_guesses: int, correct: set(str), faulty: set(str)):
        if self.correct == 1:
            print("Richtig!!")
        elif self.correct > 1:
            print(f"Du hast {self.correct} Mal richtig geraten!")

        if self.faulty == 1:
            print("Oh nein, der Polyeder kommt näher!")
        elif self.faulty > 1:
            print(f"Du hast ganze {faulty} Mal falsch geraten! Pass auf!")
            
        print(f"Noch {rem_guesses} Versuche verbleibend...")
