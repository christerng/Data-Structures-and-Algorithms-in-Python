from . import r11


def test_radd() -> None:
    vector = r11.Vector(3)
    vector[0], vector[1], vector[2] = 1, 2, 3

    sequence = [4, 5, 6]

    output = r11.Vector(3)
    output[0], output[1], output[2] = 5, 7, 9

    assert vector + sequence == sequence + vector == output
