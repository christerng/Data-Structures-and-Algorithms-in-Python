from . import r22


def test_equal() -> None:
    c_1 = r22.ConcreteSequence([1, 2, 3])
    c_2 = r22.ConcreteSequence([1, 2, 3])
    assert c_1 == c_2

    c_3 = r22.ConcreteSequence([4, 5, 6])
    assert c_1 != c_3
