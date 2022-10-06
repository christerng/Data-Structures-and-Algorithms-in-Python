from typing import Sequence

import pytest

from . import r3


@pytest.mark.parametrize(
    "d,t", [([0], (0, 0)), ([0, 1, 2, 3, 4], (0, 4)), ([4, 3, 2, 1, 0], (0, 4))]
)
def test_minmax(d: Sequence[int], t: tuple[int]) -> None:
    assert r3.minmax(d) == t
