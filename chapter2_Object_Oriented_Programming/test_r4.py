import pytest

from . import r4


@pytest.fixture
def flower() -> r4.Flower:
    return r4.Flower("name", 0, 0.0)


def test_init(flower: r4.Flower) -> None:
    f = flower
    assert f.name == "name"
    assert f.petals == 0
    assert f.price == 0.0


def test_set(flower: r4.Flower) -> None:
    f = flower
    f.name = "new_name"
    f.petals = 1
    f.price = 0.1
    assert f.name == "new_name"
    assert f.petals == 1
    assert f.price == 0.1
