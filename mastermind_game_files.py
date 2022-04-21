from turtle import Turtle, Screen
import random


COLORS = ["red", "blue", "green", "yellow", "purple", "black"]



def setup():
    global t, w
    t = Turtle()
    w = Screen()
    w.setup(width=900,height=900)
    t.speed(0)
    t.hideturtle()


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

def draw_box(width, height, x, y, color='black'):
    RIGHT = 90
    t.color(color)
    t.width(5)
    # upper play box
    t.penup()
    t.hideturtle()
    t.goto(x, y)
    t.pendown()
    t.forward(width)
    t.right(RIGHT)
    t.forward(height)
    t.right(RIGHT)
    t.forward(width)
    t.right(RIGHT)
    t.forward(height)
    t.right(RIGHT)
    t.forward(width)
    t.penup()
