def test_pytest():
    assert True


def test_pytest2(a=2, b=3):
    c = a + b
    assert c == 4
