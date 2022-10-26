import pytest

from . import r6


@pytest.fixture
def dynamic_array() -> r6.DynamicArray:
    d = r6.DynamicArray()
    d.append(0)
    d.append(1)
    d.append(3)
    d.append(4)
    return d


def test_insert(dynamic_array: r6.DynamicArray) -> None:
    dynamic_array.insert(2, 2)
    assert dynamic_array[2] == 2
