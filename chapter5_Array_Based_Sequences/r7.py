from typing import Iterable


def find_repeated(a: Iterable[int]) -> int:
    seen = set()

    for value in a:
        if value in seen:
            return value
        seen.add(value)

    return -1
