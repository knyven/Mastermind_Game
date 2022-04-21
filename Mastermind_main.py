import turtle

from mastermind_game_files import *
from Marble import Marble
from Point import Point
from turtle import Turtle




def main():
    screen = turtle.Screen()

    #Game space setup
    setup()
    draw_box(450, 650, -400, 400)
    draw_box(300, 650, 60, 400, 'blue')
    draw_box(760, 150, -400, -260)


    marble = Marble(Point(-300,350))
    marble.draw_play_board()
    marble.reset_button()


    screen.onclick(marble.click_circles)

    screen.mainloop()




if __name__ == "__main__":
    main()
