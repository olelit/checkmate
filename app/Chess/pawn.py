from app.Chess.chess import BaseChess


class Pawn(BaseChess):

    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.icons = ('♙', '♟')
        self.first_step = True
        self.chess_value = 1

    def get_steps_area(self):
        output = []
        output.append([self.x, self.y + (1 * self.get_side())])
        if self.first_step:
            output.append([self.x, self.y + (2 * self.get_side())])
        return output

    def get_variants(self):
        size = self.get_field_size()
        variants = []
        side = self.get_side()
        y = self.y + side
        if self.x - 1 > 0 and y > 0:
            variants.append([self.x - 1, y])
        if self.x + 1 < size and y < size:
            variants.append([self.x + 1, y])
        return variants
