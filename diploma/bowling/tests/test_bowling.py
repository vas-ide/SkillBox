import pytest
from src.bowling import get_score, Bowling
from contextlib import nullcontext as does_not_raise


class TestBowling:
    def test_bowling_simple(self):
        assert get_score('-5') == 5
    #
    @pytest.mark.parametrize("game_result, result", [
        ("X4/34", 42),
        ("--X4/5-34-5", 52),
        ("XXX", 60),
        ("1/XXX", 75),
    ])
    def test_bowling_param(self, game_result, result):
        assert get_score(game_result) == result

    @pytest.mark.parametrize("game_result, result, expections", [
        ("X4/34", 42, does_not_raise()),
        ("--X4/5-34-5", 52, does_not_raise()),
        ("XXX", 60, does_not_raise()),
        ("1/XXX", 75, does_not_raise()),
    ])
    def test_bowling_param_add(self, game_result, result, expections):
        assert get_score(game_result) == result
    def test_bowling_simple_errors(self):
        with pytest.raises(ValueError):
            get_score("/1XXX")
    @pytest.mark.parametrize("game_result", ["--X4/5-34-5p", "/1XXX"])
    def test_bowling_simple_errors(self, game_result):
        with pytest.raises(ValueError):
            get_score(game_result)

    @pytest.mark.parametrize("game_result, result, expections",
                             [
                                 ("X4/34", 42, does_not_raise()),
                                 ("--X4/5-34-5", 52, does_not_raise()),
                                 ("XXX", 60, does_not_raise()),
                                 ("1/XXX", 75, does_not_raise()),
                                 ("--X4/5-34-5p", 60, pytest.raises(ValueError)),
                                 ("/1XXX", 75, pytest.raises(ValueError)),
                             ])
    def test_bowling_errors(self, game_result, result, expections):
        with expections:
            assert get_score(game_result) == result
