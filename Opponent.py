from Player import Player


class Opponent(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def get_move(self, game):
        valid_square = False
        val = None

        while not valid_square:
            square = input(f'{self.symbol} \'s turn. Input move (0-9): ')
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
            except ValueError:
                print('Invalid Square, Try again')

        return val
