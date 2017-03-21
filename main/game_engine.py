class Game:
    def __init__(self):
        self.frame_scores = []

    def roll(self, pins_knocked):
        self.frame_scores.append(pins_knocked)

    def score(self):
        total = 0

        frame_count = 0
        for element in range(0, 10):
            if self.frame_scores[frame_count] + self.frame_scores[frame_count + 1] == 10:
                print("Spare!")

                total += 10 + self.frame_scores[frame_count + 1]
                frame_count += 2
            else:
                total += self.frame_scores[frame_count] + self.frame_scores[frame_count + 1]

        return total
