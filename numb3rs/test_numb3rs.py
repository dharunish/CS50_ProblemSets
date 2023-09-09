from numb3rs import validate

def test_validate():
    assert validate("cat") == False
    assert validate("1.1.1.1.1.1.1") == False
    assert validate("5.20.50.4") == True
    assert validate("1000.5.3.4") == False
    assert validate("1.5.3.4000") == False
    assert validate("234.275.234.234") == False
