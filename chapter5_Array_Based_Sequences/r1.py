import sys

data: list[None] = []
for _ in range(27):
    print(f"Length: {len(data):3d}; Size in bytes {sys.getsizeof(data):4d}")
    data.append(None)
