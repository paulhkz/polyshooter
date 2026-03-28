"""
module to abstract retrieving and shuffling the word-list/repo
"""
import os
import random

def get_word_repo(file_name: str) -> list[str]:
    """
    Purpose: gets the newline-separated words from a given file
    also shuffles the lines
    """
    word_repo = []

    filepath = os.path.abspath(__file__)
    dirpath = os.path.dirname(filepath)
    datafile = os.path.join(dirpath, file_name)

    try:
        with open(datafile, 'r', encoding="utf-8") as f:
            word_repo_lines = f.read()
            word_repo = word_repo_lines.splitlines()
    except (OSError, IOError):
        print("Etwas ist schiefgelaufen beim Öffnen der Datei")

    random.shuffle(word_repo)
    word_repo = [replace_umlauts(word) for word in word_repo]
    return word_repo

def replace_umlauts(word: str) -> str:
    """
    Purpose: replaces the umlauts/diacritics of a word
    """
    word = word.replace("ä", "ae")
    word = word.replace("ö", "oe")
    word = word.replace("ü", "ue")
    word = word.replace("Ä", "Ae")
    word = word.replace("Ö", "Oe")
    word = word.replace("Ü", "Ue")

    return word
