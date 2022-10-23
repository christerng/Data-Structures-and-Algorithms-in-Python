import pytest

from . import r7


@pytest.mark.parametrize("s,i", [("13531", 13531), ("12345", 12345), ("01234", 1234)])
def test_recursive_intify(s: str, i: int) -> None:
    assert r7.recursive_intify(s, len(s)) == i
