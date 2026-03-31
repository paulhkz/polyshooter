"""Module for managing game story and narrative elements."""
import os

MAX_ATTEMPTS = 7 # number of attempts before the johnson-solid hits the earth minus one

class Story:
    """handles the narrative and display logic of the game"""

    def __init__(self) -> None:
        self.__rem_guesses = MAX_ATTEMPTS
        self.__was_correct_guess = 0 # 0 = no guess yet, 1 = correct guess, -1 = incorrect guess

    def show_prelude(self) -> None:
        """
        Purpose: show story prelude
        """
        os.system("clear")

        print("""
        Ein unbekanntes Portal ist über der Erde aufgegangen.
        Du und ein Team sind dabei, das ganze genauer zu inspezieren...
        """)
        print()

        skip_prompt = (
            'Enter drücken um weiter zu gehen, '
            '"s", um die Story zu überspringen '
        )
        user_input = input(f"\r{skip_prompt:>150}")
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

        user_input = input(f"\r{skip_prompt:>150}")
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

    def show_continuing_scene(self) -> bool:
        """
        Purpose: Shows the scene whether the player want's to continue or not.
        Returns the player's decision
        """
        os.system("clear")
        print("""
        Wie es aussieht kommen noch mehr Körper auf die Erde zu!
        Er kommt zum Glück aber nicht auf dein Team zu.
        Ihr habt die Chance, die Mission fortzuführen oder
        an die Betroffenen weiterzuleiten.

        """)

        decision = input("Weitermachen? [y]/n: ")

        if decision == "y":
            return True
        print("Alles klar.")
        return False

    def handle_correct_guess(self) -> None:
        """
        Purpose: increment correct hit counter
        """
        self.__was_correct_guess = 1

    def handle_incorrect_guess(self) -> None:
        """
        Purpose: handle incorrect guess and check for game over
        """
        self.__rem_guesses -= 1
        if self.__rem_guesses == 0:
            self.__handle_game_over()
        else:
            self.__was_correct_guess = -1


    def __handle_game_over(self) -> None:
        """
        Purpose: display game over message and raise SolidHasHit
        """
        raise SolidHasHit

    def handle_earth_saved(self, word: str) -> None:
        """
        Purpose: print fire-sequence
        """
        os.system("clear")
        print("Initialisieren des LASER-Schusses...")
        os.system("sleep 1") # no time-module allowed

        os.system("clear")
        print("Feuer in")
        os.system("sleep 1")
        print("3")
        os.system("sleep 1")
        print("2")
        os.system("sleep 1")
        print("1")
        os.system("sleep 1")
        print("Abschuss.")
        os.system("sleep 2")

        os.system("clear")
        print(f"TREFFER! Der Körper Namens '{word}' wurde getroffen! Gratulation!")
        os.system("sleep 3")

    def display_guess_feedback(
        self,
        correct: set[str],
        faulty: set[str],
        is_first_guess: bool = False
    ) -> None:
        """
        Purpose: display guessing-feedback and known/unknown letters
        """
        if self.__was_correct_guess == 1:
            print("Richtig! Der LASER konnte sich weiter kalibrieren.")
        elif self.__was_correct_guess == -1:
            print(
                "Oh nein, der LASER konnte sich nicht "
                "kalibrieren! Der Polyeder kommt immer näher!"
            )
        elif not is_first_guess: # __was_correct_guess is 0
            print("Nichts ist passiert.")

        print(f"Korrekte Buchstaben: {", ".join(correct)}")
        print(f"Falsche Buchstaben: {" ".join(faulty)}")

        self.__was_correct_guess = 0

    def display_calibration(
        self,
        hidden_word: str,
        correct_guesses_ratio: float
    ) -> None:
        """
        Purpose: display distance/calibration stats and the hidden word
        """
        distance = f"[ DISTANZ: {self.__rem_guesses * 12}.000 km ]"
        percentage = correct_guesses_ratio * 100

        print(f"{distance:<40}", end="")
        gap = f"\n{' ' * 40}"
        print((MAX_ATTEMPTS - self.__rem_guesses) * 2 * gap, end="")

        print(f"{'〔Körper〕':^30}")
        print((self.__rem_guesses * 2 - 1) * "\n", end="")
        filled = int(percentage // 10)
        empty = int(10 - percentage // 10)
        calibration = (
            f"[ KALIBRIERUNG: "
            f"[{'█' * filled}{'-' * empty}] "
            f"{percentage:.2f}% ]"
        )
        earth = '/ˉˉˉˉˉ〔Erde〕ˉˉˉˉˉ\\'
        print(f"{calibration:<40}{earth:^30}")

        print(f"[ IDENTIFIKATION: \n{hidden_word} ]")

class SolidHasHit(Exception):
    """exception when the johnson-solid hits the earth"""
