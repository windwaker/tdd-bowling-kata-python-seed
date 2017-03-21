from main.game_engine import Game


class Tests:
    def test_worst_player(self):
        test_game = Game()

        self.multi_roll(test_game, 20, 0)

        assert Game.score(test_game) == 0

    def test_consistent_player(self):
        test_game = Game()

        self.multi_roll(test_game, 20, 1)

        assert Game.score(test_game) == 20

    def test_calculate_spare(self):
        test_game = Game()

        'first frame'
        Game.roll(test_game, 5)
        Game.roll(test_game, 5)

        'spare roll'
        Game.roll(test_game, 3)
        Game.roll(test_game, 6)

        '22 score to here'
        self.multi_roll(test_game, 8, 1)

        assert Game.score(test_game) == 38

    @staticmethod
    def multi_roll(test_game, rolls, pins_knocked):
        for attempt in range(0, rolls):
            Game.roll(test_game, pins_knocked)
