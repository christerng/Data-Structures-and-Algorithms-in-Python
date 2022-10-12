class CreditCard:
    def __init__(self, customer: str, bank: str, account: str, limit: int) -> None:
        self._customer: str = customer
        self._bank: str = bank
        self._account: str = account
        self._limit: int = limit
        self._balance: int = 0

    def charge(self, price: int) -> bool:
        if not isinstance(price, int):
            raise TypeError(f"price {price} is not type int")

        if price + self._balance > self._limit:
            return False
        self._balance += price
        return True

    def make_payment(self, amount: int) -> None:
        if not isinstance(amount, int):
            raise TypeError(f"amount {amount} is not type int")

        if amount < 0:
            raise ValueError(f"amount {amount} is negative")

        self._balance -= amount
