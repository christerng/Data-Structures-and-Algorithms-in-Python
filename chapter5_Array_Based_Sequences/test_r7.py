from typing import Iterable

import pytest

from . import r7


@pytest.mark.parametrize(
    "s,r", [([1, 1, 2, 3], 1), ([1, 2, 2, 3], 2), ([1, 2, 3, 3], 3)]
)
def test_find_repeated(s: Iterable[int], r: int) -> None:
    assert r7.find_repeated(s) == r
