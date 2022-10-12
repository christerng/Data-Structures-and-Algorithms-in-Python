from . import r12


def test_multiply() -> None:
    vector = r12.Vector(3)
    vector[0], vector[1], vector[2] = 1, 2, 3

    output = r12.Vector(3)
    output[0], output[1], output[2] = 5, 10, 15

    assert vector * 5 == output
