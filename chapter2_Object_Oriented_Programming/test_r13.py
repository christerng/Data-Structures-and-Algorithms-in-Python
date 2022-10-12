from . import r13


def test_multiply() -> None:
    vector = r13.Vector(3)
    vector[0], vector[1], vector[2] = 1, 2, 3

    output = r13.Vector(3)
    output[0], output[1], output[2] = 5, 10, 15

    assert 5 * vector == output
