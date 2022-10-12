import pytest

from . import r7


@pytest.fixture
def credit_card() -> r7.CreditCard:
    return r7.CreditCard("", "", "", 0)


def test_charge(credit_card: r7.CreditCard) -> None:
    with pytest.raises(TypeError):
        credit_card.charge("")


def test_make_payment(credit_card: r7.CreditCard) -> None:
    with pytest.raises(TypeError):
        credit_card.make_payment("")
    with pytest.raises(ValueError):
        credit_card.make_payment(-1)


def test_balance() -> None:
    c = r7.CreditCard("", "", "", 0)
    assert c._balance == 0
    c = r7.CreditCard("", "", "", 0, 1)
    assert c._balance == 1
