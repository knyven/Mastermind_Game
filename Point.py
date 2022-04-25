"""
Veniamin Knyazev
CS 5001 Spring 2022
Final Project- Point Class
"""

class Point:
    """
    Point is a class that creates objects with positional attributes.
    """
    def __init__(self, x, y):
        """
        Function : the constructor for the Point class. Assigns two
        attrubutes to Point objects x/y coordinates.
        :param x: takes an integer value for the x coordinate of object
        :param y: takes an integer value for the y coordinate of object
        """
        self.x = x
        self.y = y
