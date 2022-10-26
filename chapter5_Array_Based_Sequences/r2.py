import sys

prev_len = 0
prev_size = 0

data: list[None] = []
for _ in range(27):
    curr_len = len(data)
    curr_size = sys.getsizeof(data)

    if prev_size not in (curr_size, 0):
        print(f"Length: {prev_len:3d}; Size in bytes {prev_size:4d}")

    prev_len = curr_len
    prev_size = curr_size

    data.append(None)
