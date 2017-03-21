import pytest
from main.game_engine import Game


def test_worst_player():
    game = Game()

    for counter in range(1, 20):
        game.roll(0)

    assert game.score() == 0



