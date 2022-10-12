from . import r23


def test_equal() -> None:
    c_1 = r23.ConcreteSequence([1, 2, 3])
    c_2 = r23.ConcreteSequence([4, 5, 6])
    assert c_1 < c_2

    c_3 = r23.ConcreteSequence([1, 2, 2])
    assert c_3 < c_1
