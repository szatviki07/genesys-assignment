import unittest
from task import LetterCombinations

class TestLetterCombinations(unittest.TestCase):
    def test_empty(self):
        self.assertEqual(LetterCombinations(""), [])

    def test_oneDigit(self):
        self.assertEqual(LetterCombinations("2"), ["a", "b", "c"])

    def test_multipleDigits(self):
        result = LetterCombinations("23")
        expected = ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
        self.assertEqual(result, expected)

    def test_invalidDigit(self):
        with self.assertRaises(ValueError):
            LetterCombinations("1")

    def test_moreThan4(self):
        with self.assertRaises(ValueError):
            LetterCombinations("23456")

    def test_exactly4(self):
        self.assertTrue(len(LetterCombinations("2345")) > 0)

if __name__ == "__main__":
    unittest.main()