class BaseChess():

    def __init__(self, color, x, y):
        self.field_size = 9
        self.x = x
        self.y = y
        self.color = color
        self.icons = ()
        self.beat_variants = []
        self.chess_value = 0

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
        variants = []
        self.beat_variants = []
        variants = self.get_variants()
        if variants:
            for item in opponent.checkmate:
                if [item.x, item.y] in variants:
                    self.beat_variants.append([item.x, item.y])
        return self.beat_variants if self.beat_variants != [] else coords

    def get_variants(self):
        output = []
        return output


    def beat_chess(self, x, y, opponent, player):
        for key,item in enumerate(opponent.checkmate):
            if [item.x, item.y] in self.beat_variants:
                player.beated_chessmates.append(opponent.checkmate.pop(key))
                player.value += self.chess_value
        return
