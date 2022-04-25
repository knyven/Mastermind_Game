"""
Veniamin Knyazev
CS 5001 Spring 2022
Final Project- Test Mastermind Game
"""
import unittest
import random
from mastermind_game_files import make_code, game_logic

COLORS = ["red", "blue", "green", "yellow", "purple", "black"]

class TestMastermind(unittest.TestCase):
    """
    TestMastermind will test the game logic and make code functions to make sure
    they are creating the correct code and the number of bulls and cows that
    gets printed is correct
    """


    def test_make_code(self):
        """
        Function: test_make_code() tests if the function that generates a
        random list of 4 colors from COLORS is correctly creating the list
        :return: nothing
        """
        actual = make_code()


        for each in actual:
            if each not in COLORS:
                print("Color check failed!")
            else:
                print("Color checking passed!")

        expected = ['green', 'yellow', 'blue', 'red']
        self.assertEqual(len(actual), len(expected))

    def test_game_logic(self):
        """
        Function test_game_logic() will test the function that runs the
        check on the input guess and compares it to the secret code. The
        test function will test if the correct number of pegs colored.
        :return: nothing
        """

        code = ['green', 'yellow', 'red', 'blue']

        guess1 = ['green', 'yellow', 'blue', 'red']
        guess2 = ['red', 'yellow', 'blue', 'purple']
        guess3 = ['green', 'red', 'blue', 'yellow']
        correct_guess = ['green', 'yellow', 'red', 'blue']

        answer = game_logic(code, guess1)
        answer2 = game_logic(code, guess2)
        answer3 = game_logic(code, guess3)
        correct = game_logic(code, correct_guess)

        self.assertEqual(answer, (2, 2))
        self.assertEqual(answer2, (1, 2))
        self.assertEqual(answer3, (1, 3))
        self.assertEqual(correct, (4, 0))

def main():
    unittest.main(verbosity = 3)


if __name__ == "__main__":
    unittest.main()







