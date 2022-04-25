"""
Veniamin Knyazev
CS 5001 Spring 2022
Final Project- Marble Data Class
"""
CIRCLE_SIZE = 10


class MarbleData:
    """
    MarbleData class creates objects that contain location and color
    attributes. This allows for comparisons of clicks
    on the screen and how close they are to the marbles across the play-board
    and what color they are.
    """
    def __init__(self, x, y, color):
        """
        Function: the constructor for the MarbleData class. Assigns position
        of x and y coordinates and the color of the marbledata object.
        :param x: integer value of x-coordinate
        :param y: integer value of y-coordinate
        :param color: string that denotes the color of the MarbleData object
        """
        self.x = x
        self.y = y
        self.color = color

    def get_position(self):
        """
        Function: get_position() returns current x/y coordinates of
        MarbleData object
        :return: x, y coordinates
        """
        return self.x, self.y

    def get_position_x(self):
        """
        Function: get_position_x returns the current x coordinate
        :return: x coordinate
        """
        return self.x

    def get_position_y(self):
        """
        Function: get_position_x returns the current y coordinate
        :return: y coordinate
        """
        return self.y

    def set_position_x(self, x):
        """
        Function: set_position_x(x) takes a float/integer for new x coordinate
        :param x: takes a float/integer value for new x coordinate
        :return: nothing
        """
        self.x = x

    def set_position_y(self, y):
        """
        Function: set_position_y(y) takes a float/integer for new y coordinate
        :param y: takes a float/integer value for new y coordinate
        :return: nothing
        """
        self.y = y

    def clicked_in_region(self, x, y):
        """
        Function: clicked_in_region(x, y) takes in (x,y) as new coordinates
         and compares with self.position.x/y if the click is within the area
         the function returns True otherwise False.
        :param x: x-coordinate of new click
        :param y: y-coordinate of new click
        :return: True if click is within CIRCLE_SIZE distance and False if not
        """
        if abs(x - self.x) <= CIRCLE_SIZE * 2 and \
           abs(y - self.y - 18) <= CIRCLE_SIZE * 2:
            return True
        return False

    def set_color(self, color):
        """
        Function set_color() sets a new color for the self.color attribute
        :param color: string with new color to be associated
        :return:
        """
        self.color = color

    def get_color(self):
        """
        Function: get_color() returns the current color of the object
        :return: self.color of the object
        """
        return self.color
