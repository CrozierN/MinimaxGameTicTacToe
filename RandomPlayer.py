from Player import Player
import math
import random


class RandomPlayer(Player):
    def __init__(self, symbol):
        super().__init__(symbol)

    def get_move(self, game):  # game here is tic tac toe
        square = random.choice(game.available_moves())
        return square
