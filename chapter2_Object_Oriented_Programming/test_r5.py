import pytest

from . import r5


@pytest.fixture
def credit_card() -> r5.CreditCard:
    return r5.CreditCard("", "", "", 0)


def test_charge(credit_card: r5.CreditCard) -> None:
    with pytest.raises(TypeError):
        credit_card.charge("")


def test_make_payment(credit_card: r5.CreditCard) -> None:
    with pytest.raises(TypeError):
        credit_card.make_payment("")
