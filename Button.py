BUTTTON_CIRCLE = 15
BUTTTON = 20

class Button:
    def __init__(self, x, y, image):
        self.x = x
        self.y = y
        self.image = image

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

    def clicked_in_region_button(self, x, y):
        if abs(x - self.x) <= BUTTTON_CIRCLE * 2 and \
           abs(y - self.y) <= BUTTTON_CIRCLE * 2:
            return True
        return False
