from bank import value

def test_value():
    assert value("Hello, Newman") == 0
    assert value("Hi") == 20
    assert value("What's Happening?") == 100
