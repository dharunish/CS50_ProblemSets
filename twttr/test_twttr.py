from twttr import shorten

def test_word():
    assert shorten("Harvard") == "Hrvrd"
    assert shorten("Antelope") == "ntlp"
    assert shorten("#Video.") == "#Vd."
    assert shorten("Programmer1521") == "Prgrmmr1521"