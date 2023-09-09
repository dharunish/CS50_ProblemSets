from plates import is_valid

def test_is_alpha():
    assert is_valid("#.()") == False
    assert is_valid("AD4AJ2") == False
    assert is_valid("C50") == False


def test_begin_alpha():
    assert is_valid("CS50") == True
    assert is_valid("3CS50P") == False
    assert is_valid(".ED902") == False
    assert is_valid("#.A222") == False
    assert is_valid("CS50.") == False
    assert is_valid("CS,50") == False

def test_length():
    assert is_valid("CS50") == True
    assert is_valid("AAAAAAA33333") == False

def test_zero_placement():
    assert is_valid("CS50") == True
    assert is_valid("AAA022") == False
    assert is_valid("0CS50P") == False