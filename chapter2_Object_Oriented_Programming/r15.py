from __future__ import annotations

from typing import Sequence, Union


class Vector:
    def __init__(self, value: Union[int, Sequence]) -> None:
        if isinstance(value, int):
            self._coords = [0] * value
        elif isinstance(value, Sequence):
            self._coords = list(value)

    def __len__(self) -> int:
        return len(self._coords)

    def __getitem__(self, index: int) -> int:
        return self._coords[index]

    def __setitem__(self, index: int, value: int) -> None:
        self._coords[index] = value

    def __add__(self, other: Sequence) -> Vector:
        if len(self) != len(other):
            raise ValueError("dimensions must agree")

        v = Vector(len(self))
        for index in range(len(self)):
            v[index] = self[index] + other[index]
        return v

    def __radd__(self, other: Sequence) -> Vector:
        return self + other

    def __sub__(self, other: Sequence) -> Vector:
        if len(self) != len(other):
            raise ValueError("dimensions must agree")

        v = Vector(len(self))
        for index in range(len(self)):
            v[index] = self[index] - other[index]
        return v

    def __mul__(self, other: Sequence) -> Vector:
        if len(self) != len(other):
            raise ValueError("dimensions must agree")

        v = Vector(len(self))
        for index in range(len(self)):
            v[index] = self[index] * other[index]
        return v

    def __rmul__(self, other: Sequence) -> Vector:
        return self * other

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Vector):
            return NotImplemented
        return self._coords == other._coords

    def __neg__(self) -> Vector:
        v = Vector(len(self))
        for index in range(len(self)):
            v[index] = -self[index]
        return v