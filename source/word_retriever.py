import os, random

class WordRetriever:
    def __init__(self: WordRetriever):
        self.wordrepo = []

        try:
            with open('wordrepo.txt', 'r') as f:
                # Comment:
                wordrepo = f.read()
                self.wordrepo = wordrepo.splitlines()
        except e:
            print("Etwas ist schiefgelaufen beim Öffnen der Datei: ", e)

        random.shuffle(self.wordrepo)
        
    def get_word(self: WordRetriever) -> str:
        """
        Purpose: removes a word from the wordrepo and returns it. This makes sure no words are played twice in a game.
        """
        return self.wordrepo.pop()
