def recursive_intify(s: str, index: int) -> int:
    if index == 0:
        return 0
    return int(s[index - 1]) + 10 * recursive_intify(s, index - 1)
