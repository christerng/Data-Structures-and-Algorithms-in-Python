from typing import Sequence


def recursive_max(s: Sequence[int], index: int = 0) -> int:
    if index == len(s):
        return s[len(s) - 1]
    return max(s[index], recursive_max(s, index + 1))


# pylint: disable-next=pointless-string-statement
"""
Time complexity: O(n)
Space complexity: O(n)
"""
