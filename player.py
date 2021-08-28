class Player(object):
    def __init__(self, dice, board_to_share):
        self.current_position = 1
        self.dice = dice
        self.board = board_to_share
    
    def move_player(self):
        random_number = self.dice.get_random()
        print(f"thrown a number {random_number} from current_position {self.current_position}")
        possible_positions = self.board[self.current_position]
        try:
            next_position = possible_positions[random_number - 1]
            print(f"now going to next position {next_position}")
            self.current_position = next_position
        except IndexError as e:
            print(f"cant go out of board limits from {self.current_position}")

