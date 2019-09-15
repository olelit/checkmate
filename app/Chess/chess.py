class BaseChess():

    def __init__(self, color, x, y):
        self.field_size = 9
        self.x = x
        self.y = y
        self.color = color

    def __str__(self):
        return self.icons[self.color]

    def get_side(self):
        return -1 if self.color == 1 else 1

    def get_steps_area(size):
        return

    def get_field_size(self):
        return self.field_size

    def get_path_coords(self, size):
        output = []
        output.append([self.x, self.y])
        output = output + self.get_steps_area(size)
        return output

    def find_beated_step(self, coords, opponent):
        return
