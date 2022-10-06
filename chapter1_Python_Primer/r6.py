def sum_squares(n: int) -> int:
    sum_ = 0
    for i in range(n):
        if i >= 0 and i % 2 == 1:
            sum_ += i * i
    return sum_
