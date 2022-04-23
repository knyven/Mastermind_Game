import turtle
from Point import Point
from MarbleData import MarbleData
from Button import Button
from mastermind_game_files import make_code, game_logic
import datetime

MARBLE_RADIUS = 20
NOTIFICATION = 8
COLORS = ["red", "blue", "green", "yellow", "purple", "black"]
QUIT_BUTTON = "quit_small.gif"
CHECK_BUTTON = "checkbutton.gif"
X_BUTTON = "xbutton.gif"
WINNER = "winner.gif"
QUIT_MSG = "quitmsg.gif"
LOSE = "Lose.gif"
FILE_ERROR = "file_error.gif"
LEADER_ERROR = "leaderboard_error.gif"

class Marble:
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
        return turtle.Turtle()

    def new_screen(self):
        return turtle.Screen()

    def set_color(self, color):
        self.color = color

    def set_size(self, size):
        self.size = size

    def get_color(self):
        return self.color

    def get_column(self):
        return self.current_column

    def set_column(self, column):
        self.current_column = column

    def set_row(self, row):
        self.current_row = row

    def get_row(self):
        return self.current_row

    def set_position(self, x, y):
        self.position.x = x
        self.position.y = y

    def draw(self):
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
        self.erase()
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.pen.down()
        self.pen.circle(self.size)
        
    def erase(self):
        self.pen.clear()

    def clicked_in_region(self, x, y):
        if abs(x - self.position.x) <= self.size * 2 and \
           abs(y - self.position.y) <= self.size * 2:
            return True
        return False

    def add_upper_marbles(self):
        color = 'white'
        for y in range(350, -250, -65):
            for x in range(-300, -60, 60):
                self.position = Point(x, y)
                self.set_size(MARBLE_RADIUS)
                self.marble_data.append(MarbleData(x, y, color))
                self.set_color(color)
                self.draw()

    def draw_box(self, width, height, x, y, color='black'):
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
        self.position = self.marble_position
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

    def add_button(self, image, x, y):
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
        #self.row_pointer()



    def click_circles(self, x, y):
        #for color, location in self.marble_data:
        self.set_size(MARBLE_RADIUS)
        for input_marble_data in self.input_marble_data:
            if input_marble_data.clicked_in_region(x, y):
                if input_marble_data.color == 'white' or \
                        len(self.current_guess) > 3:
                    break
                else:
                    color = input_marble_data.get_color()
                    x1 = input_marble_data.x
                    y1 = input_marble_data.y
                    input_marble_data.set_color('white')
                    self.position.x = x1
                    self.position.y = y1
                    self.set_color('white')
                    self.draw()
                    row_num = self.get_row()
                    play_row = [self.marble_data[n:n+4] for n in
                                  range(0, len(self.marble_data), 4)]
                    column = self.get_column()
                    if play_row[row_num][column].color == 'white':
                        self.set_color(color)
                        self.current_guess.append(self.get_color())
                        self.position.x = play_row[row_num][column].x
                        self.position.y = play_row[row_num][column].y
                        self.draw()
                        self.current_column += 1
                        break
                    else:
                        continue
        print(self.secret_code)
        self.click_buttons(x, y)
        #self.row_pointer(self.current_row)

    def click_buttons(self, x, y):
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
        bulls, cows = game_logic(self.secret_code, self.current_guess)
        if bulls == 4:
            self.winner()
        column = 0
        current_row = self.get_row()
        notification_row = [self.notification_data[n:n + 4] for n in
                    range(0, len(self.marble_data), 4)]
        notification_row = notification_row[current_row]
        for bull in range(bulls):
            self.set_position(notification_row[column].get_position_x(),
                              notification_row[column].get_position_y())
            self.set_color('black')
            self.set_size(NOTIFICATION)
            self.draw()
            column += 1
        for cow in range(cows):
            self.set_position(notification_row[column].get_position_x(),
                              notification_row[column].get_position_y())
            self.set_color('red')
            self.set_size(NOTIFICATION)
            self.draw()
            column += 1
        self.current_row += 1
        #self.row_delete(self.current_row)
        self.row_pointer(self.current_row)
        self.color_input_marbles()
        if self.current_row > 9:
            self.loser()

    def reset_button(self):

        current_row = self.get_row()
        play_row = [self.marble_data[n:n + 4] for n in
                    range(0, len(self.marble_data), 4)]
        play_row = play_row[current_row]


        # fill play row with empty circles
        for marbles in play_row:
            x = marbles.get_position_x()
            y = marbles.get_position_y()
            self.set_position(x,y)
            self.set_color('white')
            self.draw()

    def quit(self):
        self.add_button(QUIT_MSG, 0, 0)
        turtle.exitonclick()

    def winner(self):
        self.add_score()
        self.add_button(WINNER, 0, 0)
        turtle.exitonclick()

    def loser(self):
        self.add_button(LOSE, 0, 0)
        s = self.new_screen()
        s.textinput("Secret Code Was", self.secret_code)
        turtle.exitonclick()

    def color_input_marbles(self):
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
        s = self.new_screen()
        return s.textinput("Master-Mind Game",
                           "Please enter your name:").strip().capitalize()

    def write_errors(self, error):

        try:
            with open('error_log.txt', 'a+') as f:
                date_time = datetime.datetime.now()
                f.write(str(date_time) + ' : ' + str(error) + '\n')

        except IOError as error:

            print(error)

    def add_score(self):
        try:
            with open('leaderboard1.txt', 'a') as w:
                w.write((str(self.current_row + 1)) +
                        " : " + self.current_player.strip().capitalize() + '\n')

        except IOError as error:
            self.write_errors(error)
            self.leader_board_error()
            print(error)


    def write_score(self):

        try:
            with open('leaderboard1.txt', 'r') as r:
                leaders = [line.strip().split(':') for line in r]
                leaders.sort()
                t = self.new_pen()
                t.hideturtle()
                t.speed(0)
                t.penup()
                t.goto(75, 300)

                for leader in leaders:
                    leader = ":".join(leader)
                    t.write(leader, font=('Verdana', 20, "normal"))
                    t.right(90)
                    t.forward(50)
                    t.left(90)

        except IOError as error:
            self.write_errors(error)
            print(error)

    def leader_board_error(self):
        self.add_button(LEADER_ERROR, 0, 0)

    def file_error(self):
        self.add_button(FILE_ERROR, 0, 0)
        self.erase()