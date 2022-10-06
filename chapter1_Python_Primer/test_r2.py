import pytest

from . import r2


@pytest.mark.parametrize("k,b", [(99, False), (100, True)])
def test_is_even(k: int, b: bool) -> None:
    assert r2.is_even(k) is b
