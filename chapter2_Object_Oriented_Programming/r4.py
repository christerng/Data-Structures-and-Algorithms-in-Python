class Flower:
    def __init__(self, name: str, petals: int, price: float) -> None:
        self._name: str = name
        self._petals: int = petals
        self._price: float = price

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, name: str) -> None:
        self._name = name

    @property
    def petals(self) -> int:
        return self._petals

    @petals.setter
    def petals(self, petals: int) -> None:
        self._petals = petals

    @property
    def price(self) -> float:
        return self._price

    @price.setter
    def price(self, price: float) -> None:
        self._price = price
