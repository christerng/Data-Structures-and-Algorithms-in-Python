from __future__ import annotations


class Progression:
    def __init__(self, start: int = 0) -> None:
        self._current = start

    def _advance(self) -> None:
        self._current += 1

    def __next__(self) -> int:
        if self._current is None:
            raise StopIteration()

        current = self._current
        self._advance()
        return current

    def __iter__(self) -> Progression:
        return self

    def print_progression(self, n: int) -> None:
        print(" ".join(str(next(self)) for _ in range(n)))


class FibonacciProgression(Progression):
    def __init__(self, first: int = 0, second: int = 1) -> None:
        super().__init__(first)
        self._prev = second - first

    def _advance(self) -> None:
        self._prev, self._current = self._current, self._prev + self._current


if __name__ == "__main__":
    f = FibonacciProgression(2, 2)
    f.print_progression(8)
