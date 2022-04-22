import random

COLORS = ["red", "blue", "green", "yellow", "purple", "black"]


def make_code():
    secret_code = random.sample(COLORS,4)
    return secret_code


def game_logic(secret_code, guess):
    if len(secret_code) != 4 or len(guess) != 4:
        raise Exception("Either secret code or guess is too short")
    bull = 0
    cow = 0
    for index in range(4):
        if guess[index] == secret_code[index]:
            bull += 1
        elif guess[index] in secret_code:
            cow += 1
    return bull, cow


