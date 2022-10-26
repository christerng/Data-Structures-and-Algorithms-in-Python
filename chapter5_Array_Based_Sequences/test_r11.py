from . import r11


def test_sum_matrix() -> None:
    assert r11.sum_matrix([[1, 2], [3, 4]]) == 10
