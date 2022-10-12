from . import r9


def test_subtract() -> None:
    vector_1 = r9.Vector(3)
    vector_1[0], vector_1[1], vector_1[2] = 10, 20, 30

    vector_2 = r9.Vector(3)
    vector_2[0], vector_2[1], vector_2[2] = 1, 2, 3

    vector_3 = r9.Vector(3)
    vector_3[0], vector_3[1], vector_3[2] = 9, 18, 27

    assert vector_1 - vector_2 == vector_3
