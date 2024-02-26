import pytest
from src.bowling import get_score


class TestBowling:
    def test_bowling_simple(self):
        assert get_score('-5') == 5

    @pytest.mark.parametrize("game_result, result",
                             [("X4/34", 42), ("--X4/5-34-5", 52), ("XXX", 60), ("1/XXX", 75)])
    def test_bowling(self, game_result, result):
        assert get_score(game_result) == result

    @pytest.mark.parametrize("game_result, result, expections",
                             [("--X4/5-34-5p", 60, pytest.raises(ValueError)),
                              ("/1XXX", 75, pytest.raises(ValueError))])
    def test_bowling_errors(self, game_result, result, expections):
        assert get_score(game_result) == result

