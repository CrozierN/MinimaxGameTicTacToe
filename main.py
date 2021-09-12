from RandomPlayer import RandomPlayer
from Opponent import Opponent
import MiniMaxGame

if __name__ == '__main__':
    x_Minimax = RandomPlayer('X')
    o_opponent_player = Opponent('O')
    t = MiniMaxGame.MinimaxGame()
    # play(t, x_player, o_player, print_game=True)
