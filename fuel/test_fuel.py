from fuel import convert
from fuel import gauge
import pytest


def test_convert():
    assert convert("1/5") == 20
    assert convert("0/5") == 0
    with pytest.raises(ZeroDivisionError):
        convert("5/0")
    with pytest.raises(ValueError):
        convert("7/5")
    with pytest.raises(ValueError):
        convert("1.5/5")

    assert convert("2/3") == 67
    with pytest.raises(ValueError):
        assert convert("cat/dog")
    with pytest.raises(ValueError):
        assert convert("3/2")
    with pytest.raises(ZeroDivisionError):
        assert convert("0/0")

def test_gauge():
    assert gauge(20) == "20%"
    assert gauge(100) == "F"
    assert gauge(0) == "E"
    assert gauge(99) == "F"
    assert gauge(1) == "E"


