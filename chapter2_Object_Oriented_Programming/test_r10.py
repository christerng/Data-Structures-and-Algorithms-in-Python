from . import r10


def test_negate() -> None:
    vector_1 = r10.Vector(3)
    vector_1[0], vector_1[1], vector_1[2] = 1, 2, 3

    vector_2 = r10.Vector(3)
    vector_2[0], vector_2[1], vector_2[2] = -1, -2, -3

    assert -vector_1 == vector_2
