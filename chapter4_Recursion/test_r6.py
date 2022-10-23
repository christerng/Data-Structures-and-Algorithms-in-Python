import pytest

from . import r6


@pytest.mark.parametrize("n,h", [(1, 1.0), (2, 1.5), (3, 1.8333333333333333)])
def test_recursive_harmonic(n: int, h: float) -> None:
    assert r6.recursive_harmonic(n) == h
