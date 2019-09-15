from app.Chess.chess import BaseChess


class Pawn(BaseChess):

    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.icons = ('♙', '♟')
        self.first_step = True

    def get_steps_area(self):
        output = []
        output.append([self.x, self.y + (1 * self.get_side())])
        if self.first_step:
            output.append([self.x, self.y + (2 * self.get_side())])
        return output

    def find_beated_step(self, coords, opponent):
        variants = []
        output = []
        size = self.get_field_size()
        if self.x - 1 > 0 and self.y - 1 > 0:
            variants.append([self.x - 1, self.y - 1])
        if self.x + 1 < size and self.y + 1 < size:
            variants.append([self.x + 1, self.y + 1])
        if variants:
            for item in opponent.checkmate:
                if [item.x, item.y] in variants:
                    output.append([item.x, item.y])
        return output if output != [] else coords
