import random
from typing import Sequence

import pytest

from . import r12

random.seed(0)


@pytest.mark.parametrize(
    "data,c", [([0], 0), ([0, 1, 2, 3, 4], 3), ([4, 3, 2, 1, 0], 4)]
)
def test_choice(data: Sequence[int], c: int) -> None:
    assert r12.choice(data) == c
