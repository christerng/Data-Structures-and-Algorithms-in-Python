import ctypes
from typing import Any


class DynamicArray:
    def __init__(self) -> None:
        self._n: int = 0
        self._capacity: int = 1
        self._A: ctypes.Array[Any] = self._make_array(self._capacity)

    def __getitem__(self, k: int) -> ctypes.py_object:
        if k >= self._n:
            raise IndexError("Invalid index")
        if k < 0:
            return self._A[k + self._n]
        return self._A[k]

    def append(self, obj: Any) -> None:
        if self._n == self._capacity:
            self._resize(2 * self._capacity)
        self._A[self._n] = obj
        self._n += 1

    def _resize(self, c: int) -> None:
        new_array = self._make_array(c)
        for k in range(self._n):
            new_array[k] = self._A[k]
        self._A = new_array
        self._capacity = c

    def _make_array(self, c: int) -> ctypes.Array[Any]:
        return (c * ctypes.py_object)()
