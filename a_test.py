import pytest
from PGBattle2019.a import get_answer


def test():
    assert get_answer(["4 3 2"]) == "No"
    assert get_answer(["5 2 2"]) == "No"
    assert get_answer(["5 2 1"]) == "No"

    assert get_answer(["8 3 6"]) == "Yes"
    assert get_answer(["8 3 5"]) == "Yes"
    assert get_answer(["8 3 4"]) == "No"
    assert get_answer(["100 50 10"]) == "No"
