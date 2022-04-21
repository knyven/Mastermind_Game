import turtle
from Point import Point
from MarbleData import MarbleData
from mastermind_game_files import make_code, game_logic

MARBLE_RADIUS = 20
NOTIFICATION = 8
COLORS = ["red", "blue", "green", "yellow", "purple", "black"]
QUIT_BUTTON = "quit_small.gif"
CHECK_BUTTON = "checkbutton.gif"
X_BUTTON = "xbutton.gif"

class Marble:
    def __init__(self, position, color = 'white', size = MARBLE_RADIUS):
        self.pen = self.new_pen()
        self.color = color
        self.position = position
        self.visible = False
        self.is_empty = True
        self.pen.hideturtle()
        self.size = size
        self.pen.speed(0)  # set to fastest drawing
        self.marble_position = Point(-350,-350)
        self.marble_data = []
        self.circle_data = []
        self.notification_data = []
        self.current_guess = []  
        self.current_row = 0
        self.current_column = 0

    def new_pen(self): 
        return turtle.Turtle()

    def set_color(self, color):
        self.color = color
        self.is_empty = False

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
        self.visible = True
        self.is_empty = False
        self.pen.down()
        self.pen.fillcolor(self.color)
        self.pen.begin_fill()
        self.pen.circle(self.size)
        self.pen.end_fill()

    def draw_empty(self):
        self.erase()
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.visible = True
        self.is_empty = True
        self.pen.down()
        self.pen.circle(self.size)
        
    def erase(self):
        self.visible = False
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
                self.circle_data.append(MarbleData(x, y, color))
                self.set_color(color)
                self.draw()

        print(len(self.circle_data))

    def add_lower_marbles(self):
        self.position = self.marble_position
        for color in COLORS:
            # record the location of the circle
            # add here ....
            self.set_size(MARBLE_RADIUS)
            self.set_color(color)
            self.marble_data.append(MarbleData(self.position.x, self.position.y,
                                                       color))
            self.draw()
            self.position.x += 60

    def add_notification_marbles(self):
        color = 'white'
        for x in range(-50, 0, 25):
            for y in range(360, -240, -65):
                for y in range(y + 10, y - 20, -25):
                    self.set_size(NOTIFICATION)
                    self.position = Point(x, y)
                    self.notification_data.append(MarbleData(x, y, color))

                    self.set_color(color)
                    self.draw()

    def add_button(self, image, x, y):
        # add image to screen

        self.t = turtle.Turtle()
        self.w = turtle.Screen()
        self.t.hideturtle()
        self.t.speed(0)
        self.t.penup()
        self.w.addshape(image)
        self.t.goto(x,y)
        self.t.shape(image)
        self.t.stamp()

    def draw_play_board(self):
        self.add_upper_marbles()
        #self.add_notification_marbles()
        self.add_lower_marbles()
        self.add_button(QUIT_BUTTON, 275, -335)
        self.add_button(CHECK_BUTTON, 50, -335)
        self.add_button(X_BUTTON, 125, -335)



    def click_circles(self, x, y):
        #for color, location in self.marble_data:
        self.set_size(MARBLE_RADIUS)
        for marble_data in self.marble_data:
            if marble_data.clicked_in_region(x, y):
                if marble_data.color == 'white' or len(self.current_guess) > 3:
                    break
                else:
                    color = marble_data.get_color()
                    x1 = marble_data.x
                    y1 = marble_data.y
                    marble_data.set_color('white')
                    self.position.x = x1
                    self.position.y = y1
                    self.set_color('white')
                    self.draw()
                    row_num = self.get_row()
                    play_row = [self.circle_data[n:n+4] for n in
                                  range(0, len(self.circle_data), 4)]
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
        print(self.current_guess)
        self.click_buttons(x, y)

    def click_buttons(self, x, y):
        pass



    def reset_button(self):

        #column = self.get_column()
        current_row = self.get_row()
        play_area = self.circle_data

        current_row = play_area[0:4:]
        for marbles in current_row:
            if marbles.color != 'white':
                self.set_position(marbles.get_position_x, marbles.get_position_y)
                self.color = 'white'
                self.draw()
