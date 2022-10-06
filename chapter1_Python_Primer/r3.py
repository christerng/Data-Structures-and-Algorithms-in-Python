from typing import Sequence


def minmax(data: Sequence[int]) -> tuple[int, int]:
    min_, max_ = data[0], data[0]
    for i in data:
        if i < min_:
            min_ = i
        if i > max_:
            max_ = i
    return min_, max_
