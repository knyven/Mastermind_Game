"""
Veniamin Knyazev
CS 5001 Spring 2022
Final Project- Game Files for mastermind game
"""
import random

COLORS = ["red", "blue", "green", "yellow", "purple", "black"]


def make_code():
    """
    Function: make_code() returns a list of 4 random colors
    :return: a list of 4 random colors from COLORS
    """
    secret_code = random.sample(COLORS,4)
    return secret_code


def game_logic(secret_code, guess):
    """
    Function: game_logic(secret_code, guess) takes secret code and guess lists
    and compares the guess to the secret code, depending on the guess prints
    out an integer value of bull/cows that indicate how close the guess was
    :param secret_code: list that contains secret code
    :param guess: list that contains current guess
    :return: number of cow/bull pegs to fill
    """
    bull = 0
    cow = 0

    for index in range(4):
        if guess[index] == secret_code[index]:
            bull += 1
        elif guess[index] in secret_code:
            cow += 1
    return bull, cow


