"""
Veniamin Knyazev
CS 5001 Spring 2022
Final Project- Marble Class
"""
from Marble import Marble
from Point import Point

def main():

    marble = Marble(Point(-350,350))
    s = marble.new_screen()
    marble.draw_play_board()
    marble.write_score()
    s.onclick(marble.click_circles)
    s.mainloop()


if __name__ == "__main__":
    main()
