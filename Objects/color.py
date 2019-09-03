WOOD = 43
DARK_WOOD = 40
DEFAULT= 0


def set_color(color):
    return '\033[{0}m \033[{1}m'.format(color, DARK_WOOD)
