import time


def time_pop_beginning(iterations: int) -> float:
    l = [None] * iterations

    start_time = time.perf_counter()
    for _ in range(iterations):
        l.pop(0)
    end_time = time.perf_counter()

    return (end_time - start_time) / iterations * 10**6


def time_pop_middle(iterations: int) -> float:
    l = [None] * iterations

    start_time = time.perf_counter()
    for _ in range(iterations):
        l.pop(len(l) // 2)
    end_time = time.perf_counter()

    return (end_time - start_time) / iterations * 10**6


def time_pop_end(iterations: int) -> float:
    l = [None] * iterations

    start_time = time.perf_counter()
    for _ in range(iterations):
        l.pop()
    end_time = time.perf_counter()

    return (end_time - start_time) / iterations * 10**6


for time_func in (time_pop_beginning, time_pop_middle, time_pop_end):
    print(time_func.__name__)
    for iterations in (100, 1_000, 10_000, 100_000):
        print(f"Iterations: {iterations:3d}; Time: {time_func(iterations):3f}")
    print()
