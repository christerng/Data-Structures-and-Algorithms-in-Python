from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any, Iterable


class AbstractSequence(ABC):
    @abstractmethod
    def __len__(self) -> int:
        pass

    @abstractmethod
    def __getitem__(self, index: int) -> Any:
        pass

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, AbstractSequence):
            raise NotImplementedError

        if len(self) != len(other):
            return False

        for index in range(len(self)):
            if self[index] != other[index]:
                return False

        return True


class ConcreteSequence(AbstractSequence):
    def __init__(self, values: Iterable) -> None:
        self._values = list(values)

    def __len__(self) -> int:
        return len(self._values)

    def __getitem__(self, index: int) -> Any:
        return self._values[index]

    def __setitem__(self, index: int, value: Any) -> None:
        self._values[index] = value

    def __lt__(self, other: ConcreteSequence) -> bool:
        return self._values < other._values
