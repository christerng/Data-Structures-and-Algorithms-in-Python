from . import r10


def test_r() -> None:
    assert list(r10.r()) == [8, 6, 4, 2, 0, -2, -4, -6, -8]
