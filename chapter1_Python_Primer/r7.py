def sum_squares(n: int) -> int:
    return sum(_ * _ for _ in range(n) if _ >= 0 and _ % 2 == 1)
