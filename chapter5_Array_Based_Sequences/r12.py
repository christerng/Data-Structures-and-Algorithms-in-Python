from typing import Iterable


def sum_matrix(m: Iterable[Iterable[int]]) -> int:
    return sum(val for row in m for val in row)
