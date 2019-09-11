class Player():

    players = []

    def __init__(self, name):
        self.name = name
        self.checkmate = []
        self.beated_chessmates = []
        self.value = 0
        self.current_chess = None
        Player.players.append(self)
    
    def do_step(self):
        return

    
    def add_chess(self, checkmate):
        self.checkmate.append(checkmate)

    
    def find_chess(self, x, y):
        self.current_chess = None
        for item in self.checkmate:
            if item.x == x and item.y == y:
                self.current_chess = item
        return self.current_chess
    