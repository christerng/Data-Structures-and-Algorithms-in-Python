import pytest

from . import r6


@pytest.mark.parametrize("n,i", [(0, 0), (3, 1), (100, 166_650)])
def test_sum_squares(n: int, i: int) -> None:
    assert r6.sum_squares(n) == i
