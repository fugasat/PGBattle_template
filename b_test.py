import pytest
from PGBattle2019.b import get_answer


def test():
    assert get_answer(["ATCODER"]) == "Maybe"

    assert get_answer(["AtCoder"]) == "Yes"
    assert get_answer(["Atcoder"]) == "Maybe"
    assert get_answer(["ACCoder"]) == "No"
