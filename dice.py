import random

class Dice(object):
    def __init__(self, crooked=False):
        self.crooked = crooked
    
    def _get_random_number(self):
        random_number = random.randint(1, 6)
        return random_number

    def get_random(self):
        random_number = self._get_random_number()
        
        if self.crooked == False:
            return random_number
        
        while (random_number % 2) != 0:
            random_number = self._get_random_number()
        
        return random_number
        