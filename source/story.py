import os

DEFAULT_ATTEMPTS = 4

class Story:
    def __init__(self) -> None:
        self.rem_guesses = DEFAULT_ATTEMPTS
        self.__current_num_of_correct_hits = 0
        self.__current_num_of_faulty_hits = 0

        self.show_prelude()

    def show_prelude(self) -> None:
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
        Nun kommt einer direkt auf euch zu. Wenn ihr ihn nicht aufhalten könnt, dann wars das.
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
        os.system("clear")
        os.system("clear")



    def handle_correct_guess(self) -> None:
        self.__current_num_of_correct_hits += 1

    def handle_incorrect_guess(self) -> None:
        self.rem_guesses -= 1
        if self.rem_guesses == 0:
            self.handle_game_over()
        else:
            self.__current_num_of_faulty_hits += 1


    def handle_game_over(self) -> None:
        print(f"{'':💥<20}")
        raise SolidHasHit

    def handle_earth_saved(self) -> None:
        # TODO
        pass

    def display_last_guess_stats(self, correct: set[str], faulty: set[str], hidden_word: str, correct_guesses_ratio: int, is_first_guess: bool = False) -> None:
        if self.__current_num_of_correct_hits == 1:
            print("Richtig! Der LASER konnte sich weiter kalibrieren.")
        elif self.__current_num_of_correct_hits > 1:
            print(f"Der LASER hat sich gerade {self.__current_num_of_correct_hits} Mal kalibrieren können!")

        if self.__current_num_of_faulty_hits == 1:
            print("Oh nein, der LASER konnte sich nicht kalibrieren! Der Polyeder kommt immer näher!")
        elif self.__current_num_of_faulty_hits > 1:
            print(f"Du hast ganze {self.__current_num_of_faulty_hits} Mal falsch geraten! Pass auf, er kommt näher!")

        if not is_first_guess and self.__current_num_of_correct_hits == 0 and self.__current_num_of_faulty_hits == 0:
            print("Nichts ist passiert.")

        print(f"Korrekte Buchstaben: {", ".join(correct)}")
        print(f"Falsche Buchstaben: {" ".join(faulty)}")

        distance = f"[ DISTANZ: {self.rem_guesses * 12}.000 km ]"
        correct_guesses_percentage = correct_guesses_ratio * 100

        print(f"{distance:<40}", end="")
        print((DEFAULT_ATTEMPTS - self.rem_guesses) * 2 * f"\n{' ' * 40}", end="")

        print(f"{'〔Körper〕':^30}")
        print((self.rem_guesses * 2 - 1) * "\n", end="")
        calibration = f"[ KALIBRIERUNG: [{'█' * int(correct_guesses_percentage // 10)}{'-' * int(10 - correct_guesses_percentage // 10)}] {correct_guesses_percentage:.2f}% ]"
        print(f"{calibration:<40}{'/ˉˉˉˉˉ〔Erde〕ˉˉˉˉˉ\\':^30}")

        print(f"[ IDENTIFIKATION: \n{hidden_word} ]")

        self.__current_num_of_correct_hits = 0
        self.__current_num_of_faulty_hits = 0

class SolidHasHit(Exception):
    def __init__(self) -> None:
        pass
