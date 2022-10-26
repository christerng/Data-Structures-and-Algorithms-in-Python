from typing import Iterable


def sum_matrix(m: Iterable[Iterable[int]]) -> int:
    s = 0
    for row in m:
        for val in row:
            s += val
    return s
