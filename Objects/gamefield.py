import Objects.color as color

class GameField():

    def __init__(self, *args, **kwargs):

        even = color.set_color(color.WOOD)
        odd = color.set_color(color.DARK_WOOD)

        counter = 0
        size = 9

        self.field = [["" for x in range(size)] for y in range(size)]

        for index_y in range(size):
            for index_x in range(size):
                self.field[index_y][index_x] = even if counter % 2 == 0 else odd
                counter+=1
        super().__init__(*args, **kwargs)

    
    def __str__(self):
        output = ''
        for item in self.field:
            output += "{0}{1}\n".format("".join(item),color.set_color(color.DEFAULT))
        return output
