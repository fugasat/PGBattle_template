import pytest
from PGBattle2019.template import get_answer


def test():
    assert get_answer(["4 10","2 3","1 2","1 1","2 1"]) == 1
    assert get_answer(["5 5","100 100","100 100","100 100","100 100","100 100"]) == 0
