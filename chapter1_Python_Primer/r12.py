import random
from typing import Sequence


def choice(data: Sequence[int]) -> int:
    return data[random.randrange(len(data))]
