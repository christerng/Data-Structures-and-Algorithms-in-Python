from . import r11


def test_l() -> None:
    assert r11.l() == [1, 2, 4, 8, 16, 32, 64, 128, 256]
