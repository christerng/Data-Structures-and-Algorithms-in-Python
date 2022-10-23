def recursive_harmonic(n: int) -> float:
    if n == 1:
        return 1
    return (1 / n) + recursive_harmonic(n - 1)
