from . import r14


def test_multiply() -> None:
    vector_1 = r14.Vector(3)
    vector_1[0], vector_1[1], vector_1[2] = 1, 2, 3

    vector_2 = r14.Vector(3)
    vector_2[0], vector_2[1], vector_2[2] = 10, 20, 30

    output = r14.Vector(3)
    output[0], output[1], output[2] = 10, 40, 90

    assert vector_1 * vector_2 == output
