CIRCLE_SIZE = 15

class MarbleData:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

    def get_position(self):
        return self.x, self.y

    def get_position_x(self):
        return self.x

    def get_position_y(self):
        return self.y

    def set_position_x(self, x):
        self.x = x

    def set_position_y(self, y):
        self.y = y

    def delta_x(self, other):
        return abs(self.x - other.x)

    def delta_y(self, other):
        return abs(self.y - other.y)

    def clicked_in_region(self, x, y):
        if abs(x - self.x) <= CIRCLE_SIZE * 2 and \
           abs(y - self.y) <= CIRCLE_SIZE * 2:
            return True
        return False

    def set_color(self, color):
        self.color = color

    def get_color(self):
        return self.color
