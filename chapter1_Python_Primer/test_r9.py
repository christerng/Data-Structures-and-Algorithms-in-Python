from . import r9


def test_r() -> None:
    assert list(r9.r()) == [50, 60, 70, 80]
