import pytest

from . import r1


@pytest.mark.parametrize("n,m,b", [(3, 2, False), (4, 2, True)])
def test_is_multiple(n: int, m: int, b: bool) -> None:
    assert r1.is_multiple(n, m) is b
