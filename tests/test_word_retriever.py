"""source/word_retriever.py"""
import sys
import os
import unittest
from unittest.mock import patch, mock_open

# add source directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'source'))

from word_retriever import replace_special_chars, get_word_repo

class TestReplaceSpecialChars(unittest.TestCase):
    """replace_special_chars"""

    def test_ae(self):
        self.assertEqual(replace_special_chars("ä"), "ae")

    def test_oe(self):
        self.assertEqual(replace_special_chars("ö"), "oe")

    def test_ue(self):
        self.assertEqual(replace_special_chars("ü"), "ue")

    def test_uppercase_ae(self):
        self.assertEqual(replace_special_chars("Ä"), "Ae")

    def test_uppercase_oe(self):
        self.assertEqual(replace_special_chars("Ö"), "Oe")

    def test_uppercase_ue(self):
        self.assertEqual(replace_special_chars("Ü"), "Ue")

    def test_braces_removed(self):
        self.assertEqual(replace_special_chars("(Cube)"), "Cube")

class TestGetWordRepo(unittest.TestCase):
    """get_word_repo"""

    # patch random.shuffle to do nothing
    @patch('source.word_retriever.random.shuffle', lambda lst: None)
    def test_file_read_returns_transformed_words(self):
        m = mock_open(read_data="Tetrahedron\n(Würfel)\n")
        with patch('builtins.open', m):
            result = get_word_repo("wordrepo.txt")
        self.assertEqual(result, ["Tetrahedron", "Wuerfel"])

if __name__ == '__main__':
    unittest.main()
