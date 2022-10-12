import pytest

from . import r6


@pytest.fixture
def credit_card() -> r6.CreditCard:
    return r6.CreditCard("", "", "", 0)


def test_charge(credit_card: r6.CreditCard) -> None:
    with pytest.raises(TypeError):
        credit_card.charge("")


def test_make_payment(credit_card: r6.CreditCard) -> None:
    with pytest.raises(TypeError):
        credit_card.make_payment("")
    with pytest.raises(ValueError):
        credit_card.make_payment(-1)
