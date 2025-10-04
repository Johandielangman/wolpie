from wolpie import add


def test_add_simple():
    assert add(1, 2) == 3


def test_add_negative():
    assert add(-1, 5) == 4
