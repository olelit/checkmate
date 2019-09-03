import Objects.color as color

class GameField():

    def __init__(self, *args, **kwargs):

        self.size = 9
        self.field = [["0" for x in range(self.size)]
                      for y in range(self.size)]

        super().__init__(*args, **kwargs)

    
    def __str__(self):
        output = ''
        i = 0
        for index_y in range(self.size):
            for index_x in range(self.size):
                output += color.set_color(i)+""+self.field[index_y][index_x]
            output+="\n"   
        return output
