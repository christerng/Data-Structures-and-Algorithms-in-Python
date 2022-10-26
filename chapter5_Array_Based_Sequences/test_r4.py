import pytest

from . import r4


@pytest.fixture
def dynamic_array() -> r4.DynamicArray:
    d = r4.DynamicArray()
    d.append(0)
    d.append(1)
    d.append(2)
    d.append(3)
    d.append(4)
    d.append(5)
    return d


@pytest.mark.parametrize("i,v", [(0, 0), (-1, 5)])
def test_getitem(dynamic_array: r4.DynamicArray, i: int, v: int) -> None:
    assert dynamic_array[i] == v
