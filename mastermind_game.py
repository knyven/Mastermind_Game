import turtle

from mastermind_game_files import *
from Marble import Marble
from Point import Point
from turtle import Turtle




def main():


    marble = Marble(Point(-300,350))
    s = marble.new_screen()
    marble.draw_play_board()
    s.onclick(marble.click_circles)
    s.mainloop()


if __name__ == "__main__":
    main()
