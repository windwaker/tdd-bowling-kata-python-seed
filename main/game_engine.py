class Game:

    def __init__(self):
        self._score = 0

    def roll(self, pins_knocked):
        self._score = pins_knocked

    def score(self):
        return self._score

