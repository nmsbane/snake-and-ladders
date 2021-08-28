from collections import defaultdict
from exceptions import InvalidConfigException

class Graph(object):
    
    def __init__(self, size=36):
        self.size = size
        self.board = defaultdict(list)
        self.board_config = dict()

    def _add_ladder_or_snake(self, start_position, end_position):
        try:
            start_position = int(start_position)
            end_position = int(end_position)
        except ValueError as e:
            raise ValueError(e)
        
        self.board_config[start_position] = end_position - start_position

    def _add_edge(self, start, end):
        self.board[start].append(end)  
    
    def add_snake(self, start_position, end_position):
        if start_position <= end_position:
            raise InvalidConfigException("start position should be greater than end position for adding snake")
        self._add_ladder_or_snake(start_position, end_position)

    def add_ladder(self, start_position, end_position):
        if start_position >= end_position:
            raise InvalidConfigException("start position should be less than end position for adding ladder")
        self._add_ladder_or_snake(start_position, end_position)

    def create_board(self):
        for start in range(1,self.size+1):
            for dice in range(1,7):
                end = start + dice + self.board_config.get(start+dice, 0)
                if end <= self.size:
                    self._add_edge(start, end)

