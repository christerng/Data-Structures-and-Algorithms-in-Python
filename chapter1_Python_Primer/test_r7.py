import pytest

from . import r7


@pytest.mark.parametrize("n,i", [(0, 0), (3, 1), (100, 166_650)])
def test_sum_squares(n: int, i: int) -> None:
    assert r7.sum_squares(n) == i
