from . import r15


def test_init() -> None:
    vector_1 = r15.Vector(3)
    vector_2 = r15.Vector([0, 0, 0])
    assert vector_1 == vector_2
