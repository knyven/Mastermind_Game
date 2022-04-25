"""
Veniamin Knyazev
CS 5001 Spring 2022
Final Project- Button Class
"""
BUTTTON_CIRCLE = 15

class Button:
    """
    Button class creates objects that contain location and image name
    attribute. This allows for comparisons of clicks on the screen and how
    close they are to image on the play-board.
    """
    def __init__(self, x, y, image):
        """
        Function: the constructor for the MarbleData class. Assigns position
        of x and y coordinates and the name of image
        :param x: integer value of x-coordinate
        :param y: integer value of y-coordinate
        :param image: string that denotes the name of the object
        """
        self.x = x
        self.y = y
        self.image = image

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

    def clicked_in_region_button(self, x, y):
        """
        Function: clicked_in_region(x, y) takes in (x,y) as new coordinates
         and compares with self.position.x/y if the click is within the area
         the function returns True otherwise False.
        :param x: x-coordinate of new click
        :param y: y-coordinate of new click
        :return: True if click is within BUTTON_CIRCLE distance and False if not
        """
        if abs(x - self.x) <= BUTTTON_CIRCLE * 2 and \
           abs(y - self.y) <= BUTTTON_CIRCLE * 2:
            return True
        return False
