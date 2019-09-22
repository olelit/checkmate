from app.Chess.chess import BaseChess


class Elephant(BaseChess):

    def __init__(self, color, x, y):
        super().__init__(color, x, y)
        self.icons = ('♗', '♝')
        self.chess_value = 2
        pass