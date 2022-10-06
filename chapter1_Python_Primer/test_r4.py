import pytest

from . import r4


@pytest.mark.parametrize("n,i", [(0, 0), (3, 5), (100, 328_350)])
def test_sum_squares(n: int, i: int) -> None:
    assert r4.sum_squares(n) == i
