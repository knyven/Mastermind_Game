"""
Veniamin Knyazev
CS 5001 Spring 2022
Final Project- Marble Class
This class contains most of the functions of the mastermind game
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
LEADER_ERROR = "leaderboard_error.gif"

class Marble:
    """
    Marble class creates objects that hold the location of the input circles,
    upper circles, notification circles, buttons. It contains functions to
    draw the game board and the leaderboard from a leaderboard text file.
    This class also does error logging for issues arising from IOFile errors
    and logs them in a text file called 'error_log'.
    """
    def __init__(self, position, color='white', size=MARBLE_RADIUS):
        """
        Function: the constructor for the Marble class. Assigns position
        through Point Class, color (default is white) and size (default
        is MARBLE_RADIUS size). Several other attributes are created
        input_marble_data, marble_data, notification_data, current_guess,
        button_location, current_row, current_column, and two function calls
        make_code() which creates the secret code and get_user() which prompts
        the user for a name and saves it to current_player attribute.
        :param position: taken as Point class object with x and y coordinates
        :param color: string passed in to denote color
        :param size: integer passed in to denote circle size
        :return nothing
        """
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
        Function new_pen() Creates a new turtle.Turtle()
        :return: a new instance of turtle
        """
        return turtle.Turtle()

    def new_screen(self):
        """
        Function new_screen() Creates a new turtle.Screen()
        :return: a new instance of turtle screen
        """
        return turtle.Screen()

    def set_color(self, color):
        """
        Function set_color() sets a new color for the self.color attribute
        :param color: string with new color to be associated
        :return:
        """
        self.color = color

    def set_size(self, size):
        """
        Function set_size() sets size of the self.size attribute
        :param size: variable that contains size of the circle to be
         drawn (integer value)
        :return:
        """
        self.size = size

    def get_color(self):
        """
        Function: get_color() returns the current color of the object
        :return: self.color of the object
        """
        return self.color

    def get_column(self):
        """
        Function: get_column() returns the current column number
        :return: returns current column number
        """
        return self.current_column

    def set_column(self, new_column):
        """
        Function: set_column() sets self.current_column to new_column
        :param new_column: integer passed in for new current column
        :return: self.current column
        """
        self.current_column = new_column

    def set_row(self, new_row):
        """
        Function: set_row() sets self.current_row to new_row
        :param new_row: integer passed in for new current row
        :return: self.current_row
        """
        self.current_row = new_row

    def get_row(self):
        """
        Function: get_row() gets the current row
        :return: returns self.current_row
        """
        return self.current_row

    def set_position(self, x, y):
        """
        Function: set_position(x, y)
        :param x: takes a floating value for new self.x position
        :param y: takes a floating value for new self.y position
        :return: returns nothing
        """
        self.position.x = x
        self.position.y = y


    def draw(self):
        """
        Function: draw() draws a circle at the current self.position.x/y
        and fills it with self.color
        :return: nothing
        """
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.pen.down()
        self.pen.fillcolor(self.color)
        self.pen.begin_fill()
        self.pen.circle(self.size)
        self.pen.end_fill()

    def erase(self):
        """
        Function: erase() erases the current drawings associated with the pen
        creates by self
        :return: nothing
        """
        self.pen.clear()

    def add_upper_marbles(self):
        """
        Function: add_upper_marbles() draws and appends object data of upper_marbles
        to Marble data in chunks of 4 (i.e rows) into a nested list.
        :return: nothing
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
        Function: draw_box(width, height, x, y, color) takes parameters and
        draws box based on desired location of x/y coordinates and the height
        and width of the box as well as the color.
        :param width: an integer value for the width of the box
        :param height: an integer value for the height of the box
        :param x: x coordinate of box starting location
        :param y: y coordinate of box starting location
        :param color: string that tells pen what color to set for the box
        :return: nothing
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
        Function: add_lower_marbles() creates the lower marbles that the user
        clicks on to initiate the upper marbles filling the desired colors.
        :return: nothing
        """
        self.position = Point(-350, -350)
        self.set_size(MARBLE_RADIUS)
        for color in COLORS:
            # record the location of the circle
            # add here ....
            self.set_color(color)
            self.input_marble_data.append(MarbleData(self.position.x,
                                                     self.position.y,
                                                     color))
            self.draw()
            self.position.x += 60

    def add_notification_marbles(self):
        """
        Function: add_notification_marbles() creates the upper marbles that
        are filled if the current row corresponds to the play row.
        :return: nothing
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

    def add_disappearing_button(self, image, x, y):
        """
        Function: add_disapearing_button(image, x, y) takes a 'image' in gif
        format and then stamps the current image at location x/y and then waits
        2 seconds and hides the image
        :param image: string name of the file that contains the image we would
        like to stamp onto the screen
        :param x: x-coordinate for location of where the image is to be stamped
        :param y: y-coordinate for location of where the image is to be stamped
        :return: nothing
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
        time.sleep(2) # sleep for 2 seconds and then hide turtle
        t.hideturtle()


    def add_button(self, image, x, y):
        """
        Function: add_disapearing_button(image, x, y) takes a 'image' in gif
        format and then stamps the current image at location x/y.
        :param image: string name of the file that contains the image we would
        like to stamp onto the screen
        :param x: x-coordinate for location of where the image is to be stamped
        :param y: y-coordinate for location of where the image is to be stamped
        :return: nothing
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
        Function: draw_play_board() combines draw_box, upper_marbles,
        notification_marbles, lower_marbles, all three buttons and the
        arrow pointer into one function to be called.
        :return: nothing
        """
        s = self.new_screen()
        s.setup(900,900)
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
        Function: redraw_play_board() is called after a win or loss in the
        event the user would like to play again. It draws upper_marbles,
        notification_marbles, lower_marbles, arrow pointer and resets the
        secret code as well as the current row and column.
        :return: nothing
        """

        self.input_marble_data.clear()
        self.marble_data.clear()
        self.notification_data.clear()
        self.current_guess = []
        self.secret_code.clear()
        self.secret_code = make_code()
        self.add_upper_marbles()
        self.add_notification_marbles()
        self.add_lower_marbles()
        self.set_row(0)
        self.set_column(0)
        self.row_pointer(self.current_row)

    def click_circles(self, x, y):
        """
        Function click_circles() main driving loop for the mastermind game,
        takes clicks and then filters the clicks depending on their location
        on the input circles and fills the play row with the corresponding
        color.
        :param x: x-coordinate for location of registered click
        :param y: y-coordinate for location of registered click
        :return: nothing
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
        self.click_buttons(x, y)

    def click_buttons(self, x, y):
        """
        Function click_buttons(x, y) takes the clicks in the click_circles
        method and checks if those clicks are in the vicinity of the buttons
        and if they are initiates the process associated with each button.
        :param x: x-coordinate for location of registered click
        :param y: y-coordinate for location of registered click
        :return: nothing
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
        Function check_button() this combines the game_logic function from
        game files and validates the guess against the secret code. Depending
        on how close the guess is to the code it prints out either cows
        or bulls.
        :return: nothing
        """
        bulls, cows = game_logic(self.secret_code, self.current_guess)
        column = 0 # sets current row to 0 index
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
        self.current_row += 1
        self.row_pointer(self.current_row)
        self.color_input_marbles()
        if bulls == 4:
            self.winner()
        elif self.current_row > 9:
            self.loser()

    def reset_button(self):
        """
        Function: reset_button() resets the color of current play row of the
        upper marbles back to white and fills them.
        :return: nothing
        """
        for marbles in self.marble_data[self.current_row]:
            x = marbles.get_position_x()
            y = marbles.get_position_y()
            self.set_position(x,y)
            self.set_color('white')
            self.draw()

    def quit(self):
        """
        Function: quit() stamps the disappearing button QUIT MESSAGE and then
        exits turtle.
        :return: nothing
        """
        self.add_disappearing_button(QUIT_MSG, 0, 0)
        turtle.bye()

    def winner(self):
        """
        Function winner() first adds score to leaderboard.txt and then stamps
        winning message onto the screen. Asks user if they would like to play
        again and if so redraw the board, otherwise quit.
        :return: nothing
        """
        self.add_score()
        tr.clear()
        self.write_score()
        self.add_disappearing_button(WINNER, 0, 0)
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
        Function winner() first stamps losing message onto the screen.
        Asks user if they would like to play again and if so redraw
        the board, otherwise quit.
        :return: nothing
        """
        self.add_disappearing_button(LOSE, 0, 0)
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
        Function color_input_marbles takes the row of input marbles
        and checks if any have attribute color set to white if so,
        check which index they are at and color them the corresponding
        color.
        :return: nothing
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
        self.set_column(0)

    def row_pointer(self, row):
        """
        Function row_pointer(row) this function takes row as parameter that
        draws the classic red turtle at the current row.
        :param row: takes an integer with the value of the current row
        :return: nothing
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
        Function: greet_user() presents user with a pop up window that prompts
        user to enter name, which is saved and returned
        :return: name of current player is returned
        """
        s = self.new_screen()
        return s.textinput("Master-Mind Game",
                           "Please enter your name:").strip().capitalize()

    def write_errors(self, error):
        """
        Function: write_errors(error) takes error as a parameter. The passes in
        error is printed out along with the time that the error was encountered.
        :param error: type of error that was encountered
        :return: nothing
        """
        try:
            with open('error_log.txt', 'a+') as f:
                date_time = datetime.datetime.now()
                f.write(str(date_time) + ' : ' + str(error) + '\n')
        except IOError as error:

            print(error)

    def add_score(self):
        """
        Function add_score() is called when user wins a game and a new score is
        added to the leaderboard.txt. If the leaderboard.txt does not exist an
        error is raised and saved through write_errors().
        :return:
        """
        try:
            with open('leaderboard.txt', 'a') as w:
                w.write((str(self.current_row)) +
                        " : " + self.current_player.strip().capitalize() + '\n')

        except IOError as error:
            self.write_errors(error)
            self.leader_board_error()
            print(error)


    def write_score(self):
        """
        Function write_score() this functions writes the score and the word
        "leaderboard" on the right square. It sorts the list from leaderboard
        and then prints its out if the number of rows is under 9 otherwise
        the lowest score(s) is dropped.
        :return: nothing
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
                leaders.sort()
                tr.goto(90, 350)
                tr.color('red')
                tr.write("Leaderboard", font=('Verdana', 30, 'normal'))
                tr.goto(75, 300)
                for i, leader in enumerate(leaders):
                    if i > 9:
                        return
                    else:
                        tr.write(str(i + 1) + PLACE[i] + ' place :' + leader[1] + "---> " +
                                 leader[0], font=('Verdana', 15, "normal"))
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
        Function leader_board_error() stamps a message that the leaderboard
        text file was not found.
        :return: nothing
        """
        self.add_disappearing_button(LEADER_ERROR, 0, 0)

