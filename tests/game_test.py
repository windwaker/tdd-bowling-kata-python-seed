import pytest
from main.game_engine import Game


class Tests:

    @classmethod
    def test_worst_player(cls):
        test_game = Game()
        score = 20

        'Knocks 0 every roll in 10 frames'
        for counter in range(1, score+1):
            Game.roll(test_game, 0)

        assert Game.score(test_game) == 0

    @classmethod
    def test_consistent_player(cls):
        test_game = Game()
        score = 20

        'Knocks 1 pin per roll in 10 frames'
        for counter in range(1, score+1):
            Game.roll(test_game, 1)

        assert Game.score(test_game) == 20

    @classmethod
    def test_calculate_spare(cls):
        test_game = Game()

        'first frame'
        Game.roll(test_game, 5)
        Game.roll(test_game, 5)

        'spare roll'
        Game.roll(test_game, 3)

        assert Game.score(test_game) == 13
