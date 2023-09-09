from seasons import validate
from seasons import total_time

def test_validate():
    assert validate("2022-7-11") == True
    assert validate("2021-7-11") == True
    assert validate("1999/1/2") == False
    assert validate("2022-67-1") == False
def test_total_time():
    assert total_time("2022-7-11") == "Five hundred twenty-five thousand, six hundred minutes"
    assert total_time("1999-4-12") == "Twelve million, seven hundred fifty-two thousand, six hundred forty minutes"