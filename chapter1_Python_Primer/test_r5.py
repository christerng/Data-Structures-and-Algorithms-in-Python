import pytest

from . import r5


@pytest.mark.parametrize("n,i", [(0, 0), (3, 5), (100, 328_350)])
def test_sum_squares(n: int, i: int) -> None:
    assert r5.sum_squares(n) == i
