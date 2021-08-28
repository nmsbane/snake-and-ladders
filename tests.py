from unittest import TestCase
from graph import Graph
from dice import Dice
from player import Player
from game_start import Game

class GraphTest(TestCase):
    def setUp(self):
        self.board = Graph()

    def test_graph_creation_size(self):
        assert self.board.size == 36
    
    def test_ladder_config(self):
        try:
            self.board.add_ladder(7, 14)
        except Exception as e:
            self.fail(e)
    
    def test_snake_config(self):
        try:
            self.board.add_snake(14, 7)
        except Exception as e:
            self.fail(e)
    
    def test_board_creation(self):
        # add ladders from 2 to 8
        # add ladders from 3 to 10
        # add ladders from 4 to 12
        # add snakes from 12 to 1
        # add snakes from 10 to 6
        # add snakes from 12 to 4
        self.board.add_ladder(2, 8)
        self.board.add_ladder(3, 10)
        self.board.add_ladder(4, 12)
        self.board.add_snake(12, 1)
        self.board.add_snake(10, 6)
        self.board.create_board()
        # print(self.board.board_config)
        # print(self.board.board)
        assert 8 in self.board.board[2]
        assert 12 in self.board.board[3]
        assert 5 in self.board.board[4]
        assert 1 in self.board.board[8]
        assert 6 in self.board.board[9]
        assert 1 in self.board.board[10]

        
class DiceTest(TestCase):
    def setUp(self):
        self.dice = Dice()
    
    def test_random_number(self):
        assert self.dice.get_random() in [1, 2, 3, 4, 5, 6]
    
    def test_crooked_number(self):
        self.dice = Dice(True)
        assert self.dice.get_random() in [2, 4, 6]

class PlayerTest(TestCase):
    def setUp(self):
        new_game = Game()
        board_to_share = new_game.game_board.board
        dice = Dice()
        self.player = Player(dice, board_to_share)

    def test_player_move(self):
        try:
            self.player.move_player()
        except Exception as e:
            self.fail("failed to move player")