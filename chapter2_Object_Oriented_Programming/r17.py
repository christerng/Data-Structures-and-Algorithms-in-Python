from typing import Any


class Goat:
    def __init__(self) -> None:
        self._tail: Any

    def milk(self) -> Any:
        pass

    def jump(self) -> Any:
        pass


class Pig:
    def __init__(self) -> None:
        self._nose: Any

    def eat(self, food: Any) -> Any:
        pass

    def wallow(self) -> Any:
        pass


class Horse:
    def __init__(self) -> None:
        self._height: Any
        self._color: Any

    def run(self) -> Any:
        pass

    def jump(self) -> Any:
        pass


class Racer(Horse):
    def race(self) -> Any:
        pass


class Equestrian(Horse):
    def __init__(self) -> None:
        super().__init__()
        self._weight: Any

    def trot(self) -> Any:
        pass

    def is_trained(self) -> Any:
        pass
