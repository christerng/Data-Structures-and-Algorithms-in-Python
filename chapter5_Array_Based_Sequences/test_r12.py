from . import r12


def test_sum_matrix() -> None:
    assert r12.sum_matrix([[1, 2], [3, 4]]) == 10
