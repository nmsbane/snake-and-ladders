from graph import Graph
from player import Player
from dice import Dice

class Game(object):
    def __init__(self):
        self.game_board = Graph()
        self.add_ladders_snakes()
        self.game_board.create_board()

    def add_ladders_snakes(self):
        self.game_board.add_ladder(2, 8)
        self.game_board.add_ladder(3, 10)
        self.game_board.add_ladder(4, 17)
        self.game_board.add_snake(12, 5)
        self.game_board.add_snake(14, 1)

if __name__ == "__main__":
    new_game = Game()
    board_to_share = new_game.game_board.board
    dice = Dice()
    player = Player(dice, board_to_share)
    turn = 1
    while turn <= 10:
        player.move_player()
        turn = turn + 1