import app.Classes.color as color
from app.Chess import *
from app.Chess.pawn import Pawn
from app.Chess.elephant import Elephant
from app.Chess.rook import Rook
from app.Classes.player import Player


class GameField:
    FIELD_SIZE = 9

    def __init__(self, *args, **kwargs):

        self.size = 9
        self.selected = 2
        self.field = [["." for x in range(self.size)]
                      for y in range(self.size)]
        self.player1 = Player('player1')
        self.player2 = Player('player2')
        self.player_now = self.player1

        self.letters = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I')

        self.coords = []

        super().__init__(*args, **kwargs)

    def __str__(self):
        output = self.set_player_name(self.player1)
        i = 0
        for item in range(self.size):
            output += " {0}".format(item + 1)
        output += "\n"
        for index_y in range(self.size):
            for index_x in range(self.size):
                coords = [index_x, index_y]
                color_cell = i
                if coords in self.coords:
                    color_cell = self.selected
                output += "({0})".format(self.letters[index_y]) if index_x == 0 else ""
                output += color.set_color(color_cell, self.field[index_y][index_x])
                i = 1 - i
            if index_y == 4:
                output += self.set_statistic(self.player1)
            if index_y == 5:
                output += self.set_statistic(self.player2)
            output += "\n"
        output += self.set_player_name(self.player2)
        return output

    def show_field(self):
        print(self)

    def start_game(self):

        self.field = self.fill_checkmate(self.field)
        self.show_field()
        game_continue = True

        while game_continue:
            for player in Player.players:
                self.coords = []
                chess = None
                while chess == None:
                    x, y = self.pars_x_y_from_terminal('Введите координаты шахматы (Например h4)')
                    chess = player.find_chess(x, y)

                opponent = Player.players[0] if Player.players[1] == player else Player.players[1]
                self.coords = chess.get_steps_area()
                self.coords = chess.find_beated_step(self.coords, opponent)
                self.show_field()
                can_step = False
                while not can_step:
                    x, y = self.pars_x_y_from_terminal('Введите координаты хода (Например h4)')
                    if [x, y] in self.coords:
                        can_step = True
                        self.set_chess_coord(x, y, chess, player)
                        chess.beat_chess(x, y, opponent, player)
                        self.reinitial_checkfield()
                self.show_field()
                self.player_now = opponent
        return

    def set_player_name(self, player):
        if player == self.player_now:
            return color.set_color_code(color.CURRENT_PLAYER, player.name) + "\n "
        return player.name

    def set_chess_coord(self, x, y, chess, player):
        self.field[chess.y][chess.x] = '.'
        chess.x = x
        chess.y = y
        self.field[y][x] = chess
        self.coords = []
        if isinstance(chess, Pawn):
            chess.first_step = False
        player.checkmate[player.checkmate.index(chess)] = chess
        return

    def pars_x_y_from_terminal(self, message):
        print(message)
        coord = input()
        y = self.letters.index(str.upper(coord[0]))
        x = int(coord[1])
        return x, y

    def fill_checkmate(self, field):
        y_coords = [1, self.size - 2]
        for index in range(2):
            y_coord = y_coords[index]
            for x_index in range(len(self.field[0])):
                chess = Pawn(index, x_index, y_coord)
                field[y_coord][x_index] = chess
                Player.players[index].add_chess(chess)

        chess = Rook(1, 0, 0)
        field[0][0] = chess
        Player.players[1].add_chess(chess)

        chess = Rook(1, 8, 0)
        field[8][0] = chess
        Player.players[0].add_chess(chess)
        return field

    def reinitial_checkfield(self):
        self.field = [["." for x in range(self.size)]
                      for y in range(self.size)]
        for player in Player.players:
            for chess in player.checkmate:
                x = chess.x
                y = chess.y
                self.field[y][x] = chess

    def set_statistic(self, player):
        return "        Игрок {0} заработал {1} баллов и забрал {2} шахмат. Его трофеи {3}" \
            .format(player.name, player.value, len(player.beated_chessmates), " ".join(player.beated_chessmates))
