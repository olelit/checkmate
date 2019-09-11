from Chess.chess import BaseChess
import ansi as ansi


class Pawn(BaseChess):

    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.icons = ('♙', '♟')
        self.first_step = True


    def get_steps_area(self):
        output = []
        output.append([self.x, self.y+(1*self.get_side())])
        if self.first_step:
            output.append([self.x, self.y+(2*self.get_side())])
        return output



