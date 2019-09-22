RED = "41"
WOOD = "43"
SELECTED = "45"
BEATED = '44'
CURRENT_PLAYER = 32

def set_color(color, value):
    color_code = 0
    if color == 2:
        color_code = SELECTED
    elif color == 3:
        color_code = BEATED
    else:
        color_code = WOOD if color == 0 else RED
    return '\033[{0}m{1} \033[0m'.format(color_code, value)

def set_color_code(color_code, value):
    return '\033[{0}m{1}\033[0m'.format(color_code, value)
