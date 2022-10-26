import sys

data: list[None] = []
for _ in range(5):
    data.append(None)
    print(f"Length: {len(data):3d}; Size in bytes {sys.getsizeof(data):4d}")
for _ in range(5):
    data.pop()
    print(f"Length: {len(data):3d}; Size in bytes {sys.getsizeof(data):4d}")
