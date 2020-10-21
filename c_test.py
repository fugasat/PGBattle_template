import pytest
from PGBattle2019.c import get_answer


def test():
    assert get_answer(["5 2","1 1","1 1","1 1","10 1", "1 2"]) == 2
    assert get_answer(["5 2","1 1","1 1","10 1","10 1", "1 1"]) == 0
    assert get_answer(["5 2","1 1","1 1","10 1","10 1", "1 2"]) == 1

    assert get_answer(["4 10","1 1","1 1","1 1","1 1"]) == 2
    assert get_answer(["5 10","1 1","1 1","1 1","1 1","1 1"]) == 3

