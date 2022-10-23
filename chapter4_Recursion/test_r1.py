from typing import Sequence

import pytest

from . import r1


@pytest.mark.parametrize(
    "s,m",
    [([0, 1, 2, 3, 4, 5], 5), ([10, 9, 8, 7, 6, 5], 10), ([-1, -2, -3, -4, -5], -1)],
)
def test_recursive_max(s: Sequence, m: int) -> None:
    assert r1.recursive_max(s) == m
