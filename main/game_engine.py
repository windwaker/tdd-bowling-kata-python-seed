class Game:

    total = 0

    def roll(self, pins_knocked):
        self.total += pins_knocked

    def score(self):
        return self.total
