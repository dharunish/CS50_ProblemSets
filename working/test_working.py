from working import convert
import pytest

def test_firstAM():
    assert convert("9:00 AM to 10:00 PM") == ("09:00 to 22:00")
    assert convert("9:00 AM to 10:00 AM") == ("09:00 to 10:00")

def test_secondPM():
    assert convert("8:00 PM to 4:00 AM") == ("20:00 to 04:00")
    assert convert("9:00 PM to 10:00 PM") == ("21:00 to 22:00")



def test_error():
    with pytest.raises(ValueError):
        convert("9:00 AM - 10:00 AM")
    with pytest.raises(ValueError):
        convert("cat")
    with pytest.raises(ValueError):
        convert("9:60 PM to 5:70 AM")
    with pytest.raises(ValueError):
        convert("9:00 AM 10:00 PM")

def test_nomin():
    assert convert("9 AM to 5 PM") == ("09:00 to 17:00")
