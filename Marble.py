"""
Veniamin Knyazev
CS 5001 Spring 2022
Final Project- Marble Class
"""
import turtle
from Point import Point
from MarbleData import MarbleData
from Button import Button
from mastermind_game_files import make_code, game_logic
import datetime
import time

MARBLE_RADIUS = 20
NOTIFICATION = 8
COLORS = ["red", "blue", "green", "yellow", "purple", "black"]
PLACE = ["st", "nd", "rd", "th", "th", "th", "th", "th", "th", "th"]
QUIT_BUTTON = "quit_button_small.gif"
CHECK_BUTTON = "checkbutton.gif"
X_BUTTON = "xbutton.gif"
WINNER = "winner.gif"
QUIT_MSG = "quitmsg.gif"
LOSE = "Lose.gif"
FILE_ERROR = "file_error.gif"
LEADER_ERROR = "leaderboard_error.gif"
WOOD = "wood.gif"

class Marble:
    """

    """
    def __init__(self, position, color='white', size=MARBLE_RADIUS):
        self.pen = self.new_pen()
        self.screen = self.new_screen()
        self.color = color
        self.position = position
        self.pen.hideturtle()
        self.size = size
        self.pen.speed(0)  # set to fastest drawing
        self.marble_position = Point(-350,-350)
        self.input_marble_data = []
        self.marble_data = []
        self.notification_data = []
        self.current_guess = []
        self.button_location = []
        self.current_row = 0
        self.current_column = 0
        self.secret_code = make_code()
        self.current_player = self.get_user()

    def new_pen(self):
        """

        :return:
        """
        return turtle.Turtle()

    def new_screen(self):
        """

        :return:
        """
        return turtle.Screen()

    def set_color(self, color):
        """

        :param color:
        :return:
        """
        self.color = color

    def set_size(self, size):
        """

        :param size:
        :return:
        """
        self.size = size

    def get_color(self):
        """

        :return:
        """
        return self.color

    def get_column(self):
        """

        :return:
        """
        return self.current_column

    def set_column(self, column):
        """

        :param column:
        :return:
        """
        self.current_column = column

    def set_row(self, row):
        """

        :param row:
        :return:
        """
        self.current_row = row

    def get_row(self):
        """

        :return:
        """
        return self.current_row

    def set_position(self, x, y):
        """

        :param x:
        :param y:
        :return:
        """
        self.position.x = x
        self.position.y = y

    def draw(self):
        """

        :return:
        """
        # if self.visible and not self.is_empty:
            # return

        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.pen.down()
        self.pen.fillcolor(self.color)
        self.pen.begin_fill()
        self.pen.circle(self.size)
        self.pen.end_fill()

    def draw_empty(self):
        """

        :return:
        """
        self.erase()
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.pen.down()
        self.pen.circle(self.size)
        
    def erase(self):
        """

        :return:
        """
        self.pen.clear()

    def clicked_in_region(self, x, y):
        """

        :param x:
        :param y:
        :return:
        """
        if abs(x - self.position.x) <= self.size * 2 and \
           abs(y - self.position.y) <= self.size * 2:
            return True
        return False

    def add_upper_marbles(self):
        """

        :return:
        """
        color = 'white'
        for y in range(350, -250, -65):
            for x in range(-300, -60, 60):
                self.position = Point(x, y)
                self.set_size(MARBLE_RADIUS)
                self.marble_data.append(MarbleData(x, y, color))
                self.set_color(color)
                self.draw()
        self.marble_data = [self.marble_data[n:n + 4] for n in
                            range(0, len(self.marble_data), 4)]

    def draw_box(self, width, height, x, y, color='black'):
        """

        :param width:
        :param height:
        :param x:
        :param y:
        :param color:
        :return:
        """
        RIGHT = 90
        t = self.new_pen()
        t.color(color)
        t.speed(0)
        t.width(5)
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

    def add_lower_marbles(self):
        """

        :return:
        """
        #self.marble_position = Point(-350, -350)
        self.position = Point(-350, -350)
        for color in COLORS:
            # record the location of the circle
            # add here ....
            self.set_size(MARBLE_RADIUS)
            self.set_color(color)
            self.input_marble_data.append(MarbleData(self.position.x,
                                                     self.position.y,
                                                     color))
            self.draw()
            self.position.x += 60

    def add_notification_marbles(self):
        """

        :return:
        """
        color = 'white'
        self.set_position(-50, 418)
        for _ in range(10):
            self.position.y -= 25
            for _ in range(2):
                self.position.y -= 20
                self.position.x = -50
                for _ in range(2):
                    self.notification_data.append(MarbleData(self.position.x,
                                                             self.position.y,
                                                             color))
                    self.set_size(NOTIFICATION)
                    self.set_color(color)
                    self.draw()
                    self.position.x += 20
        self.notification_data = [self.notification_data[n:n + 4] for n in
                                  range(0, len(self.notification_data), 4)]

    def add_dissaspearing_button(self, image, x, y):
        """

        :param image:
        :param x:
        :param y:
        :return:
        """
        # add image to screen
        t = self.new_pen()
        w = self.new_screen()
        t.hideturtle()
        t.speed(0)
        t.penup()
        w.addshape(image)
        t.goto(x,y)
        t.showturtle()
        t.shape(image)
        t.showturtle()
        time.sleep(2)
        t.hideturtle()




    def add_button(self, image, x, y):
        """

        :param image:
        :param x:
        :param y:
        :return:
        """
        # add image to screen
        t = self.new_pen()
        w = self.new_screen()
        t.hideturtle()
        t.speed(0)
        t.penup()
        w.addshape(image)
        t.goto(x,y)
        self.button_location.append((Button(x, y, image)))
        t.shape(image)
        t.stamp()

    def draw_play_board(self):
        """

        :return:
        """
        s = self.new_screen()
        s.setup(900,900)
        #s.bgpic(WOOD)
        self.draw_box(450, 650, -400, 400)
        self.draw_box(300, 650, 60, 400, 'blue')
        self.draw_box(760, 150, -400, -260)
        self.add_upper_marbles()
        self.add_notification_marbles()
        self.add_lower_marbles()
        self.add_button(QUIT_BUTTON, 275, -335)
        self.add_button(CHECK_BUTTON, 50, -335)
        self.add_button(X_BUTTON, 125, -335)
        self.row_pointer(self.current_row)

    def redraw_play_board(self):
        """

        :return:
        """
        self.input_marble_data.clear()
        self.marble_data.clear()
        self.notification_data.clear()
        self.current_guess = []
        self.secret_code.clear()
        self.secret_code = make_code()
        #self.button_location = []
        self.add_upper_marbles()
        self.add_notification_marbles()
        self.add_lower_marbles()
        self.current_row = 0
        self.current_column = 0
        self.row_pointer(self.current_row)


    def click_circles(self, x, y):
        """

        :param x:
        :param y:
        :return:
        """
        #for color, location in self.marble_data:
        self.set_size(MARBLE_RADIUS)
        for input_marble_data in self.input_marble_data:
            if input_marble_data.clicked_in_region(x, y):
                if input_marble_data.color == 'white' or \
                        len(self.current_guess) > 3 or \
                        self.current_row > 9:
                    return
                else:
                    color = input_marble_data.get_color()
                    input_marble_data.set_color('white')
                    self.position.x = input_marble_data.x
                    self.position.y = input_marble_data.y
                    self.set_color('white')
                    self.draw()
                    row_num = self.get_row()
                    column = self.get_column()
                    if self.marble_data[row_num][column].color == 'white':
                        self.set_color(color)
                        self.current_guess.append(self.get_color())
                        self.position.x = self.marble_data[row_num][column].x
                        self.position.y = self.marble_data[row_num][column].y
                        self.draw()
                        self.current_column += 1
        print(self.secret_code)
        self.click_buttons(x, y)



    def click_buttons(self, x, y):
        """

        :param x:
        :param y:
        :return:
        """
        for button_location in self.button_location:
            if button_location.clicked_in_region_button(x, y):
                if button_location.image == X_BUTTON:
                    self.reset_button()
                    self.color_input_marbles()
                elif button_location.image == CHECK_BUTTON:
                    if len(self.current_guess) != 4:
                        return
                    else:
                        self.check_button()
                elif button_location.image == QUIT_BUTTON:
                    self.quit()

    def check_button(self):
        """

        :return:
        """
        bulls, cows = game_logic(self.secret_code, self.current_guess)
        column = 0
        current_row = self.get_row()
        self.set_size(NOTIFICATION)
        notification_row = self.notification_data[current_row]
        for bull in range(bulls):
            self.set_position(notification_row[column].get_position_x(),
                              notification_row[column].get_position_y())
            self.set_color('black')
            self.draw()
            column += 1
        for cow in range(cows):
            self.set_position(notification_row[column].get_position_x(),
                              notification_row[column].get_position_y())
            self.set_color('red')
            self.draw()
            column += 1
        if bulls == 4:
            self.winner()
            return

        self.current_row += 1
        self.row_pointer(self.current_row)
        self.color_input_marbles()
        if self.current_row > 9:
            self.loser()

    def reset_button(self):
        """

        :return:
        """

        for marbles in self.marble_data[self.current_row]:
            x = marbles.get_position_x()
            y = marbles.get_position_y()
            self.set_position(x,y)
            self.set_color('white')
            self.draw()

    def quit(self):
        """

        :return:
        """
        self.add_dissaspearing_button(QUIT_MSG, 0, 0)
        turtle.bye()

    def winner(self):
        """

        :return:
        """
        self.add_score()
        tr.clear()
        self.write_score()
        self.add_dissaspearing_button(WINNER, 0, 0)
        s = self.new_screen()
        response = s.textinput("Winner Winner! Chicken Dinner!",
                               "Play again? type [n] and click ok to quit")
        if response == 'n':
            self.quit()
        else:
            self.erase()
            self.redraw_play_board()



    def loser(self):
        """

        :return:
        """
        self.add_dissaspearing_button(LOSE, 0, 0)
        s = self.new_screen()
        response = s.textinput("Secret Code Was:", str(self.secret_code) + "\n" +
                               "Play again? type [n] and click ok to quit ")
        if response == 'n':
            self.quit()
        else:
            self.erase()
            self.redraw_play_board()


    def color_input_marbles(self):
        """

        :return:
        """
        # re-color lower input circles
        for index in range(len(self.input_marble_data)):
            if self.input_marble_data[index].color == 'white':
                self.set_size(MARBLE_RADIUS)
                self.set_color(COLORS[index])
                self.input_marble_data[index].set_color(COLORS[index])
                self.set_position(
                    self.input_marble_data[index].get_position_x(),
                    self.input_marble_data[index].get_position_y())
                self.draw()

        # delete current guesses
        self.current_guess.clear()
        self.current_column = 0

    def row_pointer(self, row):
        """

        :param row:
        :return:
        """
        if row > 9:
            return
        turtle.hideturtle()
        turtle.shape('classic')
        turtle.color('red')
        turtle.penup()
        turtle.goto(-340, 370 - row * 65)
        turtle.showturtle()
        turtle.shapesize(2, 2, 2)

    def get_user(self):
        """

        :return:
        """
        s = self.new_screen()
        return s.textinput("Master-Mind Game",
                           "Please enter your name:").strip().capitalize()

    def write_errors(self, error):
        """

        :param error:
        :return:
        """
        try:
            with open('error_log.txt', 'a+') as f:
                date_time = datetime.datetime.now()
                f.write(str(date_time) + ' : ' + str(error) + '\n')

        except IOError as error:

            print(error)

    def add_score(self):
        """

        :return:
        """
        try:
            with open('leaderboard.txt', 'a') as w:
                w.write((str(self.current_row + 1)) +
                        " : " + self.current_player.strip().capitalize() + '\n')

        except IOError as error:
            self.write_errors(error)
            self.leader_board_error()
            print(error)


    def write_score(self):
        """

        :return:
        """
        global tr
        tr = self.new_pen()
        tr.hideturtle()
        tr.speed(0)
        tr.penup()
        try:
            with open('leaderboard.txt', 'r') as r:
                leaders = []
                for line in r:
                    leaders.append(line.strip().split(':'))
                #global tr
                leaders.sort()
                #tr = self.new_pen()
                #tr.hideturtle()
                #tr.speed(0)
                #tr.penup()
                tr.goto(90, 350)
                tr.color('red')
                tr.write("Leaderboard", font=('Verdana', 30, 'normal'))
                tr.goto(75, 300)
                for i, leader in enumerate(leaders):
                    if i > 9:
                        return
                    else:
                        leader = ":".join(leader)
                        tr.write(str(i + 1) + PLACE[i] + ' place  ' + leader, font=('Verdana', 15, "normal"))
                        tr.right(90)
                        tr.forward(50)
                        tr.left(90)

        except IOError as error:

            tr.goto(90, 350)
            tr.color('red')
            tr.write("Leaderboard", font=('Verdana', 30, 'normal'))
            self.write_errors(error)
            self.leader_board_error()
            print(error)

    def leader_board_error(self):
        """

        :return:
        """
        self.add_dissaspearing_button(LEADER_ERROR, 0, 0)

    def file_error(self):
        self.add_dissaspearing_button(FILE_ERROR, 0, 0)
